# Generador de Imágenes DALL-E 2
> Desarrollado por Tony Esposito | Febrero 2025

Una aplicación Streamlit que utiliza la API de OpenAI para generar imágenes con DALL-E 2.

## Características
- Interfaz intuitiva con Streamlit
- Generación de imágenes en múltiples tamaños
- Descarga directa de imágenes generadas
- Gestión segura de API keys

## Requisitos
```bash
- Python 3.8+
- openai>=1.0.0
- streamlit
- Pillow
- requests
```

## Instalación
```bash
git clone [repositorio]
cd generador-imagenes
pip install -r requirements.txt
```

## Configuración
1. Obtén tu API key de [OpenAI](https://platform.openai.com)
2. Ingresa la key en la interfaz de la aplicación

## Uso
```bash
streamlit run app.py
```

## Tamaños Disponibles
- 1024x1024 (Cuadrado)
- 1792x1024 (Panorámico)
- 1024x1792 (Vertical)

## Contacto
Tony Esposito
- Email: [antonio.d.esposito@accenture.com]


## Licencia
MIT License

