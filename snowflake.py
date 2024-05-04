import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Запитати користувача про рівень рекурсії
    level = int(input("Введіть рівень рекурсії (ціле число): "))

    # Ініціалізація модуля turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Сніжинка Коха")

    # Ініціалізація черепахи
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Намалювати сніжинку Коха
    for _ in range(3):
        koch_snowflake(t, level, 300)
        t.right(120)

    # Закрити вікно при натисканні на нього
    screen.mainloop()

if __name__ == "__main__":
    main()