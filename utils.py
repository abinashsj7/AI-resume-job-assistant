import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text, job_role):
    prompt = f"""
You are an AI career and resume advisor.

Resume:
{resume_text}

Target Job Role:
{job_role}

Perform the following:
1. Identify missing or weak skills
2. Suggest concrete resume improvements
3. Rewrite the resume to better match the job role
4. Provide interview preparation tips
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
