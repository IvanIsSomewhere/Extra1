import streamlit as st
from fontTools.misc.bezierTools import epsilon

from Custom_Plots import cplot_1, cfill_x
from functions.A11_random_walk import execute_rw
from functions.A13_simulated_annealing import ejecutar_sa


st.set_page_config(page_title="Exhaustive Search", page_icon="🌍")

st.title("Simulated Annealing")
st.write("Simulated Annealing es un algoritmo de optimización inspirado en el proceso de templado en metalurgia. "
         "A diferencia de Hill Climbing, evade óptimos locales aceptando soluciones peores de manera controlada "
         "usando una 'temperatura' que disminuye gradualmente.")


_result= 1
_result1 = 1
_default_plot_y= [0,1]
_default_plot_x =[]


col1, col2 = st.columns(2)

with col1:
    # Slider
    epsi = st.selectbox(
        "Escoje con que nivel de epsilon probar:",
        (0.1,0.01,0.001,0.001),
        index = 0,
        placeholder = "Escoger...",
        key = "Eps"
    )

    option = st.selectbox(
        "Escoge qué funcion utilizar:",
        ("rastrigin","rosenbrock","himmelblau","sphere"),
        index=0,  # Default selection
        placeholder="Escoge algorimo...",
        key="lang_select"
    )
    st.write(option)
    seleccion_algoritmo = option

    if st.button("Correr Funcion"):
        _result, _default_plot_y = ejecutar_sa(seleccion_algoritmo)
        _default_plot_x = cfill_x(_default_plot_y)

with col2:
    with col2:
        with col2:
            st.write(
                str(_result), " =  Minimo final \n",
            )
            st.subheader("historial de X")
            cplot_1(_default_plot_y)