import streamlit as st

from Custom_Plots import cplot_1
from functions.A01_Exhaustive_Search import ES_ejecutar



st.set_page_config(page_title="Exhaustive Search", page_icon="🌍")

st.title("Exhaustive")
st.write("Técnica para acotar el mínimo de una función unimodal. Comienza con un punto inicial, evalúa la función en dos"
         " puntos cercanos para determinar la dirección de búsqueda y luego usa una búsqueda exponencial para converger al óptimo.")


col1, col2 = st.columns(2)

_result = 0
_default_plot_y= [0,1,2,3]
_default_plot_x =[]

with col1:
    # Slider

    option = st.selectbox(
        "Escoge qué algoritmo utilizar:",
        ("1", "2", "3", "4", ),
        index=0,  # Default selection
        placeholder="Escoge algorimo...",
        key="lang_select"
    )
    st.write(option)
    seleccion_algoritmo = int(option)





    st.divider()

    if st.button("Correr Funcion"):
        resultado = ES_ejecutar(seleccion_algoritmo)
        _result = resultado["minimum"]
        _default_plot_y = resultado["array_steps"]
        _default_plot_x = []
        for i in range(len(_default_plot_x)):
            _default_plot_y.append(i)
with col2:
    st.write(
        str(_result),
        "\n = mejor x"
    )
    st.subheader("historial de X")
    cplot_1(_default_plot_y)


    # Create plot

st.success("Profe no me repruebe porfa")


