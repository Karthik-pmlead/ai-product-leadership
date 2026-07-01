# HOW_TO_RUN.md

# 🚀 Agentic Market Intelligence Platform

This guide explains how to set up and run the project locally.

---

# Prerequisites

Install the following:

* Python 3.11+
* Node.js 18+
* npm
* Git

Verify installation:

```bash
python3 --version
node --version
npm --version
git --version
```

---

# 1. Clone Repository

```bash
git clone https://github.com/<your-username>/agentic-market-intelligence-platform.git

cd agentic-market-intelligence-platform
```

---

# 2. Project Structure

```
agentic-market-intelligence-platform/

backend/
frontend/
docs/
README.md
HOW_TO_RUN.md
```

---

# 3. Backend Setup

Navigate to the backend folder.

```bash
cd backend
```

Create a virtual environment.

macOS / Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Configure Environment Variables

Create a file named:

```
.env
```

Example:

```
OPENAI_API_KEY=your_api_key_here
```

If using another LLM provider, configure the corresponding environment variables.

---

# 5. Start Backend

```bash
uvicorn main:app --reload
```

Backend should start on

```
http://127.0.0.1:8000
```

Open API docs

```
http://127.0.0.1:8000/docs
```

---

# 6. Frontend Setup

Open a second terminal.

Navigate to frontend.

```bash
cd frontend
```

Install packages.

```bash
npm install
```

Run development server.

```bash
npm run dev
```

Frontend should start at

```
http://localhost:5173
```

---

# 7. Run the Application

Open

```
http://localhost:5173
```

Enter a company name, for example:

```
Tesla
```

Click

```
Analyze
```

The UI streams the execution of:

* Router Agent
* Planner Agent
* Risk Agent
* Opportunity Agent
* Recommendation Agent
* Competitor Agent (when applicable)

You should see:

* Executive Summary
* Risks
* Opportunities
* Recommendations
* Evaluation Scores
* Reasoning Trace

---

# 8. Example Queries

Company analysis

```
Tesla
Microsoft
NVIDIA
Apple
```

Competitor analysis

```
Tesla vs BYD
AWS vs Azure
Visa vs Mastercard
```

Industry analysis

```
Electric Vehicle Industry
Cloud Computing
Digital Payments
```

---

# 9. Backend API

Endpoint

```
POST /api/analyze
```

Example request

```json
{
  "query": "Analyze Tesla"
}
```

---

# 10. Troubleshooting

## ModuleNotFoundError

Install missing packages.

```bash
pip install -r requirements.txt
```

---

## Port Already In Use

Backend

```bash
lsof -i :8000
kill -9 <PID>
```

Frontend

```bash
lsof -i :5173
kill -9 <PID>
```

---

## npm Dependency Issues

Delete existing packages.

```bash
rm -rf node_modules
rm package-lock.json
```

Reinstall.

```bash
npm install
```

---

## Python Virtual Environment Not Activated

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## API Returns 500

Check:

* OPENAI_API_KEY configured
* Backend running
* Frontend proxy configuration
* Terminal logs

---

## Frontend Cannot Connect

Verify backend:

```
http://127.0.0.1:8000/docs
```

If unavailable, restart the backend.

---

# 11. Running Tests

Backend

```bash
python test_router.py
python test_risk.py
python test_opportunity.py
python test_recommendation.py
python test_llm.py
```

---

# 12. Demo Workflow

1. Start backend
2. Start frontend
3. Open browser
4. Enter company name
5. Click **Analyze**
6. Observe streaming execution
7. Review final strategic report

---

# Expected Architecture

```
User
 ↓
Frontend
 ↓
FastAPI
 ↓
Router Agent
 ↓
Planner Agent
 ↓
Memory Layer
 ↓
Risk Agent
 ↓
Opportunity Agent
 ↓
Recommendation Agent
 ↓
Competitor Agent
 ↓
Evaluation Layer
 ↓
Streaming Response
```

---

# Demo Credentials

No login is required for the local demo.

---

# Support

If the application does not start:

1. Verify Python and Node.js versions.
2. Confirm all dependencies are installed.
3. Ensure the `.env` file is configured.
4. Start the backend before the frontend.
5. Review terminal logs for detailed error messages.

