def correct_sentence():
    try:
        f = open("Lab_3/replacement_needed.txt")
        content = f.read()
        f.close()
        print(f"Original content: {content}")
        
        corrected_content = content.replace('N', 'M')

        print(f"Corrected content: {corrected_content}")
        return corrected_content

    except FileNotFoundError:
        print("The file 'replacement_needed.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

correct_sentence()
