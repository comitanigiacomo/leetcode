import os
import json
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def get_difficulty_and_tags(problem_name):
    problem_name = problem_name.lower().replace(' ', '-')
    
    data = {
        "operationName": "questionData",
        "variables": {"titleSlug": problem_name},
        "query": """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                difficulty
                topicTags {
                    name
                    slug
                }
            }
        }
        """
    }

    r = requests.post('https://leetcode.com/graphql', json=data).json()

    difficulty = r['data']['question']['difficulty'] if 'difficulty' in r['data']['question'] else "Unknown"

    tags = [tag['name'] for tag in r['data']['question']['topicTags']] if 'topicTags' in r['data']['question'] else []

    return difficulty, tags

def update_challenge(data, challenge_id, title, link, tags, difficulty, solution):
    data[challenge_id] = {
        "title": title,
        "link": link,
        "tags": tags,
        "difficulty": difficulty,
        "solution": solution
    }

def main():
    json_file = 'progress.json'
    
    data = load_json(json_file)

    repo_path = os.path.abspath("problems")


    for folder_name in os.listdir(repo_path):
        folder_path = os.path.join(repo_path, folder_name)

        if os.path.isdir(folder_path):
            challenge_id = folder_name.split('.')[0]
            
            title = ' '.join(folder_name.split('.')[1:])
            
            problem_name = folder_name.replace('.', '-')
            link = f"https://leetcode.com/problems/{problem_name}/description/"

            link = f"https://leetcode.com/problems/{'.'.join(folder_name.split('.')[1:]).replace('.', '-')}/description/"

            solution_file = None
            for file in os.listdir(folder_path):
                if file.startswith("Solution."):
                    solution_file = file
                    break

            solution = f"problems/{folder_name}/{solution_file}" if solution_file else "Unknown"

            try:
                difficulty, tags = get_difficulty_and_tags(title)
            except Exception as e:
                print(f"Errore nel recupero di {title}: {e}")
                difficulty, tags = "Unknown", []

            update_challenge(data, challenge_id, title, link, tags, difficulty, solution)

    save_json(data, json_file)
    print("JSON aggiornato con successo!")

if __name__ == "__main__":
    main()
