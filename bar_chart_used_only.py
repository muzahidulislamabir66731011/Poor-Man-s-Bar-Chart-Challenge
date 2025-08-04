import string

def poor_man_bar_chart(text: str) -> str:
    text = text.lower()
    letter_counts = {}  # Start with an empty dictionary
    for letter in string.ascii_lowercase:
        letter_counts[letter] = 0

    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1

    result_lines = []
    for letter in string.ascii_lowercase:
        result_lines.append(f"{letter}: {letter_counts[letter] * '#'}")

    return '\n'.join(result_lines)

def main():
    while True:
        try:
            text = input("Write a text (press q to quit): ").strip()
            if text.lower() == "q":
                break

            if not text.replace(" ", "").isalpha():
                raise ValueError("Please enter letters only, no numbers or symbols.")

            print(poor_man_bar_chart(text))

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()