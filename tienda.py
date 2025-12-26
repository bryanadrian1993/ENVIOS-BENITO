import streamlit as st
from urllib.parse import quote

# ==============================================================================
# 🛠️ CONFIGURACIÓN
# ==============================================================================
NOMBRE_NEGOCIO = "TU TIENDA VIP"
EMOJI_LOGO = "🏍️"  # <-- Esta moto suele verse ROJA en la mayoría de celulares
COLOR_BOTON = "#D32F2F" # <-- Cambié el botón a un ROJO INTENSO para que combine
WHATSAPP_PEDIDOS = "593962362257"  # Tu número corregido

# DATOS BANCARIOS
BANCO_NOMBRE = "Banco Pichincha"
NUMERO_CUENTA = "220XXXXXXX"
TITULAR = "Tu Nombre"

# ==============================================================================
# 🚀 APP
# ==============================================================================
st.set_page_config(page_title=f"Pagos - {NOMBRE_NEGOCIO}", page_icon=EMOJI_LOGO, layout="centered")

# Estilos
st.markdown(f"""
    <style>
    .stLinkButton>a {{
        background-color: {COLOR_BOTON};
        color: white !important;
        font-size: 18px;
        border-radius: 8px;
        width: 100%;
        height: 55px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        text-decoration: none;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title(f"{EMOJI_LOGO} {NOMBRE_NEGOCIO}")
st.info("🔒 Sistema de Pedidos.")

# 1. DETALLES
st.write("### 1. Detalles")
col1, col2 = st.columns([2, 1])
with col1:
    concepto = st.text_input("¿Qué pides?", placeholder="Ej: Zapatos")
with col2:
    monto = st.number_input("Valor ($):", min_value=1.00, value=10.00)

# 2. DATOS DEL CLIENTE
st.write("### 2. Tus Datos")
cliente_nombre = st.text_input("Tu Nombre:")
cliente_notas = st.text_area("Dirección / Notas:", placeholder="Escribe aquí...")

# 3. PAGO
st.write("### 3. Pago")
st.success(f"🏦 {BANCO_NOMBRE} | 🔢 {NUMERO_CUENTA}\n👤 {TITULAR}")

st.markdown("---")

# 4. CONFIRMACIÓN
st.write("### 4. Enviar")

if st.button("🔄 PRIMERO DALE CLIC AQUÍ PARA CONFIRMAR DATOS"):
    
    if cliente_nombre and concepto:
        # Preparamos el mensaje
        texto_ws = (f"Hola *{NOMBRE_NEGOCIO}*! {EMOJI_LOGO}\n\n"
                    f"Soy *{cliente_nombre}*.\n"
                    f"💰 Pago de: *${monto}*.\n"
                    f"🛍️ *Pedido:* {concepto}\n"
                    f"📍 *Dirección/Notas:* {cliente_notas}")
                   
                    ADJUNTO COMPROBANTE DE PAGO 👇"""
        
        link = f"https://api.whatsapp.com/send?phone={WHATSAPP_PEDIDOS}&text={quote(texto_ws)}"
        
        st.success("✅ ¡Datos guardados! Ahora sí envía el pedido:")
        
        # EL BOTÓN FINAL
        st.link_button("🚀 ENVIAR AHORA POR WHATSAPP", link)
        
    else:
        st.error("⚠️ Falta tu Nombre o el Pedido.")
else:
    st.caption("👆 Presiona el botón gris para generar tu enlace de WhatsApp.")

