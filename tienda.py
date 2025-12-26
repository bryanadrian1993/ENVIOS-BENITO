import streamlit as st
import urllib.parse

# Configuración de la página
st.set_page_config(page_title="PAGO VIP", page_icon="💰")

def main():
    # Estilo personalizado para mejorar la visualización
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
        <p><b>Banco:</b> BANCO PICHINCHA</p>
        <p><b>Tipo de Cuenta:</b> Ahorros</p>
        <p><b>Número de Cuenta:</b> 2205444877</p>
        <p><b>Beneficiario:</b> GILER GILER PAUL ANDRES</p>
        <p><b>Cédula/RUC:</b> 0000000000</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("Una vez realizado el depósito, llena los datos abajo:")

    # --- CAMPOS QUE LLENA EL CLIENTE (VACÍOS) ---
    nombre = st.text_input("Tu Nombre y Apellido:", "")
    monto = st.text_input("Monto Transferido ($):", "")
    pedido = st.text_input("Producto o Pedido:", "")
    direccion = st.text_input("Dirección de entrega / Referencia:", "")
    
    # TU NÚMERO DE WHATSAPP
    mi_numero = "593999999999" 

    st.divider()

    # --- LÓGICA DEL MENSAJE Y BOTÓN ---
    if nombre and monto and pedido:
        mensaje_final = f"""Hola TU TIENDA VIP! 🏍️

Soy *{nombre}*.
💰 Pago de: ${monto}.
🛍️ Pedido: {pedido}
📍 Dirección/Notas: {direccion}

ADJUNTO COMPROBANTE DE PAGO 👇"""

        link_whatsapp = f"https://wa.me/{mi_numero}?text={urllib.parse.quote(mensaje_final)}"

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
        st.info("👆 Completa tu nombre, monto y pedido para habilitar el botón de envío.")

if __name__ == "__main__":
    main()

