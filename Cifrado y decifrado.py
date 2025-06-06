from cryptography.fernet import Fernet
import os

def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

def cargar_clave():
    return open("clave.key", "rb").read()

def cifrar_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("❌ El archivo que intentas cifrar no existe.")
        return

    clave = cargar_clave()
    f = Fernet(clave)

    with open(nombre_archivo, "rb") as file:
        datos = file.read()

    datos_cifrados = f.encrypt(datos)

    with open(nombre_archivo + ".cifrado", "wb") as file:
        file.write(datos_cifrados)

    print(f"✅ Archivo cifrado: {nombre_archivo}.cifrado")

def descifrar_archivo(nombre_archivo_cifrado):
    if not os.path.exists(nombre_archivo_cifrado):
        print("❌ El archivo cifrado no existe.")
        return

    clave = cargar_clave()
    f = Fernet(clave)

    with open(nombre_archivo_cifrado, "rb") as file:
        datos_cifrados = file.read()

    try:
        datos = f.decrypt(datos_cifrados)
    except Exception as e:
        print("❌ Error al descifrar:", e)
        return

    nombre_descifrado = nombre_archivo_cifrado.replace(".cifrado", ".descifrado")
    with open(nombre_descifrado, "wb") as file:
        file.write(datos)

    print(f"✅ Archivo descifrado: {nombre_descifrado}")

# --- MAIN ---
if __name__ == "__main__":
    
    
    if not os.path.exists("clave.key"):
        generar_clave()
        print(" Clave generada y guardada como 'clave.key'")

    accion = input("¿Qué deseas hacer? (cifrar / descifrar): ").lower()
    archivo = input(" Ingresa el nombre del archivo: ")

    if accion == "cifrar":
        cifrar_archivo(archivo)
    elif accion == "descifrar":
        descifrar_archivo(archivo)
    else:
        print("❌ Acción no válida.")
