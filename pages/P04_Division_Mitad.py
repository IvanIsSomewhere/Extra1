import streamlit as st

from Custom_Plots import cplot_2, cfill_x
from functions.A04_InternalHalvingMethod import IHM_execute




st.set_page_config(page_title="Exhaustive Search", page_icon="🌍")

st.title("Internal Halving Method")
st.write("El Internal Halving Method es un algoritmo eficiente para optimización que busca soluciones dividiendo iterativamente el espacio de búsqueda a la mitad. Su fortaleza está en su rapidez y simplicidad, ideal para funciones unimodales donde reduce drásticamente el número de evaluaciones necesarias. Perfecto para aplicaciones prácticas que requieren equilibrio entre precisión y velocidad.")


col1, col2 = st.columns(2)

_result = 0
_default_plot_y= [[0,1],[0,-1]]
_default_plot_x =[]

with col1:
    # Slider
    num_points = st.slider("Margen de error:", 0.01, 0.05, 0.1)

    st.write(num_points)

    option = st.selectbox(
        "Escoge qué algoritmo utilizar:",
        ("1", "2", "3", "4", ),
        index=0,  # Default selection
        placeholder="Escoge algorimo...",
        key="lang_select"
    )
    st.write(option)
    seleccion_algoritmo = int(option)

    if st.button("Correr Funcion"):
        _result, _default_plot_y = IHM_execute(seleccion_algoritmo)
        _default_plot_x = cfill_x(_default_plot_y)


with col2:
    st.write(
        str(_result),
        "\n = X estimada (punto medio entre los rangos)"
    )
    st.subheader("historial de X")
    cplot_2(_default_plot_y)


    # Create plot

st.success("Profe no me repruebe porfa")


