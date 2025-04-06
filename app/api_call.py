import requests
user_id = 400000000
def get_product_info(barcode_num):
    # URL der OpenEAN API
    api_url = f"https://opengtindb.org/?ean={barcode_num}&cmd=query&queryid={user_id}"
    
    try:
        # GET-Anfrage senden
        response = requests.get(api_url)

        # Überprüfen, ob die Anfrage erfolgreich war
        if response.status_code == 200:
            # Antwort verarbeiten und ausgeben
            daten = response.text
            return daten
        else:
            print(f"Fehler: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None
