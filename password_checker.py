import re
import string
import sys
from typing import List, Tuple


def _length_points(pwd: str) -> int:
    """Return length-based points (0–3)."""
    n = len(pwd)
    if n >= 16:
        return 3
    if n >= 12:
        return 2
    if n >= 8:
        return 1
    return 0

def evaluate_password(pwd: str) -> Tuple[int, str, List[str]]:
    """Return (score, label, suggestions). Total score is 0–11."""
    checks = {
        "lowercase": bool(re.search(r"[a-z]", pwd)),
        "uppercase": bool(re.search(r"[A-Z]", pwd)),
        "digit": bool(re.search(r"\d", pwd)),
        "special": bool(re.search(rf"[{re.escape(string.punctuation)}]", pwd)),
    }

    char_points = sum(2 for ok in checks.values() if ok)  # 0–8
    len_points = _length_points(pwd)                      # 0–3
    score = char_points + len_points                      # 0–11

    if score <= 3:
        label = "Weak"
    elif score <= 6:
        label = "Fair"
    elif score <= 8:
        label = "Strong"
    else:
        label = "Very Strong"

    suggestions: List[str] = []
    if not checks["lowercase"]:
        suggestions.append("Add lowercase letters.")
    if not checks["uppercase"]:
        suggestions.append("Add uppercase letters.")
    if not checks["digit"]:
        suggestions.append("Include digits (0–9).")
    if not checks["special"]:
        suggestions.append("Add special characters (e.g., !@#$%).")
    if len_points < 2:
        suggestions.append("Increase password length to at least 12 characters.")

    return score, label, suggestions


def _cli() -> None:
    """Evaluate a password provided as CLI arg or via visible input prompt."""
    if len(sys.argv) > 1:
        pwd = sys.argv[1]
    else:
        pwd = input("Enter password to evaluate: ")

    score, label, suggestions = evaluate_password(pwd)

    print(f"Score: {score}/11")
    print(f"Strength: {label}")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f" – {s}")

if __name__ == "__main__":
    _cli()
