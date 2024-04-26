import random

class RSA:
    def __init__(self):
        self.primos = []
        self.p = None
        self.q = None
        self.n = None
        self.phi = None
        self.e = None
        self.d = None

    def gerar_primos(self, limite_inferior=100, limite_superior=1000):
        self.primos = []
        for num in range(limite_inferior, limite_superior+1):
            if self.e_primo(num):
                self.primos.append(num)

    def e_primo(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def gerar_chaves(self):
        self.p = random.choice(self.primos)
        self.q = random.choice(self.primos)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.gerar_expoente_publico()
        self.d = self.gerar_expoente_privado()

    def gerar_expoente_publico(self):
        for e in range(2, self.phi):
            if self.mdc(e, self.phi) == 1:
                return e

    def gerar_expoente_privado(self):
        for d in range(1, self.phi):
            if (self.e * d) % self.phi == 1:
                return d

    def mdc(self, a, b):
        if b == 0:
            return a
        else:
            return self.mdc(b, a % b)

    def codificar(self, mensagem):
        tamanho = len(mensagem)
        indice = 0
        lista = []
        while indice < tamanho:
            aux = ord(mensagem[indice])
            cript = pow(aux, self.e, self.n)
            lista.append(str(cript))
            indice += 1
        return ' '.join(lista)

    def decodificar(self, cifra):
        tamanho = len(cifra)
        indice = 0
        lista = []
        while indice < tamanho:
            aux = cifra[indice]
            decript = pow(aux, self.d, self.n)
            lista.append(chr(decript))
            indice += 1
        return ''.join(lista)

# Exemplo de uso
rsa = RSA()
rsa.gerar_primos()
rsa.gerar_chaves()
print(f"*====CRIPTOGRAFIA RSA====*")
print("\n")
print(f"Primos gerados - P: {rsa.p} e Q: {rsa.q }")
print(f"N: {rsa.n}")
print(f"Phi(N): {rsa.phi}")
print(f"\n")
print(f"Chave privada D: {rsa.d}")
print(f"Chave pública: e = {rsa.e} n = {rsa.n}")
print("\n")

def codificar():
    e2 = int(input("Digite chave pública - e: "))
    while e2!= rsa.e:
        print("Chave incorreta, tente novamente: ")
        e2 = int(input("Digite chave pública - e:"))
    n2 = int(input("Digite chave pública - n: "))
    while n2!= rsa.n:
        print("Chave incorreta, tente novamente: ")
        n2 = int(input("Digite chave pública - n: "))
    mensagem = input("Digite sua mensagem a ser codificada: ")
    cifra = rsa.codificar(mensagem)
    print(f"\n")
    print("*====Mensagem codificada====*")
    print(f"\n")
    print(cifra)
    print(f"\n\n")

def decodificar():
    chave_d = int(input(f"Digite sua chave privada D: "))
    while chave_d!= rsa.d:
        print("Chave incorreta, tente novamente.")
        chave_d = int(input(f"Digite sua chave privada D: "))
    cifra = [int(x) for x in input("Digite sua mensagem codificada: ").split()]
    decodificada = rsa.decodificar(cifra)
    print("*====Mensagem decodificada====*")
    print(f"\n")
    print(decodificada)

while True:
    print("O que deseja fazer? 1 - Codificar; 2 - Decodificar; 3 - Encerrar")
    resposta = input("Opção desejada: ")
    if resposta == "1":
        codificar()
    elif resposta == "2":
        decodificar()
    elif resposta == "3":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
