def const():

    n=int(input("Dime un número: "))
    nom=str()
    
    while n!=0:
        op=float(n*(n+1)/2)
        n=n-1
        nom+=str(f"{op} -")
    return nom
print(const())

    
