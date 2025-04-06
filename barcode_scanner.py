import cv2
import pytesseract
import re

def scan_barcode(image_path):
    # Bild laden und in Graustufen umwandeln
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # OCR mit Tesseract
    text = pytesseract.image_to_string(gray)

    # Barcodes finden: z.B. 12–13 Ziffern für EAN/UPC
    matches = re.findall(r'\b\d{12,13}\b', text)

    print("OCR Text:", text)
    print("Gefundene Barcodes:", matches)

    return matches[0] if matches else None