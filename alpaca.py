import json

input_file_path = "/JPSFT/9_final.json"
output_file_path = "/JPSFT/alpaca_final.json"

with open(input_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

alpaca_format = []
for item in data:
    alpaca_item = {
        "instruction": item["query"],
        "input": "",
        "output": item["output"]
    }
    alpaca_format.append(alpaca_item)

with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(alpaca_format, f, ensure_ascii=False, indent=4)

output_file_path