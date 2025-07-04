from tqdm import tqdm
import easygui
import hashlib
import sys

class sha256sum():
    
    def __init__(self):
        # Inicia objeto con tres atributos de texto sum, path del archivo y objeto sha256_hash
        self.__sum, self.__file, self.__sha256_hash = None, None, None
        if len(sys.argv)==2:
            # Si hay argumnto en script lo va a ingresar en la variable sum
            self.__sum = sys.argv[1]
            # Abre dialogo para otener path del archivo
            self.__file = easygui.fileopenbox()
            # Crea objeto hashlib
            self.__sha256_hash = hashlib.sha256()
            
    def __get_sum(self) -> bool:
        if self.__file and self.__sum:
            print('*** SHA256sum ***')
            # Si existe archivo y texto sum, recorreá el archivo.
            with open(self.__file, "rb") as f:
                print('Analizando archvio', self.__file.split('/')[-1])
                # Obtendrá el numero de partes de lectura
                n = 0
                while True:
                    if not f.read(4096):
                        break
                    n+=1
                f.close()
                
            # Vuelve a procesar archivo esta vez ingresando partes a ojeto hashlib
            with open(self.__file, "rb") as f:
                for i in tqdm(range(n), desc='Procesando Archivo'):
                    self.__sha256_hash.update(f.read(4096))
                f.close()
            # Devuelve booleano si realiza o no el proceso
            return True
        return False

    def check_sum(self):
        # Si realiza el checkeo entrega informe de lo realizado
        if self.__get_sum():
            print('\n*** Resultado ***')
            print('SHA256sum referancia :', self.__sum)
            print('SHA256sum archivo    :', self.__sha256_hash.hexdigest())
            print('Estado               :', self.__sha256_hash.hexdigest()==self.__sum) 
        else:
            print('\n*** Operación Cancelada ***')

sha256sum().check_sum()