from ..Logic.main import *


def test_function_convert_to_eng():
    assert convert_to_english(".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--") == ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D', '!']


def test_function_convert_to_morse():
    assert convert_to_morse("Hello World!".upper()) == ['....', '.', '.-..', '.-..', '---', '/', '.--', '---', '.-.', '.-..', '-..', '-.-.--']


def main():
    test_function_convert_to_morse()
    test_function_convert_to_eng()


if __name__ == '__main__':
    main()