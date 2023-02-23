import streamlit as st
import math
import numpy as np
import plotly
import plotly.graph_objects as go
import numpy as np

def main():
    st.title("Curva de distribución de Boltzmann-Maxwell")
    st.markdown("""La función de [distribución de Maxwell-Boltzmann](https://es.wikipedia.org/wiki/Distribuci%C3%B3n_de_Maxwell-Boltzmann) 
    define la distribución de velocidad de las partículas que componen un gas en función de la temperatura. 
    Esta basada en la [estadística de Maxwell-Boltzmann](https://es.wikipedia.org/wiki/Estad%C3%ADstica_de_Maxwell-Boltzmann), 
    esta ecuación hace parte del formalismo de la  [teoría cinética de los gases](https://es.wikipedia.org/wiki/Teor%C3%ADa_cin%C3%A9tica_de_los_gases). 
    La ecuación de distribución de Maxwell-Boltzmann puede definirse de la siguiente manera:""")
    st.latex(r"""\small f(v)=4\pi(\frac{m}{2\pi k_{B}T})^{\frac{3}{2}}v^2e^{\frac{-mv^2}{2k_{B}T}}\kern 2pc(1)""")
    st.markdown("""
    Donde $\small  v$ es la velocidad, $\small  m$ es la masa de la molécula, $\small  k_{B}$ es la [constante de Boltzmann](https://en.wikipedia.org/wiki/Boltzmann_constant)
    y $\small T $ es la temperatura absoluta.""")

    st.markdown("""
    En la estadística de Boltzamnn-Maxwell podemos obtener tres tipos diferentes de velocidades para las particulas que componen el gas: (i) velocidad más probable ($\small v_{mp}$), (ii) velocidad 
    promedio ($\small v_{mean}$), (iii) velocidad raiz cuadratica media "root-mean-square" ($\small v_{rms}$). De acuerdo a la siguiente formulación:""")
    st.latex(r"""\small v_{mp}=\sqrt{\frac{2RT}{M}}\kern 2pc(2)""")
    st.latex(r"""\small v_{mean}=\sqrt{\frac{8RT}{\pi M}}\kern 2pc(3)""")
    st.latex(r"""\small v_{rms}=\sqrt{\frac{3RT}{M}}\kern 2pc(4)""")
    st.markdown("""
    Donde $\small R$ es la constante de los gases ($\small 8.314 J.mol^{-1}.K^{-1}$), $\small T$ es la temperatura absoluta y $\small M$ es la masa molar en $\small Kg.mol^{-1}$   .

    *Con este simulador podrás obtener la curva de distribución de Boltzmann-Maxwell $\small f(v)$ en función de la $\small T$ para cuatro gases diferentes.
    Puedes consultar el artículo de referencia en el siguiente link: [doi:10.1021/acs.jchemed.2c00665](https://pubs.acs.org/doi/10.1021/acs.jchemed.2c00665) *""")


    with st.sidebar.form(key='my_form'):
        st.subheader('Efecto Temperatura')
        T_1= st.slider("T\u2081 (K)", 30, 1500, 30, key='T_1')
        T_2= st.slider("T\u2082 (K)", 30, 1500, 150, key='T_2')
        T_3= st.slider("T\u2083 (K)", 30, 1500, 250, key='T_3')
        T_4= st.slider("T\u2084 (K)", 30, 1500, 1000, key='T_4')

        submit_button = st.form_submit_button(label='Graficar!')
    
    with st.expander("Efecto Temperatura"):
        option = st.selectbox('Selecciona un gas',('He', 'N\u2082', 'Kr',"Ar"))
        if submit_button:
            if option == "He":
                M= 4.0026*1.673534e-27
            elif option == "N\u2082":
                M= 14.007*1.673534e-27
            elif option == "Kr":
                M= 83.80*1.673534e-27
            else: M = 39.948*1.673534e-27
                
            He = 4.0026*1.673534e-27     # masa en unidades de Dalstons Kg/mol
            N2 = 14.007*1.673534e-27
            Kr = 83.80*1.673534e-27
            Ar = 39.948*1.673534e-27

            kB = 1.3806503e-23           # Constante de Boltzmann 
            R = 8.314                    # Constante de los gases
            v = np.arange(0.0, 2500, 0.01)
            
            V_BM5=4*np.pi*v*v*((Kr/(2*np.pi*kB*st.session_state.T_1))**1.5) * np.exp((-M*v*v)/(2*kB*st.session_state.T_1))
            V_BM6=4*np.pi*v*v*((Kr/(2*np.pi*kB*st.session_state.T_2))**1.5) * np.exp((-M*v*v)/(2*kB*st.session_state.T_2))
            V_BM7=4*np.pi*v*v*((Kr/(2*np.pi*kB*st.session_state.T_3))**1.5) * np.exp((-M*v*v)/(2*kB*st.session_state.T_3))
            V_BM8=4*np.pi*v*v*((Kr/(2*np.pi*kB*st.session_state.T_4))**1.5) * np.exp((-M*v*v)/(2*kB*st.session_state.T_4))

            col1, col2, col3 = st.columns((1,4,1))
            with col2:
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=v, y=V_BM5, mode='lines', name=f"{T_1} K"))
                fig.add_trace(go.Scatter(x=v, y=V_BM6, mode='lines', name=f"{T_2} K"))
                fig.add_trace(go.Scatter(x=v, y=V_BM7, mode='lines', name=f"{T_3} K"))
                fig.add_trace(go.Scatter(x=v, y=V_BM8, mode='lines', name=f"{T_4} K"))
                
                fig.update_xaxes(title_text=r"Velocidad (m/s)")
                fig.update_yaxes(title_text=r"f(v)")
                fig.update_layout(title=f"Efecto de la Temperatura (Gas {option})")
                fig.update_layout(height=500,width=500)
                #fig.update_layout(yaxis_range=[-0.001,0.012])
                fig.update_layout(xaxis_range=[0,2500])
                fig.update_layout(legend=dict(yanchor="top", y=0.9, xanchor="left", x=0.7))
                st.plotly_chart(fig)

main()