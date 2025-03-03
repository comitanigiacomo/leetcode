import json

from sympy import li

README_FILE = "README.md"
PROGRESS_FILE = "progress.json"

def load_progress(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_difficulty_badge(difficulty):
    badges = {
        "easy": "![Easy](https://img.shields.io/badge/-Easy-brightgreen)",
        "medium": "![Medium](https://img.shields.io/badge/-Medium-orange)",
        "hard": "![Hard](https://img.shields.io/badge/-Hard-red)"
    }
    return badges.get(difficulty.lower(), "")

def get_tag_badges(tags):
    tag_colors = {
        "Array": "rgb(0, 0, 255)",  # Blu
        "String": "rgb(0, 128, 0)",  # Verde
        "Hash Table": "rgb(255, 165, 0)",  # Arancione
        "Dynamic Programming": "rgb(255, 0, 0)",  # Rosso
        "Math": "rgb(128, 0, 128)",  # Viola
        "Sorting": "rgb(255, 255, 0)",  # Giallo
        "Greedy": "rgb(0, 255, 0)",  # Lime
        "Depth-First Search": "rgb(0, 128, 128)",  # Teal
        "Binary Search": "rgb(0, 255, 255)",  # Ciano
        "Database": "rgb(255, 0, 255)",  # Magenta
        "Matrix": "rgb(165, 42, 42)",  # Marrone
        "Tree": "rgb(128, 128, 0)",  # Oliva
        "Breadth-First Search": "rgb(0, 0, 139)",  # Blu scuro
        "Bit Manipulation": "rgb(0, 100, 0)",  # Verde scuro
        "Two Pointers": "rgb(139, 0, 0)",  # Rosso scuro
        "Prefix Sum": "rgb(139, 0, 139)",  # Magenta scuro
        "Heap (Priority Queue)": "rgb(0, 139, 139)",  # Ciano scuro
        "Binary Tree": "rgb(255, 140, 0)",  # Arancione scuro
        "Simulation": "rgb(107, 142, 35)",  # Oliva scuro
        "Stack": "rgb(173, 216, 230)",  # Azzurro chiaro
        "Graph": "rgb(144, 238, 144)",  # Verde chiaro
        "Counting": "rgb(240, 128, 128)",  # Corallo chiaro
        "Sliding Window": "rgb(250, 128, 114)",  # Salmone chiaro
        "Design": "rgb(32, 178, 170)",  # Verde mare chiaro
        "Enumeration": "rgb(135, 206, 235)",  # Azzurro cielo chiaro
        "Backtracking": "rgb(176, 196, 222)",  # Blu acciaio chiaro
        "Union Find": "rgb(255, 255, 224)",  # Giallo chiaro
        "Linked List": "rgb(255, 182, 193)",  # Rosa chiaro
        "Number Theory": "rgb(230, 230, 250)",  # Lavanda
        "Ordered Set": "rgb(216, 191, 216)",  # Cardo
        "Monotonic Stack": "rgb(221, 160, 221)",  # Prugna
        "Segment Tree": "rgb(238, 130, 238)",  # Viola
        "Trie": "rgb(218, 112, 214)",  # Orchidea
        "Combinatorics": "rgb(186, 85, 211)",  # Viola medio
        "Bitmask": "rgb(106, 90, 205)",  # Blu ardesia
        "Queue": "rgb(65, 105, 225)",  # Blu reale
        "Divide and Conquer": "rgb(100, 149, 237)",  # Blu fiordaliso
        "Recursion": "rgb(30, 144, 255)",  # Blu dodger
        "Memoization": "rgb(0, 191, 255)",  # Azzurro profondo
        "Binary Indexed Tree": "rgb(135, 206, 250)",  # Azzurro cielo
        "Geometry": "rgb(176, 224, 230)",  # Azzurro polvere
        "Binary Search Tree": "rgb(175, 238, 238)",  # Turchese pallido
        "Hash Function": "rgb(224, 255, 255)",  # Ciano chiaro
        "String Matching": "rgb(245, 255, 250)",  # Crema di menta
        "Topological Sort": "rgb(240, 255, 240)",  # Melata
        "Shortest Path": "rgb(240, 255, 255)",  # Azzurro
        "Rolling Hash": "rgb(240, 248, 255)",  # Bianco alice
        "Game Theory": "rgb(248, 248, 255)",  # Bianco fantasma
        "Interactive": "rgb(245, 245, 245)",  # Fumo bianco
        "Data Stream": "rgb(220, 220, 220)",  # Grigio guadagno
        "Monotonic Queue": "rgb(211, 211, 211)",  # Grigio chiaro
        "Brainteaser": "rgb(192, 192, 192)",  # Argento
        "Randomized": "rgb(169, 169, 169)",  # Grigio scuro
        "Merge Sort": "rgb(128, 128, 128)",  # Grigio
        "Doubly-Linked List": "rgb(105, 105, 105)",  # Grigio dim
        "Counting Sort": "rgb(0, 0, 0)",  # Nero
        "Iterator": "rgb(188, 143, 143)",  # Marrone rosato
        "Concurrency": "rgb(205, 92, 92)",  # Rosso indiano
        "Probability and Statistics": "rgb(178, 34, 34)",  # Rosso mattone
        "Quickselect": "rgb(165, 42, 42)",  # Marrone
        "Suffix Array": "rgb(128, 0, 0)",  # Granata
        "Bucket Sort": "rgb(139, 0, 0)",  # Rosso scuro
        "Line Sweep": "rgb(160, 82, 45)",  # Terra di Siena
        "Minimum Spanning Tree": "rgb(139, 69, 19)",  # Marrone sella
        "Shell": "rgb(210, 105, 30)",  # Cioccolato
        "Reservoir Sampling": "rgb(205, 133, 63)",  # Perù
        "Strongly Connected Component": "rgb(218, 165, 32)",  # Goldenrod
        "Eulerian Circuit": "rgb(184, 134, 11)",  # Goldenrod scuro
        "Radix Sort": "rgb(210, 180, 140)",  # Tan
        "Rejection Sampling": "rgb(222, 184, 135)",  # Burlywood
        "Biconnected Component": "rgb(245, 245, 220)"  # Beige
    }
    return " ".join(
        f"<center>![{tag}](https://img.shields.io/badge/-{tag.replace('#','')}-{tag_colors.get(tag, 'lightgrey')})</center>"
        for tag in tags
    )

def generate_table(progress):
    table_header = "### LeetCode Progress Tracker 📅\n"
    table_header += "|🎯 Problem ID |📌 Title |🏷️ Tags |⚡ Difficulty |📝 Solution | 📖Explanation |\n"
    table_header += "|:------------:|:-------:|:------:|:------------:|:----------:|:--------------:|\n"

    table_rows = ""
    for problem_id, data in progress.items():
        title = data["title"]
        link = f"[{title}]({data['link']}/)"
        tags = get_tag_badges(data["tags"])
        difficulty_badge = get_difficulty_badge(data.get("difficulty", ""))
        solution = f"[solution]({data['solution']})"
        explanation = f"[explanation]({data['explanation']}/)" if data.get('explanation') else "<center>❌</center>"

        table_rows += f"| {problem_id} | {link} | {tags} | {difficulty_badge} | {solution} | {explanation} |\n"

    return table_header + table_rows

def update_readme(readme_path, table_content):
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    # Trova la posizione della tabella esistente
    start_marker = "### LeetCode Progress Tracker 📅\n"
    table_start = None
    table_end = None

    for i, line in enumerate(lines):
        if start_marker in line:
            table_start = i
            # Trova la fine della tabella (prima riga che non comincia con "|")
            table_end = i + 1
            while table_end < len(lines) and lines[table_end].startswith("|"):
                table_end += 1
            break

    # Se esiste una tabella, rimuoviamola
    if table_start is not None and table_end is not None:
        lines = lines[:table_start] + lines[table_end:]

    # Inseriamo la nuova tabella
    profile_marker = "You can view my LeetCode account by clicking [here](https://leetcode.com/GiacomoLeetCode/)"
    profile_index = None

    # Troviamo l'indice dove si trova il link al profilo
    for i, line in enumerate(lines):
        if profile_marker in line:
            profile_index = i
            break

    # Inseriamo la nuova tabella subito dopo il profilo
    if profile_index is not None:
        lines = lines[:profile_index + 1] + [table_content] + lines[profile_index + 1:]

    # Scriviamo il file aggiornato
    with open(readme_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    progress = load_progress(PROGRESS_FILE)
    new_table = generate_table(progress)
    update_readme(README_FILE, new_table)
    print("README aggiornato con successo!")
