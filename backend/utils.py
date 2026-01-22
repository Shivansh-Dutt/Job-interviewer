import json
import re

def extract_json(text):
    if not text:
        return None

    # Find first JSON-like block
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        return None

    json_str = match.group()

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None
