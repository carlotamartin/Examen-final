

def bitcoinToEuros (bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value

def eurosToBitcoin (euros_amount, bitcoin_value_euros):
    bitcoin_value = euros_amount / bitcoin_value_euros
    return bitcoin_value

def Bitcoin_debajo(euros_value):
    if euros_value < 30000:
        return True
    bitcoin_amount = float(input("Enter the amount of bitcoins: "))