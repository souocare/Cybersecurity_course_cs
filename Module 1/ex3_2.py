import sys
import random
import math

# def keys_rsa(p_variavel, q_variavel):
#     n = p_variavel * q_variavel
#     ohm_n = (p)

# assert(5, 11)



# https://stackoverflow.com/questions/18114138/computing-eulers-totient-function


# ex 3.2 - Protocolo de Diffie-Hellman
def chave_partilhada_DH(p, alpha, x_alice, y_bob):
    '''
    p -> número primo
    alpha -> número inteiro decidido
    '''
    X_alice = (alpha**x_alice) % p
    B_bob = (alpha**y_bob) % p

    X_alice_secretkey = (B_bob ** x_alice) % p
    B_bob_secretkey = (X_alice ** y_bob) % p
    if (X_alice_secretkey == B_bob_secretkey):
        return X_alice_secretkey
    else:
        return "Error"


def hack_DH(p, alpha, mensagemA, mensagemB):
    a = random.randint(1, 100)      # syntax reference: https://docs.python.org/3/library/random.html
    b = random.randint(1, 100)
    A = ((pow(alpha, a)) % p)           # syntax reference: https://www.geeksforgeeks.org/pow-in-python/
    B = ((pow(alpha, b)) % p)
    Ka = ((pow(B, a)) % p)
    Kb = ((pow(A, b)) % p)
    print("Secret key at A = ", str(Ka))
    print("Secret key at B = ", str(Kb))
    print(math.log(mensagemA,alpha))
    print(𝑌=4⋅𝐾−1(mod𝑃−1))
    return None


print(chave_partilhada_DH(23, 7, 15, 13))
assert(chave_partilhada_DH(23, 7, 15, 13) == 11)


print(hack_DH(23, 7, 14, 20))
