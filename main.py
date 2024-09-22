import math

n = 16
h = [0] * n
alpha = [0] * n
l = [0] * n
u = [0] * n
z = [0] * n
c = [0] * (n + 1)  
b = [0] * n
a = [0] * n
d = [0] * n

def trazador_natural(numeros, valores):
    for i in range(1, n):
        h[i] = numeros[i] - numeros[i - 1]
    
    for i in range(1, n - 1):
        alpha[i] = (3 * (valores[i + 1] - valores[i]) / h[i + 1]) - (3 * (valores[i] - valores[i - 1]) / h[i])
    
    l[0], u[0], z[0] = 1, 0, 0
    for i in range(1, n - 1):  # Cambié el rango para evitar que `i` exceda `n-1`
        l[i] = 2 * (numeros[i] - numeros[i - 2]) - (h[i - 1] * u[i - 1])
        u[i] = h[i] / l[i]
        z[i] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]
    
    c[n - 1] = 0  # Establezco el límite superior correctamente
    for i in range(n - 2, -1, -1):  # Cambio el rango para evitar errores de índice
        c[i] = z[i] - u[i] * c[i + 1]
        b[i] = (valores[i + 1] - valores[i]) / h[i + 1] - h[i + 1] * (c[i + 1] + 2 * c[i]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i + 1])
        a[i] = valores[i]
        print(f"a[{i}] = {a[i]},\tb[{i}] = {b[i]},\tc[{i}] = {c[i]},\td[{i}] = {d[i]}")

def trazador_sujeto(numeros, valores, dx_y0, dx_yn):
    for i in range(1, n):
        h[i] = numeros[i] - numeros[i - 1]
    
    alpha[0] = (3 * (valores[1] - valores[0]) / h[1]) - 3 * dx_y0
    alpha[n - 1] = 3 * dx_yn - (3 * (valores[n - 1] - valores[n - 2]) / h[n - 1])
    
    for i in range(1, n - 1):
        alpha[i] = (3 * (valores[i + 1] - valores[i]) / h[i + 1]) - (3 * (valores[i] - valores[i - 1]) / h[i])
    
    l[0], u[0], z[0] = 2 * h[1], 0.5, alpha[0] / l[0]
    for i in range(1, n - 1):  # Cambié el rango
        l[i] = 2 * (numeros[i] - numeros[i - 2]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / l[i]
        z[i] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]
    
    c[n - 1] = (alpha[n - 1] - h[n - 1] * z[n - 1]) / (h[n - 1] * (2 - u[n - 1]))
    for i in range(n - 2, -1, -1):  # Cambio el rango para evitar errores de índice
        c[i] = z[i] - u[i] * c[i + 1]
        b[i] = (valores[i + 1] - valores[i]) / h[i + 1] - h[i + 1] * (c[i + 1] + 2 * c[i]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i + 1])
        a[i] = valores[i]
        print(f"a[{i}] = {a[i]},\tb[{i}] = {b[i]},\tc[{i}] = {c[i]},\td[{i}] = {d[i]}")

def main():
    x = [0.5671103861938, 1.234794275492, 1.8882721245922, 2.5701620540882, 
         3.2378459433863, 4.2606808376302, 4.60342404572, 4.9904228068154, 
         5.2881141615042, 5.3774215679108, 5.6751129225995, 6.0521886385386, 
         6.4788795802592, 6.8758013865109, 7.1238775154182, 7.2131849218248]
    y = [2.2999410712407, 2.9250068399453, 3.4080122066716, 3.7631632116174,
         3.9194296537935, 3.6637209302326, 3.7212369857068, 3.7013908953942, 
         3.4433917213306, 3.0167007796101, 2.7686246507028, 2.5800867927332, 
         2.4213180702326, 2.2228571671067, 2.0442423542935, 1.3198600578841]
    
    dx_y0 = (y[1] - y[0]) / (x[1] - x[0])
    dx_yn = (y[-1] - y[-2]) / (x[-1] - x[-2])
    
    print("Trazador natural")
    trazador_natural(x, y)
    
    print("\nTrazador sujeto")
    trazador_sujeto(x, y, dx_y0, dx_yn)

if __name__ == "__main__":
    main()
