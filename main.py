import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import pandas as pd  

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
    resultados = []

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
    print("\nTrazador Natural:")
    print(f"{'i':<5} {'a':<10} {'b':<15} {'c':<15} {'d':<15} {'Ecuación'}")
    print("="*70)
    
    for i in range(1, n):
        c[i] = z[i] - (u[i] * c[i + 1]) if i < n - 1 else 0
        b[i] = (y[i] - y[i - 1]) / h[i] - (h[i] * (c[i + 1] + 2 * c[i])) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
        a[i] = y[i - 1]
        
        ecuacion = f"S_{i-1}(x) = {a[i]} + {b[i]}*(x - {x[i-1]}) + {c[i]}*(x - {x[i-1]})^2 + {d[i]}*(x - {x[i-1]})^3"
        
        print(f"{i:<5} {a[i]:<10} {b[i]:<15} {c[i]:<15} {d[i]:<15} {ecuacion}")
        
        resultados.append([i, a[i], b[i], c[i], d[i], ecuacion])

    return resultados

def trazador_sujeto(dx_y0, dx_yn):
    global h, alpha, l, u, z, c, b, a, d
    resultados = []

    for i in range(1, n):
        h[i] = x[i] - x[i - 1]

    alpha[0] = (3 * (y[1] - y[0]) / h[1]) - 3 * dx_y0
    alpha[n - 1] = (3 * dx_yn) - (3 * (y[n - 1] - y[n - 2]) / h[n - 1])
    
    for i in range(1, n - 1):
        alpha[i] = (3 * (y[i + 1] - y[i]) / h[i + 1]) - (3 * (y[i] - y[i - 1]) / h[i])
    
    l[0], u[0], z[0] = 2 * h[1], 0.5, alpha[0] / l[0]
    print("\nTrazador Sujeto:")
    print(f"{'i':<5} {'a':<10} {'b':<15} {'c':<15} {'d':<15} {'Ecuación'}")
    print("="*70)
    
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
        
        # Formatear la ecuación
        ecuacion = f"S_{i-1}(x) = {a[i]} + {b[i]}*(x - {x[i-1]}) + {c[i]}*(x - {x[i-1]})^2 + {d[i]}*(x - {x[i-1]})^3"
        
        print(f"{i:<5} {a[i]:<10} {b[i]:<15} {c[i]:<15} {d[i]:<15} {ecuacion}")
        
        resultados.append([i, a[i], b[i], c[i], d[i], ecuacion])

    return resultados

def main():
    dx_y0 = (y[1] - y[0]) / (x[1] - x[0])
    dx_yn = (y[-1] - y[-2]) / (x[-1] - x[-2])
    
    resultados_natural = trazador_natural()
    resultados_sujeto = trazador_sujeto(dx_y0, dx_yn)

    df_natural = pd.DataFrame(resultados_natural, columns=['i', 'a', 'b', 'c', 'd', 'Ecuación'])
    df_sujeto = pd.DataFrame(resultados_sujeto, columns=['i', 'a', 'b', 'c', 'd', 'Ecuación'])
    
    with pd.ExcelWriter('resultados_trazadores.xlsx') as writer:
        df_natural.to_excel(writer, sheet_name='Trazador Natural', index=False)
        df_sujeto.to_excel(writer, sheet_name='Trazador Sujeto', index=False)

    print("\nResultados exportados a 'resultados_trazadores.xlsx'.")

    plt.figure(figsize=(364/103, 1))  

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
