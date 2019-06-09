def print_formatted(number):
    dec = []
    octal = []
    hexa = []
    biny = []
    
    width = len('{:b}'.format(number))
    
    for i in range(1, number+1):
        print(str(i).rjust(width, ' ') + ' ' + ('{:o}'.format(i)).rjust(width, ' ') + ' ' + ('{:X}'.format(i)).rjust(width, ' ') + ' ' + ('{:b}'.format(i).rjust(width, ' ')))