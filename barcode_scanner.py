import cv2
import pyzxing  # Barcode Decoder

def scan_barcode(bild_pfad):
    # Bild mit OpenCV laden
    bild = cv2.imread(bild_pfad)

    # Barcode-Decoder initialisieren
    reader = pyzxing.BarCodeReader()

    # Barcode dekodieren
    barcode = reader.decode(bild_pfad)

    print(barcode)

    if barcode:
        return barcode[0]["parsed"]
    else:
        print("Kein Barcode gefunden.")
        return None