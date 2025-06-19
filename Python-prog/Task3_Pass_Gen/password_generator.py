import random
import string

def get_user_preferences():
    print("🔐 Welcome to the Password Generator\n")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError
    except ValueError:
        print("❌ Invalid length. Please enter a positive integer.")
        exit()

    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").strip().lower() == 'y'

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("❌ No character types selected. Cannot generate password.")
        exit()

    return length, use_upper, use_lower, use_digits, use_symbols

def build_char_pool(use_upper, use_lower, use_digits, use_symbols):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return chars

def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

def evaluate_strength(password):
    length = len(password)
    if length < 6:
        return "Weak"
    elif length < 10:
        return "Medium"
    else:
        return "Strong"

def copy_to_clipboard(password):
    try:
        import pyperclip
        pyperclip.copy(password)
        print("📋 Password copied to clipboard!")
    except ImportError:
        print("⚠️ 'pyperclip' not installed. Clipboard copy skipped.")

def main():
    length, upper, lower, digits, symbols = get_user_preferences()
    char_pool = build_char_pool(upper, lower, digits, symbols)

    while True:
        password = generate_password(length, char_pool)
        strength = evaluate_strength(password)

        print(f"\n✅ Generated Password: {password}")
        print(f"🔎 Password Strength: {strength}")

        choice = input("Is this password okay? (y/n): ").strip().lower()
        if choice == 'y':
            copy_to_clipboard(password)
            print("🎉 Password finalized!")
            break
        else:
            print("🔁 Generating a new password...\n")

if __name__ == "__main__":
    main()
