#  Cifrado y Descifrado de Archivos – Python

Este script permite **cifrar y descifrar archivos** usando una clave secreta generada automáticamente con la librería `cryptography`, asegurando la confidencialidad de la información.

---

##  Características

-  Genera una clave segura (`clave.key`)
-  Cifra cualquier archivo en formato binario (textos, imágenes, etc.)
-  Permite descifrar archivos previamente cifrados
-  Usa el estándar **Fernet** (basado en AES)

---

##  Tecnologías utilizadas

- Python 3
- Librería externa: [`cryptography`](https://pypi.org/project/cryptography/)

---

##  Instalación

```bash
pip install cryptography
git clone https://github.com/Rick5001/cifrar-decifrar-archivo.git
cd cifrar-decifrar-archivo
