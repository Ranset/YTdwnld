from pytube import YouTube, Playlist
from pytube.cli import on_progress
from pySmartDL import SmartDL
import os

class DownTube:

    def _rename(self, old:str, dest:str, filename:str, extention:str):
        new = dest + filename + '.' + extention
        os.rename(old, new)
        print(new)

    def get_video_url(self, url:str):
        yt = YouTube(url)
        print(f'Fetching video: {yt.title}')

        #Alternativa:
        #links = yt.streams.filter(progressive=True, res='720p')

        stream = yt.streams.get_lowest_resolution()
        sizeMb = stream.filesize / 1000000

        print(f'Descargando {round(sizeMb,2)} MB')

        dest = "C:\\Downloads\\"

        obj = SmartDL(stream.url, dest)
        obj.start()

        path = obj.get_dest()

        self._rename(path, dest, yt.title, stream.subtype)


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
            links = yt.streams.filter(progressive=True, res='720p')

            for link in links:
                downUrl += link.url + ' '

        print('Escribiendo fichero')

        f = open('./urls.txt', 'w')
        f.write(downUrl)
        f.close()

        print('Completado!')

if __name__ == "__main__":
    tube = DownTube()
    #tube.get_list('https://www.youtube.com/watch?v=5FsBXcrQ1XI&list=PLyDw0WMdjWprMilid88cuq85JX_oIW9lK')
    tube.get_video_url('https://www.youtube.com/watch?v=V1WW1n0tEVM')
    #tube._rename('C:\Downloads\oldest',"C:\\Downloads\\",'new.txt')