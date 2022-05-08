

def bitcoinToEuros (bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value


def Bitcoin_debajo(euros_value):
    if euros_value < 30000:
        return print('El bitcoin cae por debajo de 30.000 euros')
    else:
        return print('El bitcoin está por encima de 30.000 euros')

if __name__ == '__main__':
    bitcoin_amount = int(input('Introduce la cantidad de bitcoins que posees: '))
    bitcoin_value_euros = int(input('Introduce el valor de los bitcoins en USD: '))
    euros_value = bitcoinToEuros(bitcoin_amount, bitcoin_value_euros)
    print('El valor del bitcoin en es: ', bitcoin_value_euros)
    print('El valor del bitcoin en euros es: ', euros_value)
    Bitcoin_debajo(euros_value)


