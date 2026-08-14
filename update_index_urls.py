import os
import re

def find_file(root_dir, filename):
    # filename is like "Two-Sum" (without .md)
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if f"{filename}.md" in filenames:
            return os.path.join(dirpath, f"{filename}.md")
    return None

def extract_leetcode_url(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for **LeetCode Link:** [Title](url)
            match = re.search(r'\*\*LeetCode Link:\*\* \[.*?\]\((.*?)\)', content)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return None

def update_index(index_path, root_dir):
    with open(index_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_table = False
    header_processed = False

    for line in lines:
        # Check if it's a table row
        if line.strip().startswith('|'):
            parts = [p.strip() for p in line.strip().split('|')]
            # parts[0] is empty string because line starts with |
            # parts[1] is #
            # parts[2] is Problem
            # parts[3] is Difficulty
            # parts[4] is Status
            # parts[5] is empty string (if line ends with |)
            
            # Check if it's a header row
            if 'Problem' in line and 'Difficulty' in line:
                # Add LC column
                # Current: | # | Problem | Difficulty | Status |
                # New: | # | Problem | LC | Difficulty | Status |
                new_line = "| # | Problem | LC | Difficulty | Status |\n"
                new_lines.append(new_line)
                header_processed = True
                continue
            
            # Check if it's a separator row
            if '---' in line:
                # Add separator for LC column
                new_line = "|---|---|---|---|---|\n"
                new_lines.append(new_line)
                continue

            # Data row
            # Extract filename from wikilink [[Filename\|Display]]
            # Regex to match [[Filename\| or [[Filename|
            match = re.search(r'\[\[(.*?)(?:\\\||\|)', line)
            if match:
                filename = match.group(1).strip()
                filepath = find_file(root_dir, filename)
                lc_url = ""
                if filepath:
                    lc_url = extract_leetcode_url(filepath)
                
                lc_link = f"[Link]({lc_url})" if lc_url else "-"
                
                # Reconstruct the line with LC column
                # parts indices might vary if there are extra spaces or empty strings
                # Let's assume standard format: | # | Problem | Difficulty | Status |
                # We want: | # | Problem | LC | Difficulty | Status |
                
                # Filter out empty strings from split
                clean_parts = [p.strip() for p in line.split('|') if p.strip() != '']
                
                if len(clean_parts) >= 4:
                    num = clean_parts[0]
                    problem = clean_parts[1] # Contains the wikilink
                    difficulty = clean_parts[2]
                    status = clean_parts[3]
                    
                    new_line = f"| {num} | {problem} | {lc_link} | {difficulty} | {status} |\n"
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    index_file = r"d:\Obsedian\LeetCode\Top-75-Index.md"
    root_directory = r"d:\Obsedian\LeetCode"
    update_index(index_file, root_directory)
    print("Index updated with LeetCode URLs")
