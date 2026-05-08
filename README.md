# Proyecto Final - Ciencia de Datos

Modelo de regresión lineal múltiple utilizando un dataset de Spotify para analizar la relación entre las variables `shuffle`, `skipped` y el tiempo de reproducción `ms_played`.

## 📌 Objetivo

El objetivo de este proyecto es implementar y evaluar un modelo de regresión lineal múltiple en Python para determinar si las variables:

* `shuffle`
* `skipped`

permiten predecir el tiempo de reproducción de una canción (`ms_played`).

Además, se evalúa el desempeño del modelo mediante métricas estadísticas y pruebas de supuestos de regresión lineal.

---

## 🛠️ Tecnologías utilizadas

* Python 3
* Pandas
* NumPy
* Statsmodels
* Scikit-learn
* Matplotlib
* SciPy
* Visual Studio Code
* GitHub Copilot Agent

---

## 📂 Estructura del proyecto

```bash
Proyecto-Final-Ciencia-de-Datos/
│
├── data/
│   └── Ejercicio1_spotify_2787903.xlsx
│
├── src/
│   └── modelo.py
│
├── dashboard_2787903.png
│
├── README.md
│
└── Proyecto_Final_Brandon_Pedraza.docx
```

---

#IMPORTANTE: el archivo de model.py es porque queria hacer un análizis del proyecto con un LLM local fine tuneado para añadirle una capa más de profundidad al proyecto, más que nada para poner a prueba si mi modelo local entrenado es capas de hacer el mismo análisis que nostros realizamos, más si este archivo se encuentra vacio significa que aun no he tenido tiempo de implementarlo, es un añadido extra que quiero implementar.

## 📊 Dataset

El proyecto utiliza un dataset de Spotify previamente procesado durante la Actividad 3 (ETL en Excel).

Variables utilizadas:

| Variable  | Descripción                                            |
| --------- | ------------------------------------------------------ |
| shuffle   | Indica si la canción fue reproducida en modo aleatorio |
| skipped   | Indica si la canción fue saltada                       |
| ms_played | Tiempo reproducido en milisegundos                     |

---

## ▶️ Ejecución del proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/Brandonschool349/Proyecto-Final-Ciencia-de-Datos.git
```

2. Instalar dependencias:

```bash
pip install pandas numpy matplotlib scipy scikit-learn statsmodels openpyxl
```

3. Ejecutar el modelo:

```bash
python src/modelo.py
```

---

## 📈 Métricas evaluadas

El modelo analiza:

* Predicciones
* Residuales
* Desviación estándar de errores
* Correlación de Pearson
* R²
* RMSE
* Reporte OLS
* Durbin-Watson
* Breusch-Pagan
* QQ-Plot

---

## 📉 Resultados principales

| Métrica               | Resultado |
| --------------------- | --------- |
| R²                    | 0.0692    |
| RMSE                  | 113687.77 |
| Durbin-Watson         | 0.9601    |
| Breusch-Pagan P-value | 0.0000    |

### Conclusión general

El modelo es estadísticamente significativo, pero presenta baja capacidad predictiva y no cumple correctamente varios supuestos de regresión lineal, por lo que no se recomienda para toma de decisiones reales.

---

## 🤖 Uso de GitHub Copilot

Durante el desarrollo del proyecto se utilizó GitHub Copilot Agent dentro de Visual Studio Code como apoyo para:

* Estructurar el código
* Corregir errores
* Generar visualizaciones
* Implementar métricas estadísticas

El análisis e interpretación de resultados fueron realizados manualmente.

---

## 📷 Dashboard generado

El proyecto genera automáticamente un dashboard con:

* Residuales vs predichos
* QQ-Plot
* Histograma de residuales
* Valores reales vs predichos

El dashboard se guarda como:

```bash
dashboard_2787903.png
```

---

## 👨‍💻 Autor

**Brandon Pedraza**
Matrícula: 2787903

Proyecto Final — Ciencia de Datos — Mayo 2026
