import json

def is_long_enough(text, min_length=3):
    return len(text.strip()) >= min_length

input_file = '/JPSFT/8_at_removed.json'
output_file = '/JPSFT/9_final.json'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

filtered_data = [
    item for item in data 
    if is_long_enough(item['query']) and is_long_enough(item['output'])
]

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)

print(f"Processing complete. Original entries: {len(data)}, Filtered entries: {len(filtered_data)}")
print(f"Check '{output_file}' for the result.")