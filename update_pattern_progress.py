import os
import re

PATTERNS_DIR = r"d:\obsidian\DSA/Patterns"
INDEX_FILE = os.path.join(PATTERNS_DIR, "00 - Index.md")

def count_progress(practice_path):
    """Count completed vs total problems from checkboxes in a Practice.md file."""
    if not os.path.exists(practice_path):
        return 0, 0
    with open(practice_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Count total problem list items (lines starting with "- [x]" or "- [ ]")
    total = len(re.findall(r'^\s*-\s*\[[ x]\]\s+\S', content, re.MULTILINE))
    completed = len(re.findall(r'^\s*-\s*\[x\]\s+\S', content, re.MULTILINE))
    return completed, total

def parse_index_lines(lines):
    """Parse the index file to find lines with pattern links."""
    results = []
    for i, line in enumerate(lines):
        if line.strip().startswith('| [[') and '/Practice.md' in line:
            match = re.search(r'\[\[(.+?/Practice\.md)', line)
            if match:
                rel_path = match.group(1)
                results.append((i, rel_path))
    return results

def update_index():
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    link_lines = parse_index_lines(lines)

    for line_num, rel_path in link_lines:
        practice_path = os.path.join(PATTERNS_DIR, rel_path)
        completed, total = count_progress(practice_path)

        # Find the end of the wikilink (]] marks the end of [[path|display]])
        # Everything after ]] is the completed/total columns
        wikilink_end = lines[line_num].rfind(']]')
        if wikilink_end != -1:
            prefix = lines[line_num][:wikilink_end + 2]
            # Rebuild the suffix with new values
            # Format: | Completed | Total |
            suffix = f' | {completed} | {total} |\n'
            lines[line_num] = prefix + suffix

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("Progress counts updated in index!")
    print(f"  File: {INDEX_FILE}")

    # Print summary
    for line_num, rel_path in link_lines:
        practice_path = os.path.join(PATTERNS_DIR, rel_path)
        completed, total = count_progress(practice_path)
        print(f"  {rel_path}: {completed}/{total}")

if __name__ == "__main__":
    update_index()
