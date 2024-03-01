#GERAÇÃO DE CHAVE RSA

cont=1
m_1=1
n_2=1
primos=[]
for m_1 in range(100,1000):
    cont=0
    for n_2 in range(1,m_1+1):
        if m_1%n_2==0:
            cont+=1
    if cont<=2:
        primos.append(m_1)
        
##'1. Escolher dois números primos'
        
import random
p= random.choice(primos)
q= random.choice(primos)
n=p*q

#CALCULO PHI(N)

##'2. Calcular Phi(n)'

phi=(p-1)*(q-1)
print(f"*====CRIPTOGRAFIA RSA====*")
print("\n")
print(f"Primos gerados - P: {p} e Q: {q }")
print(f"N: {n}")
print(f"Phi(N): {phi}")

#GERAR EXPOENTE E - OBTENÇÃO CHAVE PÚBLICA

##'3. Selecionar expoente público tal que MDC (e,Phi(n)) = 1 (Coprimos)'
lista_3=[]
for a in range(1,999):
    mdc=a
    while a% mdc !=0 or phi% mdc !=0:
        mdc = mdc-1
        if mdc == 1:
            lista_3.append(a)
import random
e = random.choice(lista_3)

        

#CALCULAR CHAVE PRIVADA "d"  TAL QUE ->   'd*e mod(Phi(n)) =1'


d =1
while (e*d) % phi !=1:
    d+=1    
    if (e*d)% phi == 1:
        break
encerrar = "0"    
while encerrar != "encerrar":
    print(f"\n")
    print("*====Chave gerada====*")
    print(f"\n")
    print(f"Chave privada D: {d}")
    print(f"Chave pública: e = {e} n = {n}")
    print("\n")
    print("O que deseja fazer? 1 - Codificar e 2 - Decodificar")
    resposta = str(input("Opção desejada: "))
    if resposta== "1":
        e2 = int(input("Digite chave pública - e: "))
        while e2 != e:
            print("Chave incorreta, tente novamente: ")
            e2 = int(input("Digite chave pública - e: "))
        n2 = int(input("Digite chave pública - n: "))
        while n2 != n:
            print("Chave incorreta, tente novamente: ")
            n2 = int(input("Digite chave pública - n: "))
        mensagem=input("Digite sua mensagem a ser codificada: ")
        tamanho=len(mensagem)
        indice=0
        indice2=0
        lista=[]
        lista2=[]
        lista99=[]
        indice4=0
        while indice < tamanho: # 1 < m < n-1
            aux = mensagem[indice]
            cript = ord(aux)    
            f = (cript**e) % n
            lista.append(f)
            indice+=1
        tamanho2=len(lista)
        print(f"\n")
        print("*====Mensagem codificada====*")
        print(f"\n")
        print(lista)
        print(f"\n\n")
        encerrar = str(input("RSA - Digite 'encerrar' para fechar ou ENTER para continuar: "))
    if resposta == "2":
        frase = 0
        lista_cifra = []
        lista_decod = []
        indice99 = 0        
        chave_d=int(input(f"Digite sua chave privada D: "))
        while chave_d != d:
            print("Chave incorreta, tente novamente.")
            chave_d=int(input(f"Digite sua chave privada D: "))
        decod = input("Deseja decodificar a mensagem acima? S ou N: ")
        if decod == "S" or decod == "s":
            print(f"\n")
            indice2=0
            while indice2 <tamanho2:
                aux3 = lista[indice2]
                aux4 =(aux3**chave_d)%n
                decript = chr(aux4)
                lista2.append(decript)
                indice2+=1
            print("*====Mensagem decodificada====*")
            print(f"\n")
            print(''.join(lista2))
        if decod == "N" or decod == "n":
            while frase != -1:
                frase = int(input("Digite a mensagem nos intervalos listados ou '-1' para encerrar: "))
                if frase == -1:
                    break
                lista_cifra.append(frase)       
            while indice99 < len(lista_cifra):
                 aux01 = lista_cifra[indice99]
                 aux02 = (aux01**chave_d)%n
                 decript_2 = chr(aux02)
                 lista_decod.append(decript_2)
                 indice99+=1
            print("\n")
            print("*====MENSAGEM DECODIFICADA====*")
            print(''.join(lista_decod))
        

            
                
                
                
                
                
            
        




        
        


















