import os
import json
import requests
from bs4 import BeautifulSoup

# Funzione per caricare il file JSON esistente
def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Funzione per salvare il file JSON
def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Funzione per ottenere la difficoltà e i tag da LeetCode
def get_difficulty_and_tags(problem_name):
    url = f"https://leetcode.com/problems/{problem_name}/description/"
    response = requests.get(url)

    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trova la difficoltà
    difficulty_div = soup.find('div', {'class': 'difficulty'})
    difficulty = difficulty_div.text.strip() if difficulty_div else "Unknown"

    # Trova i tag
    tags = [tag.text.strip() for tag in soup.find_all('a', {'class': 'tag__2hMI5H'})]

    return difficulty, tags

# Funzione per aggiornare un problema nel JSON
def update_challenge(data, challenge_id, title, link, tags, difficulty, solution):
    data[challenge_id] = {
        "title": title,
        "link": link,
        "tags": tags,
        "difficulty": difficulty,
        "solution": solution
    }

# Funzione principale per iterare sulle cartelle e aggiornare il JSON
def main():
    # Nome del file JSON da aggiornare
    json_file = 'progress.json'
    
    # Carica il JSON esistente
    data = load_json(json_file)

    # Percorso alla root della tua repo
    repo_path = '/home/giacomocomitani/personale/leetcode/problems'

    # Itera su tutte le cartelle del repository
    for folder_name in os.listdir(repo_path):
        folder_path = os.path.join(repo_path, folder_name)

        # Verifica che sia una cartella
        if os.path.isdir(folder_path):
            # Estrai l'ID (numero) dalla cartella, prima del primo punto
            challenge_id = folder_name.split('.')[0]
            
            # Costruisci il title, rimuovendo il numero e il primo punto, e sostituendo i punti con gli spazi
            title = ' '.join(folder_name.split('.')[1:])
            
            # Costruisci il link per il problema LeetCode
            problem_name = folder_name.replace('.', '-')
            link = f"https://leetcode.com/problems/{problem_name}/description/"

            # Costruisci il link, sostituendo i punti con i trattini
            link = f"https://leetcode.com/problems/{'.'.join(folder_name.split('.')[1:]).replace('.', '-')}/description/"

            # Nome della soluzione
            # Cerca automaticamente il file Solution con qualsiasi estensione
            solution_file = None
            for file in os.listdir(folder_path):
                if file.startswith("Solution."):
                    solution_file = file
                    break

            # Se trovi un file di soluzione, costruisci il percorso
            solution = f"problems/{folder_name}/{solution_file}" if solution_file else "Unknown"

            # Ottieni difficoltà e tag
            try:
                difficulty, tags = get_difficulty_and_tags(title)
            except Exception as e:
                print(f"Errore nel recupero di {title}: {e}")
                difficulty, tags = "Unknown", []

            # Aggiungi o aggiorna il problema nel JSON
            update_challenge(data, challenge_id, title, link, tags, difficulty, solution)

    # Salva il JSON aggiornato
    save_json(data, json_file)
    print("JSON aggiornato con successo!")

if __name__ == "__main__":
    main()
