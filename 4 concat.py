import os

source_folder = "/JPSFT/3_extracted_1475"
output_file = "/JPSFT/4_concat.json"

combined_data = []

for i in range(1, 1476):
    file_path = os.path.join(source_folder, f"extracted_chunk_{i}.json")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            combined_data.append(content)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('[' + ','.join(combined_data) + ']')

print(f"All files concatenated and saved to {output_file}")