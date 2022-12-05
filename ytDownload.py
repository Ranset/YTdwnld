from pytube import YouTube, Playlist
from pySmartDL import SmartDL
from random import random
import os

class DownTube:

    def _rename(self, old:str, dest:str, filename:str, extention:str):
        new = dest + filename + '.' + extention
        try:
            os.rename(old, new)
        except FileExistsError:
            new = dest + filename + '_' + str(random()) + '.' + extention
            os.rename(old, new)

        print(new)

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

                self._rename(path, dest, yt.title, stream.subtype)


    def download_list(self, url:str, destination:str):
        p = Playlist(url)
        try:
            total = p.length
        except:
            print('Ah ocurrido un error. Revise la url de la lista')
        else:
            print(f'Abriendo lista: {p.title} con {total} videos')

            for vidUrl in p.video_urls:
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
                print(f'Video {nro} de {total} - {yt.title} dur: {yt.length}')
                link = yt.streams.get_highest_resolution()

                downUrl += link.url + ' '

            print('Escribiendo fichero')

            f = open('./urls.txt', 'w')
            f.write(downUrl)
            f.close()

            print('Completado!')

if __name__ == "__main__":
    tube = DownTube()
    #tube.get_list('https://www.youtube.com/playlist?list=PLyDw0WMdjWpr60_G-pbPzBTWLitr6pd60')
    #tube.download_video('https://www.youtube.com/watch?v=V1WW1n0tEVM')
    tube._rename('C:\\Downloads\\videoplayback','C:\\Downloads\\','Spot Servicios de Correos en APK','mp4')
    #tube.download_list('https://www.youtube.com/playlist?list=PLyDw0WMdjWpr60_G-pbPzBTWLitr6pd60')