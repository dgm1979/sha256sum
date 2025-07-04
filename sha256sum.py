from tqdm import tqdm
import easygui
import hashlib
import sys

class sha256sum():
    
    def __init__(self):
        self.__sum, self.__file, self.__sha256_hash = None, None, None
        if len(sys.argv)==2: 
            self.__sum = sys.argv[1]
            self.__file = easygui.fileopenbox()
            self.__sha256_hash = hashlib.sha256()
            
    def __get_sum(self):
        if self.__file and self.__sum:
            print('*** SHA256sum ***\n')
            with open(self.__file, "rb") as f:
                n = 0
                while True:
                    if not f.read(4096):
                        break
                    n+=1
                f.close()    

            with open(self.__file, "rb") as f:
                for i in tqdm(range(n)):
                    self.__sha256_hash.update(f.read(4096))
                f.close()
            return True
        return False

    def check_sum(self):
        if self.__get_sum():
            print('Archivo : ', self.__file.split('/')[-1])
            print('SHA256sum : ', self.__sum)
            print('SHA256sum archivo: ', self.__sha256_hash.hexdigest())
            print('Estado : ', self.__sha256_hash.hexdigest()==self.__sum) 
        else:
            print('Operación Cancelada')

sha256sum().check_sum()