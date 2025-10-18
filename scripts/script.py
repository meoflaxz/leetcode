import os
import re
from pathlib import Path
from datetime import datetime

def parse_problems_by_difficulty():
    """Parse easy, medium, hard directories"""
    all_problems = {'easy': [], 'medium': [], 'hard': []}
    
    for difficulty in ['easy', 'medium', 'hard']:
        diff_dir = Path(difficulty)
        if not diff_dir.exists():
            continue
        
        for file in sorted(diff_dir.iterdir()):
            if file.is_file() and file.suffix in ['.py', '.js', '.java', '.cpp', '.go']:
                # Extract problem info from filename
                # Expected format: 0001-two-sum.py or two-sum.py
                name = file.stem
                match = re.match(r'^(\d+)-(.+)$', name)
                
                if match:
                    number = int(match.group(1))
                    problem_name = match.group(2).replace('-', ' ').title()
                else:
                    number = 0
                    problem_name = name.replace('-', ' ').title()
                
                all_problems[difficulty].append({
                    'number': number,
                    'name': problem_name,
                    'file': file.name,
                    'language': file.suffix[1:]
                })
    
    return all_problems

def generate_table(problems):
    """Generate markdown table for problems"""
    if not problems:
        return 'No problems solved yet.'
    
    lines = ['| # | Problem | Language |', '|---|---------|----------|']
    
    for problem in sorted(problems, key=lambda x: x['number'], reverse=True):
        num = f"{problem['number']}" if problem['number'] > 0 else '-'
        lines.append(
            f"| {num} | [{problem['name']}]({problem['file']}) | `{problem['language']}` |"
        )
    
    return '\n'.join(lines)

def update_readme(all_problems):
    """Update README.md with problem lists"""
    readme_path = Path('README.md')
    content = readme_path.read_text()
    
    # Count totals
    easy_count = len(all_problems['easy'])
    medium_count = len(all_problems['medium'])
    hard_count = len(all_problems['hard'])
    total = easy_count + medium_count + hard_count
    
    # Update stats
    stats = f"""<!-- LEETCODE-STATS:START -->
- Total: {total} problems
- Easy: {easy_count}
- Medium: {medium_count}
- Hard: {hard_count}
<!-- LEETCODE-STATS:END -->"""
    
    content = re.sub(
        r'<!-- LEETCODE-STATS:START -->.*?<!-- LEETCODE-STATS:END -->',
        stats,
        content,
        flags=re.DOTALL
    )
    
    # Update Easy section
    easy_table = f"<!-- LEETCODE-EASY:START -->\n{generate_table(all_problems['easy'])}\n<!-- LEETCODE-EASY:END -->"
    content = re.sub(
        r'<!-- LEETCODE-EASY:START -->.*?<!-- LEETCODE-EASY:END -->',
        easy_table,
        content,
        flags=re.DOTALL
    )
    
    # Update Medium section
    medium_table = f"<!-- LEETCODE-MEDIUM:START -->\n{generate_table(all_problems['medium'])}\n<!-- LEETCODE-MEDIUM:END -->"
    content = re.sub(
        r'<!-- LEETCODE-MEDIUM:START -->.*?<!-- LEETCODE-MEDIUM:END -->',
        medium_table,
        content,
        flags=re.DOTALL
    )
    
    # Update Hard section
    hard_table = f"<!-- LEETCODE-HARD:START -->\n{generate_table(all_problems['hard'])}\n<!-- LEETCODE-HARD:END -->"
    content = re.sub(
        r'<!-- LEETCODE-HARD:START -->.*?<!-- LEETCODE-HARD:END -->',
        hard_table,
        content,
        flags=re.DOTALL
    )
    
    readme_path.write_text(content)
    print(f"✅ Updated README with {total} problems (Easy: {easy_count}, Medium: {medium_count}, Hard: {hard_count})")

if __name__ == '__main__':
    all_problems = parse_problems_by_difficulty()
    update_readme(all_problems)