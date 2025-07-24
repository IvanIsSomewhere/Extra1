import streamlit as st
from fontTools.misc.bezierTools import epsilon

from Custom_Plots import cplot_1, cfill_x
from functions.A08_BISECCION import ejecutar_biseccion
from functions.A03_ELIMINACION_REGIONES import eliminar_regiones



st.set_page_config(page_title="Exhaustive Search", page_icon="🌍")

st.title("Secante")
st.write("Algoritmo eficiente para hallar raíces sin derivadas, usando aproximaciones sucesivas basadas "
         "en rectas secantes. Más rápido que la bisección pero menos estable. "
         "Ideal cuando evaluar derivadas es costoso y se prioriza velocidad sobre garantías absolutas.")


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
        "Escoge qué funcion utilizar (este es incompatible con ciertas funciones):",
        ( "3", "4", ),
        index=0,  # Default selection
        placeholder="Escoge algorimo...",
        key="lang_select"
    )
    st.write(option)
    seleccion_algoritmo = int(option)

    if st.button("Correr Funcion"):
        _result, _default_plot_y = ejecutar_biseccion(seleccion_algoritmo,epsi)
        _default_plot_x = cfill_x(_default_plot_y)

with col2:


    st.write(
        str(_result), " =  Minimo final \n",
    )
    st.subheader("historial de X")
    cplot_1(_default_plot_y)


    # Create plot

st.success("Profe no me repruebe porfa")


