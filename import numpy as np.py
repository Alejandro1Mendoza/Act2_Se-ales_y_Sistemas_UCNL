import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# 1. Parámetros de la señal
frecuencia_muestreo = 1000  # Hz
tiempo_total = 1  # segundos
f1, f2 = 50, 120  # Frecuencias de las componentes (Hz)

# 2. Generación de la señal temporal
t = np.linspace(0, tiempo_total, int(frecuencia_muestreo * tiempo_total), endpoint=False)
senal = 0.7 * np.sin(2 * np.pi * f1 * t) + 1.0 * np.sin(2 * np.pi * f2 * t)
ruido = 0.5 * np.random.normal(size=len(t))
senal_ruidosa = senal + ruido

# 3. Cálculo de la Transformada Rápida de Fourier (FFT)
N = len(senal_ruidosa)
yf = fft(senal_ruidosa)
xf = fftfreq(N, 1 / frecuencia_muestreo)

# 4. Visualización
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Señal temporal
ax1.plot(t, senal_ruidosa, alpha=0.7, label='Señal con ruido')
ax1.plot(t, senal, 'r', alpha=0.5, linewidth=2, label='Señal original')
ax1.set_xlabel('Tiempo [s]')
ax1.set_ylabel('Amplitud')
ax1.legend()
ax1.grid()

# Espectro de frecuencia
ax2.plot(xf[:N//2], 2.0/N * np.abs(yf[:N//2]), label='Espectro')
ax2.axvline(f1, color='r', alpha=0.5, linestyle='--', label=f'Frecuencia {f1} Hz')
ax2.axvline(f2, color='g', alpha=0.5, linestyle='--', label=f'Frecuencia {f2} Hz')
ax2.set_xlabel('Frecuencia [Hz]')
ax2.set_ylabel('Amplitud')
ax2.legend()
ax2.grid()
ax2.set_xlim(0, 200)

plt.tight_layout()
plt.show()

# 5. Análisis de componentes principales
indices = np.where(xf >= 0)[0]
amplitudes = 2.0/N * np.abs(yf[indices])
frecuencias = xf[indices]

# Encontrar picos dominantes
umbral = 0.5
picos = np.where(amplitudes > umbral)[0]

print("Componentes detectadas:")
for p in picos:
    if frecuencias[p] <= frecuencia_muestreo/2:  # Teorema de Nyquist
        print(f'Frecuencia: {frecuencias[p]:.1f} Hz | Amplitud: {amplitudes[p]:.2f}')