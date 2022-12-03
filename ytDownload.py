from pytube import YouTube, Playlist

class DownTube:

    def get_video_url(self):
        yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
        print(f'Fetching video: {yt.title}')
        #links = yt.streams.filter(progressive=True, res='720p')

        #print(links[0].url)

        links = yt.streams.filter(progressive=True, res='720p')

        for link in links:
            print(link.url)

    def get_list_titles(self):
        p = Playlist('https://www.youtube.com/watch?v=5FsBXcrQ1XI&list=PLyDw0WMdjWprMilid88cuq85JX_oIW9lK')
        print(f'Fetching lista: {p.title}')
        total = p.length
        nro = 0
        downUrl = ''

        for video in p.videos:
            links = video.streams.filter(progressive=True, res='720p')

            for link in links:
                nro += 1
                print(f'fetching {nro} de {total} - {link.title} dur {link.vid_info}')
                downUrl += link.url + ' '

        print(downUrl)

    def get_list(self):
        p = Playlist('https://www.youtube.com/watch?v=5FsBXcrQ1XI&list=PLyDw0WMdjWprMilid88cuq85JX_oIW9lK')
        print(f'Fetching lista: {p.title}')
        total = p.length
        nro = 0
        downUrl = ''

        for url in p.video_urls:
            yt = YouTube(url)
            print(f'fetching {nro} de {total} - {yt.title} dur: {yt.length}')
            links = yt.streams.filter(progressive=True, res='720p')

            for link in links:
                downUrl += link.url + ' '

        print(downUrl)

if __name__ == "__main__":
    tube = DownTube()
    #tube.get_video_url()
    tube.get_list()