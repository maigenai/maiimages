import streamlit as st
from openai import OpenAI
import os
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Generador de Imágenes DALL-E", layout="wide")

def init_openai():
    if 'OPENAI_API_KEY' not in st.session_state:
        st.session_state['OPENAI_API_KEY'] = ''

def generate_image(client, prompt, size="1024x1024"):
    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size=size,
            quality="standard",
            n=1
        )
        image_url = response.data[0].url
        return Image.open(BytesIO(requests.get(image_url).content))
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def main():
    st.title("🎨 Generador de Imágenes DALL-E")
    
    init_openai()
    
    api_key = st.text_input("Ingresa tu clave API de OpenAI:", 
                           value=st.session_state['OPENAI_API_KEY'],
                           type="password")
    
    if api_key:
        st.session_state['OPENAI_API_KEY'] = api_key
        client = OpenAI(api_key=api_key)
        
        prompt = st.text_area("Describe la imagen que quieres generar:", 
                            placeholder="Ej: un gato siamés blanco en estilo fotorrealista")
        
        size = st.selectbox("Tamaño:", ["1024x1024", "1792x1024", "1024x1792"])
        
        if st.button("Generar Imagen", type="primary"):
            if prompt:
                with st.spinner("Generando..."):
                    image = generate_image(client, prompt, size)
                    if image:
                        st.image(image, caption="Imagen generada", use_column_width=True)
                        
                        buf = BytesIO()
                        image.save(buf, format="PNG")
                        st.download_button(
                            label="Descargar imagen",
                            data=buf.getvalue(),
                            file_name="imagen_generada.png",
                            mime="image/png"
                        )
            else:
                st.warning("Por favor, ingresa una descripción de la imagen.")
    else:
        st.warning("Por favor, ingresa tu clave API de OpenAI para comenzar.")

if __name__ == "__main__":
    main()