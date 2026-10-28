import os
from openai import OpenAI

# Initialize the OpenAI client with environment variables
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def extract_keywords(text: str) -> str:
    """
    Extracts exactly 5 job-relevant keywords from a resume paragraph,
    returned as a single comma-separated string.
    """
    prompt = (
        f"Analyze the following resume paragraph and extract exactly five job-relevant keywords. "
        f"Your response must contain ONLY the five keywords separated by commas, with no other text, "
        f"markdown, introduction, or punctuation outside the commas.\n\n"
        f"Resume Paragraph:\n{text}"
    )
    
    response = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0
    )
    
    # Extract the clean string response
    keywords = response.choices[0].message.content.strip()
    return keywords

if __name__ == "__main__":
    resume_text = "Experienced DevOps engineer skilled in Python, Kubernetes, Docker, CI/CD pipelines, and cloud automation."
    
    extracted = extract_keywords(resume_text)
    print("Extracted Keywords:", extracted)
