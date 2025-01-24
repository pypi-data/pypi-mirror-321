import sys
import requests
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("trcss ajax6font 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css' Kısmından indirilir.")
        sys.exit(1)

    dosya_ismi = sys.argv[1]
    url = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
    hedef_dosya = Path(f"{dosya_ismi}.css")

    try:
        # CSS dosyasını URL'den indir
        response = requests.get(url)
        response.raise_for_status()  # HTTP hatalarını kontrol et

        # CSS içeriğini dosyaya yaz
        with open(hedef_dosya, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"{hedef_dosya} başarıyla oluşturuldu ve CSS içeriği indirildi.")
    except requests.exceptions.RequestException as e:
        print(f"CSS dosyasını indirirken bir hata oluştu: {e}")
        sys.exit(1)