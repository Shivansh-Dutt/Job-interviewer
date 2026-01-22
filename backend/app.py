from flask import Flask,request,jsonify
from prompts import get_evaluation_prompt,get_question_prompt
from llm import call_llm

app = Flask(__name__)

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
    
    feedback = call_llm(eval_prompt)
    
    interview_state["question_number"] += 1
    
    return jsonify({
        "feedback": feedback
    })
    
if __name__ == "__main__":
    app.run(debug=True)
    
    