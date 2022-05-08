

def bitcoinToEuros (bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value

def eurosToBitcoin (euros_amount, bitcoin_value_euros):
    bitcoin_value = euros_amount / bitcoin_value_euros
    return bitcoin_value

def Bitcoin_debajo(euros_value):
    if euros_value < 30000:
        return print('Bitcoin debajo de 30.000 euros')
    else:
        return print('Bitcoin encima de 30.000 euros')

if __name__ == '__main__':
    bitcoin_amount = int(input('Introduce la cantidad de bitcoins: '))
    bitcoin_value_euros = int(input('Introduce el valor de los bitcoins en euros: '))
    euros_amount = int(input('Introduce la cantidad de euros: '))
    euros_value_euros = int(input('Introduce el valor de los euros en euros: '))
    euros_value = bitcoinToEuros(bitcoin_amount, bitcoin_value_euros)
    bitcoin_value = eurosToBitcoin(euros_amount, euros_value_euros)
    Bitcoin_debajo(euros_value)
    print('El valor de los bitcoins en euros es: ', bitcoin_value_euros)
    print('El valor de los euros en euros es: ', euros_value_euros)
    print('El valor de los bitcoins es: ', bitcoin_value)
    print('El valor de los euros es: ', euros_value)


