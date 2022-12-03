from pytube import YouTube, Playlist
from pytube.cli import on_progress
from pySmartDL import SmartDL
import os

class DownTube:

    def _rename(self, old:str, dest:str, filename:str, extention:str):
        new = dest + filename + '.' + extention
        os.rename(old, new)
        print(new)

    def download_video(self, url:str):
        yt = YouTube(url)
        print(f'Descargando video: {yt.title}')

        #Alternativa:
        #links = yt.streams.filter(progressive=True, res='720p')

        stream = yt.streams.get_lowest_resolution()
        sizeMb = stream.filesize / 1000000

        print(f'Tamaño: {round(sizeMb,2)} MB {stream.resolution}')

        dest = "C:\\Downloads\\"

        obj = SmartDL(stream.url, dest)
        obj.start()

        path = obj.get_dest()

        self._rename(path, dest, yt.title, stream.subtype)


    def download_list(self, url:str):
        p = Playlist(url)
        total = p.length
        print(f'Abriendo lista: {p.title} con {total} videos')

        for vidUrl in p.video_urls:
            self.download_video(vidUrl)

        print(f'Descarga de lista {p.title} completada')


    def get_list(self, url:str):
        p = Playlist(url)
        print(f'Fetching lista: {p.title}')
        total = p.length
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
    tube.get_list('https://www.youtube.com/playlist?list=PLyDw0WMdjWpr60_G-pbPzBTWLitr6pd60')
    #tube.download_video('https://www.youtube.com/watch?v=V1WW1n0tEVM')
    #tube._rename('C:\Downloads\oldest',"C:\\Downloads\\",'new.txt')
    #tube.download_list('https://www.youtube.com/playlist?list=PLyDw0WMdjWpr60_G-pbPzBTWLitr6pd60')