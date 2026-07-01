#!/usr/bin/env python3

print("-"*59)
print("AUTHOUR : inza57765-sketch")
print("DATE : 2026-06-30")
print("PROJET : REQUEST-BOT")
print("VERSION : 1.0")
print("-"*59)

"""
onutil pour récupérer le HTML5 
de n'importe quel page web

"""

import requests
from datetime import datetime
from terminal_visualisation import affiche



def main():
    try:
        url = input("\n\nURL : ")
        print(f"\nprogramme lancé : [{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}]\n")
        head = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; win64x; x64) AppleWebKit/537.36"
        }

        time = 5
        response = requests.get(url, headers=head, timeout=time)
        url_view = response.ok
        status = response.status_code
        server = response.headers.get("server","Non Indiqué")
        html = response.text
        doc_type = response.headers.get("Content-Type","Non indiqué")


        if response.status_code == 200:
            affiche(url, url_view, status, server, html, doc_type)


        else:
            print(f"STATUS : {status}")
            print("la page est inaccéssible")

            print("-"*59)
            print("\t\t      REQUESTS-BOT")
            print("-"*59)


    except requests.exceptions.ConnectionError:
        print("impossible de se connecter au site")
        
        print("-"*59)
        print("\t\t      REQUESTS-BOT")
        print("-"*59)


    except requests.exceptions.Timeout:
        print("le serveur à mis trop de temps à répondre")
        
        print("-"*59)
        print("\t\t      REQUESTS-BOT")
        print("-"*59)

    except FileNotFoundError:
        print("il y à un fichier introuvable")

    except Exception as e:
        print(f"Erreur inattendue de : {e}")

    except KeyboardInterrupt:
        print("Programme arrêté")

        print("-"*59)
        print("\t\t      REQUESTS-BOT")
        print("-"*59)


if __name__ == '__main__':
      main()
