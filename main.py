print("Calculadra da Lei de Ohm")
while(1):
  print("Escolha as opções a seguir: ")
  print("1. Calcular Tensão.")
  print("2. Calcular Corrente.")
  print("3. Calcular Resistência.")
  print("4. Outra Opção Pra Desistir.")
  opcao = input(">: ")

  if (opcao == "1"):
    print("Calculando Tensão")
    i=float(input("A Corrente:"))
    r=float(input("A Resistência"))
    v=i*r      #v = tensão ; u = tensão ; i = corrente ; r = resistencia
    print("A Tensão é ",format(v,".2f"))

  elif (opcao == "2"):
    print("Calculando Resistência")
    v=float(input("A Tensão: "))
    i=float(input("A Corrente: "))
    r=v/i
    print("A Resistência é ",format(r,".2f"))
  elif (opcao == "3"):
    print("Calculando Corrente")
    v=float(input("A Tensão: "))
    r=float(input("A Resistência: "))
    i=v/r
    print("A Resistência é ",format(i,".2f"))
  elif(opcao=="4"):
    break
  else:
    print("Não é uma opção. Tente de novo.")