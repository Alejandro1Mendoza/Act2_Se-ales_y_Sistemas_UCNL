# Act2_Señales_y_Sistemas_UCNL
Simulación y análisis de señales con la transformada de Fourier
Análisis de Señales con Ruido (Dominio Temporal y Espectral)
Este script de Python utiliza las librerías numpy, matplotlib, y scipy para generar una señal compuesta, añadirle ruido y analizar sus componentes de frecuencia utilizando la Transformada Rápida de Fourier (FFT).

El objetivo es demostrar cómo la FFT permite descomponer una señal compleja del dominio del tiempo en sus frecuencias constituyentes, incluso en presencia de ruido.

🚀 Requisitos
Asegúrate de tener instaladas las siguientes librerías de Python:

```bash

pip install numpy matplotlib scipy

```

⚙️ Estructura y Funcionamiento del Código
El script está dividido en cinco secciones lógicas:

1. Parámetros de la Señal
Se definen la frecuencia de muestreo (F 
s
​
 =1000 Hz), el tiempo total de la muestra y las frecuencias de las componentes puras (f 
1
​
 =50 Hz, f 
2
​
 =120 Hz).

2. Generación de la Señal
Se crea un vector de tiempo (t) y se construye la señal pura como la suma de dos senoides. Luego, se agrega ruido aleatorio gaussiano (modelado como np.random.normal) para simular un escenario real.

3. Cálculo de la FFT
Se calcula la Transformada Rápida de Fourier (fft) de la señal ruidosa, y se genera el vector de frecuencias (fftfreq) para el correcto mapeo del espectro.

4. Visualización
Se generan dos gráficos:

Dominio Temporal (Arriba): Muestra la señal ruidosa superpuesta a la señal original.

Dominio Espectral (Abajo): Muestra el espectro de amplitud (normalizado) con picos en las frecuencias 50 Hz y 120 Hz.

5. Análisis de Componentes
Se realiza una detección simple de picos en el espectro de frecuencia positiva, utilizando un umbral fijo (umbral = 0.5), e imprime las frecuencias dominantes detectadas.

📊 Resultados Esperados
Al ejecutar el script, se abrirá una ventana que muestra dos gráficos:

Señal Temporal
Verás una señal compleja que oscila irregularmente debido al ruido, pero su patrón base es la superposición de las ondas de 50 Hz y 120 Hz.

Espectro de Frecuencia
El gráfico de frecuencias mostrará un espectro con un pico notable en 50 Hz y otro en 120 Hz. La altura de estos picos debe ser cercana a las amplitudes de la señal original (0.7 y 1.0). El resto de las frecuencias mostrarán amplitudes bajas, representando el ruido.

📝 Uso
Guarda el código fuente como Act2_Se-ales_y_Sistemas_UCNL.py

```bash
Act2_Se-ales_y_Sistemas_UCNL.py
```

Revisa la salida de la consola para ver las componentes detectadas:

Cierra la ventana de gráficos para finalizar la ejecución.