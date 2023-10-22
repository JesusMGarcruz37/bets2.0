import streamlit as st
import statistics

def main():
    st.title("Análisis de Partidos de Fútbol")

    nh = st.number_input("Ingresa el número de la muestra h")
    n_winsh = st.number_input("Ingresa el número de victorias casa")
    n_drawsh = st.number_input("Ingresa el número de empates casa")
    n_losesh = st.number_input("Ingresa el número de derrotas casa")

    # Resto de la entrada de datos...

    # Calcular probabilidades
    prob_winh = (n_winsh / nh)
    prob_drawh = n_drawsh/nh
    prob_losesh = n_losesh/nh
    prob_wdh = (n_winsh + n_drawsh)/nh

    # Resto del código...

    # Mostrar resultados
    st.write(f"PROBABILIDAD DE VICTORIA LOCAL ES: {promediow}")
    st.write(f"PROBABILIDAD DE VICTORIA VISITANTE ES: {promediol}")
    # ...

    # Verifica si hay valor y muestra el resultado
    if prob_CA < promediow or prob_CA < promediol or prob_CA < promediod or prob_CA < promedioeste or prob_CA < promedio_historico or prob_CA < prob_corners:
        st.success("HAY VALOR")
    else:
        st.warning("NO HAY VALOR")

    # Resto del código...

if __name__ == "__main__":
    main()
