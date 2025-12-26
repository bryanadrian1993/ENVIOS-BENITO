import streamlit as st
import urllib.parse

# Configuración de la página
st.set_page_config(page_title="TU TIENDA VIP", page_icon="🏍️")

def main():
    # Estilo personalizado para que se vea más profesional
    st.markdown("""
        <style>
        .main { background-color: #0e1117; }
        .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #25D366; color: white; border: none; font-weight: bold; }
        .stTextInput>div>div>input { border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🏍️ Envíos Benito")
    st.write("Verifica los datos de tu pedido abajo:")

    # --- CAMPOS DE DATOS ---
    # Usamos valores por defecto para que nunca den error (NameError)
    nombre = st.text_input("Nombre:", "Adrian Campoverde")
    monto = st.text_input("Monto:", "10.0")
    pedido = st.text_input("Pedido:", "Arroz")
    direccion = st.text_input("Dirección:", "Barrio Central")
    
    # Tu número de teléfono (CÁMBIALO AQUÍ)
    mi_numero = "593999999999" 

    st.divider()

    # --- CONSTRUCCIÓN DEL MENSAJE ---
    # Nota: El texto está pegado a la izquierda para evitar IndentationError
    mensaje_final = f"""Hola TU TIENDA VIP! 🏍️

Soy *{nombre}*.
💰 Pago de: ${monto}.
🛍️ Pedido: {pedido}
📍 Dirección/Notas: {direccion}

ADJUNTO COMPROBANTE DE PAGO 👇"""

    # Codificación para WhatsApp
    link_whatsapp = f"https://wa.me/{mi_numero}?text={urllib.parse.quote(mensaje_final)}"

    # --- BOTÓN DE ENVÍO ---
    st.markdown(f'''
        <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
            <div style="
                background-color: #25D366;
                color: white;
                padding: 15px;
                text-align: center;
                border-radius: 15px;
                font-size: 18px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            ">
                ENVIAR A WHATSAPP 📲
            </div>
        </a>
    ''', unsafe_allow_html=True)

    # Vista previa opcional
    with st.expander("Ver vista previa del mensaje"):
        st.code(mensaje_final)

if __name__ == "__main__":
    main()

