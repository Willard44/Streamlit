import streamlit as st
import numpy as np
import pandas as pd
# .\launch_app.ps1 can be used in terminal to launch the app

# Título de la aplicación
st.header('Lanzar una moneda')

# Control deslizante para elegir el número de intentos
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)

# Botón para ejecutar el experimento
start_button = st.button('Ejecutar')

# Lógica del experimento
if start_button:
    # Simulación de lanzamientos: 0 = cara, 1 = cruz
    results = np.random.randint(0, 2, size=number_of_trials)

    # Cálculo de la media acumulada
    cumulative_mean = np.cumsum(results) / np.arange(1, number_of_trials + 1)

    # Mostrar gráfico de evolución de la media
    st.line_chart(cumulative_mean)

    # Mostrar tabla con resultados individuales y media acumulada
    df = pd.DataFrame({
        'Intento': np.arange(1, number_of_trials + 1),
        'Resultado': results,
        'Media acumulada': cumulative_mean
    })
    st.dataframe(df)

    # Mostrar resultado final
    final_mean = cumulative_mean[-1]
    st.write(
        f'📊 Media final después de {number_of_trials} intentos: {final_mean:.2f}')
else:
    st.write('Esta aplicación aún no es funcional. En construcción.')
