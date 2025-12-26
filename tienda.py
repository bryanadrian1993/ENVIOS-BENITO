import streamlit as st
import urllib.parse

# Configuración de la página
st.set_page_config(page_title="ENVIOS BENITO", page_icon="🛵")

def main():
    # Estilo personalizado optimizado
    st.markdown("""
        <style>
        .datos-banca {
            background-color: #262730;
            padding: 20px;
            border-radius: 15px;
            border-left: 5px solid #25D366;
            margin-bottom: 25px;
            color: white;
        }
        .stButton>button { 
            width: 100%; 
            border-radius: 20px; 
            height: 3em; 
            background-color: #25D366; 
            color: white; 
            border: none; 
            font-weight: bold; 
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🛵 Envios Benito")
    
    # --- SECCIÓN FIJA DE DATOS BANCARIOS ---
    st.markdown("""
    <div class="datos-banca">
        <h3 style='margin-top:0; color:#25D366;'>🏦 Datos de Transferencia</h3>
        <p><b>Banco:</b> PICHINCHA</p>
        <p><b>Tipo:</b> Ahorros</p>
        <p><b>Cuenta:</b> 2205444877</p>
        <p><b>Beneficiario:</b> GILER GILER PAUL ANDRES</p>
        <p><b>Cédula:</b> 00000000</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("Completa los datos de tu comprobante:")

    # --- CAMPOS DE ENTRADA ---
    nombre = st.text_input("Tu Nombre y Apellido:", key="nom")
    monto = st.text_input("Monto Transferido ($):", key="mon")
    pedido = st.text_input("Producto o Pedido:", key="ped")
    direccion_cliente = st.text_input("Dirección de entrega / Referencia:", key="dir")
    
    # TU NÚMERO DE WHATSAPP
    mi_numero = "593962362257" 

    st.divider()

    # --- VALIDACIÓN Y BOTÓN ---
    if nombre and monto and pedido and direccion_cliente:
        
        # El mensaje se construye sin espacios extra al inicio de las líneas
        mensaje_final = f"Hola BENITO! 🏍️\n\nSoy *{nombre}*.\n💰 Pago de: ${monto}.\n🛍️ Pedido: {pedido}\n📍 Dirección/Notas: {direccion_cliente}\n\nADJUNTO COMPROBANTE DE PAGO 👇"

        # Codificación segura
        mensaje_url = urllib.parse.quote(mensaje_final)
        link_whatsapp = f"https://wa.me/{mi_numero}?text={mensaje_url}"

        # Botón HTML con diseño móvil
        st.markdown(f'''
            <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
                <div style="
                    background-color: #25D366;
                    color: white;
                    padding: 18px;
                    text-align: center;
                    border-radius: 15px;
                    font-size: 18px;
                    font-weight: bold;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
                ">
                    ENVIAR COMPROBANTE AHORA 📲
                </div>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Completa los 4 campos de arriba para activar el botón de envío.")

if __name__ == "__main__":
    main()
