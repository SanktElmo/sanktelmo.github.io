import cv2
from pyzbar.pyzbar import decode

def scan_barcode(image_path):
    img = cv2.imread(image_path)
    barcodes = decode(img)

    if barcodes:
        results = []
        for barcode in barcodes:
            results.append(barcode.data.decode('utf-8'))
        return results
    else:
        return []