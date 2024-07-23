from PIL import Image
import os

def convert_webp_to_jpg(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.webp'):
            webp_path = os.path.join(source_folder, filename)
            with Image.open(webp_path) as img:
                jpg_filename = f'{os.path.splitext(filename)[0]}.jpg'
                jpg_path = os.path.join(destination_folder, jpg_filename)
                
                img.convert('RGB').save(jpg_path, 'JPEG')
                print(f'Convertido {filename} a {jpg_filename} y guardado en {destination_folder}')

source_folder = 'officinaw'
destination_folder = 'oficina' 

convert_webp_to_jpg(source_folder, destination_folder)
