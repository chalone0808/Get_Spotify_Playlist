import urllib.request
import re


class Spotify:
    def __init__(self):
        # This is my favorite playlist name called "Chill Deine Base" on Spotify
        self.url = 'https://open.spotify.com/playlist/3yLRFPxEtzOyuscyHK5cZs?si=VfjUmeX9QDOj8Z24L7h90Q'
        self.User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        self.url_content = None

    def open_url(self):
        req = urllib.request.Request(self.url)
        req.add_header('User-Agent', self.User_Agent)
        response = urllib.request.urlopen(self.url)
        return response.read()

    def get_track_names(self):
        html = Spotify.open_url(self).decode('utf-8')
        track_name_re = r"<span class=\"track-name\" dir=\"auto\">(.+?)</span>"
        track_artist_re = r"<span dir=\"auto\">(.+?)</span></a>"
        track_name = re.findall(track_name_re, html)

        # just to replace the single quote symbol
        for x in range(len(track_name)):
            try:
                track_name[x] = track_name[x].replace('&#039;', ' ')
            except:
                pass
        return track_name


if __name__ == '__main__':
    s = Spotify()
    print(s.get_track_names())
