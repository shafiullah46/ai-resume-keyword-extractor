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
Installation & Setup
1. Clone the Repository
git clone [https://github.com/shafiullah46/ai-resume-keyword-extractor.git](https://github.com/shafiullah46/ai-resume-keyword-extractor.git)
cd ai-resume-keyword-extractor

2. Set Up Virtual Environment
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Set your API key and custom base URL (if using private proxy/endpoints):

Windows PowerShell:
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_API_BASE="your_base_url_here" # Optional for standard OpenAI
Linux / macOS:
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_API_BASE="your_base_url_here"

💻 Usage Example
Run the main extraction script:
python resume_extractor.py
Input Paragraph:
"Experienced DevOps engineer skilled in Python, Kubernetes, Docker, CI/CD pipelines, and cloud automation."

Output:
DevOps, Python, Kubernetes, Docker, CI/CD
👨‍💻 Author
Shafiullah Niazi

Deputy Director ML/DevOps | Cloud & AI Infrastructure Specialist
