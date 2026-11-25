import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Make the password at least 8 characters long (12+ recommended).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\/'~`;]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., @, #, $, %, &).")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, score, feedback


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to evaluate: ")

    if not password:
        print("Error: Password cannot be empty.")
        return

    strength, score, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength} (Score: {score}/6)")

    if feedback:
        print("\nSuggestions to improve security:")
        for tip in feedback:
            print(f" - {tip}")
    else:
        print("\nGreat job! Your password meets all security criteria.")


if __name__ == "__main__":
    main()
