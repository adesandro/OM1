# Before:
# action = json.loads(response.text)

# After (Meaningful Improvement):
from src.utils.json_fixer import extract_and_parse_json

action = extract_and_parse_json(response.text)
if not action:
    # Trigger a "retry" or a "wait" action instead of crashing
    action = {"action": "wait", "reason": "Received invalid response format from AI"}
