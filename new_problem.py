import sys
import os
import re
import requests
import json

PROBLEMS_DIR = "problems"
SOLUTION_FILENAME = "Solution.py"
DEFAULT_LANG_SLUG = "python3"

def get_daily_challenge():
    query = """
    query questionOfToday {
        activeDailyCodingChallengeQuestion {
            question {
                questionFrontendId
                title
                titleSlug
            }
        }
    }
    """
    
    payload = {
        "operationName": "questionOfToday",
        "variables": {},
        "query": query
    }
        
    try:
        response = requests.post('https://leetcode.com/graphql', json=payload)
        response.raise_for_status()
        data = response.json()

        question_data = data.get("data", {}).get("activeDailyCodingChallengeQuestion")
        
        if not question_data or not question_data.get("question"):
            return None, None, None

        question = question_data["question"]
        problem_id = question["questionFrontendId"]
        problem_title = question["title"]
        api_slug = question["titleSlug"]
        
        return problem_id, problem_title, api_slug

    except requests.exceptions.RequestException as e:
        print(f"Errore API LeetCode: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response is not None:
             print(f"Dettagli risposta: {e.response.text}", file=sys.stderr)
        return None, None, None
    except json.JSONDecodeError:
        return None, None, None

def get_problem_boilerplate(title_slug):
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            codeSnippets {
                langSlug
                code
            }
        }
    }
    """
    
    variables = {"titleSlug": title_slug}
    payload = {
        "operationName": "questionData",
        "variables": variables,
        "query": query
    }
    
    
    try:
        response = requests.post('https://leetcode.com/graphql', json=payload)
        response.raise_for_status()
        data = response.json()

        if data.get("data", {}).get("question") is None:
            print(f"Errore: Problema non trovato con slug '{title_slug}'.", file=sys.stderr)
            return None

        snippets = data["data"]["question"]["codeSnippets"]
        for snippet in snippets:
            if snippet["langSlug"] == DEFAULT_LANG_SLUG:
                return snippet["code"]
        
        print(f"Attenzione: Boilerplate '{DEFAULT_LANG_SLUG}' non trovato.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Errore durante il recupero del boilerplate: {e}", file=sys.stderr)
        return None

def slugify_folder_name(title):
    slug = title.lower()
    slug = re.sub(r'[^\w\s]', '', slug)
    slug = re.sub(r'\s+', '.', slug).strip()
    return slug

def main():
    problem_id, problem_title, api_slug = get_daily_challenge()
    
    if not problem_id:
        sys.exit(1)

    folder_slug = slugify_folder_name(problem_title)
    folder_name = f"{problem_id}.{folder_slug}"
    dir_path = os.path.join(PROBLEMS_DIR, folder_name)
    file_path = os.path.join(dir_path, SOLUTION_FILENAME)

    if os.path.exists(dir_path):
        print(file_path)
        sys.exit(0)

    boilerplate_code = get_problem_boilerplate(api_slug)
    if boilerplate_code is None:
        boilerplate_code = "class Solution:\n    def solve(self):\n        pass\n"

    try:
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(boilerplate_code)
        
        print(file_path) 

    except OSError as e:
        print(f"Errore OS: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()