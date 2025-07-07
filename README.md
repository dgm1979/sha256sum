## SHA256sum para verificar imagenes ISO

Este es un proyecto personal par verificar imagnes ISO mediante la función SHA256.

Requiere librerías del archivo "requirements.txt" para funcionar.  Pueden instalar de la siguiente manera:

pip install -r requirements.txt

Solo deben ejecutar el archivo y agragar el codigo SHA256sum que le entregue el 

python sha256sum.py -s [codigo SHA256sum]

o

python sha256sum.py --sum=[codigo SHA256sum]

El programa abrirá un dialog donde deberán seleccionar el archivo a verificar, y liso.

Si requiere ayuda, puede obtenerla mediante comando:

python sha256sum.py --help