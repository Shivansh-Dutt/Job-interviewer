import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

def call_llm(prompt):
    response = client.chat.completions.create(
        model="zai-org/GLM-4.7-Flash:novita",
        messages=[
            {
                "role": "system",
                "content": "You are a strict technical interviewer. Follow instructions exactly."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=300   # ✅ CRITICAL FIX
    )

    return response.choices[0].message["content"]
