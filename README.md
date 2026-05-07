# Interview Transcript Summarizer

This project analyzes interview transcripts using an LLM and generates structured candidate summaries.

## Features

The script extracts:

1. Topics Covered
2. Candidate Profile
3. Candidate Summary

## Tech Stack

- Python
- Groq API
- Llama 3.1 8B Instant

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

## Run the Script

```bash
python summarizer.py sample_transcript_assignment_1.txt
```

or

```bash
python summarizer.py sample_transcript_assignment_2.txt
```

## Files Included

- `summarizer.py` → Main summarization script
- `prompt_iterations.md` → Prompt engineering iterations
- `README.md` → Documentation and setup instructions

## Reflection

One thing that surprised me was how sensitive the output quality was to prompt structure. Small additions such as explicitly asking for balanced evaluation and communication assessment significantly improved consistency.

If I had more time, I would improve:
- handling of extremely long transcripts
- structured JSON output support
- scoring/ranking system for candidates
- automated keyword extraction and sentiment analysis

One limitation is that the model may occasionally infer candidate seniority too strongly from partial information available in the transcript.