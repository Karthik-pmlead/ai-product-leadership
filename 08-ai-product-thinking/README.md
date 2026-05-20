# AI PRD Thinking

A comprehensive framework and collection of AI product templates and projects for building production-ready AI applications.

---

## Purpose

This repository provides a structured approach to AI product development through:

- **Standardized Templates**: Reusable templates for AI PRDs, decision matrices, evaluation plans, MLOps checklists, and more
- **Framework Guidance**: Proven frameworks like FOBW (Find-Order-Buy-Win) for systematic AI project progression
- **Reference Projects**: Real-world AI implementations across different use cases to learn from and build upon
- **Best Practices**: Industry-standard practices for AI/ML product development, from problem definition to production deployment

Whether you're a product manager, ML engineer, or developer, this repository equips you with the tools and examples needed to build AI products systematically and successfully.

---

## Projects

This repository contains the following AI projects:

| Project | Description | Type | Status | Key Technologies |
|---------|-------------|------|--------|------------------|
| [aspect-sentiment](./aspect-sentiment) | Aspect-based sentiment analysis for customer reviews and feedback | NLP / Classification | ✅ Production Ready | Python, transformers, spaCy, FastAPI |
| [chatbot](./chatbot) | Intelligent conversational chatbot with contextual understanding and multi-turn dialogue | NLP / LLM | ✅ Production Ready | Python, LangChain, LLM APIs, vector DB |
| [doc-extr](./doc-extr) | Document extraction and information extraction from PDFs, images, and structured documents | NLP / OCR / Extraction | ✅ Production Ready | Python, Tesseract, PyPDF2, transformers |
| [reccom](./reccom) | Recommendation system for personalized content and product recommendations | ML / Recommendation | ✅ Production Ready | Python, scikit-learn, TensorFlow, ALS |
| [template](./template) | Base template project for scaffolding new AI projects with best practices | Template / Starter | ✅ Production Ready | Python, structure, CI/CD, MLOps |

---

## Recommended rule

| Question | Folder |
|---|---|
| Should we use AI? | `03_ai_decisioning` |
| Which model/architecture should we use? | `05_solution_design` |
| How do we ship and operate it? | `09_ml_system_design_and_mlops` |

## Design principles

| Principle | Meaning |
|---|---|
| Separate decision from design | Decide what to build before choosing how to build it. |
| Separate design from operations | Model choice is not the same as deployment and monitoring. |
| Keep templates reusable | Use the same structure across multiple AI products. |
| Optimize for business impact | Every folder should support building successful AI products. |

## Best Practices

### For Product Managers
- ✅ Use the **AI PRD Canvas** before starting any AI project
- ✅ Complete the **Business Case** template for stakeholder approval
- ✅ Define clear success metrics in the **Evaluation Plan**
- ✅ Review **Model Cards** for ethical considerations

### For ML Engineers
- ✅ Follow the **MLOps Checklist** before production deployment
- ✅ Document models using **Model Cards**
- ✅ Use **Evaluation Plans** for systematic testing
- ✅ Implement **Solution Design** before coding

### For Developers
- ✅ Start with the **template** project for consistent structure
- ✅ Use **Launch Checklist** before deploying
- ✅ Follow CI/CD practices from the template
- ✅ Reference existing projects for patterns

---

## Getting Help

- 📖 **Documentation**: Check individual project READMEs
- 🗺️ **Framework**: Read `fobw_framework.md` for AI project guidance
- 📋 **Templates**: Use templates in `99_templates/` for your projects
- 💬 **Questions**: Open an issue for support

---

## Acknowledgements

This repository is inspired by industry best practices from:
- Product School AI Product Management
- Google's Model Cards framework
- Microsoft's AI product guidelines
- Industry MLOps standards
