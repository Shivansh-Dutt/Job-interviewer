import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState(null);
  const [started, setStarted] = useState(false);

  const startInterview = async () => {
    const res = await fetch("http://127.0.0.1:5000/start", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        role: "backend developer",
        level: "fresher",
        type: "technical",
      }),
    });

    const data = await res.json();
    setQuestion(data.question);
    setStarted(true);
  };

  const submitAnswer = async () => {
    const res = await fetch("http://127.0.0.1:5000/answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answer }),
    });

    const data = await res.json();
    console.log(data)
    if (data.feedback) {
      setFeedback(data.feedback);
    }

    if (data.message === "Interview completed") {
      setQuestion("Interview Completed 🎉");
    }

    setAnswer("");
  };

  return (
    <div style={{ width: "80%", margin: "auto", fontFamily: "Arial" }}>
      <h2>AI Mock Interviewer</h2>

      {!started && (
        <button onClick={startInterview}>Start Interview</button>
      )}

      {question && (
        <>
          <div style={{ marginTop: "20px" }}>
            <strong>Interviewer:</strong>
            <p>{question}</p>
          </div>

          <textarea
            rows="4"
            style={{ width: "100%" }}
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            placeholder="Type your answer..."
          />

          <button onClick={submitAnswer} style={{ marginTop: "10px" }}>
            Submit Answer
          </button>
        </>
      )}

      {feedback && (
        <div style={{ marginTop: "30px", background: "#f4f4f4", padding: "15px" }}>
          <h4>Feedback</h4>
          <p><b>Score:</b> {feedback.score}/10</p>

          <p><b>Strengths:</b></p>
          <ul>
            {feedback.strengths.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>

          <p><b>Improvements:</b></p>
          <ul>
            {feedback.improvements.map((i, idx) => (
              <li key={idx}>{i}</li>
            ))}
          </ul>

          <p><b>Better Answer:</b></p>
          <p>{feedback.sample_better_answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;
