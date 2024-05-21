print("Olá, Sou Uma Calculadora De Taxa Metabolica")
def input_inteiro(prompt):
    while True:
        try:
            valor = int(input(prompt))
            if valor > 0:
                return valor
            else:
                print("Por favor, insira um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
def input_decimal(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor > 0:
                return valor 
            else:
                print("Entrada Inválida, Por Favor Insira um Numero Positivo")
        except ValueError:
            print("Entrada Inválida, Por Favor Insira um Numero Decimal Positivo")
nome=input("Qual Seu Nome?")
print("Olá,", nome)
idade=input_inteiro("Qual é a Sua Idade?")
peso =input_decimal("Qual é o Peso (kg)?")
altura =input_inteiro("Qual é a Sua Altura (Cm)?")
while True:
  genero=str(input("Qual é o Seu Genero? Homem/Mulher")).strip().lower()
  if genero in ["homem", "mulher",]:
    break
  else:
    print("Por Favor Insira seu Genero Para Contiuar")
if genero == "homem":
  tmb=88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)
if genero == "mulher":
  tmb=447.6+(9.2*peso)+(3.1*altura)-(4.3*idade)
print("Niveis de Atividade Fisica")
print("Taxa metabolica: (Caso Queira Saber Somente Quanto Seu Corpo Gasta em Repouso)")
print("Sedentario: (Nao Faço Exercicios Durante a Semana)")
print("Leve: (Treino 1 A 3 Vezes na Semana)")
print("Moderado: (Treino 3 A 5 Vezes na Semana)")
print("Intensa: (Treino 5 A 7 Vezes na Semana)")
print("Muito Intensa: (Trabalho Fisico e Exercicio Muito Intenso 7x na Semana)")
while True:
  atividade_fisica=str(input("Qual Seu Nivel de Atividade Fisica?")).strip().lower()
  if atividade_fisica in ["taxa metabolica", "sedentario", "leve", "moderado", "intensa", "muito intensa"]:
    break
  else:
    print("Parece Que Voce Nao Escolheu Sua Atividade Fisica,Vamos Tentar Denovo")
if atividade_fisica=="taxa metabolica":
  print("Sua Taxa Metabolica Basal é Entorno de:", int(tmb))
if atividade_fisica=="sedentario":
  tmb=tmb*1.2
  print("Sua Taxa Metabolica Basal é Entorno de:", int(tmb))
if atividade_fisica=="leve":
  tmb=tmb*1.375
  print("Sua Taxa Metabolica Basal é Entorno de:", int(tmb))
if atividade_fisica=="moderado":
  tmb=tmb*1.55
  print("Sua Taxa Metabolica Basal é Entorno de:", int(tmb))
if atividade_fisica=="intensa":
  tmb=tmb*1.725
  print("Sua Taxa Metabolica Basal é Entorno de:", int(tmb))
if atividade_fisica=="muito intensa":
  tmb=tmb*1.9
  print("Sua Taxa Metabolica Basal é Entorno de:", int(tmb))