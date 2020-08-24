cpdia = int(input("Cigarros por dia: "))
afumo = int(input("Anos de fumante: "))*365

totfumo = cpdia * afumo

minfumo = ((totfumo * 10)/60)/24

print("Dias perdidos: %d"%minfumo)



