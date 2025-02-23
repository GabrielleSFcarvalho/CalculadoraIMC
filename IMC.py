nome = input("Escreva seu nome: ")
altura = float(input("Escreva sua altura: "))
peso = float(input("Escreva seu peso: "))

imc = peso/ (altura **2)

txt = f"{nome} o seu IMC é {imc:.2f}. Classificação segundo a OMS:"
if imc < 18.5: print (txt, "Abaixo do peso normal") 
elif 18.5 <= imc <= 24.9: print(txt, "Peso normal")
elif imc < 25: print (txt, "Excesso de peso")
elif imc < 30: print(txt, "Obesidade classe 1")
elif 35 <= imc <= 39.9 : print (txt, "Obesidade classe 2") 
else: print(txt,"Obesidade classe 3")
 