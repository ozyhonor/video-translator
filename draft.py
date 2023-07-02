import configparser 
import sys


if __name__ == "__main__":
    
    # Чтение данных из INI-файла
    try:
        config = configparser.ConfigParser()
        config.read('./secret/master-kqys.ini')
        #print(config['a'])
    except: 
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"Произошла ошибка типа: {exc_type.__name__},  {exc_traceback}")

