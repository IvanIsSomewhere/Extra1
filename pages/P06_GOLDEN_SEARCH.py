import streamlit as st
from fontTools.misc.bezierTools import epsilon

from Custom_Plots import cplot_2, cfill_x
from functions.A06_GOLDEN_SEARCH import execute_GS
from functions.A03_ELIMINACION_REGIONES import eliminar_regiones



st.set_page_config(page_title="Exhaustive Search", page_icon="🌍")

st.title("Golden Search")
st.write("El método de la búsqueda dorada (Golden Search) es un algoritmo eficiente para encontrar el máximo o mínimo de"
         " funciones unimodales. Su principal ventaja es que no requiere calcular derivadas y converge más rápido que"
         " una bisección tradicional, usando la proporción áurea para seleccionar puntos de evaluación."
         " Es especialmente útil en optimización numérica cuando se busca"
         " un equilibrio óptimo entre precisión y eficiencia computacional")


_result= 1
_result1 = 1
_default_plot_y= [[0,1],[0,-1]]
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
        "Escoge qué algoritmo utilizar:",
        ("1", "2", "3", "4", ),
        index=0,  # Default selection
        placeholder="Escoge algorimo...",
        key="lang_select"
    )
    st.write(option)
    seleccion_algoritmo = int(option)

    if st.button("Correr Funcion"):
        _result, _default_plot_y = execute_GS(seleccion_algoritmo,epsi)
        _default_plot_x = cfill_x(_default_plot_y[0])

with col2:


    st.write(
        str(_result), " =  Longitud final \n",
    )
    st.subheader("historial de X")
    cplot_2(_default_plot_y)


    # Create plot

st.success("Profe no me repruebe porfa")


