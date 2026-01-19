import json
import re

def extract_and_parse_json(text: str):
    """
    Meaningful fix: Extracts JSON from LLM responses that might 
    contain conversational filler or markdown formatting.
    """
    # Search for content between ```json and ``` or just ```
    match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
    
    if match:
        clean_json = match.group(1)
    else:
        # Fallback: find the first '{' and last '}'
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1:
            clean_json = text[start:end+1]
        else:
            clean_json = text

    try:
        return json.loads(clean_json)
    except json.JSONDecodeError as e:
        # Log the error but don't crash the whole agent
        print(f"Failed to parse LLM response: {e}")
        return None
