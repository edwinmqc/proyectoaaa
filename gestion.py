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

from cryptography.hazmat.primitives import poly1305

key = os.urandom(32)              # 256 bits (32 bytes)
mensaje="Universidad Distrital"

p = poly1305.Poly1305(key)
p.update(bytes(mensaje, encoding='utf-8'))
P = p.finalize()
P.hex()               # 128 bits (16 bytes)

# Generación y verificación exitosa
mensaje="Universidad Distrital"
key2 = os.urandom(32)             # 256 bits (32 bytes)

p2 = poly1305.Poly1305(key2)
p2.update(bytes(mensaje, encoding='utf-8'))      # Generar tag, del mensaje que será transmitido
Tag2 = p2.finalize()
# Se transmite el mensaje y el tag
mensaje_rec = "Universidad Distrital"

p3 = poly1305.Poly1305(key2)                     # Se utiliza la misma clave
p3.update(bytes(mensaje_rec, encoding='utf-8')) # Se genera el tag del mensaje recibido     
p3.verify(Tag2)                                 # Se verifica el tag generado, respecto al tag recibido (Tag2)
