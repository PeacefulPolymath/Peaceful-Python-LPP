def tick_tock(num):
    msg = ''
    if not isinstance(num , int):
        return 'Invalid Input!'
    else:
        for i in range(num):
            if i % 2 == 0:
                msg += 'Tick...\n'
            else:
                if i+1 == num:
                    msg+='Tock...'
                else:
                    msg += 'Tock...\n'
    return msg
print(tick_tock(2))