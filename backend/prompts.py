def get_question_prompt(role, level, interview_type):
    return f"""
You are a senior interviewer.
Ask ONE {interview_type} interview question
for a {level} {role}.

Only return the question
"""

def get_evaluation_prompt(question, answer, role):
    return f"""
You are a strict but fair interview.

Question.
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return ONLY valid JSON in this format:

{{
    "score" : 0-10,
    "strengths": [],
    "improvements": [],
    "sample_better_answer": ""
}}
"""