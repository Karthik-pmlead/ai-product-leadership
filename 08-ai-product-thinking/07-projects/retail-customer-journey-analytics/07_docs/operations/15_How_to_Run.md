# 15_How_to_Run.md

# 🚀 Complete Setup & Execution Guide: Retail Customer Journey Analytics Pipeline

**From Zero to Live Dashboards** – Complete step-by-step instructions to set up the entire pipeline, from dataset download to live Metabase dashboards and Streamlit app.

**Estimated Time:** 45–60 minutes  
**Difficulty:** Intermediate (requires AWS account + Python)  
**Cost:** ~$300–400/month for MVP (AWS free tier eligible for first 12 months)  
**Prerequisites:** AWS account, Python 3.8+, Git, PostgreSQL client (psql or DBeaver), Kaggle account

***

## 📋 Table of Contents

1. [Prerequisites & Setup](#prerequisites--setup)
2. [Step 1: Download Dataset](#step-1-download-dataset)
3. [Step 2: Configure AWS CLI](#step-2-configure-aws-cli)
4. [Step 3: Create S3 Buckets](#step-3-create-s3-buckets)
5. [Step 4: Create Redshift Cluster](#step-4-create-redshift-cluster)
6. [Step 5: Create IAM Role for Redshift](#step-5-create-iam-role-for-redshift)
7. [Step 6: Launch EC2 Instance](#step-6-launch-ec2-instance)
8. [Step 7: Run ETL Pipeline](#step-7-run-etl-pipeline)
9. [Step 8: Set Up Metabase Dashboard](#step-8-set-up-metabase-dashboard)
10. [Step 9: Run Streamlit App](#step-9-run-streamlit-app)
11. [Step 10: Verify & Test](#step-10-verify--test)
12. [Troubleshooting](#troubleshooting)
13. [Cleanup (Stop Costs)](#cleanup-stop-costs)

***

## Prerequisites & Setup

### Required Software

```bash
# 1. Install Python 3.8+ (if not installed)
# macOS: brew install python@3.11
# Linux: sudo apt-get install python3.11 python3-pip
python --version  # Should show Python 3.8+

# 2. Install AWS CLI
# macOS: brew install awscli
# Linux:
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip
unzip awscliv2.zip
sudo ./aws/install
aws --version  # Should show AWS CLI/2.x

# 3. Install Git
git --version

# 4. Install PostgreSQL client (for querying Redshift)
# macOS: brew install postgresql
# Linux: sudo apt-get install postgresql-client
psql --version

# 5. Install Kaggle CLI (for dataset)
pip install kaggle
```

### Clone Repository

```bash
git clone https://github.com/Karthik-pmlead/Retail-Customer-Journey-Analytics-Pipeline.git
cd Retail-Customer-Journey-Analytics-Pipeline
```

### Install Python Dependencies

```bash
pip install boto3 pandas psycopg2-binary streamlit python-dotenv great-expectations
```

***

## Step 1: Download Dataset

### Option A: Kaggle CLI (Recommended)

```bash
# 1. Generate API token (one-time setup)
# Visit: https://www.kaggle.com/settings → Account → Create New API Token
# This downloads kaggle.json to ~/Downloads/

# 2. Move token to correct location
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# 3. Download dataset
kaggle datasets download -d olistbr/brazilian-ecommerce

# 4. Create data directory and extract
mkdir -p 01_data/raw
unzip brazilian-ecommerce.zip -d 01_data/raw/

# 5. Verify files
ls 01_data/raw/
# Expected: customers.csv, orders.csv, order_items.csv, payments.csv, 
#           reviews.csv, products.csv, sellers.csv, geolocation.csv
```

### Option B: Manual Download

```bash
# 1. Go to: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
# 2. Click "Download" → Save zip file (~50 MB)
# 3. Extract:
unzip brazilian-ecommerce.zip -d 01_data/raw/

# OR use Google Drive backup:
# https://drive.google.com/drive/folders/1TGEc66YKbD443nslRi1bWgVd238gJCnb
# Download all 8 CSV files → 01_data/raw/
```

### Verify Dataset Integrity

```bash
# Check row counts
wc -l 01_data/raw/*.csv

# Expected (including header):
# customers.csv: ~100,001
# orders.csv: ~100,001
# order_items.csv: ~152,342
# payments.csv: ~121,457
# reviews.csv: ~50,235

# Check first few rows
head -3 01_data/raw/orders.csv
```

***

## Step 2: Configure AWS CLI

```bash
# 1. Get AWS credentials:
#    Go to: https://console.aws.amazon.com/iam/
#    Select your user → Security credentials → Create access key (CLI)
#    Download the .csv file with Access Key ID + Secret Access Key

# 2. Configure AWS CLI
aws configure

# Input when prompted:
# AWS Access Key ID: [YOUR_ACCESS_KEY]           # From .csv file
# AWS Secret Access Key: [YOUR_SECRET_KEY]       # From .csv file
# Default region name: us-east-1
# Default output format: json

# 3. Verify configuration
aws sts get-caller-identity
# Should return your account ARN
```

***

## Step 3: Create S3 Buckets

```bash
# Replace YOUR_USERNAME with your unique identifier
export BUCKET_RAW="retail-cj-raw-${USER}"
export BUCKET_CURATED="retail-cj-curated-${USER}"

# 1. Create raw data bucket
aws s3 mb s3://${BUCKET_RAW} --region us-east-1

# 2. Create curated data bucket
aws s3 mb s3://${BUCKET_CURATED} --region us-east-1

# 3. Verify buckets created
aws s3 ls
# Expected:
# 2026-05-28 18:30:00 retail-cj-raw-yourusername
# 2026-05-28 18:30:05 retail-cj-curated-yourusername

# 4. Upload CSVs to raw bucket
aws s3 cp 01_data/raw/ s3://${BUCKET_RAW}/raw/ --recursive

# 5. Verify upload
aws s3 ls s3://${BUCKET_RAW}/raw/
# Expected: 8 CSV files listed
```

***

## Step 4: Create Redshift Cluster

### Option A: AWS Console (Recommended for MVP)

1. **Go to:** [AWS Console → Redshift](https://console.aws.amazon.com/redshift/)
2. **Click:** **Create cluster**
3. **Configure:**

| Setting | Value |
|---------|-------|
| Cluster identifier | `retail-cj-analytics` |
| Node type | `dc2.large` (2 vCPU, 16 GB) |
| Number of nodes | `2` |
| DB name | `analytics` |
| Master username | `analyst` |
| Master password | `YourSecurePass123!` (≥12 chars) |
| VPC | Default VPC |
| Subnet | Private subnet |
| Security group | Create new → Name: `redshift-sg` |
| Inbound rule | TCP port `5439` from `redshift-sg` (self) |
| Encryption | Enabled ✓ |
| Publicly accessible | **No** |

4. **Click:** **Create cluster** (takes 15–20 minutes)
5. **Wait:** Status changes from "Creating" → "Available"

### Option B: AWS CLI

```bash
# 1. Create security group
aws ec2 create-security-group \
  --group-name redshift-sg \
  --description "Security group for Redshift"

export REDSHIFT_SG=$(aws ec2 describe-security-groups \
  --group-names redshift-sg \
  --query 'SecurityGroups[0].GroupId' --output text)

# 2. Create Redshift cluster
aws redshift create-cluster \
  --cluster-identifier retail-cj-analytics \
  --node-type dc2.large \
  --number-of-nodes 2 \
  --master-username analyst \
  --master-user-password "YourSecurePass123!" \
  --db-name analytics \
  --vpc-security-group-ids ${REDSHIFT_SG} \
  --cluster-type multi-node \
  --publicly-accessible false \
  --encrypted

# 3. Wait for cluster (poll every 30 secs)
aws redshift wait cluster-available --cluster-identifier retail-cj-analytics

# 4. Get endpoint
aws redshift describe-clusters \
  --cluster-identifier retail-cj-analytics \
  --query 'Clusters[0].Endpoint'

# Save endpoint:
export REDSHIFT_HOST="retail-cj-analytics.xxx.us-east-1.redshift.amazonaws.com"
export REDSHIFT_PORT="5439"
```

***

## Step 5: Create IAM Role for Redshift

```bash
# 1. Create trust policy
cat > redshift-s3-trust.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "redshift.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

# 2. Create IAM role
aws iam create-role \
  --role-name RedshiftS3AccessRole \
  --assume-role-policy-document file://redshift-s3-trust.json

# 3. Attach S3 policy
aws iam attach-role-policy \
  --role-name RedshiftS3AccessRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

# 4. Get role ARN
export ROLE_ARN=$(aws iam get-role \
  --role-name RedshiftS3AccessRole \
  --query 'Role.Arn' --output text)

echo "Role ARN: ${ROLE_ARN}"
# Save this for later COPY command
```

***

## Step 6: Launch EC2 Instance

### Option A: AWS Console

1. **Go to:** [EC2 Console → Launch Instance](https://console.aws.amazon.com/ec2/home#LaunchInstance:)
2. **Configure:**

| Setting | Value |
|---------|-------|
| Name | `retail-etl-instance` |
| AMI | Amazon Linux 2023 |
| Instance type | `t3.medium` |
| Key pair | Create new → `retail-etl-key` → Download `.pem` |
| Security group | Name: `etl-sg` |
| Inbound SSH | Port 22 from your IP only |
| User data | Paste script below |

**User data script:**
```bash
#!/bin/bash
yum update -y
yum install -y python3 python3-pip git wget gcc
pip3 install boto3 pandas psycopg2-binary streamlit python-dotenv

cd /home/ec2-user
git clone https://github.com/Karthik-pmlead/Retail-Customer-Journey-Analytics-Pipeline.git
cd Retail-Customer-Journey-Analytics-Pipeline

# Create .env (REPLACE VALUES)
cat > .env << EOFENV
AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
AWS_REGION=us-east-1
S3_RAW_BUCKET=${BUCKET_RAW}
S3_CURATED_BUCKET=${BUCKET_CURATED}
REDSHIFT_HOST=${REDSHIFT_HOST}
REDSHIFT_PORT=5439
REDSHIFT_DB=analytics
REDSHIFT_USER=analyst
REDSHIFT_PASSWORD=YourSecurePass123!
EOFENV
```
3. **Launch instance** (3–5 mins)

### Option B: AWS CLI

```bash
# 1. Create security group
aws ec2 create-security-group \
  --group-name etl-sg \
  --description "ETL instance security group"

export ETL_SG=$(aws ec2 describe-security-groups \
  --group-names etl-sg \
  --query 'SecurityGroups[0].GroupId' --output text)

# 2. Allow SSH from your IP
YOUR_IP=$(curl -s ifconfig.me)
aws ec2 authorize-security-group-ingress \
  --group-id ${ETL_SG} \
  --protocol tcp \
  --port 22 \
  --cidr ${YOUR_IP}/32

# 3. Create key pair
aws ec2 create-key-pair --key-name retail-etl-key \
  --query 'KeyMaterial' --output text > retail-etl-key.pem
chmod 400 retail-etl-key.pem

# 4. Launch instance
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --count 1 \
  --instance-type t3.medium \
  --key-name retail-etl-key \
  --security-group-ids ${ETL_SG} \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=retail-etl-instance}]'

# Get instance ID
export INSTANCE_ID=$(aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=retail-etl-instance" \
  --query 'Reservations[0].Instances[0].InstanceId' --output text)

# 5. Wait for running
aws ec2 wait instance-running --instance-ids ${INSTANCE_ID}

# 6. Get public IP
export EC2_PUBLIC_IP=$(aws ec2 describe-instances \
  --instance-ids ${INSTANCE_ID} \
  --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)

echo "EC2 IP: ${EC2_PUBLIC_IP}"
```

***

## Step 7: Run ETL Pipeline

### 7.1 Connect to EC2

```bash
# Option A: SSH
ssh -i retail-etl-key.pem ec2-user@${EC2_PUBLIC_IP}

# Option B: Session Manager
aws ssm start-session --target ${INSTANCE_ID}
```

### 7.2 Set Environment Variables

```bash
cd /home/ec2-user/Retail-Customer-Journey-Analytics-Pipeline

# Load .env
source .env

# OR set manually
export AWS_ACCESS_KEY_ID="your_key"
export AWS_SECRET_ACCESS_KEY="your_secret"
export S3_RAW_BUCKET="retail-cj-raw-yourusername"
export S3_CURATED_BUCKET="retail-cj-curated-yourusername"
export REDSHIFT_HOST="retail-cj-analytics.xxx.us-east-1.redshift.amazonaws.com"
export REDSHIFT_PORT="5439"
export REDSHIFT_DB="analytics"
export REDSHIFT_USER="analyst"
export REDSHIFT_PASSWORD="YourSecurePass123!"
```

### 7.3 Run Ingestion (CSV → S3)

```bash
python 03_python/etl/ingest_to_s3.py

# Expected output:
# ✅ Uploaded 8 files to S3 (39.4 MB total)
# Runtime: 23 seconds
```

### 7.4 Run Transformation

```bash
python 03_python/etl/transform_ec2.py

# Expected output:
# ✅ Cleaned: customers (99,999), orders (99,500), order_items (152,341)
# ✅ Calculated delivery_time_days, estimated_vs_actual_gap
# ✅ Saved parquet to S3 curated layer
# Runtime: 18 minutes
```

### 7.5 Load to Redshift

```bash
python 03_python/etl/load_redshift.py

# Expected output:
# ✅ Connected to Redshift
# ✅ Loaded stg_customers: 99,999 rows (45 secs)
# ✅ Loaded stg_orders: 99,500 rows (52 secs)
# ✅ Loaded stg_order_items: 152,341 rows (68 secs)
# ✅ Loaded stg_payments: 121,456 rows
# ✅ Loaded stg_reviews: 50,234 rows
# Total runtime: ~4 minutes
```

**Verify in Redshift:**
```bash
psql -h $REDSHIFT_HOST -p $REDSHIFT_PORT -U $REDSHIFT_USER -d $REDSHIFT_DB

# Enter password when prompted

SELECT COUNT(*) FROM stg_customers;  -- Expected: 99999
SELECT COUNT(*) FROM stg_orders;     -- Expected: 99500
SELECT COUNT(*) FROM stg_order_items; -- Expected: 152341
```

***

## Step 8: Set Up Metabase Dashboard

### 8.1 Deploy Metabase on EC2

```bash
# Stop current EC2, create new instance or use same one

# Run Metabase container
docker run -d -p 3000:3000 \
  --name metabase \
  -e MB_DB_TYPE=postgres \
  -e MB_DB_DBNAME=metabase \
  -e MB_DB_PORT=5439 \
  -e MB_DB_HOST=$REDSHIFT_HOST \
  -e MB_DB_USER=analyst \
  -e MB_DB_PASS=YourSecurePass123! \
  metabase/metabase:latest
```

### 8.2 Configure Metabase

1. **Open browser:** `http://${EC2_PUBLIC_IP}:3000`
2. **Setup wizard:**
   - Create admin account (email/password)
   - Company name: "Target Retail Analytics"
3. **Add database:**
   - Click **Admin → Databases → Add database**
   - Database type: **PostgreSQL**
   - Host: `$REDSHIFT_HOST`
   - Port: `5439`
   - Database: `analytics`
   - Username: `analyst`
   - Password: `YourSecurePass123!`
   - Click **Add database**

### 8.3 Create Dashboards

```sql
-- Dashboard 1: Monthly Order Trends
SELECT 
  DATE_TRUNC('month', order_purchase_timestamp) AS month,
  COUNT(*) AS orders,
  SUM(price + freight_value) AS revenue
FROM stg_orders
GROUP BY 1
ORDER BY 1;

-- Dashboard 2: Delivery Performance by State
SELECT 
  customer_state AS state,
  AVG(delivery_time_days) AS avg_delivery_days,
  AVG(estimated_vs_actual_gap) AS gap_days,
  COUNT(*) AS orders
FROM stg_orders
WHERE order_status = 'delivered'
GROUP BY 1
ORDER BY avg_delivery_days;

-- Dashboard 3: Payment Method Distribution
SELECT 
  payment_type,
  COUNT(*) AS orders,
  COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS percentage
FROM stg_payments
GROUP BY 1
ORDER BY orders DESC;
```

**In Metabase:**
1. Click **New → Question**
2. Write SQL query above
3. Visualize as **Line chart** / **Bar chart** / **Pie chart**
4. Save as "Monthly Order Trends"
5. Click **Save → Add to dashboard → Create new dashboard**
6. Repeat for all 3 queries
7. Click **Dashboard → Share → Public link** (optional)

***

## Step 9: Run Streamlit App

```bash
# On EC2 or local machine
cd 04_app

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run ecommerceApp.py --server.port 8501 --server.address 0.0.0.0
```

**Access app:**
- Local: `http://localhost:8501`
- EC2: `http://${EC2_PUBLIC_IP}:8501`

**App features:**
1. **Login page** (email/password)
2. **Acquisition Funnel** tab → stage counts + conversion rates
3. **Retention Cohorts** tab → 90-day retention by month
4. **Dashboards** tab → embedded Metabase charts

***

## Step 10: Verify & Test

### Test Pipeline End-to-End

```bash
# 1. Check S3 buckets
aws s3 ls s3://${BUCKET_RAW}/raw/
aws s3 ls s3://${BUCKET_CURATED}/

# 2. Check Redshift tables
psql -h $REDSHIFT_HOST -p $REDSHIFT_PORT -U $REDSHIFT_USER -d $REDSHIFT_DB -c "
SELECT 
  'stg_customers' AS table_name, COUNT(*) AS rows FROM stg_customers
UNION ALL
SELECT 'stg_orders', COUNT(*) FROM stg_orders
UNION ALL
SELECT 'stg_order_items', COUNT(*) FROM stg_order_items;
"

# Expected output:
# stg_customers | 99999
# stg_orders    | 99500
# stg_order_items | 152341

# 3. Check Metabase dashboard loads
curl -I http://${EC2_PUBLIC_IP}:3000
# Expected: HTTP/1.1 200 OK

# 4. Check Streamlit app responds
curl -I http://${EC2_PUBLIC_IP}:8501
# Expected: HTTP/1.1 200 OK
```

### Valid
