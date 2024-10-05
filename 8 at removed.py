import json

def contains_at_symbol(text):
    return '@' in text

with open('/JPSFT/7_usernames_removed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filtered_data = [
    item for item in data 
    if not (contains_at_symbol(item['query']) or contains_at_symbol(item['output']))
]

with open('/JPSFT/8_at_removed.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)

print(f"Processing complete. Original entries: {len(data)}, Filtered entries: {len(filtered_data)}")