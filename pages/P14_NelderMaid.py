import streamlit as st
from fontTools.misc.bezierTools import epsilon

from Custom_Plots import cplot_1, cfill_x
from functions.A14_neldermaid_simplex import execute_nm



st.set_page_config(page_title="Exhaustive Search", page_icon="🌍")

st.title("Nelder Maid")
st.write("Nelder-Mead es un método de optimización directa que no requiere derivadas, ideal para funciones irregulares o"
         " donde el cálculo de gradientes es complicado. Trabaja modificando un simplex (figura geométrica) que se "
         "adapta al espacio de búsqueda, contraéndose o expandiéndose para encontrar óptimos. Su fortaleza radica "
         "en su flexibilidad para manejar problemas no lineales y multivariables")


_result= 1
_result1 = 1
_default_plot_y= [0,1]
_default_plot_x =[]


col1, col2 = st.columns(2)

with col1:
    # Slider


    option = st.selectbox(
        "Escoge qué funcion utilizar:",
        ("rastrigin","rosenbrock","himmelblau","sphere","booth"),
        index=0,  # Default selection
        placeholder="Escoge algorimo...",
        key="lang_select"
    )
    st.write(option)
    seleccion_algoritmo = option

    if st.button("Correr Funcion"):
        _result, _default_plot_y = execute_nm(seleccion_algoritmo)
        _default_plot_x = cfill_x(_default_plot_y)

with col2:
    with col2:
        with col2:
            st.write(
                str(_result), " =  Minimo final \n",
            )
            st.subheader("historial de X")
            cplot_1(_default_plot_y)