from ytDownload import DownTube, os

import sys

proxy =''
dest = ''

try:
    f = open('config.txt')
except:
    print('No existe el archivo config.txt')
else:
    dest = f.readline()
    dest = f.readline()
    proxy = f.readline()
    proxy = f.readline()
    f.close()

if proxy != '':
    os.environ['http_proxy'] = proxy 
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    print(f'Proxy fijado en: {proxy}')
    print('')


dyt = DownTube()


if len(sys.argv) != 3:
    print('Administrador de descarga de Youtube')
    print('Por Ranset Fleites - ransetfleites0@gmail.com')
    print('Cliente CLI v 1.4.5')
    print('')
    print('AYUDA:')
    print('Debe colocar 2 argumentos:')
    print('El primer argumento es la opción y el segundo la URL')
    print('OPCIONES:')
    print('-dv      Download video (Descargar un video)')
    print('-dl      Download list (Descargar una lista)')
    print('-gl      Get list (Obtener links de descarga de una lista en un txt)')
    print('')
    print('-u txt    Ver urls ya descargadas')
    print('')
    print('EJEMPLO:')
    print('cli.exe -gl https://www.youtube.com/playlist?list=PLyDw0WMdjWprGIEt1zyejRS9fZuzhRO-M')

else:
    select1 = sys.argv[1]
    url = sys.argv[2]

    if select1 == '-dv':
        dyt.download_video(url, dest)
    elif select1 == '-dl':
        dyt.download_list(url, dest)
    elif select1 == '-gl':
        dyt.get_list(url)
    elif select1 == '-u':
        dyt.open_urls(url)