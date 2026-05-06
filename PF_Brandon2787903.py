import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import het_breuschpagan
import scipy.stats as stats

# Cargar datos
df = pd.read_excel(r"data/Ejercicio1_spotify_2787903.xlsx")

# Variables
X = df[["shuffle", "skipped"]].astype(int)
y = df["ms_played"]

# Modelo
X_const = sm.add_constant(X)
modelo = sm.OLS(y, X_const).fit()

print("\nPaso 9: Generar predicciones")
# Coeficientes
a = modelo.params["const"]
b1 = modelo.params["shuffle"]
b2 = modelo.params["skipped"]
print(f"Ecuación: Y = {a:.2f} + {b1:.2f}*X1 + {b2:.2f}*X2")
# Predicciones
pred = modelo.predict(X_const)
print("Predicciones generadas para todos los datos.")
# Ejemplo de predicciones para shuffle=1, skipped=0 y shuffle=0, skipped=1
pred_shuffle = a + b1 * 1 + b2 * 0
pred_skipped = a + b1 * 0 + b2 * 1
print(f"Predicción para shuffle=1, skipped=0: {pred_shuffle:.2f}")
print(f"Predicción para shuffle=0, skipped=1: {pred_skipped:.2f}")

print("\nPaso 11: Calcular residuales")
res = y - pred
print("Residuales calculados.")

print("\nPaso 12: Desviación estándar de residuales")
std_res = res.std()
print(f"Desviación estándar de residuales: {std_res:.2f}")

print("\nPaso 13: Matriz de correlación")
corr_matrix = df[["ms_played", "shuffle", "skipped"]].corr()
print(corr_matrix)

print("\nPaso 14: R2")
r2 = modelo.rsquared
print(f"R2: {r2:.4f}")

print("\nPaso 15: RMSE")
rmse = np.sqrt(mean_squared_error(y, pred))
print(f"RMSE: {rmse:.2f}")

print("\nPaso 16-17: Summary del modelo")
print(modelo.summary())

print("\nPaso 19: Durbin Watson")
dw = durbin_watson(res)
print(f"Durbin Watson: {dw:.4f}")
if 1.5 <= dw <= 2.5:
    print("✔️ No hay autocorrelación, el modelo cumple el supuesto de independencia")
elif dw < 1.5:
    print("❌ Autocorrelación positiva, el modelo NO es confiable")
else:
    print("❌ Autocorrelación negativa, el modelo NO es confiable")

print("\nPaso 20: Breusch Pagan")
bp = het_breuschpagan(res, X_const)
print(f"P-value Breusch Pagan: {bp[1]:.4f}")

print("\nPaso 21: QQ plot")
print("QQ plot generado dentro del dashboard")
# plt.show()  # Eliminado para evitar mostrar antes del dashboard

print("\nPaso 10: Dashboard")
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Dashboard del Modelo de Regresión Lineal Múltiple")

# 1. Residuos vs valores predichos
axs[0, 0].scatter(pred, res, alpha=0.5)
axs[0, 0].axhline(y=0, color='r', linestyle='--')
axs[0, 0].set_title('Residuales vs Valores Predichos')
axs[0, 0].set_xlabel('Valores Predichos')
axs[0, 0].set_ylabel('Residuales')

# 2. QQ plot de residuales
stats.probplot(res, dist="norm", plot=axs[0, 1])
axs[0, 1].set_title('QQ Plot de Residuales')

# 3. Histograma de residuales
axs[1, 0].hist(res, bins=50, alpha=0.7)
axs[1, 0].set_title('Histograma de Residuales')
axs[1, 0].set_xlabel('Residuales')
axs[1, 0].set_ylabel('Frecuencia')

# 4. ms_played real vs ms_played predicho
axs[1, 1].scatter(y, pred, alpha=0.5)
axs[1, 1].plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')
axs[1, 1].set_title('ms_played Real vs Predicho')
axs[1, 1].set_xlabel('ms_played Real')
axs[1, 1].set_ylabel('ms_played Predicho')

plt.tight_layout()
plt.savefig("dashboard_2787903.png")
plt.show()