from PIL import Image
import os

def convert_to_webp(input_path, output_path, quality=60):
    """Bir resmi WebP formatına dönüştürür."""
    with Image.open(input_path) as img:
        img.save(output_path, "WEBP", quality=quality)
        print(f"{input_path} başarıyla {output_path} olarak dönüştürüldü.")


def convert_images_in_directory(quality=60):
    """Kodun bulunduğu dizindeki 'resimler' klasöründeki tüm resimleri WebP formatına dönüştürür."""
    # Kodun bulunduğu dizinde 'resimler' klasörünü bul
    directory_path = os.getcwd()  # Kodun çalıştığı dizin
    resimler_directory = os.path.join(directory_path, "resimler")

    # 'resimler_webp' isimli çıktı klasörünü oluştur
    output_directory = os.path.join(directory_path, "resimler_webp")

    # Eğer 'resimler_webp' klasörü yoksa oluştur
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 'resimler' klasöründeki tüm dosyaları dönüştür
    for filename in os.listdir(resimler_directory):
        file_path = os.path.join(resimler_directory, filename)
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            # WebP uzantısını ekleyerek çıktı dosyasının yolunu oluştur
            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_directory, output_filename)
            
            # Resmi dönüştür
            convert_to_webp(file_path, output_path, quality)


if __name__ == "__main__":
    # Resimleri dönüştür
    convert_images_in_directory()
