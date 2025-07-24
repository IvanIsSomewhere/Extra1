import streamlit as st
from fontTools.misc.bezierTools import epsilon

from Custom_Plots import cplot_2, cfill_x
from functions.A07_NEWTONNEWTONRAPHSON import ejecutar_nw
from functions.A03_ELIMINACION_REGIONES import eliminar_regiones



st.set_page_config(page_title="Exhaustive Search", page_icon="🌍")

st.title("Exhaustive")
st.write("El método Newton-Raphson es un algoritmo potente para encontrar raíces de funciones de forma rápida y precisa. Su mayor ventaja es su velocidad de convergencia cuadrática cuando la estimación inicial es buena, superando a muchos otros métodos numéricos. Usa derivadas para aproximarse iterativamente a la solución, lo que lo hace ideal para problemas complejos en física, ingeniería o machine learning. Sin embargo, requiere que la función sea diferenciable y puede ser sensible al punto de partida. Perfecto cuando se necesita alta precisión con pocas iteraciones.")


_result= 1
_result1 = 1
_default_plot_y= [0,1,0,-1]
cfill_x(_default_plot_y)


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
        ("1", "2", "3", "4", ),
        index=0,  # Default selection
        placeholder="Escoge algorimo...",
        key="lang_select"
    )
    st.write(option)
    seleccion_algoritmo = int(option)

    if st.button("Correr Funcion"):
        _result, _default_plot_y = ejecutar_nw(seleccion_algoritmo,epsi)
        _default_plot_x = cfill_x(_default_plot_y)

with col2:


    st.write(
        str(_result), " =  Minimo final \n",
    )
    st.subheader("historial de X")
    cplot_1(_default_plot_y)


    # Create plot

st.success("Profe no me repruebe porfa")


