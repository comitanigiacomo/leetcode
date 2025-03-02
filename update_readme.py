import json

README_FILE = "README.md"
PROGRESS_FILE = "progress.json"

# Funzione per caricare i progressi dal file JSON
def load_progress(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Funzione per generare la tabella da inserire nel README
def generate_table(progress):
    table_header = "| Problem ID | Title | Tags | Solution Link |\n"
    table_header += "|------------|-------|------|---------------|\n"

    table_rows = ""
    for problem_id, data in progress.items():
        title = data["title"]
        link = f"[Link]({data['link']})"
        tags = " ".join(data["tags"])
        status = "✅" if data["completed"] else "❌"
        
        table_rows += f"| {problem_id} | {title} | {tags} | {link} {status} |\n"
    
    return table_header + table_rows

# Funzione per aggiornare solo la tabella nel README
def update_readme(readme_path, table_content):
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    start_marker = "### LeetCode Progress Tracker 📅"
    end_marker = "|------------|-------|------|---------------|"

    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
        if start_index is not None and end_marker in line and i > start_index:
            end_index = i
            break

    # Sezione della tabella non trovata, la creiamo
    if start_index is not None and end_index is not None:
        lines = lines[:start_index + 1]  # Mantieni il contenuto prima della tabella
    else:
        lines.append("\n### LeetCode Progress Tracker 📅\n")  # Aggiungi la sezione se non esiste

    lines.append(table_content)  # Aggiungi la nuova tabella

    with open(readme_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    progress = load_progress(PROGRESS_FILE)

    new_table = generate_table(progress)

    update_readme(README_FILE, new_table)
    print("README aggiornato con successo!")
