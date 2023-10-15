change_owed = 0
amount_due = 50

while amount_due > 0:
    input_coins = int(input('Insert Coin: '))

    if input_coins != 25 and input_coins != 10 and input_coins != 5:
        print(f'Amount Due: {amount_due}')
    else:
        amount_due -= input_coins
        if amount_due > 0:
            print(f'Amount Due: {amount_due}')
        else:
            change_owed = abs(amount_due)
            print(f'Change Owed: {change_owed}')