import streamlit as st
import urllib.parse

# Configuración de la página
st.set_page_config(page_title="PAGO VIP", page_icon="💰")

def main():
    # Estilo personalizado
    st.markdown("""
        <style>
        .datos-banca {
            background-color: #262730;
            padding: 20px;
            border-radius: 15px;
            border-left: 5px solid #25D366;
            margin-bottom: 25px;
        }
        .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #25D366; color: white; border: none; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🛵 Envios Benito")
    
    # --- SECCIÓN FIJA DE DATOS BANCARIOS ---
    st.markdown("""
    <div class="datos-banca">
        <h3 style='margin-top:0;'>🏦 Datos de Transferencia</h3>
        <p><b>Banco:</b> PICHINCHA</p>
        <p><b>Tipo:</b> Ahorros</p>
        <p><b>Cuenta:</b> 2205444877</p>
        <p><b>Beneficiario:</b> GILER GILER PAUL ANDRES</p>
        <p><b>Cédula:</b> 00000000</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("Completa los datos de tu comprobante:")

    # --- CAMPOS DE ENTRADA (Asegúrate de que no tengan espacios al final) ---
    nombre = st.text_input("Tu Nombre y Apellido:", "")
    monto = st.text_input("Monto Transferido ($):", "")
    pedido = st.text_input("Producto o Pedido:", "")
    direccion_cliente = st.text_input("Dirección de entrega / Referencia:", "")
    
    # TU NÚMERO DE WHATSAPP (Cámbiado por el tuyo)
    mi_numero = "593999999999" 

    st.divider()

    # --- VALIDACIÓN: El botón solo aparece si llenan los campos ---
    if nombre and monto and pedido and direccion_cliente:
        
        # Construcción del mensaje con la variable direccion_cliente
        mensaje_final = f"""Hola TU TIENDA VIP! 🏍️

Soy *{nombre}*.
💰 Pago de: ${monto}.
🛍️ Pedido: {pedido}
📍 Dirección/Notas: {direccion_cliente}

ADJUNTO COMPROBANTE DE PAGO 👇"""

        # Codificación segura para URL
        mensaje_url = urllib.parse.quote(mensaje_final)
        link_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"

        # Botón visual
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
                    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                ">
                    ENVIAR COMPROBANTE AHORA 📲
                </div>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Por favor, escribe tu NOMBRE, MONTO, PEDIDO y DIRECCIÓN para enviar.")

if __name__ == "__main__":
    main()
