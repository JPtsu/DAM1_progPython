# Escribe: "Dame un número inicial, un incremento y un número final"
# lee numI, inc, numF
# crea una lista desde numI hasta numF
# Escribe lista  
#
numI = int(input("Dame un número inicial:"))
inc = int(input("Dame un incremento:"))
numF = int(input("Dame un número final:"))
serie= list(range(numI-1,numF+1))
serie= serie[numI:numF:inc]
print(serie)

    
    
        


