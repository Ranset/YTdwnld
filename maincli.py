from ytDownload import DownTube, os

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

print('Bienvenido a YouDL v1.3.2')
print('Administrador de descarga de Youtube')
print('Por Ranset Fleites - ransetfleites0@gmail.com')

while True:
    print('')
    print('1 - Descargar un video')
    print('2 - Descargar lista')
    print('3 - Obtener links IDM de una lista')

    select1 = input('Elija una opción: ')

    dyt = DownTube()

    if select1 == '1':
        url = input('Coloque la url del video: ')
        dyt.download_video(url, dest)
    elif select1 == '2':
        url = input('Coloque la url del la lista: ')
        dyt.download_list(url, dest)
    
    elif select1 == '3':
        url = input('Coloque la url del la lista: ')
        dyt.get_list(url)
    elif select1 == 'exit':
        break
    else:
        print('No ha seleccionado nada')