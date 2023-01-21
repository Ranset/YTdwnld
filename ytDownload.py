from pytube import YouTube, Playlist
from pySmartDL import SmartDL
from random import random
import os
import re
from urllib.parse import quote_plus
from time import sleep
from colorama import init, deinit, reinit, Fore, Back, Style, Cursor

class DownTube:

    def _rename(self, old:str, dest:str, filename:str, extention:str):
        new = dest + filename + '.' + extention
        try:
            os.rename(old, new)
        except FileExistsError:
            new = dest + filename + '_' + str(random()) + '.' + extention
            os.rename(old, new)

            print(new)

    def segundos_a_segundos_minutos_y_horas(self, segundos):
        horas = int(segundos / 60 / 60)
        segundos -= horas*60*60
        minutos = int(segundos/60)
        segundos -= minutos*60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    def _clearString (self, string:str):
        regex = re.compile('[^0-9a-zA-Z&¡!{()}#$@,.óáéíñúüÁÉÍÓÚÜÑ]+')
        s = regex.sub(' ', string)
        return s

    def download_video(self, url:str, destination:str):
        try:
            yt = YouTube(url)
        except:
            print('Ah ocurrido un error. Revise la url del video')
        else:
            try:
                init(autoreset=True)
                print('Descargando video: '+ Fore.YELLOW + f'{yt.title}')
                deinit()
            except:
                print('No se pudo encontrar el video. Revise la conexión')
            else:

                #Alternativa:
                #links = yt.streams.filter(progressive=True, res='720p')

                try:
                    stream = yt.streams.get_highest_resolution()
                except:
                    print('No se pudo obtener link de descarga')
                else:
                    sizeMb = stream.filesize / 1000000

                    print(f'Tamaño: {round(sizeMb,2)} MB {stream.resolution}')
                    print('')

                    dest = destination.replace('\n','')

                    obj = SmartDL(stream.url, dest, progress_bar=False, timeout=15)
                    obj.start(blocking=False)

                    reinit()
                    while not obj.isFinished():
                        print("Velocidad: %s" % obj.get_speed(human=True))
                        print("Descargado: %s" % obj.get_dl_size(human=True))
                        print("Eta: %s" % obj.get_eta(human=True))
                        print("Progress: " + Fore.GREEN + f"{round(obj.get_progress()*100)}%")
                        print(f"Status: {obj.get_status()}"+"\n" + Cursor.UP(6))
                        sleep(0.2)

                    print(" "*50)
                    print(" "*50)

                    #print(Cursor.UP(13))
                    deinit()

                    if obj.isSuccessful:
                        path = obj.get_dest()

                        self._rename(path, dest, self._clearString(yt.title), stream.subtype)

                    else:
                        print("Hubo un error durante la descrga:")
                        for e in obj.get_errors():
                            print(str(e))


    def download_list(self, url:str, destination:str):
        p = Playlist(url)
        try:
            total = p.length
        except:
            print('Ah ocurrido un error. Revise la url de la lista')
        else:
            print(f'Abriendo lista: {p.title} con {total} videos')
            nro = 0

            for vidUrl in p.video_urls:
                nro += 1
                print('')
                print(f'Video {nro} de {total}')
                self.download_video(vidUrl, destination)

            reinit()
            print(Back.GREEN + Fore.BLACK + f'Descarga de lista "{p.title}" completada')
            deinit()

    def get_list(self, url:str):
        p = Playlist(url)
        try:
            total = p.length
        except:
            print('Ah ocurrido un error. Revise la url de la lista')
        else:
            print(f'Fetching lista: {p.title}')
            nro = 0
            downUrl = ''

            for vidUrl in p.video_urls:
                yt = YouTube(vidUrl)
                nro += 1
                print(f'Video {nro} de {total} - {yt.title} - dur: {self.segundos_a_segundos_minutos_y_horas(yt.length)}')
                link = yt.streams.get_highest_resolution()

                downUrl += link.url + '&title=' + quote_plus(self._clearString(self._clearString(yt.title))) + ' '

            print('Escribiendo fichero')

            f = open('./urls.txt', 'w')
            f.write(downUrl)
            f.close()

            print('Completado!')

            os.system('urls.txt')

if __name__ == "__main__":
    tube = DownTube()
    #tube.get_list('https://www.youtube.com/playlist?list=PLyDw0WMdjWprGIEt1zyejRS9fZuzhRO-M') # test
    #tube.get_list('https://www.youtube.com/playlist?list=PLyDw0WMdjWpr60_G-pbPzBTWLitr6pd60') # job
    tube.download_video('https://www.youtube.com/watch?v=V1WW1n0tEVM', 'E:\TEMP\\')
    #tube._rename('C:\\Downloads\\videoplayback','C:\\Downloads\\','Spot Servicios de Correos en APK','mp4')
    #tube.download_list('https://www.youtube.com/playlist?list=PLyDw0WMdjWprGIEt1zyejRS9fZuzhRO-M', 'E:\TEMP\\')
    #print(tube._clearString('Cómo mamá /\>><< | * : leé leí año ayú camagüey'))
    #print(tube.segundos_a_segundos_minutos_y_horas(70))
