"""
CAPSTONE 16 - simple terminal viva practice demo
Run: python viva_practice_demo.py
This is a prototype. Answers are scored with a small keyword heuristic, not a validated AI grader.
"""
import csv, random
from pathlib import Path

BANK = Path(__file__).with_name("Viva_Question_Bank.csv")

def load_bank():
    with BANK.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # Only use answers after a human has verified them and changed Status to PASS.
    return [r for r in rows if r["Status"].strip().upper() == "PASS"]

def main():
    bank = load_bank()
    if not bank:
        print("No approved questions yet. Verify the CSV against your official manual, then mark approved rows PASS.")
        return
    print("ECE Viva Practice — type 'quit' to stop.")
    score = 0
    random.shuffle(bank)
    for n, item in enumerate(bank, 1):
        print(f"\\nQ{n}: {item['Question']}")
        attempt = input("Your answer: ").strip()
        if attempt.lower() == "quit":
            break
        # Prototype heuristic: compare a few answer terms; teacher review is recommended.
        keywords = [w.lower().strip(".,():;") for w in item["ModelAnswer"].split()
                    if len(w.strip(".,():;")) >= 5][:8]
        hits = sum(1 for w in set(keywords) if w in attempt.lower())
        points = 2 if hits >= 3 else (1 if hits >= 1 else 0)
        score += points
        print(f"Prototype score: {points}/2")
        print("Model answer:", item["ModelAnswer"])
        print("Feedback: compare your answer with the key concepts above; keyword scoring can miss correct paraphrases.")
    print(f"Session score: {score} points (rough prototype score, not a formal assessment).")

if __name__ == "__main__":
    main()
