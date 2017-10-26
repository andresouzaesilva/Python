string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
tam1 = str.__len__(string1)
tam2 = str.__len__(string2)
print("String 1: %s" %string1)
print("String 2: %s" %string2)
print("Tamanho de ''%s'' : %d caracteres" %(string1,tam1))
print("Tamanho de ''%s'' : %d caracteres" %(string2,tam2))
if tam1 == tam2:
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")
if string1 == string2:
    print("As duas strings possuem conteúdo iguais.")
else:
    print("As duas strings possuem conteúdo diferentes.")

