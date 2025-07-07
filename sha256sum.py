from tqdm import tqdm
import easygui
import hashlib
import sys
import optparse

class sha256sum():
    
    def __init__(self):
        # Inicia objeto con tres atributos de texto sum, path del archivo y objeto sha256_hash
        print('*** SHA256sum ***')
        self.__sum, self.__file, self.__sha256_hash = self.__get_atributes()
            
    def __get_atributes(self):
        # Obtiene atributos mediante paser de opciones.
        parser = optparse.OptionParser()
        parser.add_option('-s','--sum', dest='sum', help='SHA256sum to verify file integrity')
        opt, args = parser.parse_args()
        if not opt.sum:
            print('[-] Please specfy a SHA256sum. Use --help for more info')
        else:
            file = easygui.fileopenbox()
            sha256_hash = hashlib.sha256()
            return opt.sum, file, sha256_hash
        return None, None, None
        
    def __get_sum(self) -> bool:
        if self.__file and self.__sum:
            # Si existe archivo y texto sum, recorreá el archivo.
            with open(self.__file, "rb") as f:
                print('[+] Loading file:', self.__file.split('/')[-1])
                # Obtendrá el numero de partes de lectura
                n = 0
                while True:
                    if not f.read(4096):
                        break
                    n+=1
                f.close()
                
            # Vuelve a procesar archivo esta vez ingresando partes a ojeto hashlib
            with open(self.__file, "rb") as f:
                for i in tqdm(range(n), desc='[+] Checking file'):
                    self.__sha256_hash.update(f.read(4096))
                f.close()
            # Devuelve booleano si realiza o no el proceso
            return True
        return False

    def check_sum(self):
        # Si realiza el checkeo entrega informe de lo realizado
        if self.__get_sum():
            print('[+] Reference SHA256sum :', self.__sum)
            print('[+] File SHA256sum      :', self.__sha256_hash.hexdigest())
            print('[+] Final Result        :', self.__sha256_hash.hexdigest()==self.__sum)
        else:
            print('[-] Operation canceled' )

if __name__=='__main__':
    sha256sum().check_sum()