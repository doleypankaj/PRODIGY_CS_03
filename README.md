# PRODIGY_CS_03

# Password Strength Checker

A lightweight Python utility that **scores and classifies password strength** while offering actionable feedback to improve weak passwords. It can be run directly from the command line or imported as a library.

---

## ✨ Features

| Feature                    | Details                                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Comprehensive scoring**  | Evaluates length, lowercase, uppercase, digits, and special characters for a score out of **11**       |
| **Human‑readable labels**  | Categorises results as *Weak*, *Fair*, *Strong*, or *Very Strong*                                      |
| **Actionable suggestions** | Tells users exactly how to strengthen their password                                                   |
| **Flexible input**         | Accepts a password via CLI argument or interactive prompt (characters **visible** for demo simplicity) |
| **Embeddable**             | Expose a single `evaluate_password()` function for use in other Python projects                        |

---

## 🚀 Quick Start

> **Prerequisite:** Python 3.8 +

```bash
# Clone or copy the file
python password_strength_checker.py "MyP@ssw0rd!"
```

If you omit the argument, you'll be prompted:

```text
$ python password_strength_checker.py
Enter password to evaluate (visible): hunter2
Score: 3/11
Strength: Weak
Suggestions:
 – Add uppercase letters.
 – Add special characters (e.g., !@#$%).
 – Increase password length to at least 12 characters.
```

---

## 📚 Library Usage

```python
from password_strength_checker import evaluate_password

score, label, advice = evaluate_password("CorrectHorseBatteryStaple!")
print(score, label)
for tip in advice:
    print("•", tip)
```

---

## 🔢 Scoring Logic (0–11)

| Criterion        | Points |
| ---------------- | ------ |
| Length ≥ 16      | 3      |
| Length ≥ 12      | 2      |
| Length ≥ 8       | 1      |
| Lowercase \[a‑z] | 2      |
| Uppercase \[A‑Z] | 2      |
| Digits \[0‑9]    | 2      |
| Special chars    | 2      |

*0–3 → Weak  4–6 → Fair  7–8 → Strong  9–11 → Very Strong*

---

## 🛠️ Extending / Customising

* **Entropy‑based metric:** Replace the simple class‑point system with Shannon entropy for more precision.
* **Masked input:** Swap `input()` for `getpass.getpass()` and expose a `--visible` flag.
* **GUI/Web front‑end:** Wrap the core function in a Tkinter, PyQT, or Flask interface.
* **Dictionary blacklist:** Cross‑check against common password lists (e.g., `rockyou.txt`).

PRs are welcome! 🥳

---

## 🙋 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is released under the MIT License — see `LICENSE` for details.
