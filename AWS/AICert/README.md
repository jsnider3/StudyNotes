# AWS AI Certification Study Notes

This repository contains study materials for the AWS Certified AI Practitioner (AIF-C01) certification.

## Contents

*   **flashcards.py**: A command-line tool for reviewing key concepts across the certification domains.

## Usage

### Flashcards

To use the flashcard script, run it from your terminal:

```bash
python3 flashcards.py
```

By default, it runs in an interactive mode that presents questions from all domains based on their weighted importance in the exam.

#### Options

*   **Interactive Mode**: `python3 flashcards.py -i`
*   **Non-Interactive Mode**: `python3 flashcards.py -n` (prints all questions and answers)
*   **Select a Domain**: `python3 flashcards.py --domain <number>` (e.g., `--domain 1`)
*   **Shuffle Questions**: `python3 flashcards.py --shuffle` (for non-interactive mode)

For more details, run:
```bash
python3 flashcards.py --help
```
