# 📄 AI Resume Keyword Extractor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

An intelligent, Python-based AI microservice built for ATS (Applicant Tracking Systems) and HR technology workflows. It extracts exactly five high-impact, job-relevant keywords from candidate resume profiles using OpenAI's API with deterministic output configuration.

---

## 🚀 Key Highlights

- **ATS-Optimized Extraction:** Uses structured prompt engineering to isolate exactly 5 job-specific technical keywords.
- **Deterministic Sampling:** Configured with `temperature=0` to eliminate variance and guarantee reproducible results across runs.
- **Zero-Boilerplate Formatting:** Prompts strictly enforce clean, comma-separated outputs ready for downstream vector search, database tagging, or ATS indexing.
- **Environment-Driven Configuration:** Securely loads API credentials and custom endpoints via system environment variables (`OPENAI_API_KEY` and `OPENAI_API_BASE`).

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **SDK:** `openai` (Official Python Library)
- **Environment:** Virtualenv (`venv`)

---

## 📂 Project Structure

```text
ai-resume-keyword-extractor/
│
├── resume_extractor.py     # Main Python script with extraction logic
├── requirements.txt        # Project dependencies
├── .gitignore              # Ignored files (venv, cache, env)
└── README.md               # Project documentation
