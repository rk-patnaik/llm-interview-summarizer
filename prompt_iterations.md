# Prompt Iteration 1

## Prompt

```text
Summarize this interview transcript.
Mention topics, candidate profile and candidate summary.
```

## Input

```text
Candidate discussed Angular, React, Ionic, Tailwind and AI-assisted development.
```

## Output

```text
The candidate is a software engineer with frontend experience.
```

## What Worked / What Didn't

- The output was too generic.
- Topics were not structured properly.
- Candidate profile lacked justification.
- The summary did not mention weaknesses or communication concerns.

---

# Prompt Iteration 2

## Prompt

```text
You are an expert recruiter.

Analyze the interview transcript and provide:
1. Topics Covered
2. Candidate Profile
3. Candidate Summary

Mention strengths and weaknesses.
Avoid hallucinating information.
```

## Input

```text
Candidate discussed fraud prevention systems, vendor management and stakeholder communication.
```

## Output

```text
Topics Covered:
- Fraud detection
- Vendor management
- Stakeholder engagement
```

## What Worked / What Didn't

- Structure improved significantly.
- Topics became clearer and more relevant.
- However, summaries were still slightly verbose.
- Some outputs generalized seniority too broadly.

---

# Prompt Iteration 3 (Final)

## Prompt

```text
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
```

## Input

```text
Candidate discussed Angular, React Query, Tailwind, AI coding assistants and mobile app development.
```

## Output

```text
The candidate appears suitable for a Senior Frontend / Mobile Application Engineer role with strong Angular and Ionic expertise.
```

## What Worked / What Didn't

- Final structure was consistent across both transcripts.
- Balanced evaluation improved realism.
- Mentioning communication quality added recruiter-style assessment.
- Prompt generalized better across technical and managerial interviews.