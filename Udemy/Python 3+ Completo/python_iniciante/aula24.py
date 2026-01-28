# Aula 24 -> Operadores in e not in

phrase = input("Type a phrase: ")
search_term = input("Type a search term: ")

if search_term in phrase:
    print(f"The term '{search_term}' was found in the phrase '{phrase}'.")
elif search_term not in phrase: # ou simplesmente 'else:'
    print(f"The term '{search_term}' was NOT found in the phrase '{phrase}'.")