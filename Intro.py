# -*- coding: utf-8 -*-
# Portafolio • Laura Orozco • Interfaces Multimodales
# Tema: viaje estelar por tus proyectos (pasteles, estrellas y planetas)

import streamlit as st

st.set_page_config(page_title="Portafolio • Laura Orozco", page_icon="🪐", layout="wide")

# ===================== ESTILOS =====================
st.markdown("""
<style>
/* Fondo pastel con galaxia suave y estrellitas */
[data-testid="stAppViewContainer"]{
  background:
    radial-gradient(80% 80% at 10% 10%, #ffe8f6 0%, transparent 60%),
    radial-gradient(70% 70% at 90% 0%, #e8f7ff 0%, transparent 55%),
    radial-gradient(65% 65% at 0% 100%, #f9ffe7 0%, transparent 60%),
    linear-gradient(180deg, #faedf9 0%, #edf6ff 50%, #f6fff0 100%) !important;
}

/* Tipografía y container */
h1,h2,h3,h4,p,span,div,label{ color:#2b2b2b; }
.block-container{ padding-top: 1.6rem; }

/* Tarjeta de presentación */
.hero{
  background: rgba(255,255,255,.7);
  border: 1.5px solid rgba(0,0,0,.06);
  border-radius: 22px;
  padding: 1.1rem 1.3rem;
  box-shadow: 0 18px 40px rgba(0,0,0,.07);
  backdrop-filter: blur(8px);
}

/* Chips */
.chip{
  display:inline-flex; align-items:center; gap:.45rem;
  background: #ffffffaa;
  border: 1.5px solid #00000010;
  border-radius: 999px; padding:.32rem .72rem; margin:.18rem .28rem .18rem 0;
  font-weight:700; font-size:.86rem; color:#333;
}

/* Tarjetas de proyecto */
.card{
  background: #ffffffcc;
  border: 1.5px solid #00000012;
  border-radius: 20px;
  padding: .9rem 1rem 1rem 1rem;
  box-shadow: 0 16px 36px rgba(0,0,0,.06);
  height: 100%;
}

/* Título de tarjeta */
.card h3{
  margin: .2rem 0 .4rem 0;
  font-size: 1.05rem;
}

/* Botón tipo enlace */
.astro-btn{
  display:inline-block; text-decoration:none; font-weight:800; color:#1f1f1f;
  background: linear-gradient(95deg, #ffc6ff, #caffbf, #bdb2ff, #a0c4ff);
  background-size: 300% 300%;
  padding:.58rem .9rem; border-radius: 14px; border: 1.5px solid #00000012;
  box-shadow: 0 8px 18px rgba(0,0,0,.08);
  transition: transform .08s ease, filter .2s ease;
}
.astro-btn:hover{ transform: translateY(-1px); filter: brightness(1.03); }

/* Pequeñas estrellitas flotantes */
.star{ position: fixed; z-index: -1; opacity:.55; filter: blur(.2px); }
.star.s1{ top:8%; left:8%; font-size: 26px; }
.star.s2{ top:14%; right:10%; font-size: 22px; }
.star.s3{ bottom:12%; left:6%; font-size: 20px; }
.star.s4{ bottom:18%; right:8%; font-size: 28px; }
.star.s5{ top:50%; left:2%; font-size: 18px; }
.star.s6{ top:64%; right:3%; font-size: 20px; }

/* Sidebar glass */
[data-testid="stSidebar"] > div:first-child{
  background: #ffffffaa;
  border-right: 1.5px solid #00000010;
  backdrop-filter: blur(6px);
}
hr{ border:none; height:1px; background:linear-gradient(90deg, #a0c4ff, transparent); margin:.6rem 0 1rem 0; }
</style>

<!-- Estrellitas y planetas "flotando" -->
<div class="star s1">✨</div>
<div class="star s2">🪐</div>
<div class="star s3">🌟</div>
<div class="star s4">🌙</div>
<div class="star s5">💫</div>
<div class="star s6">🛰️</div>
""", unsafe_allow_html=True)

# ===================== SIDEBAR =====================
with st.sidebar:
    st.markdown("## 🌌 Navegación")
    st.write("Explora mis apps con un clic:")
    st.caption("Todos los enlaces abren en una nueva pestaña.")
    st.markdown("---")
    st.write("Hecho con 💜 por **Laura Orozco** (EAFIT).")

# ===================== NARRATIVA =====================
st.markdown("""
<div class="hero">
  <h1 style="margin:.2rem 0">🚀 Portafolio Intergaláctico</h1>
  <p style="margin:.2rem 0">
    ¡Hola! Soy <b>Laura Orozco</b>, estudiante de EAFIT. 
    Te invito a este pequeño <b>viaje por mis constelaciones de proyectos</b> en 
    la materia <i>Creación de Interfaces Multimodales</i>.
  </p>
  <p style="margin:.3rem 0 .2rem 0">
    Cada estrella que verás es una app: pulsa su botón y saltarás en un 
    <i>warp</i> directo hasta el planeta del proyecto correspondiente. ¡Buen viaje!
  </p>
  <div class="chip">🌈 Pastel UI</div>
  <div class="chip">🪐 Universo temático</div>
  <div class="chip">✨ Interacción directa</div>
  <div class="chip">🎓 Multimodalidad</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

# ===================== PROYECTOS (orden EXACTO) =====================
projects = [
    {"title": "INTRO", "url": "https://lalizamar-intro-app-9o5m1q.streamlit.app", "emoji": "🌠",
     "desc": "Presentación y primeros componentes en Streamlit."},
    {"title": "IMM1", "url": "https://primerintro.streamlit.app", "emoji": "🪐",
     "desc": "Primeros pasos en interfaces multimodales."},
    {"title": "TRADUCTOR", "url": "https://traductor-vkmqpghzqdkcouqdj8idgk.streamlit.app", "emoji": "🗣️",
     "desc": "Voz ↔ Texto multilenguaje, con UI tierna."},
    {"title": "OCR", "url": "https://gmoudtge33rnnr4w4brunc.streamlit.app", "emoji": "🔎",
     "desc": "Reconocimiento óptico de caracteres en imágenes."},
    {"title": "OCR AUDIO", "url": "https://ocr-audio-sfifg4q4vrkedhzmfnnvfo.streamlit.app", "emoji": "🎧",
     "desc": "OCR + síntesis de voz con estilo kawaii."},
    {"title": "ANÁLISIS SENTIMIENTO", "url": "https://lalizamar-tx2-analisis-app-pactgs.streamlit.app", "emoji": "💖",
     "desc": "TextBlob/NLTK con temática arcoíris y emociones."},
    {"title": "TF-IDF", "url": "https://lalizamar-tf-idf-inicio-9tqrc2.streamlit.app", "emoji": "📊",
     "desc": "Búsqueda por similitud (inglés), UI de estaciones."},
    {"title": "TF-IDF ESPAÑOL", "url": "https://lalizamar-tdf-esp-inicio-7tls9u.streamlit.app", "emoji": "📈",
     "desc": "TF-IDF con stemmer en español + narrativa climática."},
    {"title": "YOLOv5", "url": "https://yololaura.streamlit.app", "emoji": "🛰️",
     "desc": "Detección de objetos en imágenes."},
    {"title": "TM", "url": "https://lalizamar-tm-app-93fqle.streamlit.app", "emoji": "🌌",
     "desc": "Topic Modeling: exploración temática de textos."},
    {"title": "CHATPDF", "url": "https://lalizamar-chat-pdf-app-kykbml.streamlit.app", "emoji": "📜",
     "desc": "RAG: conversa con tu PDF (ARCHIVUM, el guardián)."},
    {"title": "VISION APP", "url": "https://lalizamar-vision-app-app-9lgdjo.streamlit.app", "emoji": "👁️",
     "desc": "Análisis/visión computacional de imágenes."},
    {"title": "HAND W", "url": "https://lalizamar-hand-w-app-wfi1ws.streamlit.app", "emoji": "✋",
     "desc": "Control/gestos de mano (Hand Tracking)."},
    {"title": "DRAWRECOG", "url": "https://hellodrawrecog.streamlit.app", "emoji": "✏️",
     "desc": "Dibuja y reconoce: interacción creativa."},
    {"title": "TABLERO", "url": "https://lalizamar-hist-inf-inicio-6a9vxl.streamlit.app", "emoji": "🧩",
     "desc": "Tablero/visualización: bits de historia e info."},
    {"title": "RECEP MQTT", "url": "https://lalizamar-recep-mqtt-inicio-gymovx.streamlit.app", "emoji": "📡",
     "desc": "Recepción MQTT para sistemas ciberfísicos."},
    {"title": "CTRL VOICE", "url": "https://lalizamar-ctrl-voice-app-trtduz.streamlit.app", "emoji": "🎙️",
     "desc": "Control por voz: comandos y acciones."},
    {"title": "CMQTT", "url": "https://lalizamar-send-cmqtt-app-hdoxp7.streamlit.app", "emoji": "🛰️",
     "desc": "Cliente MQTT para publicación/envío."},
]

# ===================== RENDER EN TARJETAS =====================
# 3 columnas por fila
cols_per_row = 3
rows = (len(projects) + cols_per_row - 1) // cols_per_row

idx = 0
for r in range(rows):
    cols = st.columns(cols_per_row, gap="large")
    for c in range(cols_per_row):
        if idx >= len(projects):
            break
        p = projects[idx]
        with cols[c]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"### {p['emoji']} {p['title']}")
            st.caption(p["desc"])
            st.markdown(
                f'<a class="astro-btn" href="{p["url"]}" target="_blank" rel="noopener">Ir a la app</a>',
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)
        idx += 1

st.markdown("<br/>", unsafe_allow_html=True)

# ===================== PIE =====================
st.markdown("""
<div class="hero" style="text-align:center;">
  <p>
    Gracias por visitar mi universo de apps 🌠  
    Si alguna estrella te gustó en especial, ¡cuéntame cuál y por qué!  
  </p>
  <p style="opacity:.75;">Laura Orozco — EAFIT • Creación de Interfaces Multimodales</p>
</div>
""", unsafe_allow_html=True)
