import streamlit as st
from fontTools.misc.bezierTools import epsilon

from Custom_Plots import cplot_2,cplot_1, cfill_x
from functions.A08_BISECCION import ejecutar_biseccion
from functions.A03_ELIMINACION_REGIONES import eliminar_regiones



st.set_page_config(page_title="Exhaustive Search", page_icon="🌍")

st.title("Biseccion")
st.write("Algoritmo robusto para encontrar raíces en funciones continuas. Divide iterativamente un intervalo a la "
         "mitad, garantizando convergencia (lenta pero segura). Ideal cuando se necesita precisión "
         "absoluta y la función cambia de signo en el intervalo.")


_result= 1
_result1 = 1
_default_plot_y= [0,1,0,-1]
_default_plot_x = cfill_x(_default_plot_y)


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
        ( "1","2","3", "4", ),
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


