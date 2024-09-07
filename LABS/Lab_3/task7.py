def correct_sentence():
    try:
        f = open("Lab_3/replacement_needed.txt")
        content = f.read()
        f.close()
        print(f"Original content: {content}")
        word = input("Enter Word to Change: ")
        old_char = input("Enter character to Change: ")
        new_char = input("Enter new character: ")
        new_word = word.replace(old_char,new_char)
        corrected_content = content.replace(word,new_word)

        print(f"Corrected content: {corrected_content}")
        return corrected_content

    except FileNotFoundError:
        print("The file 'replacement_needed.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

correct_sentence()
