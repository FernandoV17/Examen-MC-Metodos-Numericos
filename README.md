# Spline Cúbico Natural y Sujeto

Este proyecto implementa un método de interpolación por **splines cúbicos** tanto en su forma **natural** como **sujeto a condiciones de frontera**, utilizando los datos provistos de una serie de puntos para generar una curva suave que los conecte.

## Descripción

El código resuelve el problema de interpolación utilizando splines cúbicos. Se ofrecen dos enfoques:

1. **Spline Cúbico Natural**: Los segundos valores de las derivadas en los puntos extremos son nulos.
2. **Spline Cúbico Sujeto**: Las derivadas en los puntos extremos son especificadas.

Este código fue escrito en Python y utiliza bibliotecas como `matplotlib` para la visualización de los resultados y `pandas` para la exportación de los datos obtenidos.

## Archivos

- `main.py`: Archivo principal que contiene la implementación del spline cúbico.
- `resultados_trazadores.xlsx`: Archivo que se genera tras la ejecución del código, que contiene los coeficientes de los polinomios para cada spline, tanto para el método natural como para el sujeto.
- `README.md`: Este archivo de documentación.

## Requisitos

Para ejecutar el código, es necesario contar con las siguientes bibliotecas de Python:

- `matplotlib`

Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

O bien, puedes instalarlas manualmente:

```bash
pip install matplotlib 
```

## Uso

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/FernandoV17/Examen-MC-Metodos-Numericos.git
   ```

2. Asegúrate de tener instaladas las dependencias y luego ejecuta el archivo `main.py`:

   ```bash
   python main.py
   ```

3. El programa generará dos conjuntos de resultados:

   - **Trazador Natural**: Un spline cúbico natural calculado a partir de los datos ingresados.
   - **Trazador Sujeto**: Un spline cúbico sujeto a condiciones de frontera, donde las pendientes iniciales y finales están especificadas.

4. Los resultados se exportan automáticamente a un archivo `resultados_trazadores.xlsx`, el cual contiene los coeficientes \(a\), \(b\), \(c\) y \(d\) para cada spline.

## Visualización

El programa genera una gráfica que muestra los puntos originales junto con las curvas interpoladas, tanto para el spline natural como para el spline sujeto. Esto te permite visualizar la calidad del ajuste.

## Ejemplo de Salida

```plaintext
Trazador Natural:
i     a          b             c             d             Ecuación
1     4.38       0.64          0.12          -0.03         S_0(x) = 4.38 + 0.64*(x - 3.31) + 0.12*(x - 3.31)^2 + -0.03*(x - 3.31)^3
...

Trazador Sujeto:
i     a          b             c             d             Ecuación
1     4.38       0.64          0.12          -0.03         S_0(x) = 4.38 + 0.64*(x - 3.31) + 0.12*(x - 3.31)^2 + -0.03*(x - 3.31)^3
...
```


## Estructura del Código

El archivo `main.py` sigue la siguiente estructura:

- **Variables y listas iniciales**: Donde se almacenan los valores de las coordenadas \(x\) y \(y\) y se inicializan las listas para los coeficientes.
- **Funciones**:
  - `trazador_natural()`: Implementa el spline cúbico natural.
  - `trazador_sujeto(dx_y0, dx_yn)`: Implementa el spline cúbico sujeto, recibiendo las derivadas en los extremos.
- **`main()`**: Ejecuta las funciones anteriores y exporta los resultados en formato Excel.
