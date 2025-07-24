import streamlit as st
from fontTools.misc.bezierTools import epsilon

from Custom_Plots import cplot_2, cfill_x
from functions.A05_FIBBONACCI_SEARCH import execute_Fib




st.set_page_config(page_title="Exhaustive Search", page_icon="🌍")

st.title("Fibbonaci Method")
st.write("Un algoritmo para encontrar el mínimo de una función unimodal, inspirado en la sucesión de Fibonacci."
         " En lugar de evaluar puntos uniformemente, usa intervalos que se ajustan según la proporción áurea, reduciendo "
         "el espacio de búsqueda de manera óptima en cada iteración.")


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
        _result, _result1, _default_plot_y = execute_Fib(seleccion_algoritmo,epsi)
        _default_plot_x = cfill_x(_default_plot_y[0])


with col2:


    st.write(
        str(_result), " = A lmite donde se encuentra el punto optimo \n",
        str(_result1), " = B limite donde se encuentra el punto optimo \n"
    )
    st.subheader("historial de X")
    cplot_2(_default_plot_y)


    # Create plot

st.success("Profe no me repruebe porfa")


