def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_count = 0
    total_words = len(translations)
    
    for english_word, spanish_word in translations.items():
        user_answer = input("What is the Spanish translation for "+ english_word +"?").strip().lower()
        if user_answer == spanish_word:
            print("That is correct!")
            print()
            correct_count += 1
        else:
            print("That is incorrect, the Spanish translation for "+ english_word+" is "+ spanish_word+".")
            print()
    print("You got "+ str(correct_count)+"/"+str(total_words) + " words correct, come study again soon!")

if __name__ == '__main__':
    main()
