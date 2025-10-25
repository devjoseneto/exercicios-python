def eh_palindromo(text):
    clean_text = ''.join(text.lower().split())
    return clean_text == clean_text[::-1]

print(eh_palindromo('Ovo'))
print(eh_palindromo('Carro'))