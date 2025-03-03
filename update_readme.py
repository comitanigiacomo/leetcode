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
        "Array": "blue", "String": "green", "Hash Table": "orange", "Dynamic Programming": "red", 
        "Math": "purple", "Sorting": "yellow", "Greedy": "brightgreen", "Depth-First Search": "orange", 
        "Binary Search": "dodgerblue", "Database": "darkblue", "Matrix": "brown", "Tree": "forestgreen", 
        "Breadth-First Search": "lightblue", "Bit Manipulation": "darkgreen", "Two Pointers": "darkred", 
        "Prefix Sum": "darkmagenta", "Heap (Priority Queue)": "darkcyan", "Binary Tree": "darkorange", 
        "Simulation": "olive", "Stack": "lightgreen", "Graph": "lightcoral", "Counting": "lightsalmon", 
        "Sliding Window": "lightseagreen", "Design": "lightskyblue", "Enumeration": "lightsteelblue", 
        "Backtracking": "lightyellow", "Union Find": "lightpink", "Linked List": "lavender", 
        "Number Theory": "thistle", "Ordered Set": "plum", "Monotonic Stack": "violet", "Segment Tree": "orchid", 
        "Trie": "mediumpurple", "Combinatorics": "slateblue", "Bitmask": "royalblue", "Queue": "cornflowerblue", 
        "Divide and Conquer": "deepskyblue", "Recursion": "skyblue", "Memoization": "powderblue", 
        "Binary Indexed Tree": "paleturquoise", "Geometry": "lightcyan", "Binary Search Tree": "mintcream", 
        "Hash Function": "honeydew", "String Matching": "azure", "Topological Sort": "aliceblue", 
        "Shortest Path": "ghostwhite", "Rolling Hash": "whitesmoke", "Game Theory": "gainsboro", 
        "Interactive": "lightgray", "Data Stream": "silver", "Monotonic Queue": "darkgray", "Brainteaser": "gray", 
        "Randomized": "dimgray", "Merge Sort": "black", "Doubly-Linked List": "rosybrown", 
        "Counting Sort": "indianred", "Iterator": "firebrick", "Concurrency": "brown", 
        "Probability and Statistics": "maroon", "Quickselect": "darkred", "Suffix Array": "sienna", 
        "Bucket Sort": "saddlebrown", "Line Sweep": "chocolate", "Minimum Spanning Tree": "peru", 
        "Shell": "goldenrod", "Reservoir Sampling": "darkgoldenrod", "Strongly Connected Component": "tan", 
        "Eulerian Circuit": "burlywood", "Radix Sort": "beige", "Rejection Sampling": "white", 
        "Biconnected Component": "lightgrey"
    }
    
    return " ".join(
        f"![{tag}](https://img.shields.io/badge/-{tag.replace(' ', '_')}-{tag_colors.get(tag, 'lightgrey')})"
        for tag in tags
    )

def generate_table(progress):
    table_header = "### LeetCode Progress Tracker 📅\n"
    table_header += "|🎯 Problem ID |📌 Title |🏷️ Tags |⚡ Difficulty |📝 Solution |\n"
    table_header += "|--------------|---------|--------|--------------|------------|\n"

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
