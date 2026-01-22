from flask import Flask,request,jsonify
from prompts import get_evaluation_prompt,get_question_prompt,get_json_repair_prompt
from llm import call_llm
from flask_cors import CORS
from utils import extract_json

app = Flask(__name__)
CORS(app)

interview_state = {} #later db

@app.route("/start", methods=["POST"])
def start_interview():
    data = request.json
    
    interview_state["role"] = data["role"]
    interview_state["level"] = data["level"]
    interview_state["type"] = data["type"]
    interview_state["question_number"] = 1
    
    prompt  = get_question_prompt(
        role=data["role"],
        level=data["level"],
        interview_type=data["type"]
    )
    
    question = call_llm(prompt)
    
    interview_state["current_question"] = question
    
    return jsonify({
        "question": question
    })
    
@app.route("/answer", methods=["POST"])
def submit_answer():
    data = request.json
    user_answer = data["answer"]

    eval_prompt = get_evaluation_prompt(
        question=interview_state["current_question"],
        answer=user_answer,
        role=interview_state["role"]
    )

    # First pass (raw evaluation)
    raw_output = call_llm(eval_prompt)

    feedback = extract_json(raw_output)

    # Second pass (JSON repair if needed)
    if feedback is None:
        repair_prompt = get_json_repair_prompt(raw_output)
        repaired_output = call_llm(repair_prompt)
        feedback = extract_json(repaired_output)

    # Final fallback (never crash frontend)
    if feedback is None:
        feedback = {
            "score": 0,
            "strengths": [],
            "improvements": ["Unable to evaluate answer reliably"],
            "sample_better_answer": ""
        }

    interview_state["question_number"] += 1

    return jsonify({
        "feedback": feedback
    })

if __name__=="__main__":
    app.run(debug=True)