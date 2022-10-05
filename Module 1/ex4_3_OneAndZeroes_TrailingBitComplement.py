
def padd_oneandzeroes(sequencia_bits, n_bits):
    sequencia_bits_str = str(sequencia_bits)
    resultado_sequencias_separadas = []
    for idx in range(0, len(sequencia_bits_str), n_bits):
        resultado_sequencias_separadas.append(sequencia_bits_str[idx : idx + n_bits])

    if len(str(resultado_sequencias_separadas[-1])) == n_bits:
        text_to_add = "1" + "0"*(n_bits-1)
        resultado_sequencias_separadas.append(int(text_to_add))
    elif len(str(resultado_sequencias_separadas[-1])) == n_bits - 1:
        text_to_add = str(resultado_sequencias_separadas[-1]) + "1"
        resultado_sequencias_separadas.pop()
        resultado_sequencias_separadas.append(text_to_add)
    else:
        text_to_add = str(resultado_sequencias_separadas[-1]) + "1"  + "0"*(n_bits - len(str(resultado_sequencias_separadas[-1]))- 1)
    return resultado_sequencias_separadas









sequencia_bits = 110001
n_bits = 4

sequencia_bits_str = str(sequencia_bits)
resultado_sequencias_separadas = []
for idx in range(0, len(sequencia_bits_str), n_bits):
    resultado_sequencias_separadas.append(sequencia_bits_str[idx : idx + n_bits])

print(resultado_sequencias_separadas)
print(len(str(resultado_sequencias_separadas[-1])))
if len(str(resultado_sequencias_separadas[-1])) == n_bits:
    text_to_add = "1" + "0"*(n_bits-1)
    resultado_sequencias_separadas.append(int(text_to_add))
elif len(str(resultado_sequencias_separadas[-1])) == n_bits - 1:
    text_to_add = str(resultado_sequencias_separadas[-1]) + "1"
    resultado_sequencias_separadas.pop()
    resultado_sequencias_separadas.append(text_to_add)
else:
    print("entra aqui")
    text_to_add = str(resultado_sequencias_separadas[-1]) + "1"  + "0"*(n_bits - len(str(resultado_sequencias_separadas[-1]))- 1)
    print(text_to_add)


print(resultado_sequencias_separadas)