import os

def split_logs_by_lines(file_path, lines_per_file=100):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    output_dir = '/JPSFT/1_chunked'
    os.makedirs(output_dir, exist_ok=True)

    chunk_count = 0
    for i in range(0, len(lines), lines_per_file):
        chunk_lines = lines[i:i + lines_per_file]
        chunk_count += 1
        file_name = os.path.join(output_dir, f'log_chunk_{chunk_count}.txt')
        with open(file_name, 'w', encoding='utf-8') as chunk_file:
            chunk_file.writelines(chunk_lines)

    print(f'Successfully split the file into {chunk_count} files.')

file_path = 'original_file.txt'

split_logs_by_lines(file_path)