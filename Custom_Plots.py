import matplotlib.pyplot as plt
import streamlit as st


def cfill_x(list = [0,1,2]):
    _x = []
    for i in range(len(list)):
        _x.append(i)
    return _x

def cplot_2(list = [[1,2,4],[-1,-2,-4]]):

    _x = []

    for j in range(len(list[0])):
        #print(j)
        _x.append(j)


    if min(list[0]) > min(list[1]):
        _min = min(list[1]) - 1
    else: _min = min(list[0]) - 1

    if max(list[0]) < max(list[1]):
        _max = max(list[1]) + 1
    else: _max = max(list[0]) + 1



    #print(list[0])
    #print(_x)
    #plt.ylim(_min, _max)
    plt.ylim(min(list[0]), max(list[0]))

    plt.plot(_x,list[0],_x,list[1])  # Plot the data
    plt.title("Rangos_Importados")  # Add title

    #plt.show()
    st.pyplot(plt.gcf())



def cplot_1(list = [0,1,2]):
    _x = cfill_x(list)

    plt.ylim(min(list),max(list))
    plt.plot(_x,list)
    #plt.show()
    st.pyplot(plt.gcf())


#test
cplot_2()