# Python
import os
key_prueba = os.urandom(1)     # Longitud en bytes
key_prueba.hex()

print(key_prueba)


# Generación. Ejemplo de Tag
# import os

from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms
key = os.urandom(16)              # Para AES: 128 bits (16 bytes) o 256 bits (32 bytes)

c = cmac.CMAC(algorithms.AES(key))
c.update(b"Universidad Distrital 2022")
C = c.finalize()
C.hex()                           #32 bits

# Generación y verificación exitosa
mensaje="Universidad Distrital"
key2 = os.urandom(16) 

c2 = cmac.CMAC(algorithms.AES(key2))
c2.update(bytes(mensaje, encoding='utf-8'))      # Generar tag, del mensaje que será transmitido
Tag2 = c2.finalize()

# Creación del tag erróneo
mensaje="Universidad Distrital 2022"

key4 = os.urandom(16) 

c4 = cmac.CMAC(algorithms.AES(key4))
c4.update(bytes(mensaje, encoding='utf-8'))      # Generar tag, del mensaje que será transmitido
Tag3 = c4.finalize()

# Generación de tag
from cryptography.hazmat.primitives import hashes, hmac

mensaje="Universidad Distrital"
key7 = os.urandom(32) 

h = hmac.HMAC(key7, hashes.SHA256())
h.update(bytes(mensaje, encoding='utf-8'))
signature = h.finalize()
#signature
signature.hex()

# Generación y verificación exitosa

mensaje="Universidad Distrital"
key8 = os.urandom(32) 

h2 = hmac.HMAC(key, hashes.SHA256())
h2.update(bytes(mensaje, encoding='utf-8'))
Signature2 = h2.finalize()
# Se transmite el mensaje y el tag
mensaje_rec = "Universidad Distrital"

# Verificación
h3 = hmac.HMAC(key, hashes.SHA256())
h3.update(bytes(mensaje_rec, encoding='utf-8'))
h3.verify(Signature2)