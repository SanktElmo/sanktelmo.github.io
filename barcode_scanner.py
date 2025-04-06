import cv2
from pyzbar.pyzbar import decode

def scan_barcode(bild_pfad):
    # Bild mit OpenCV laden
    bild = cv2.imread(bild_pfad)

    # Barcode dekodieren
    barcodes = decode(bild)

    print(f"Gefundene Barcodes: {len(barcodes)}")

    for barcode in barcodes:
        barcode_daten = barcode.data.decode("utf-8")
        barcode_typ = barcode.type
        print(f"Typ: {barcode_typ}, Daten: {barcode_daten}")
        return barcode_daten  # Nur den ersten Barcode zurückgeben

    print("Kein Barcode gefunden.")
    return None