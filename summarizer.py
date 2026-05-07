import os
import sys
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)

PROMPT = """
You are an expert recruiter and interview analyst.

Analyze the interview transcript carefully.

Return the output in the following format:

1. Topics Covered
- List the major themes discussed in the interview
- Use concise bullet points

2. Candidate Profile
- Suggest the most suitable role and seniority level
- Explain briefly why the candidate fits this role

3. Candidate Summary
- Write a professional summary in 3-6 sentences
- Include:
  - background
  - strengths
  - weaknesses or concerns
  - communication quality
  - overall impression

Keep the response professional and balanced.
Do not hallucinate information not present in the transcript.
"""

def summarize_transcript(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        transcript = file.read()

    final_prompt = PROMPT + "\n\nTranscript:\n" + transcript

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python summarizer.py <transcript_file>")
        sys.exit(1)

    transcript_path = sys.argv[1]

    result = summarize_transcript(transcript_path)

    print("\n========== SUMMARY ==========\n")

    print(result)