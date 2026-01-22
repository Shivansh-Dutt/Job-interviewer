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
You are a strict but fair interviewer for a {role} role.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

STRICT RULES:
- Return ONLY valid JSON
- No explanation outside JSON
- No markdown
- No extra text

JSON FORMAT:

{{
  "score": 0-10,
  "strengths": ["..."],
  "improvements": ["..."],
  "sample_better_answer": "..."
}}
"""
