# ex 3.2 - Diffie-Hellman protocol
def chave_partilhada_DH(p, alpha, x_user1, y_user2):
    '''
    p -> prime number
    alpha -> base value, also prime
    '''
    # User 1 
    Xpublic_user1 = (alpha**x_user1) % p
    
    # User Alice 
    B_bob = (alpha**y_user2) % p

    X_user1_secretsharedkey = (B_bob ** x_user1) % p
    Y_user2_secretsharedkey = (Xpublic_user1 ** y_user2) % p
    if (X_user1_secretsharedkey == Y_user2_secretsharedkey):
        return X_user1_secretsharedkey
    else:
        return "Error"




def hack_DH(p, x, mensagemA, mensagemB):
    publicmessage_User1 = mensagemA
    publicmessage_User2 = mensagemB
    
    #Decode public message of User1:
    privatemessage_user1 = 0

    # Knowing that i is the the private message of user 1 and     1 ≤ i ≤ p−2
    for i in range(1, p-2): #Loop on the range of the condition above
        #Using "(x**i) % p" to brute force the private message
        if (x**i) % p == publicmessage_User1:
            privatemessage_user1 = i
            break
        else:
            pass

    
    #Decode public message of User2:
    privatemessage_user2 = 0

    # Knowing that i is the the private message of user 2 and     1 ≤ i ≤ p−2
    for i in range(1, p-2): #Loop on the range of the condition above
        #Using "(x**i) % p" to brute force the private message
        if (x**i) % p == publicmessage_User2:
            privatemessage_user2 = i
            break
        else:
            pass
    
    return privatemessage_user1, privatemessage_user2



# Print result of shared key using Diffie-Hellman using key exchange
print(chave_partilhada_DH(13, 6, 4, 2))
assert(chave_partilhada_DH(13, 6, 4, 2) == 3)


# Print result of private keys using Diffie-Hellman key exchange
print(hack_DH(13, 6, 9, 10))
assert(hack_DH(23, 7, 9, 10) == (4, 2))
