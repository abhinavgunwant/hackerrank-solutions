def print_rangoli(size):
    if size == 1:
        print('a')
        return
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    #width = (2*size-1)*2
    width = 2 * size - 1
    width += width - 1
    for i in range(1, size):
        line = ''
        for j in range(1, i+1):
            if j > 1:
                line += '-'
            line += alpha[size - j]
        
        if i > 1:
            line += '-'
              
        for j in range(i, 1, -1):
            line += alpha[size - j + 1]
            
            if j > 0:
                line += '-'
        l.append(line)       
        print(line.center(width, '-'))
        
    line = ''
    
    for j in range(1, size+1):
        if j > 1:
            line += '-'
        line += alpha[size - j]
        
    line += '-'
              
    for j in range(size, 1, -1):
        line += alpha[size - j + 1]
        
        if j > 2:
            line += '-'
            
    print(line.center(width, '-'))
                
    for i in reversed(l):
        print(i.center(width, '-'))