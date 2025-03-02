import json

README_FILE = "README.md"
PROGRESS_FILE = "progress.json"

# Funzione per caricare i progressi dal file JSON
def load_progress(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Funzione per generare la tabella da inserire nel README
def generate_table(progress):
    table_header = "### LeetCode Progress Tracker 📅\n\n"
    table_header += "| Problem ID | Title | Tags | Solution Link |\n"
    table_header += "|------------|-------|------|---------------|\n"

    table_rows = ""
    for problem_id, data in progress.items():
        title = data["title"]
        link = f"[My Solution]({data['mylink']})"
        tags = " ".join(data["tags"])
        leetcode = f"[Explanation]({data['leetcodelink']}/)"

        table_rows += f"| {problem_id} | {title} | {tags} | {link} | {leetcode} |\n"

    return table_header + table_rows

# Funzione per aggiornare la tabella nel README
def update_readme(readme_path, table_content):
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    # Troviamo la riga con il link al profilo LeetCode
    profile_marker = "You can view my LeetCode account by clicking [here](https://leetcode.com/GiacomoLeetCode/)"
    profile_index = None

    for i, line in enumerate(lines):
        if profile_marker in line:
            profile_index = i
            break

    # Verifichiamo se la tabella esiste già (cercando il titolo della tabella)
    table_marker = "### LeetCode Progress Tracker 📅"
    table_start = None
    table_end = None

    for i, line in enumerate(lines):
        if table_marker in line:
            table_start = i
            break

    # Rimuoviamo la tabella solo, lasciando intatta la parte dei badges
    if table_start is not None:
        table_end = None
        for i in range(table_start + 1, len(lines)):
            if lines[i].startswith("|------------|"):  # trovo la linea che separa la tabella
                for j in range(i + 1, len(lines)):
                    if not lines[j].startswith("|"):  # finisce la tabella
                        table_end = j
                        break
                if table_end is None: table_end = i + 1
                break

        # Rimuoviamo solo la tabella, mantenendo la parte successiva intatta
        if table_start is not None and table_end is not None:
            lines = lines[:table_start + 1] + lines[table_end:]

    # Se la tabella non esiste, la creiamo dopo il link del profilo
    if profile_index is not None:
        # Aggiungiamo solo la tabella, senza titolo, se il titolo è già presente
        if not any(table_marker in line for line in lines):
            # Aggiungiamo la tabella subito dopo il link al profilo LeetCode
            lines = lines[:profile_index + 1] + [table_content] + lines[profile_index + 1:]
        else:
            # Se la tabella esiste già, la rimuoviamo e la ristampiamo
            lines = [line for line in lines if not line.startswith(table_marker)]
            lines = lines[:profile_index + 1] + [table_content] + lines[profile_index + 1:]

    # Scriviamo il file modificato
    with open(readme_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    # Carichiamo i dati dei progressi
    progress = load_progress(PROGRESS_FILE)
    
    # Generiamo la tabella
    new_table = generate_table(progress)
    
    # Aggiorniamo il README
    update_readme(README_FILE, new_table)
    
    print("README aggiornato con successo!")
