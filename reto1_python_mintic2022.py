

def solucion(b,n):
    num=0
    attemp=1
    while True:
        num=int(input("Ingrese el número: "))
        if num>n and num<=b:
            print("¡Ups! Te pasaste")
        elif num<n and num>=0:
            print("¡Ups! Estás por debajo")
        elif num<0 or num>b:
            print("¡Te saliste del intervalo!")
            attemp-=1
        elif num==n:
            print(f"¡LO LOGRASTE! Usaste {attemp} intentos")
            break
        attemp+=1
    
