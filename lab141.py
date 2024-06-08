#defino n y la función is_prime
def is_prime(n):
    if n < 2:
        return False
#Si es menor a 2 devuelve falso porque los numeros primos son naturales mayores o iguales a 2
    for i in range(2, n):
        if n % i == 0:
            return False
#si la division tiene resto 0 entonces no es primo
    return True
#que itera desde 2 hasta n - 1

#defino la funcion main()
def main():
    primes = [num for num in range(1, 251) if is_prime(num)]
#creo la lista hasta 250
    with open("results.txt", "w") as f:
        for prime in primes:
            f.write(str(prime) + "\n")
    print("Prime numbers between 1 to 250 have been written to results.txt")

if __name__ == "__main__":
    main()


#Luego, abre el archivo results.txt en modo de escritura ("w") utilizando un bloque with para garantizar que se cierre adecuadamente después de su uso.
#Itera sobre la lista de números primos y escribe cada número en una línea separada en el archivo results.txt.
#Finalmente, imprime un mensaje indicando que los números primos entre 1 y 250 se han escrito en el archivo results.txt.


def is_prime(number): 
    for divisor in  range (2, number):
         if number % divisor == 0:
            return False
    return True

inicial_number = 2
final_number = 250

for number in range (inicial_number, final_number+1):
    if is_prime(number):
                print(number)
                with open ("results.txt", "a") as result_file:
                     result_file.write(str(number+"\n"))