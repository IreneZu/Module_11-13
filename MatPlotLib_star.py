import matplotlib.pyplot as plt
import numpy as np

a = 1/2
c = 2
dt = .00117

cnt = 0

while (True):


    cnt += 1
    if 1/a > 50 or a > 50:
        c = 1/c
    a *= c
    dt *= c

    t = np.linspace(-a, +a, 330)

    # Картинку звездочки нашла в сети моя дочка Мария
    # сделали из нее 2 картинки - Звездочку и цветочек

    plt.subplot(1, 2, 1)
    plt.title('Звездочка')
    plt.ylim(-10, 10)

    x = 2 * np.cos(t) + 5 * np.cos(2 * (t) / 3)
    y = 2 * np.sin(t) - 5 * np.sin(2 * (t) / 3)
    line = plt.scatter(x, y, color='r', linewidth=2)  # [0]

    # Теперь рисуем цветок

    plt.subplot(1, 2, 2)
    plt.title('Цветок')
    plt.ylim(-10, 10)

    x = 2* np.cos(t) + 5 * np.cos(2*(t*dt)/3)
    y = 2* np.sin(t) - 5 * np.sin(2*(t*dt)/3)
    graph = plt.scatter(x, y, color='y')#[0]
    x *= .94
    y *= .94
    graph1 = plt.scatter(x, y, color='r', linewidth=3)
    x *= .94
    y *= .94
    graph2 = plt.scatter(x, y, color='C4', alpha=0.5)

    # Пауза
    plt.pause(0.4)

    if cnt > 6: # останавливаем рисование
        break

    line.remove()
    graph.remove()
    graph1.remove()
    graph2.remove()

plt.show()