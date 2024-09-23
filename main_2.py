import matplotlib.pyplot as plt

# Datos
x = [3.31, 7.05, 10.17, 13.16, 16, 18.75, 20.69, 22.62, 25.31, 26.89, 27.82, 30.06, 31.34, 33.14, 34.9, 38.51, 41.77, 45.24, 48.45]
y = [4.38, 5.97, 7.46, 8.25, 10, 11.07, 10.63, 10.15, 12.57, 10.59, 12.26, 10.59, 11.16, 10.32, 9.13, 8.61, 6.8, 5.26, 4.29]
n = len(x)

h = [0] * n
alpha = [0] * n
l = [0] * n
u = [0] * n
z = [0] * n
c = [0] * (n+1)
b = [0] * n
a = [0] * n
d = [0] * n

def trazador_natural():
    global h, alpha, l, u, z, c, b, a, d
    
    for i in range(1, n):
        h[i] = x[i] - x[i - 1]
    
    for i in range(1, n - 1):
        alpha[i] = (3 * (y[i + 1] - y[i]) / h[i + 1]) - (3 * (y[i] - y[i - 1]) / h[i])
    
    l[0], u[0], z[0] = 1, 0, 0
    for i in range(1, n):
        if i == 1:
            l[i] = 2 * h[i]
        else:
            l[i] = 2 * (x[i] - x[i - 2]) - (h[i - 1] * u[i - 1])
        
        u[i] = h[i] / l[i]
        z[i] = (alpha[i - 1] - (h[i - 1] * z[i - 1])) / l[i]
    
    c[n - 1] = 0
    for i in range(n - 1, 0, -1):
        c[i] = z[i] - (u[i] * c[i + 1]) if i < n - 1 else 0
        b[i] = (y[i] - y[i - 1]) / h[i] - (h[i] * (c[i + 1] + 2 * c[i])) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
        a[i] = y[i - 1]
        print(f"a[{i}] = {a[i]},\t\tb[{i}] = {b[i]},\t\tc[{i}] = {c[i]},\t\td[{i}] = {d[i]}")

def trazador_sujeto(dx_y0, dx_yn):
    global h, alpha, l, u, z, c, b, a, d
    
    for i in range(1, n):
        h[i] = x[i] - x[i - 1]

    alpha[0] = (3 * (y[1] - y[0]) / h[1]) - 3 * dx_y0
    alpha[n - 1] = (3 * dx_yn) - (3 * (y[n - 1] - y[n - 2]) / h[n - 1])
    
    for i in range(1, n - 1):
        alpha[i] = (3 * (y[i + 1] - y[i]) / h[i + 1]) - (3 * (y[i] - y[i - 1]) / h[i])
    
    l[0], u[0], z[0] = 2 * h[1], 0.5, alpha[0] / l[0]
    for i in range(1, n):
        l[i] = 2 * (x[i] - x[i - 2]) - (h[i - 1] * u[i - 1])
        u[i] = h[i] / l[i]
        z[i] = (alpha[i - 1] - (h[i - 1] * z[i - 1])) / l[i]
    
    c[n - 1] = (alpha[n - 1] - (h[n - 1] * z[n - 1])) / (h[n - 1] * (2 - u[n - 1]))
    for i in range(n - 1, 0, -1):
        c[i] = z[i] - (u[i] * c[i + 1])
        b[i] = (y[i] - y[i - 1]) / h[i] - (h[i] * (c[i + 1] + 2 * c[i])) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
        a[i] = y[i - 1]
        print(f"a[{i}] = {a[i]},\t\tb[{i}] = {b[i]},\t\tc[{i}] = {c[i]},\t\td[{i}] = {d[i]}")

def main():
    dx_y0 = (y[1] - y[0]) / (x[1] - x[0])
    dx_yn = (y[-1] - y[-2]) / (x[-1] - x[-2])
    
    print("Trazador natural")
    trazador_natural()
    
    print("\nTrazador Sujeto")
    trazador_sujeto(dx_y0, dx_yn)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Datos Originales')
    
    for i in range(1, n):
        xs = [x[i-1] + (j / 100.0) * (x[i] - x[i-1]) for j in range(101)]
        ys = [a[i] + b[i] * (xi - x[i-1]) + c[i] * (xi - x[i-1])**2 + d[i] * (xi - x[i-1])**3 for xi in xs]
        plt.plot(xs, ys, label=f'Trazador {i}')

    plt.title('Trazador Natural y Trazador Sujeto')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
