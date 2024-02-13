def print_inscription(n):
    
    inscription = []
    
    
    for i in range(n):
        line = ''
        for j in range(n):
            line += str((i*j) % 10)
        inscription.append(line)
    
    
    for line in inscription:
        print(line)


print_inscription(10)
