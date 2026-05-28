# 12_Tradeoffs.md

## 🎯 Technology Selection Tradeoffs

### Tradeoff 1: AWS vs GCP (Cloud Provider)

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| **AWS (Selected)** | - Mature Redshift (columnar warehouse)<br>- Strong S3 ecosystem<br>- Team expertise | - Costly at scale<br>- Vendor lock-in | ✅ **Selected** (MVP) |
| **GCP (Alternative)** | - BigQuery (serverless, no ops)<br>- Cheaper at scale<br>- Better ML integration | - Smaller ecosystem<br>- Team less familiar | 🔄 **Future** (Phase 3 dual-cloud) |

**Why AWS?**
- Team has AWS experience (EC2, S3, Redshift)
- MVP timeline: 6 weeks (AWS faster to set up)
- Cost at 100K rows: AWS ~$300/month, GCP ~$250/month (small difference)

**Migration Plan to GCP:**
1. S3 → GCS (gsutil rsync)
2. EC2 → GCE (containerize with Docker)
3. Redshift → BigQuery (SQL translation layer)
4. Metabase → Looker (dashboard migration)

---

### Tradeoff 2: Redshift vs BigQuery (Analytics Warehouse)

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| **Redshift (Selected)** | - Columnar (fast aggregations)<br>- SQL-compatible<br>- Works with Metabase | - Requires cluster ops<br>- Scaling = add nodes | ✅ **Selected** (MVP) |
| **BigQuery (Alternative)** | - Serverless (no ops)<br>- Auto-scaling<br>- Pay-per-query | - Costly at high volume<br>- Less control | 🔄 **Future** (Phase 3) |

**Why Redshift?**
- MVP: 100K rows (Redshift handles 1B+ rows easily)
- Team knows Redshift SQL (PostgreSQL-compatible)
- Cost: $170/month (dc2.large) vs BigQuery $200/month (estimated)

**When to switch to BigQuery:**
- Volume > 10B rows
- Need real-time streaming ingest
- Team wants serverless (no ops)

---

### Tradeoff 3: Batch vs Real-time (Pipeline Architecture)

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| **Batch (Selected)** | - Simple (EC2 script)<br>- Cost-effective ($50/month)<br>- Accurate (full dataset) | - 24hr latency<br>- Not real-time | ✅ **Selected** (MVP) |
| **Real-time (Alternative)** | - Sub-minute latency<br>- Up-to-date
