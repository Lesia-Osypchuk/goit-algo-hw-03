def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск {n} з {source} на {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Перемістити диск {n} з {source} на {target}")
    hanoi(n-1, auxiliary, target, source)

def main():
    n = int(input("Введіть кількість дисків: "))
    hanoi(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()