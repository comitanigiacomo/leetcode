import json

from sympy import li

README_FILE = "README.md"
PROGRESS_FILE = "progress.json"

def load_progress(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_difficulty_badge(difficulty):
    badges = {
        "easy": "![Easy](https://img.shields.io/badge/-Easy-yellow)",
        "medium": "![Medium](https://img.shields.io/badge/-Medium-yellow)",
        "hard": "![Hard](https://img.shields.io/badge/-Hard-yellow)"
    }
    return badges.get(difficulty.lower(), "")

def get_tag_badges(tags):
    return " ".join(
        f"![{tag}](https://img.shields.io/badge/-{tag.replace(' ', '_').replace('-', '_').lower()}-blue)"
        for tag in tags
    )

def generate_table(progress):
    table_header = "### LeetCode Progress Tracker 📅\n"
    table_header += "|🎯 Problem ID |📌 Title |🏷️ Tags |⚡ Difficulty |📝 Solution |\n"
    table_header += "|:------------:|---------|:------:|:------------:|:----------:|\n"

    table_rows = ""
    for problem_id, data in progress.items():
        title = data["title"]
        link = f"[{title}]({data['link']}/)"
        tags = get_tag_badges(data["tags"])
        difficulty_badge = get_difficulty_badge(data.get("difficulty", ""))
        solution = f"[solution]({data['solution']})"

        table_rows += f"| {problem_id} | {link} | {tags} | {difficulty_badge} | {solution}|\n"

    return table_header + table_rows

def update_readme(readme_path, table_content):
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    start_marker = "### LeetCode Progress Tracker 📅\n"
    table_start = None
    table_end = None

    for i, line in enumerate(lines):
        if start_marker in line:
            table_start = i
            table_end = i + 1
            while table_end < len(lines) and lines[table_end].startswith("|"):
                table_end += 1
            break

    if table_start is not None and table_end is not None:
        lines = lines[:table_start] + lines[table_end:]

    profile_marker = "You can view my LeetCode account by clicking [here](https://leetcode.com/GiacomoLeetCode/)"
    profile_index = None

    for i, line in enumerate(lines):
        if profile_marker in line:
            profile_index = i
            break

    if profile_index is not None:
        lines = lines[:profile_index + 1] + [table_content] + lines[profile_index + 1:]

    with open(readme_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    progress = load_progress(PROGRESS_FILE)
    new_table = generate_table(progress)
    update_readme(README_FILE, new_table)
    print("README aggiornato con successo!")
