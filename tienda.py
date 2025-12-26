import streamlit as st
from urllib.parse import quote

# ==============================================================================
# 🛠️ CONFIGURACIÓN (Edita esto con los datos de tu cliente)
# ==============================================================================
NOMBRE_NEGOCIO = "ENVIOS BENITO"
EMOJI_LOGO = "💎"
COLOR_BOTON = "#2E86C1"          # Color elegante (Azul)
WHATSAPP_PEDIDOS = "593962362257" # TU NÚMERO AQUÍ (Sin el +)

# DATOS BANCARIOS
BANCO_NOMBRE = "Banco Pichincha"
TIPO_CUENTA = "Ahorros"
NUMERO_CUENTA = "2205444877"
TITULAR_CUENTA = "GILER GILER PAUL ANDRES"
CEDULA_CUENTA = "17XXXXXXX"
USUARIO_PAYPAL = "tuusuario"

# ==============================================================================
# 🚀 MOTOR DE LA APP
# ==============================================================================
st.set_page_config(page_title=f"Pagos - {NOMBRE_NEGOCIO}", page_icon=EMOJI_LOGO, layout="centered")

# Estilos CSS para que se vea costoso
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
        border: none;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        text-decoration: none;
    }}
    .stLinkButton>a:hover {{
        background-color: {COLOR_BOTON};
        filter: brightness(85%);
    }}
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.markdown(f"<h1 style='text-align: center;'>{EMOJI_LOGO} {NOMBRE_NEGOCIO}</h1>", unsafe_allow_html=True)
st.info("🔒 Terminal de Pagos Segura.")

# --- SECCIÓN 1: DETALLES ---
st.write("### 1. Detalles del Pedido")
col1, col2 = st.columns([2, 1])
with col1:
    concepto = st.text_input("¿Qué estás pagando?", placeholder="Ej: Zapatos Nike / Asesoría")
with col2:
    monto = st.number_input("Monto Total ($):", min_value=1.00, value=10.00, step=0.50)

# --- SECCIÓN 2: CLIENTE ---
st.write("### 2. Tus Datos")
cliente_nombre = st.text_input("Tu Nombre Completo:")
cliente_notas = st.text_area("Dirección de Envío / Notas Adicionales:", placeholder="Ej: Calle Principal 123 y Secundaria. Casa verde.")

# --- SECCIÓN 3: PAGO ---
st.write("### 3. Forma de Pago")
tab_banco, tab_paypal = st.tabs(["🏛️ Transferencia", "💳 PayPal / Tarjeta"])

with tab_banco:
    st.success("Cuentas Oficiales:")
    st.markdown(f"""
    **Banco:** {BANCO_NOMBRE}  
    **Cuenta:** {NUMERO_CUENTA} ({TIPO_CUENTA})  
    **Titular:** {TITULAR_CUENTA} | **C.I.:** {CEDULA_CUENTA}
    """)
    st.caption("⚠️ Sube tu comprobante al chat de WhatsApp al finalizar.")

with tab_paypal:
    if USUARIO_PAYPAL:
        link_pp = f"https://paypal.me/{USUARIO_PAYPAL}/{monto}"
        st.info("Paga seguro con PayPal.")
        st.link_button(f"👉 Pagar ${monto} ahora", link_pp)
    else:
        st.warning("Pago con tarjeta no habilitado.")

st.markdown("---")

# --- SECCIÓN 4: FINALIZAR (AQUÍ ESTÁ LA MAGIA QUE SÍ FUNCIONA) ---
st.write("### 4. Confirmar y Enviar")

# 1. Preparamos el mensaje con TODOS los datos del diseño anterior
texto_ws = (f"Hola *{NOMBRE_NEGOCIO}*! {EMOJI_LOGO}\n\n"
            f"Soy *{cliente_nombre}*.\n"
            f"Acabo de realizar el pago de: *${monto}*.\n"
            f"🛍️ *Concepto:* {concepto}\n"
            f"📍 *Datos/Dirección:* {cliente_notas}\n\n"
            f"Adjunto mi comprobante a continuación 👇")

# 2. Creamos el link (Usando la lógica que te funcionó)
link_final = f"https://api.whatsapp.com/send?phone={WHATSAPP_PEDIDOS}&text={quote(texto_ws)}"

if cliente_nombre and concepto:
    # MOSTRAMOS LAS DOS OPCIONES (La visual y la infalible)
    
    # Opción A: El Botón Grande y Bonito
    st.link_button("✅ ENVIAR PEDIDO A WHATSAPP (Botón)", link_final)
    
    # Opción B: El Enlace de Respaldo (Por si el botón falla en PC)
    st.caption("¿El botón no abre? Usa el enlace directo de abajo:")
    st.markdown(f"### [👉 CLIC AQUÍ PARA ABRIR WHATSAPP (Enlace Directo)]({link_final})")
    
else:

    st.warning("✍️ Por favor completa tu Nombre y qué estás pagando para activar el botón.")
