while True:
    resposta = input("Olá, Sou uma Calculadora de Taxa Metabólica Basal, posso calcular sua TMB? sim/nao ")
    if resposta == "sim":
        IDADE = int(input("Qual a sua idade? "))
        PESO = float(input("Qual seu peso? "))
        ALTURA = int(input("Qual sua Altura em Cm? "))
        GENERO = input("Qual é o seu Gênero? homem/mulher ")
        if GENERO=="homem":
            ATIVIDADE = (input("Qual Seu Nível De Atividade Física? TMB/SEDENTARIO/MODERADO/ATLETA "))
            if ATIVIDADE=="sedentario"or"SEDENTARIO":
                SEDENTARIO = 1.3
                TMB = 66+(13.7*PESO)+(5*ALTURA)-(6*IDADE)
                print ("Sua Taxa Metabólica Basal é Aproximadamente:",int(TMB*SEDENTARIO))
                ALTURAMETROS = ALTURA/100
                ALTURA = ALTURAMETROS*ALTURAMETROS
                IMC = PESO/ALTURA
                print("Obrigado Por Usar Minha Calculadora ❤️ Aqui esta um presente:")
                print("🎁👉Seu Imc: ", int(IMC))
                break
            elif ATIVIDADE=="moderado"or"MODERADO":
                MODERADO = 1.5
                TMB = 66+(13.7*PESO)+(5*ALTURA)-(6*IDADE)
                print ("Sua Taxa Metabólica Basal é Aproximadamente:",int(TMB*MODERADO))
                ALTURAMETROS = ALTURA/100
                ALTURA = ALTURAMETROS*ALTURAMETROS
                IMC = PESO/ALTURA
                print("Obrigado Por Usar Minha Calculadora ❤️ Aqui esta um presente:")
                print("🎁👉Seu Imc: ", int(IMC))
                break
            elif ATIVIDADE=="atleta"or"ATLETA":
                ATLETA = 1.7
                TMB = 66+(13.7*PESO)+(5*ALTURA)-(6*IDADE)
                print ("Sua Taxa Metabólica Basal é Aproximadamente: ",int(TMB*ATLETA))
                ALTURAMETROS = ALTURA/100
                ALTURA = ALTURAMETROS*ALTURAMETROS
                IMC = PESO/ALTURA
                print("Obrigado Por Usar Minha Calculadora ❤️ Aqui esta um presente:")
                print("🎁👉Seu Imc: ", int(IMC))
                break
            elif ATIVIDADE=="tmb"or"TMB":
                TMB = 66+(13.7*PESO)+(5*ALTURA)-(6*IDADE)
                print ("Sua Taxa Metabólica Basal é Aproximadamente: ",int(TMB))
                ALTURAMETROS = ALTURA/100
                ALTURA = ALTURAMETROS*ALTURAMETROS
                IMC = PESO/ALTURA
                print("Obrigado Por Usar Minha Calculadora ❤️ Aqui esta um presente:")
                print("🎁👉Seu Imc: ", int(IMC))
                break
            else:
                print("Vamos tentar denovo")
        elif GENERO=="mulher":
            ATIVIDADE = input("Qual Seu Nível De Atividade Física? TMB/SEDENTARIO/MODERADO/ATLETA ")
            TMB = 655+(9.6*PESO)+(1.7*ALTURA)-(4.7*IDADE)
            if ATIVIDADE=="sedentario":
                SEDENTARIO = 1.3
                TMB = 655+(9.6*PESO)+(1.7*ALTURA)-(4.7*IDADE)
                print ("Sua Taxa Metabólica Basal é Aproximadamente:",int(TMB*SEDENTARIO))
                ALTURAMETROS = ALTURA/100
                ALTURA = ALTURAMETROS*ALTURAMETROS
                IMC = PESO/ALTURA
                print("Obrigado Por Usar Minha Calculadora ❤️ Aqui esta um presente:")
                print("🎁👉Seu Imc: ", int(IMC))
                break
            elif ATIVIDADE=="moderado":
                MODERADO = 1.5
                TMB = 655+(9.6*PESO)+(1.7*ALTURA)-(4.7*IDADE)
                print ("Sua Taxa Metabólica Basal é Aproximadamente:",int(TMB*MODERADO))
                ALTURAMETROS = ALTURA/100
                ALTURA = ALTURAMETROS*ALTURAMETROS
                IMC = PESO/ALTURA
                print("Obrigado Por Usar Minha Calculadora ❤️ Aqui esta um presente:")
                print("🎁👉Seu Imc: ", int(IMC))
                break
            elif ATIVIDADE=="atleta":
                ATLETA = 1.7
                TMB = 655+(9.6*PESO)+(1.7*ALTURA)-(4.7*IDADE)
                print ("Sua Taxa Metabólica Basal é Aproximadamente: ",int(TMB*ATLETA))
                ALTURAMETROS = ALTURA/100
                ALTURA = ALTURAMETROS*ALTURAMETROS
                IMC = PESO/ALTURA
                print("Obrigado Por Usar Minha Calculadora ❤️ Aqui esta um presente:")
                print("🎁👉Seu Imc: ", int(IMC))
                break
            elif ATIVIDADE=="tmb":
                TMB = 655+(9.6*PESO)+(1.7*ALTURA)-(4.7*IDADE)
                print ("Sua Taxa Metabólica Basal é Aproximadamente: ",int(TMB))
                ALTURAMETROS = ALTURA/100
                ALTURA = ALTURAMETROS*ALTURAMETROS
                IMC = PESO/ALTURA
                print("Obrigado Por Usar Minha Calculadora ❤️ Aqui esta um presente:")
                print("🎁👉Seu Imc: ", int(IMC))
                break
    elif(resposta)=="nao":
            pergunta = input("você tem certeza?")
            if pergunta == "nao":
                resposta
            elif pergunta == "sim":
                break
                 
                     
                