from pytube import YouTube, Playlist

class DownTube:

    def get_video_url(self):
        yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
        print(f'Fetching video: {yt.title}')
        #links = yt.streams.filter(progressive=True, res='720p')

        #print(links[0].url)

        links = yt.streams.filter(progressive=True)

        for link in links:
            print(link.url)

    def get_list_titles(self):
        p = Playlist('https://www.youtube.com/playlist?list=PLyDw0WMdjWpq6qml1jT3Il5zlHLi7z_Kp')
        print(f'Fetching video: {p.title}')

        for video in p.videos:
            print(video.title)

if __name__ == "__main__":
    tube = DownTube()
    tube.get_video_url()