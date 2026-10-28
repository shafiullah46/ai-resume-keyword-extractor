import os
from openai import OpenAI, APIConnectionError

# Retrieve API credentials and custom base URL if available
api_key = os.environ.get('OPENAI_API_KEY', 'dummy_key')
base_url = os.environ.get('OPENAI_API_BASE')

# Initialize OpenAI Client (handles custom endpoints like KodeKloud or standard OpenAI)
client = OpenAI(
    api_key=api_key,
    base_url=base_url if base_url else None
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
    
    # Use lab model if custom base URL exists, else default to standard OpenAI model
    model_name = "gpt-5.6-luna" if base_url else "gpt-4o-mini"
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except APIConnectionError as e:
        return f"[Error] Could not connect to API endpoint ({base_url or 'api.openai.com'}). Ensure valid OPENAI_API_KEY and OPENAI_API_BASE environment variables are set."

if __name__ == "__main__":
    resume_text = "Experienced DevOps engineer skilled in Python, Kubernetes, Docker, CI/CD pipelines, and cloud automation."
    
    extracted = extract_keywords(resume_text)
    print("Extracted Keywords:", extracted)
