import numpy as np
import matplotlib.pyplot as plt

def orientacja(p, q, r):
    pq_x, pq_y = q[0] - p[0], q[1] - p[1]
    pr_x, pr_y = r[0] - p[0], r[1] - p[1]
    iloczyn_wektorowy = pq_x * pr_y - pq_y * pr_x
    if iloczyn_wektorowy < 0:
        return False
    elif iloczyn_wektorowy == 0:
        return (pr_x * pq_x + pr_y * pq_y) > 0
    else:
        return True

def otoczka_jarvisa(punkty):
    punkt_start = punkty[0]
    for punkt in punkty[1:]:
        if punkt[1] < punkt_start[1]:
            punkt_start = punkt
    otoczka = [punkt_start]

    punkt_biezacy = punkt_start

    while True:
        punkt_nastepny = punkty[0]
        for punkt in punkty[1:]:
            if (punkt != punkt_biezacy and (punkt_nastepny == punkt_biezacy or not orientacja(punkt_biezacy, punkt_nastepny, punkt))):
                punkt_nastepny = punkt

        if punkt_nastepny == punkt_start:
            break

        otoczka.append(punkt_nastepny)
        punkt_biezacy = punkt_nastepny

    return otoczka

def wizualizacja_otoczki(punkty, otoczka):
    fig, ax = plt.subplots()
    ax.scatter([p[0] for p in punkty], [p[1] for p in punkty])
    x_otoczka = [p[0] for p in otoczka]
    y_otoczka = [p[1] for p in otoczka]
    ax.plot(x_otoczka + [x_otoczka[0]], y_otoczka + [y_otoczka[0]], 'y-')
    ax.set_title('Otoczka wypukła')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()

data = np.loadtxt('ksztalt_3.txt', skiprows=1)
x_coords = data[:, 0]
y_coords = data[:, 1]
points = list(zip(x_coords, y_coords))

otoczka = otoczka_jarvisa(points)
wizualizacja_otoczki(points, otoczka)