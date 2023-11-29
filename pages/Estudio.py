import streamlit as st

st.set_page_config(layout='wide')

st.header('Estudio Tren EFE Provincia de Llanquihue')
st.caption('SimpliCity - Déficit Cero')
#st.caption('SimpliCity - Versión Beta 1.0.0')

st.markdown("""
            <style>
            .text-justify {
                text-align: justify;
            }
            </style>
            <div class="text-justify">
            La pestaña <strong>Estudio</strong> ofrece visualizaciones interactivas de la Provincia de Llanquihue, en específico de las comunas de Puerto Montt, Puerto Varas y Llanquihue. Considera un Escenario Base (ceteris paribus) y un Escenario Alternativo (con proyecto del Tren EFE), en 2023 y 2050.             <br>
            <br>
            """, unsafe_allow_html=True)


municipalities = ['PUERTO MONTT',
                  'PUERTO VARAS',
                  'LLANQUIHUE']

agents = ['HABITACIONAL', 
            'COMERCIAL']

subagents = ['H1', 'H2', 'H3', 'C']

scenarios = ['BASE',
             'ALTERNATIVO']

years = ['2023',
         '2050']

st.warning('Instrucciones de Uso: Para comenzar, selecciona los datos que deseas analizar para el Escenario 1 y el Escenario 2. Una vez seleccionados, puedes comparar ambos escenarios utilizando nuestro mapa interactivo. Este mapa te ofrece la posibilidad de acceder a información agregada sobre todos los agentes ubicados en la comuna o en cualquier área de estudio que elijas. Para definir estas áreas, utiliza las herramientas de dibujo disponibles en el panel derecho, lo que te permitirá obtener detalles específicos de las zonas que te interesan.', icon='📄')

selected_municipality = st.selectbox("ESCOGE UNA COMUNA", municipalities)

selected_agent = st.selectbox("ESCOGE UN AGENTE", agents)

col1, col2 = st.columns(2)

with col1: 
    selected_scenario1 = st.selectbox("ESCOGE EL ESCENARIO 1", [scenarios[0]])

with col2:
    selected_scenario2 = st.selectbox("ESCOGE EL ESCENARIO 2", scenarios)

col1, col2 = st.columns(2)

with col1: 
    selected_year1 = st.selectbox("ESCOGE EL AÑO 1", years)

with col2:
    selected_year2 = st.selectbox("ESCOGE EL AÑO 2", [years[1]])

st.divider()

path = selected_municipality+' '+selected_agent+' '+selected_scenario1+' '+selected_year1+' '+selected_scenario2+' '+selected_year2
print(path)

with open(f'study/maps/{path}.html', "r", encoding="utf-8") as f:
    html_content = f.read()
st.components.v1.html(html_content, width=None, height=700, scrolling=True)

st.subheader(" ")
st.subheader('RECURSOS ADICIONALES')

st.markdown("""
            <style>
            .text-justify {
                text-align: justify;
            }
            </style>
            <div class="text-justify">
            Te ofrecemos una serie de recursos adicionales de los modelos estimados por SimpliCity para la Provincia de Llanquihue. Estos recursos están diseñados para facilitar un análisis más profundo de los resultados obtenidos. Además, estamos trabajando para incluir próximamente datos de accesibilidad, con el objetivo de enriquecer el análisis.             <br>
            <br>
            """, unsafe_allow_html=True)

with st.expander("FUNCIONES DE UTILIDAD"):
    selected_subagent = st.selectbox(" ", subagents)
    with open(f'study/utility/{selected_subagent}.html', "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, width=None, height=300, scrolling=True)