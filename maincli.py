from ytDownload import DownTube, os

proxy =''

try:
    f = open('config.txt')
except:
    print('No existe el archivo config.txt')
else:
    proxy = f.readline()
    proxy = f.readline()

if proxy != '':
    os.environ['http_proxy'] = proxy 
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    print(f'Proxy fijado en: {proxy}')

print('Bienvenido a YouDL v1.1')
print('Administrador de descarga de Youtube')
print('Por Ranset Fleites - ransetfleites0@gmail.com')

while True:
    print('')
    print('Para descargar un video marque 1')
    print('Para descargar lista marque 2')
    print('Para obtener links IDM de una lista marque 3')
    print('exit para salir')

    select1 = input()

    dyt = DownTube()

    if select1 == '1':
        url = input('Coloque la url del video: ')
        dyt.download_video(url)
    elif select1 == '2':
        url = input('Coloque la url del la lista: ')
        dyt.download_list(url)
    elif select1 == '3':
        url = input('Coloque la url del la lista: ')
        dyt.get_list(url)
    elif select1 == 'exit':
        break
    else:
        print('No ha seleccionado nada')