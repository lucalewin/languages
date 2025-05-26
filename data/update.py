import json
import re

input_filename = 'input.json'
output_filename = 'output_fixed.json'

# Read raw content
with open(input_filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace single backslashes that are not part of a valid escape sequence
# This is a heuristic and might not cover all cases perfectly
content_fixed = re.sub(r'\\([^"\\/bfnrtu])', r'\\\\\1', content)

try:
    data = json.loads(content_fixed)
except json.JSONDecodeError as e:
    print("Still JSON decode error:", e)
    exit(1)

# Remove the 'russian' key from each object
for item in data:
    if 'russian' in item:
        del item['russian']

# Save cleaned and modified JSON
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Processed and saved to {output_filename}")