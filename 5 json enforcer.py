import re

input_file_path = '/JPSFT/4_concat.json'
output_file_path = '/JPSFT/5_concat_json.json'

with open(input_file_path, 'r', encoding='utf-8') as f:
    raw_content = f.read()

cleaned_content = re.sub(r'```json|```', '', raw_content)
cleaned_content_with_commas = re.sub(r'}\s*{', '},\n{', cleaned_content)
final_cleaned_content = '[\n' + cleaned_content_with_commas + '\n]'

with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(final_cleaned_content)

print(f"JSON file has been cleaned and saved to: {output_file_path}")