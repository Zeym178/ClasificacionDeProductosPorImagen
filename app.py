import os
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Cargar el modelo
modelo = tf.keras.models.load_model('Modelo_Reconocimiento_Mercado.keras')

# Nombres de las categorías del modelo
nombres_categorias = ['bebidas', 'carnes', 'dormitorio', 'frutas_verduras', 'oficina']  # Cambia esto según tus categorías

def clasificar_imagenes(imagen):
    imagen_entrada = tf.keras.utils.img_to_array(imagen)
    imagen_entrada = tf.image.resize(imagen_entrada, (180, 180))
    imagen_entrada = tf.expand_dims(imagen_entrada, 0)  # Agregar una dimensión de batch

    predicciones = modelo.predict(imagen_entrada)
    resultado = tf.nn.softmax(predicciones[0])

    # Obtener los índices de las dos mayores probabilidades
    indices_mayores = np.argsort(resultado)[-2:][::-1]

    resultado_primero = nombres_categorias[indices_mayores[0]]
    puntuacion_primero = resultado[indices_mayores[0]] * 100
    resultado_segundo = nombres_categorias[indices_mayores[1]]
    puntuacion_segundo = resultado[indices_mayores[1]] * 100

    return resultado_primero

# Crear la aplicación Streamlit
st.title('Formulario de Producto')

# Crear columnas para organizar la interfaz
col1, col2 = st.columns([1, 2])

with col1:
    # Subir una imagen
    archivo_subido = st.file_uploader('Sube una imagen', type=['jpg', 'jpeg', 'png'])

# Variables para almacenar los valores del formulario
nombre_producto = ''
categoria_producto = ''
descripcion_producto = ''
precio_producto = ''

if archivo_subido is not None:
    imagen = Image.open(archivo_subido)
    
    with col1:
        st.image(imagen, caption='Imagen subida', use_column_width=True)
    
    # Actualizar los valores del formulario
    nombre_producto = archivo_subido.name.split('.')[0]
    categoria_producto = clasificar_imagenes(imagen)

with col2:
    # Mostrar el formulario con los valores actualizados
    nombre_producto = st.text_input('Nombre del Producto', value=nombre_producto)
    categoria_producto = st.text_input('Categoría', value=categoria_producto)
    descripcion_producto = st.text_input('Descripción', 'Descripción')
    precio_producto = st.text_input('Precio', 'Precio de Venta')
