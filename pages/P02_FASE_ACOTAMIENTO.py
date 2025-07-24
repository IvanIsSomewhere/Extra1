import streamlit as st

from Custom_Plots import cplot_1,cfill_x
from functions.A02_Fase_Acotamiento import execute_FA




st.set_page_config(page_title="Fase Acotamiento", page_icon="🌍")

st.title("Fase Acotamiento")
st.write("La fase de acotamiento Consiste en definir rangos, condiciones o criterios que permitan acotar (delimitar) las"
         " posibles alternativas, evitando así analizar opciones irrelevantes o fuera de los parámetros deseados. Esta "
         "fase es clave en algoritmos de programación matemática, inteligencia artificial o métodos heurísticos, ya que "
         "mejora la eficiencia al enfocarse solo en las soluciones factibles")


col1, col2 = st.columns(2)

_result = 0
_default_plot_y= [0,1,2,3]
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
        _result, _default_plot_y = execute_FA(seleccion_algoritmo)


with col2:
    st.write(
        str(_result),
        "\n = Longitud del area minima"
    )
    st.subheader("historial de L")
    cplot_1(_default_plot_y)


    # Create plot

st.success("Profe no me repruebe porfa")


