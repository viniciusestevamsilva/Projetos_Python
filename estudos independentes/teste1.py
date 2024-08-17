# Autor: Vinícius Estevam da Silva
# Projeto bem simple, feito apenas para passar o tempo, com ajuda do chat gpt
# 16/08/2024
import os

os.system('cls')

# Dicionário para codificação e decodificação Morse
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '@': '.--.-', ' ': '/'
}

# Inverter o dicionário para decodificação
morse_code_dict_rev = {v: k for k, v in morse_code_dict.items()}

def text_to_morse(text):
    """Converte um texto em código Morse"""
    text = text.upper()
    morse_code = ''
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code += '/ '
        else:
            morse_code += '? '
    return morse_code.strip()

def morse_to_text(morse_code):
    """Converte um código Morse em texto"""
    words = morse_code.split(' / ')
    decoded_message = ''
    
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in morse_code_dict_rev:
                decoded_message += morse_code_dict_rev[letter]
            else:
                decoded_message += '?'
        decoded_message += ' '
    
    return decoded_message.strip()

# Função principal para interação com o usuário

print("Tradutor de Código Morse")
print("1: Texto para Morse")
print("2: Morse para Texto")
choice = input("Escolha uma opção (1 ou 2): ")

if choice == '1':
    text = input("Digite o texto para converter em código Morse: ")
    encoded = text_to_morse(text)
    print(f"Texto em Código Morse: {encoded}")
elif choice == '2':
    morse_code = input("Digite o código Morse para converter em texto: ")
    decoded = morse_to_text(morse_code)
    print(f"Código Morse em Texto: {decoded}")
else:
    print("Opção inválida!")
# kira
#