# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  #  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# lista sortată în ordine crescătoare
ascendent = sorted(lista)
print("Lista ordonata cresc: ", ascendent)

# lista sortată în ordine descrescătoare
descendent = sorted(lista, reverse=True)
print("Lista ordonata descr: ", descendent)

# numerele cu indici pari
pari = lista[::2]
print("Numerele cu indici pari: ", pari)

# numerele cu indici impari
impari = lista[1::2]
print("Numerele cu indici impari: ", impari)

# elementele multipli ai lui 3
multipli_3 = [nr for nr in lista if nr % 3 == 0]
print("Elementele multipli ai lui 3: ", multipli_3)

