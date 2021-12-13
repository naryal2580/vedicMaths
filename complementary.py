def complementary(number):
    if len(str(number)) == 1:
        return 10 - int(number)
    numbers = []
    for n in str(number):
        numbers.append(int(n))
    outputs = ''
    ln = numbers[-1]
    for n in numbers[:-1]:
        outputs += str(9 - n)
    if ln:
        outputs += str(10 - ln)
    else:
        outputs = outputs[:-1] + str( int(outputs[-1]) + 1 )
    return int(outputs)
