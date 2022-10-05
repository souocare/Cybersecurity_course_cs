
def sequence_processing(sequencia, n_bits_separation):
    sequencia_bits_str = str(sequencia)
    resultado_sequencias_separadas = []
    for idx in range(0, len(sequencia_bits_str), n_bits_separation):
        resultado_sequencias_separadas.append(sequencia_bits_str[idx : idx + n_bits_separation])
    return resultado_sequencias_separadas
    


def padd_oneandzeroes(sequencia_bits, n_bits):
    resultado_sequencias_separadas = sequence_processing(sequencia_bits, n_bits)

    if len(str(resultado_sequencias_separadas[-1])) == n_bits:
        text_to_add = "1" + "0"*(n_bits-1)
        resultado_sequencias_separadas.append(str(text_to_add))
    elif len(str(resultado_sequencias_separadas[-1])) == n_bits - 1:
        text_to_add = str(resultado_sequencias_separadas[-1]) + "1"
        resultado_sequencias_separadas.pop()
        resultado_sequencias_separadas.append(text_to_add)
    else:
        text_to_add = str(resultado_sequencias_separadas[-1]) + "1"  + "0"*(n_bits - len(str(resultado_sequencias_separadas[-1]))- 1)
        resultado_sequencias_separadas.pop()
        resultado_sequencias_separadas.append(text_to_add)
    return ''.join(resultado_sequencias_separadas)



def unpadd_oneandzeroes(sequencia_bits, n_bits):
    resultado_sequencias_separadas = sequence_processing(sequencia_bits, n_bits)

    get_last_item = str(resultado_sequencias_separadas[-1])
    resultado_sequencias_separadas.pop()
    resultado_sequencias_separadas.append(get_last_item[:get_last_item.rfind("1")])

    return ''.join(resultado_sequencias_separadas)



def unpadd_oneandzeroesv2(sequencia_bits, n_bits):
    sequencia_bits_str = str(sequencia_bits)

    return sequencia_bits_str[:sequencia_bits_str.rfind("1")]



def padd_trailingbitcom(sequencia_bits, n_bits):
    resultado_sequencias_separadas = sequence_processing(sequencia_bits, n_bits)

    if str(str(resultado_sequencias_separadas[-1])[-1]) == "1":
        digit_to_complete = "0"
    else:
        digit_to_complete = "1"

    if len(str(resultado_sequencias_separadas[-1])) == n_bits:
        text_to_add = digit_to_complete * (n_bits)
        resultado_sequencias_separadas.append(str(text_to_add))

    elif len(str(resultado_sequencias_separadas[-1])) == n_bits - 1:
        text_to_add = str(resultado_sequencias_separadas[-1]) + digit_to_complete
        resultado_sequencias_separadas.pop()
        resultado_sequencias_separadas.append(text_to_add)
    else:
        text_to_add = str(resultado_sequencias_separadas[-1]) + digit_to_complete * (n_bits - len(str(resultado_sequencias_separadas[-1])))
        resultado_sequencias_separadas.pop()
        resultado_sequencias_separadas.append(text_to_add)
    return ''.join(resultado_sequencias_separadas) 





def unpadd_trailingbitcom(sequencia_bits, n_bits):
    sequencia_bits_str = str(sequencia_bits)
    get_last_bite = str(str(sequencia_bits_str[-1])[-1])
    if get_last_bite == "0":
        return sequencia_bits_str[:sequencia_bits_str.rfind("1")+1]
    else:
        return sequencia_bits_str[:sequencia_bits_str.rfind("0")+1]





# Testings

# Testing padd_oneandzeroes() function
print(padd_oneandzeroes('0100111101', 8))
assert(padd_oneandzeroes('0100111101', 8) == "0100111101100000")



# Testing padd_trailingbitcom() function
print(padd_trailingbitcom('0100110', 4))
assert(padd_trailingbitcom('0100110', 4) == "01001101")



# Testing unpadd_oneandzeroes() function
print(unpadd_oneandzeroes('0100111101100000', 8))
assert(unpadd_oneandzeroes('0100111101100000', 8) == "0100111101")



# Testing unpadd_trailingbitcom() function
print(unpadd_trailingbitcom('01001101', 4))
assert(unpadd_trailingbitcom('01001101', 4) == "0100110")
