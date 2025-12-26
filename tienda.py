import streamlit as st
import urllib.parse

def main():
    st.title("Generador de Pedidos VIP 🏍️")
    st.write("Llena los datos y genera el enlace automáticamente.")

    # ---------------------------------------------------------
    # 1. FORMULARIO DE DATOS (Para que puedas escribir en la web)
    # ---------------------------------------------------------
    telefono_tienda = st.text_input("Tu Número de WhatsApp (con código país):", "593999999999")
    
    # Dividimos en columnas para que se vea ordenado
    col1, col2 = st.columns(2)
    with col1:
        nombre_cliente = st.text_input("Nombre del Cliente:", "Adrian Campoverde")
        monto = st.text_input("Monto del Pago ($):", "10.0")
    with col2:
        pedido = st.text_input("Producto/Pedido:", "Arroz")
        direccion = st.text_input("Dirección:", "Barrio Central")

    st.markdown("---")

    # ---------------------------------------------------------
    # 2. BOTÓN PARA GENERAR
    # ---------------------------------------------------------
    if st.button("GENERAR ENLACE WHATSAPP"):
        
        # AQUI CREAMOS EL MENSAJE (Cuidado con los espacios, no tocar la izquierda)
        mensaje = f"""Hola TU TIENDA VIP! 🏍️

Soy *{nombre_cliente}*.
💰 Pago de: ${monto}.
🛍️ Pedido: {pedido}
📍 Dirección/Notas: {direccion}

ADJUNTO COMPROBANTE DE PAGO 👇"""

        # Codificamos el mensaje para internet
        mensaje_codificado = urllib.parse.quote(mensaje)
        link_final = f"https://wa.me/{telefono_tienda}?text={mensaje_codificado}"

        # ---------------------------------------------------------
        # 3. MOSTRAR EL RESULTADO
        # ---------------------------------------------------------
        st.success("¡Enlace generado!")
        
        # Mostramos un botón grande y verde que funciona como link
        st.markdown(f"""
            <a href="{link_final}" target="_blank">
                <button style="
                    background-color:#25D366; 
                    color:white; 
                    padding:15px 32px; 
                    text-align:center; 
                    text-decoration:none; 
                    display:inline-block; 
                    font-size:16px; 
                    border-radius:10px; 
                    border:none; 
                    cursor:pointer;
                    width: 100%;">
                    👉 ENVIAR COMPROBANTE AHORA
                </button>
            </a>
            """, unsafe_allow_html=True)
            
        # También mostramos el texto por si quieren copiarlo
        st.info("O si prefieres copiar el mensaje:")
        st.code(mensaje, language="text")

if __name__ == "__main__":
    main()
