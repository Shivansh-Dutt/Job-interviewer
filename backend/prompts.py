def get_question_prompt(role, level, interview_type):
    return f"""
You are a senior interviewer.

TASK:
Ask ONE {interview_type} interview question.

CONSTRAINTS:
- Role: {role}
- Level: {level}
- Only ONE question
- No explanation
- No preamble

QUESTION:
"""

def get_evaluation_prompt(question, answer, role):
    return f"""
You are a strict interviewer evaluating a {role} candidate.

RULES:
- Output ONLY valid JSON
- No explanation
- No markdown
- No extra text

Question:
{question}

Candidate Answer:
{answer}

Return EXACTLY this JSON structure:

{{
  "score": 0,
  "strengths": ["..."],
  "improvements": ["..."],
  "sample_better_answer": "..."
}}

JSON OUTPUT:
"""
def get_json_repair_prompt(text):
    return f"""
You are a JSON formatter.

TASK:
Convert the following text into VALID JSON.

RULES:
- Output ONLY valid JSON
- No explanation
- No markdown
- Follow this exact structure:

{{
  "score": number,
  "strengths": [string],
  "improvements": [string],
  "sample_better_answer": string
}}

TEXT:
{text}

JSON OUTPUT:
"""
