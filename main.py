import math
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

# Almacenar los polinomios cúbicos en forma de texto
polinomios = []

def imprimir_polinomios():
    for i in range(n - 1):
        # Mostrar el polinomio en el intervalo [x_i, x_{i+1}]
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
    
    # Graficar los puntos originales
    plt.scatter(numeros, valores, color='red', zorder=5, label="Puntos originales")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Trazadores cúbicos")
    plt.grid(True)
    # Guardar la gráfica en un archivo en lugar de mostrarla
    plt.savefig('trazadores_cubicos.png')
    print("\nLa gráfica ha sido guardada como 'trazadores_cubicos.png'.")

def main():
    global x, y, d
    x = [0.5671103861938, 1.234794275492, 1.8882721245922, 2.5701620540882, 
         3.2378459433863, 4.2606808376302, 4.60342404572, 4.9904228068154, 
         5.2881141615042, 5.3774215679108, 5.6751129225995, 6.0521886385386, 
         6.4788795802592, 6.8758013865109, 7.1238775154182, 7.2131849218248]
    y = [2.2999410712407, 2.9250068399453, 3.4080122066716, 3.7631632116174,
         3.9194296537935, 3.6637209302326, 3.7212369857068, 3.7013908953942, 
         3.4433917213306, 3.0167007796101, 2.7686246507028, 2.5800867927332, 
         2.4213180702326, 2.2228571671067, 2.0442423542935, 1.3198600578841]
    
    d = [0] * n  # Asegurarse de que d esté definido y tenga el tamaño correcto

    print("Trazador natural")
    trazador_natural(x, y)
    
    graficar_trazadores(x, y)

if __name__ == "__main__":
    main()
