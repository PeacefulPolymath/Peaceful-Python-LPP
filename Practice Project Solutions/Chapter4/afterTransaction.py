def after_transaction(balance , transaction):
    if not isinstance(balance ,int) or not isinstance(transaction , int):
        print('Invalid Format')
    else:
        if balance + transaction < 0:
            return balance
        else:
            return balance + transaction
#print(after_transaction(100 , -200))