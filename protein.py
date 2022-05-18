import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import streamlit as st

st.set_page_config(layout="wide")
st.title("Curva de Estabilidad Termodinámica")
st.markdown("""
La ecuación de "Gibbs-Helmholtz" permite obtener el valor de la energía libre de Gibbs ($\small ΔG$) como función de la temperatura para el equilibrio idealizado 
de una proteína desde su estado Nativo ($\small [N]$)
(plegada) a un único estado desnaturalizado ($\small [D]$):""")
st.latex(r"""\small \Delta G=\Delta H(1-\frac{T}{T_m})-\Delta C_p(T_m-T+Tln(\frac{T}{T_m}))""")
st.markdown("""
Donde $\small T_m$ representa aquella temperatura en la que $\small [N]=[D]$.
El valor de la constante de equilibrio puede ser determinado a partir de la ecuación: 
""")
st.latex("""\small ΔG=-RTLn(k_e)""")
st.markdown("""
Donde $\small k_e$ representa la constante de equilibrio. A partir del valor de ($\small k_e$) es 
posible determinar la fración de proteìna en estado nativo $\small f_N$.

*Con este simulador podrás obtener la curva  $\small ΔG$ y la curva de $\small f_N$ en función de $\small T$*
""")
with st.expander("Detalles:"):
    st.markdown("""
Las [proteínas](https://es.wikipedia.org/wiki/Prote%C3%ADna)
son compuestos macrocíclicos formados por cadenas lineales de aminoácidos. 
La organización conformacional de estas cadenas da origen a diferentes tipos de estructuras para las proteínas
(primaria, secundaria, terciaria y cuaternaria). Las conformaciones tridimensionales permiten que las proteínas participen
en todo tipo de reacciones bioquímicas. Cuando una proteína pierde su conformación estable de plegamiento (estado nativo)
se dice que la proteína sufre [desnaturalización](https://es.wikipedia.org/wiki/Desnaturalizaci%C3%B3n_(bioqu%C3%ADmica)). 
El estado de plegamiento de las proteínas se encuentra en equilibrio con diferente tipo de conformaciones que son inactivas 
(en conjunto representan el estado desnaturalización). Para el [equilibrio de desnaturalización](https://en.wikipedia.org/wiki/Equilibrium_unfolding), 
el cambio de $\small \Delta G$ con la temperatura $\small (ΔG(T))$ puede ser descrito por la ecuación de "Gibbs–Helmholtz".""")

Tm= st.sidebar.slider("Tm (K)", 300, 350, 340)
Cp= st.sidebar.slider('ΔCp (J/mol.K)', 15, 50, 35)
H= st.sidebar.slider('ΔH (KJ/mol.K)', 750, 950, 800)
T=np.arange(270,370,1)
G=H*(1-T/Tm)-Cp*(Tm-T+T*(np.log(T/Tm)))
Go=np.zeros(100)           
k=np.exp((-G*1000)/(8.314*T))
fn=1/(1+k)
fu=1-fn

fig=make_subplots(rows=1,cols=2,subplot_titles=("Curva de estabilidad","Fracción de proteína"))
fig.add_trace(go.Scatter(x=T, y=G,mode='lines',name="ΔG(T)", legendgroup=1), row=1,col=1)
fig.add_trace(go.Scatter(x=T, y=Go,mode='lines',name=r"ΔG(T)=0"), row=1,col=1)
fig.add_trace(go.Scatter(x=T, y=fn,mode='lines',name=r"f<sub>N</sub>"), row=1,col=2)  
fig.add_trace(go.Scatter(x=T, y=fu,mode='lines',name=r"f<sub>U</sub>"), row=1,col=2)

fig.update_xaxes(title_text=r"Temperatura (K)",row=1,col=1)
fig.update_xaxes(title_text=r"Temperatura (K)",row=1,col=2)   
fig.update_yaxes(title_text=r"ΔG(kJ.mol<sup>-1</sup>K<sup>-1</sup>)",row=1,col=1)
fig.update_yaxes(title_text=r"fracción molar",row=1,col=2)
fig.update_layout(height=550,width=900)
fig.update_layout(yaxis_range=[-10,50])
st.plotly_chart(fig)

with st.expander("Deducción ecuación de la curva de estabilidad"):
    st.markdown("""Inicialmente para el equilibrio:""")
    st.latex(r"""[N] \rightleftharpoons [D]""")
    st.markdown("""El cambio de entalpía de este equilibrio se puede expresar como: """)
    st.latex(r"""\Delta H= \Delta H_D- \Delta H_N=\Delta H_{D,T_{ref}}- \Delta H_{N,T_{ref}}+C_{p,D}(T-T_{ref})-C_{p,N}(T-T_{ref})""")
    st.latex(r"""\Delta H= \Delta H_{T_{ref}}+ \Delta C_{p}(T-T_{ref})""")
    st.markdown("""El cambio de entropía para este equilibrio se puede determinar por:""")
    st.latex(r"""\Delta S=S_{D,T{ref}}+C_{p,D}ln \left ( \frac{T}{T_{ref}} \right )-S_{N,T{ref}}+C_{p,N}ln \left ( \frac{T}{T_{ref}} \right )""")
    st.latex(r"""\Delta S=\Delta S_{T{ref}}+ \Delta C_{p}ln \left ( \frac{T}{T_{ref}} \right )""")
    st.markdown("""Teniendo en ecuenta que:""")
    st.latex(r"""\Delta S_{ref}= \left ( \frac{\Delta H_{ref}}{T_{ref}} \right )""")
    st.markdown("""Y asumiendo:""")
    st.latex(r"""T_{ref}=T_m""")
    st.markdown("""Remplazamos la ecuación de entalpía y entropía en la ecuación general de la energía libre de Gibbs:""")
    st.latex(r"""\Delta G= \Delta H - T \Delta S""")
    st.markdown("""Finalmente, obtenemos:""")
    st.latex(r"""\small \Delta G=\Delta H(1-\frac{T}{T_m})-\Delta C_p(T-T_m)- \frac{T \Delta H_{T_m}}{T_m}-\Delta C_pTln(\frac{T}{T_m})""")
    st.latex(r"""\small \Delta G=\Delta H(1-\frac{T}{T_m})-\Delta C_p(T_m-T+Tln(\frac{T}{T_m}))""")