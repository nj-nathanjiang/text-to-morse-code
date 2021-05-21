print("Welcome to the Text to Morse Code Converter! Please enter only letters, spaces, numbers and punctuation marks/basic symbols.")
text_to_morse_code = {"a": ".-",
                      "b": "-...",
                      "c": "-.-.",
                      "d": "-..",
                      "e": ".",
                      "f": "..-.",
                      "g": "--.",
                      "h": "....",
                      "i": "..",
                      "j": ".---",
                      "k": "-.-",
                      "l": ".-..",
                      "m": "--",
                      "n": "-.",
                      "o": "---",
                      "p": ".--.",
                      "q": "--.-",
                      "r": ".-.",
                      "s": "...",
                      "t": "-",
                      "u": "..-",
                      "v": "...-",
                      "w": ".--",
                      "x": "-..-",
                      "y": "-.--",
                      "z": "--..",
                      " ": "/",
                      "1": ".----",
                      "2": "..---",
                      "3": "...--",
                      "4": "....-",
                      "5": ".....",
                      "6": "-....",
                      "7": "--...",
                      "8": "---..",
                      "9": "----.",
                      "0": "-----",
                      ".": ".-.-.-",
                      ",": "--..--",
                      "?": "..--..",
                      "'": ".----.",
                      "!": "-.-.--",
                      "/": "-..-.",
                      "(": "-.--.",
                      ")": "-.--.-",
                      "&": ".-...",
                      ":": "---...",
                      ";": "-.-.-.",
                      "=": "-...-",
                      "+": ".-.-.",
                      "-": "-....-",
                      "_": "..--.-",
                      '"': ".-..-.",
                      "$": "...-..-",
                      "@": ".--.-."}

program_on = True
while program_on:
    text = input("Enter your text. Enter exit to exit this morse code_converter: ")
    if text == "exit":
        program_on = False
        break

    try:
        list_of_morse_code = [text_to_morse_code[char.lower()] for char in list(text)]
        output = ""
        index = 1
        for morse in list_of_morse_code:
            if index != 1:
                output += f" {morse}"
            else:
                output += morse
            index += 1
        print(f"This is your morse code: {output}")
    except KeyError:
        output = "Sorry, a character in your text was not a letter, number, whitespace, punctuation mark, or simple symbol."
        print(output)

print("Bye, see you again.")
