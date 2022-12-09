from pytube import YouTube, Playlist
from pySmartDL import SmartDL
from random import random
import os
import re
from urllib.parse import quote_plus

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
        regex = re.compile('[^0-9a-zA-Z&¡!{()}#$@,.óáéíñúü]+')
        s = regex.sub(' ', string)
        return s

    def download_video(self, url:str, destination:str):
        try:
            yt = YouTube(url)
        except:
            print('Ah ocurrido un error. Revise la url del video')
        else:
            try:
                print(f'Descargando video: {yt.title}')
            except:
                print('No se pudo encontrar el video. Revise la conexión')
            else:

                #Alternativa:
                #links = yt.streams.filter(progressive=True, res='720p')

                stream = yt.streams.get_highest_resolution()
                sizeMb = stream.filesize / 1000000

                print(f'Tamaño: {round(sizeMb,2)} MB {stream.resolution}')

                dest = destination.replace('\n','')

                obj = SmartDL(stream.url, dest)
                obj.start()

                path = obj.get_dest()

                self._rename(path, dest, self._clearString(yt.title), stream.subtype)


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

            print(f'Descarga de lista {p.title} completada')


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
    #tube.download_list('https://www.youtube.com/playlist?list=PLyDw0WMdjWpr60_G-pbPzBTWLitr6pd60')
    #print(tube._clearString('Cómo mamá /\>><< | * : leé leí año ayú camagüey'))
    #print(tube.segundos_a_segundos_minutos_y_horas(70))