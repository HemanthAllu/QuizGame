def word_count(text):
    # Implement word counting logic here
    words = text.split()
    return len(words)

def main():
    print("Welcome to Word Counter!")
    user_input = input("Please enter a sentence or paragraph: ")

    # Check for empty input
    if not user_input.strip():
        print("Error: Input cannot be empty.")
        return

    # Calculate word count
    count = word_count(user_input)

    # Display output
    print(f"Word count: {count}")

if __name__ == "__main__":
    main()
