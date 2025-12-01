from ..Logic.main import *


def test_function_convert_to_eng():
    assert convert_to_english(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. / .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----") == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], "convert_to_eng function did not output the expected result".upper()


def test_function_convert_to_morse():
    assert convert_to_morse("abcdefghijklmnopqrstuvwxyz 1234567890".upper()) == ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '/', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----'], "convert_to_morse function did not output the expected result".upper()


def test_IDK_in_both_functions():
    assert convert_to_english("---------") == ["IDK"]
    assert convert_to_morse("◙") == ["IDK"], "if ValueError: empty separator, Solution: components/Logic/main.py  fix the Statment user_input.split() maybe the separator is changed just put \" \"" 


def main():
    test_function_convert_to_morse()
    test_function_convert_to_eng()
    test_IDK_in_both_functions()


if __name__ == '__main__':
    main()