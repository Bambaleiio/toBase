def toBase(n, base):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    return digits[::-1]

def main():
    n = input("Enter the number: ")

    if not n.isnumeric():
        print("incorrect input")
        return
    n = int(n)
        
    base = input("Enter the base of the number system: ")
    
    if base not in ['2', '8']:
        print("incorrect input")
        return
    base = int(base)

    print(*toBase(n, base), sep = "")

if __name__ == '__main__':
    main()
