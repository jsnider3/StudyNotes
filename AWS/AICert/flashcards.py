#!/usr/bin/env python3

import random
import os
import sys
import argparse
import json
from typing import List, Tuple, Dict, Optional
from datetime import datetime

# Constants
CLEAR_COMMAND = 'cls' if os.name == 'nt' else 'clear'
DOMAINS_FILE = 'flashcards_data.json'
LOG_FILE = 'answer_log.jsonl'

def load_flashcards_data() -> List[Dict]:
    """Load flashcard data from the JSON file."""
    try:
        with open(DOMAINS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The data file '{DOMAINS_FILE}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not decode the JSON from '{DOMAINS_FILE}'. Please check its format.")
        sys.exit(1)

def get_domain_name_from_number(domain_number: int, domains: List[Dict]) -> Optional[str]:
    """Finds the full domain name string from its number."""
    if 1 <= domain_number <= len(domains):
        return domains[domain_number - 1]["name"]
    return None

def get_flashcards(domains: List[Dict], domain_number: Optional[int] = None, limit: Optional[int] = None, review_wrong: bool = False) -> List[Tuple[str, str]]:
    """
    Returns a list of (question, answer) tuples.
    - If review_wrong is True, it returns only questions the user previously got wrong.
    - If a domain_number is specified, it returns flashcards for that domain.
    - If no domain_number is specified, it returns a weighted random list of all flashcards.
    - If a limit is set, it returns that number of questions.
    """
    if review_wrong:
        return get_wrongly_answered_questions(limit)

    if domain_number:
        if 1 <= domain_number <= len(domains):
            cards = domains[domain_number - 1].get("cards", {})
            questions_list = list(cards.items())
            random.shuffle(questions_list)
        else:
            return []
    else:
        all_questions = []
        weights = []
        for domain_data in domains:
            weight = domain_data.get("weight", 1)
            for question, answer in domain_data.get("cards", {}).items():
                all_questions.append((question, answer))
                weights.append(weight)
        
        if not all_questions:
            return []
        
        num_to_sample = limit if limit and limit < len(all_questions) else len(all_questions)
        questions_list = random.choices(all_questions, weights=weights, k=num_to_sample)

    return questions_list[:limit] if limit else questions_list

def log_answer(question: str, correct_answer: str, user_answer: str, assessment: str):
    """Logs the user's answer to the log file."""
    log_record = {
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "correct_answer": correct_answer,
        "user_answer": user_answer,
        "assessment": assessment
    }
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(log_record) + '\n')

def get_wrongly_answered_questions(limit: Optional[int] = None) -> List[Tuple[str, str]]:
    """Processes the log file to get questions the user has marked as 'wrong'."""
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return []

    # Use a dictionary to track the last assessment for each question
    last_assessments = {}
    for line in lines:
        record = json.loads(line)
        last_assessments[record['question']] = {
            "assessment": record['assessment'],
            "answer": record['correct_answer']
        }

    # Filter for questions last marked as 'wrong'
    wrong_questions = [
        (q, d['answer']) for q, d in last_assessments.items() if d['assessment'] == 'wrong'
    ]
    
    random.shuffle(wrong_questions)
    return wrong_questions[:limit] if limit else wrong_questions

def clear_screen():
    """Clears the terminal screen if in interactive mode."""
    if sys.stdout.isatty():
        os.system(CLEAR_COMMAND)

def interactive_mode(domains: List[Dict], domain_number: Optional[int] = None, limit: Optional[int] = None, review_wrong: bool = False):
    """Runs the flashcard app in interactive mode with scoring."""
    clear_screen()
    
    session_type = "Review Weakest Questions" if review_wrong else "All Domains"
    domain_name = get_domain_name_from_number(domain_number, domains) if domain_number else session_type
    
    questions_list = get_flashcards(domains, domain_number, limit, review_wrong)
    
    if not questions_list:
        print("Error: No flashcards available for the selected criteria!")
        if review_wrong:
            print("You haven't marked any questions as wrong yet, or the log file is empty. Keep studying!")
        return

    total = len(questions_list)
    correct_answers = 0
    
    print(f"=== AWS AI Certification Flashcard App ({domain_name}) ===")
    print(f"Studying {total} questions. Type 'q' to quit.")
    print("-" * 60)
    
    try:
        for i, (question, answer) in enumerate(questions_list, 1):
            print(f"Question {i}/{total}: {question}")
            user_answer = input("\nYour answer (press Enter to reveal): ")
            
            print(f"\nCorrect Answer: {answer}")
            
            while True:
                feedback = input("\nWere you correct? (y/n/q): ").strip().lower()
                if feedback in ['y', 'n', 'q']:
                    break
                print("Invalid input. Please enter 'y', 'n', or 'q'.")

            if feedback == 'y':
                correct_answers += 1
                log_answer(question, answer, user_answer, "correct")
            elif feedback == 'n':
                log_answer(question, answer, user_answer, "wrong")
            elif feedback == 'q':
                break
            
            clear_screen()
        
        print("\n=== Study Session Complete ===")
        score = (correct_answers / total) * 100 if total > 0 else 0
        print(f"You answered {correct_answers} out of {total} questions correctly ({score:.2f}%).")
        
        restart = input("\nRestart session? (y/n): ").strip().lower()
        if restart == 'y':
            interactive_mode(domains, domain_number, limit, review_wrong)
        else:
            print("\nGood luck with your certification!")
            
    except KeyboardInterrupt:
        print("\n\nSession interrupted. Keep up the good work!")

def non_interactive_mode(domains: List[Dict], shuffle: bool = False, domain_number: Optional[int] = None, limit: Optional[int] = None):
    """Runs the flashcard app in non-interactive mode."""
    domain_name = get_domain_name_from_number(domain_number, domains) if domain_number else "All Domains"
    if domain_number and not domain_name:
        print(f"Error: Domain {domain_number} not found.")
        return

    questions_list = get_flashcards(domains, domain_number, limit)
    
    if not questions_list:
        print("Error: No flashcards available for the selected criteria!")
        return
        
    if shuffle:
        random.shuffle(questions_list)
    
    print(f"=== AWS AI Certification Flashcards ({domain_name}) ===")
    if shuffle:
        print("(Questions shuffled)")
    print("-" * 60)
    
    for question, answer in questions_list:
        print(f"Q: {question}")
        print(f"A: {answer}\n")
        print("-" * 60)

def main():
    """Main function to run the flashcard app."""
    domains = load_flashcards_data()
    
    parser = argparse.ArgumentParser(
        description='AWS AI Certification Flashcard Tool',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('-i', '--interactive', action='store_true', help='Run in interactive mode with scoring.')
    mode_group.add_argument('-n', '--non-interactive', action='store_true', help='Run in non-interactive (print) mode.')
    mode_group.add_argument('--review-wrong', action='store_true', help='Review questions you previously answered incorrectly.')

    parser.add_argument('--shuffle', action='store_true', help='Shuffle questions in non-interactive mode.')
    parser.add_argument('-l', '--limit', type=int, help='Limit the number of questions in the session.')
    
    domain_help_text = "Select a specific domain to study:\n"
    for i, domain_data in enumerate(domains, 1):
        name = domain_data['name']
        weight = domain_data['weight']
        domain_help_text += f"  {i}: {name} ({weight}%%)\n"
        
    parser.add_argument('--domain', type=int, choices=range(1, len(domains) + 1), help=domain_help_text)
    args = parser.parse_args()

    try:
        is_interactive = args.interactive or args.review_wrong or (not args.non_interactive and sys.stdout.isatty())

        if is_interactive:
            interactive_mode(domains, domain_number=args.domain, limit=args.limit, review_wrong=args.review_wrong)
        else:
            non_interactive_mode(domains, shuffle=args.shuffle, domain_number=args.domain, limit=args.limit)
            
    except KeyboardInterrupt:
        print("\n\nStudy session interrupted. Good luck with your certification!")

if __name__ == "__main__":
    main()
