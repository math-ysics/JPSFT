import json
import re

def load_usernames(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def process_json(json_filename, usernames_filename, output_filename):
    usernames = load_usernames(usernames_filename)
    usernames.sort(key=len, reverse=True)
    
    with open(json_filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for entry in data:
        for field in ['query', 'output']:
            for username in usernames:
                if entry[field].startswith(username):
                    entry[field] = re.sub(f'^{re.escape(username)}(\\s|→|:|$)', '', entry[field], flags=re.UNICODE).lstrip()
                    break
    
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

json_filename = '/JPSFT/5_concat_json.json'
usernames_filename = '/JPSFT/6_usernames_only.txt'
output_filename = '/JPSFT/7_usernames_removed.json'

process_json(json_filename, usernames_filename, output_filename)
print("Processing complete. Check the output file.")