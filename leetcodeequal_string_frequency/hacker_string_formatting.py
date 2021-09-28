def print_formatted(number):
    space= len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{0:{space}d} {0:{space}o} {0:{space}X} {0:{space}g}".format(i,space=space))