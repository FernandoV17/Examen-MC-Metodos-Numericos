import matplotlib.pyplot as plt

n = 16
h = [0] * n
alpha = [0] * n
l = [0] * n
u = [0] * n
z = [0] * n
c = [0] * (n + 1)
b = [0] * n
a = [0] * n

polinomios = []

def imprimir_polinomios():
    for i in range(n - 1):
        polinomio = f"S_{i}(x) = {a[i]} + {b[i]}*(x - {x[i]}) + {c[i]}*(x - {x[i]})^2 + {d[i]}*(x - {x[i]})^3"
        print(polinomio)
        polinomios.append(polinomio)

def trazador_natural(numeros, valores):
    for i in range(1, n):
        h[i] = numeros[i] - numeros[i - 1]
    
    for i in range(1, n - 1):
        alpha[i] = (3 * (valores[i + 1] - valores[i]) / h[i + 1]) - (3 * (valores[i] - valores[i - 1]) / h[i])
    
    l[0], u[0], z[0] = 1, 0, 0
    for i in range(1, n - 1):
        l[i] = 2 * (numeros[i] - numeros[i - 2]) - (h[i - 1] * u[i - 1])
        u[i] = h[i] / l[i]
        z[i] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]
    
    c[n - 1] = 0
    for i in range(n - 2, -1, -1):
        c[i] = z[i] - u[i] * c[i + 1]
        b[i] = (valores[i + 1] - valores[i]) / h[i + 1] - h[i + 1] * (c[i + 1] + 2 * c[i]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i + 1])
        a[i] = valores[i]
    
    imprimir_polinomios()

def graficar_trazadores(numeros, valores):
    plt.figure()
    for i in range(n - 1):
        x_range = [numeros[i] + (numeros[i + 1] - numeros[i]) * j / 100 for j in range(101)]
        y_range = [
            a[i] + b[i] * (x - numeros[i]) + c[i] * (x - numeros[i]) ** 2 + d[i] * (x - numeros[i]) ** 3
            for x in x_range
        ]
        plt.plot(x_range, y_range, label=f"S_{i}(x)")
    
    plt.scatter(numeros, valores, color='red', zorder=5, label="Puntos originales")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Trazadores cúbicos")
    plt.grid(True)
    plt.savefig('trazadores_cubicos.png')
    print("\nLa gráfica ha sido guardada como 'trazadores_cubicos.png'.")

def main():
    global x, y, d
    x = [3.31, 7.05, 10.17, 13.16, 16, 18.75, 20.69, 22.62, 25.31, 26.89, 27.82, 30.06, 31.34, 33.14, 34.9, 38.51, 41.77, 45.24, 48.45]
    y = [4.38, 5.97, 7.46, 8.25, 10, 11.07, 10.63, 10.15, 12.57, 10.59, 12.26, 10.59, 11.16, 10.32, 9.13, 8.61, 6.8, 5.26, 4.29]
    
    d = [0] * n

    print("Trazador natural")
    trazador_natural(x, y)
    
    graficar_trazadores(x, y)

if __name__ == "__main__":
    main()
