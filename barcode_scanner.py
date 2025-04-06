import os
from pyzbar.pyzbar import decode
from PIL import Image

def scan_barcode(bild_pfad):
    # Bild laden
    bild = Image.open(bild_pfad)
    
    # Barcode/QR-Code decodieren
    barcodes = decode(bild)
    
    # Die erste gefundene Nummer ausgeben
    if barcodes:
        for barcode in barcodes:
            barcode_daten = barcode.data.decode("utf-8")
            return barcode_daten
    else:
        print("Kein Barcode gefunden.")
        return None
