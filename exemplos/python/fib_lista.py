# Calcule os n primeiros números de fibonacci e adicione-os 
# na lista fib
def main():
    n = int(input("n: "))
    fib = [1, 1]

    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    print(fib[:n])


if __name__ == "__main__":
    main()
