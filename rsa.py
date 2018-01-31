import random

def euclid(a, b):
    while b > 0: a, b = b, a % b
    return a

#Algoritmo de Euclides extendido
def xEuclid(d,f):
    x1, x2, x3 = 1, 0, f
    y1, y2, y3 = 0, 1, d
    while True:
        if y3==0:return x3
        if y3==1:return y2+f
        q=x3/y3
        x1, x2, x3, y1, y2, y3 = y1, y2, y3, x1-q*y1, x2-q*y2, x3-q*y3

#Teste de primalidade de Miller - Rabbin
def isProbablyPrime(p, k=40):

    if p % 2 == 0:
        return False
    r, d = 0, p - 1

    while d % 2 == 0:
        r += 1
        d /= 2

    for _ in range(k):
        a = random.randrange(2, p-1)
        x = pow(a, d, p)
        if x == 1 or x == p-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, p) # potencias de 2
            if x == p-1:
                break
        else:
            return False
    return True

#Algoritmo para elevar o inteiro correspondente a 'msg' a uma potencia inteira 'e' mod n
def muls(msg, n,e):

    msg = ''.join(map(str, msg))
    d , x = 1, int(msg, 2)

    e_bin = [int(z) for z in bin(e)[2:]]

    for i in range(0,len(e_bin)):
        if i != 0:
            x = pow(x,2) % n
        if e_bin.pop() == 1:
            d = (d*x) % n
    return d

#Gerar chaves
def keygen(b):
    #Gerar numeros impares de forma que sejam primos
    while(True):
        p = random.getrandbits(b) * 2 + 1
        if(isProbablyPrime(p)):
            break
    while(True):
        q = random.getrandbits(b) * 2 + 1
        if (isProbablyPrime(q)):
            break

    n=p*q
    phi_n = (p - 1)*(q - 1)

    #Gerar 'e' (da chave publica) tal que seja primo com phi_n e menor que este
    while(True):
        e = random.randrange(1,phi_n)
        if(euclid(e,phi_n)==1):
            break

    #Gerar d (da chave privada)
    d = xEuclid(e,phi_n)

    return (n,p,q,e,d)

def cipher(msg,n,e):
    #A representacao ao nivel do bloco funciona como uma lista de 0's e 1's, onde
    #os inteiros que representam a msg estao codificados em tipo 'int' e o padding em tipo 'str'
    #esta decisao foi tomada para evitar escrever um header no bloco que desse informacao sobre o tamanho da msg
    c=muls(msg,n,e)
    c_binary = [int(x) for x in bin(c)[2:]]

    block = ['0'] * n.bit_length()

    for index,digit in enumerate(c_binary):
        block[index]=digit

    return block

def decipher(msg,n,d):
    #remover padding que sao os elementos 'str' deixando apenas a representacao do inteiro cifrado
    msg_filtered = list(filter(lambda k: type(k) == int, msg))
    print msg_filtered
    deciphered = muls(msg_filtered,n,d)
    deciphered_binary = [int(z) for z in bin(deciphered)[2:]]
    return deciphered_binary

if __name__ == "__main__":
    print "#######################################################################################################################"
    print "A quick demo is provided here at main. You'll be prompted to provide the number of bits of your RSA key.\n" \
          "Your public and private key will be displayed back at you and then a random message (list of 1's and 0's) will be set.\n" \
          "Cipher/Decipher process will take place after this.\n" \
          "Last, a simple check can be made (at your will) to assure you that Decipher(Cipher(m)) == m as a proof of concept " \
          "to \nthe given implementation."
    print "#######################################################################################################################"
    try:
        n = int(input("\nSelect number of bits for your RSA key (1024 bit key is considered by default if no input given)\n"))
    except SyntaxError:
        n = 1024
    print "Calculating RSA key (",n,"bits )...\n"
    mykey = keygen(1024)
    print "Your Public key is:\n"
    print "[ ",mykey[0], " , ", mykey[3], " ] \n"
    print "Your Private key is:\n"
    print "[ ",mykey[0], " , ", mykey[4], " ] \n"
    print "Generating random msg to cipher...(you can change this to another msg)\n"
    msg = list()
    for i in range(0,100):
        msg.append(random.randint(0,1))
    print "\nDone. Your ciphered text:\n"
    ciphered = cipher(msg, mykey[0], mykey[3])
    print ciphered
    print "\nYour deciphered text:\n"
    print decipher(ciphered,mykey[0],mykey[4])
