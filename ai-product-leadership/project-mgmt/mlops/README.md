# 🔄 MLOps Frameworks for Production AI

**Model → Production → Scale → Monitor** | **Zero-downtime deployments**

## 📋 MLOps Checklist (Production Ready)
| Stage | Checklist | Owner |
|-------|-----------|-------|
| **Model Registry** | MLflow versioning, staging approval | DS Lead |
| **CI/CD Pipeline** | GitHub Actions → Docker → K8s | DevOps |
| **Canary Deploy** | 1% traffic → 100% over 2hr | PM |
| **Synthetic Monitoring** | Latency p95<100ms, drift<5% | SRE |
| **Rollback** | Blue-green, 5min recovery | On-call |

**Templates:** [Deployment Checklist](deployment-checklist.md)


MLOps belongs in project-mgmt/ because it's fundamentally PROJECT MANAGEMENT for AI/ML workflows.
Traditional PM: "Ship the code"
AI PM: "Ship the MODEL + monitor drift + retrain + redeploy"

MLOps IS project management for the entire ML lifecycle:

MLOps = End-to-End Project Execution

Week 1-4: Model development ✅ (Data Science)
Week 5: Model registry + approval ✅ (PM governance) 
Week 6: CI/CD pipeline ✅ (DevOps coordination)
Week 7: Canary deployment ✅ (Risk management)
Week 8+: Monitoring + retraining ✅ (Ongoing operations)

🛠️ PM Owns These MLOps Decisions
✅ "When to retrain?" → Capacity planning
✅ "Canary %?" → Risk mitigation  
✅ "Drift threshold?" → Success criteria
✅ "Rollback plan?" → Contingency planning
✅ "Stakeholder sync?" → Cross-team alignment

AI Director: "I orchestrate MLOps across 50 engineers"
