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
    tag_badges = {
        "Array": "![Array](https://img.shields.io/badge/-Array-blue)",
        "String": "![String](https://img.shields.io/badge/-String-green)",
        "Hash Table": "![Hash Table](https://img.shields.io/badge/-Hash_Table-orange)",
        "Dynamic Programming": "![Dynamic Programming](https://img.shields.io/badge/-Dynamic_Programming-red)",
        "Math": "![Math](https://img.shields.io/badge/-Math-purple)",
        "Sorting": "![Sorting](https://img.shields.io/badge/-Sorting-yellow)",
        "Greedy": "![Greedy](https://img.shields.io/badge/-Greedy-brightgreen)",
        "Depth-First Search": "![Depth-First Search](https://img.shields.io/badge/-Depth_First_Search-blueviolet)",
        "Binary Search": "![Binary Search](https://img.shields.io/badge/-Binary_Search-dodgerblue)",
        "Database": "![Database](https://img.shields.io/badge/-Database-darkblue)",
        "Matrix": "![Matrix](https://img.shields.io/badge/-Matrix-brown)",
        "Tree": "![Tree](https://img.shields.io/badge/-Tree-forestgreen)",
        "Breadth-First Search": "![Breadth-First Search](https://img.shields.io/badge/-Breadth_First_Search-lightblue)",
        "Bit Manipulation": "![Bit Manipulation](https://img.shields.io/badge/-Bit_Manipulation-darkgreen)",
        "Two Pointers": "![Two Pointers](https://img.shields.io/badge/-Two_Pointers-darkred)",
        "Prefix Sum": "![Prefix Sum](https://img.shields.io/badge/-Prefix_Sum-darkmagenta)",
        "Heap (Priority Queue)": "![Heap (Priority Queue)](https://img.shields.io/badge/-Heap_Priority_Queue-darkcyan)",
        "Binary Tree": "![Binary Tree](https://img.shields.io/badge/-Binary_Tree-darkorange)",
        "Simulation": "![Simulation](https://img.shields.io/badge/-Simulation-olive)",
        "Stack": "![Stack](https://img.shields.io/badge/-Stack-lightgreen)",
        "Graph": "![Graph](https://img.shields.io/badge/-Graph-lightcoral)",
        "Counting": "![Counting](https://img.shields.io/badge/-Counting-lightsalmon)",
        "Sliding Window": "![Sliding Window](https://img.shields.io/badge/-Sliding_Window-lightseagreen)",
        "Design": "![Design](https://img.shields.io/badge/-Design-lightskyblue)",
        "Enumeration": "![Enumeration](https://img.shields.io/badge/-Enumeration-lightsteelblue)",
        "Backtracking": "![Backtracking](https://img.shields.io/badge/-Backtracking-lightyellow)",
        "Union Find": "![Union Find](https://img.shields.io/badge/-Union_Find-lightpink)",
        "Linked List": "![Linked List](https://img.shields.io/badge/-Linked_List-lavender)",
        "Number Theory": "![Number Theory](https://img.shields.io/badge/-Number_Theory-thistle)",
        "Ordered Set": "![Ordered Set](https://img.shields.io/badge/-Ordered_Set-plum)",
        "Monotonic Stack": "![Monotonic Stack](https://img.shields.io/badge/-Monotonic_Stack-violet)",
        "Segment Tree": "![Segment Tree](https://img.shields.io/badge/-Segment_Tree-orchid)",
        "Trie": "![Trie](https://img.shields.io/badge/-Trie-mediumpurple)",
        "Combinatorics": "![Combinatorics](https://img.shields.io/badge/-Combinatorics-slateblue)",
        "Bitmask": "![Bitmask](https://img.shields.io/badge/-Bitmask-royalblue)",
        "Queue": "![Queue](https://img.shields.io/badge/-Queue-cornflowerblue)",
        "Divide and Conquer": "![Divide and Conquer](https://img.shields.io/badge/-Divide_and_Conquer-deepskyblue)",
        "Recursion": "![Recursion](https://img.shields.io/badge/-Recursion-skyblue)",
        "Memoization": "![Memoization](https://img.shields.io/badge/-Memoization-powderblue)",
        "Binary Indexed Tree": "![Binary Indexed Tree](https://img.shields.io/badge/-Binary_Indexed_Tree-paleturquoise)",
        "Geometry": "![Geometry](https://img.shields.io/badge/-Geometry-lightcyan)",
        "Binary Search Tree": "![Binary Search Tree](https://img.shields.io/badge/-Binary_Search_Tree-mintcream)",
        "Hash Function": "![Hash Function](https://img.shields.io/badge/-Hash_Function-honeydew)",
        "String Matching": "![String Matching](https://img.shields.io/badge/-String_Matching-azure)",
        "Topological Sort": "![Topological Sort](https://img.shields.io/badge/-Topological_Sort-aliceblue)",
        "Shortest Path": "![Shortest Path](https://img.shields.io/badge/-Shortest_Path-ghostwhite)",
        "Rolling Hash": "![Rolling Hash](https://img.shields.io/badge/-Rolling_Hash-whitesmoke)",
        "Game Theory": "![Game Theory](https://img.shields.io/badge/-Game_Theory-gainsboro)",
        "Interactive": "![Interactive](https://img.shields.io/badge/-Interactive-lightgray)",
        "Data Stream": "![Data Stream](https://img.shields.io/badge/-Data_Stream-silver)",
        "Monotonic Queue": "![Monotonic Queue](https://img.shields.io/badge/-Monotonic_Queue-darkgray)",
        "Brainteaser": "![Brainteaser](https://img.shields.io/badge/-Brainteaser-gray)",
        "Randomized": "![Randomized](https://img.shields.io/badge/-Randomized-dimgray)",
        "Merge Sort": "![Merge Sort](https://img.shields.io/badge/-Merge_Sort-black)",
        "Doubly-Linked List": "![Doubly-Linked List](https://img.shields.io/badge/-Doubly_Linked_List-rosybrown)",
        "Counting Sort": "![Counting Sort](https://img.shields.io/badge/-Counting_Sort-indianred)",
        "Iterator": "![Iterator](https://img.shields.io/badge/-Iterator-firebrick)",
        "Concurrency": "![Concurrency](https://img.shields.io/badge/-Concurrency-brown)",
        "Probability and Statistics": "![Probability and Statistics](https://img.shields.io/badge/-Probability_and_Statistics-maroon)",
        "Quickselect": "![Quickselect](https://img.shields.io/badge/-Quickselect-darkred)",
        "Suffix Array": "![Suffix Array](https://img.shields.io/badge/-Suffix_Array-sienna)",
        "Bucket Sort": "![Bucket Sort](https://img.shields.io/badge/-Bucket_Sort-saddlebrown)",
        "Line Sweep": "![Line Sweep](https://img.shields.io/badge/-Line_Sweep-chocolate)",
        "Minimum Spanning Tree": "![Minimum Spanning Tree](https://img.shields.io/badge/-Minimum_Spanning_Tree-peru)",
        "Shell": "![Shell](https://img.shields.io/badge/-Shell-goldenrod)",
        "Reservoir Sampling": "![Reservoir Sampling](https://img.shields.io/badge/-Reservoir_Sampling-darkgoldenrod)",
        "Strongly Connected Component": "![Strongly Connected Component](https://img.shields.io/badge/-Strongly_Connected_Component-tan)",
        "Eulerian Circuit": "![Eulerian Circuit](https://img.shields.io/badge/-Eulerian_Circuit-burlywood)",
        "Radix Sort": "![Radix Sort](https://img.shields.io/badge/-Radix_Sort-beige)",
        "Rejection Sampling": "![Rejection Sampling](https://img.shields.io/badge/-Rejection_Sampling-white)",
        "Biconnected Component": "![Biconnected Component](https://img.shields.io/badge/-Biconnected_Component-lightgrey)"
    }
    return " ".join(
        tag_badges.get(tag, f"![{tag}](https://img.shields.io/badge/-{tag}-lightgrey)") for tag in tags
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
