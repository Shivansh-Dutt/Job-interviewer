import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

def call_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="zai-org/GLM-4.7-Flash:novita",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional technical interviewer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            max_tokens=40
        )
        # Extract the text content
        return response.choices[0].message["content"]
    
    except Exception as e:
        return f"Error calling the model: {e}"

