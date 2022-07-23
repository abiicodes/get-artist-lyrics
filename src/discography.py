from hmac import trans_5C
import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius
import pprint

class Discography:
    baseUrl = "http://api.genius.com/"
    discography_dict = ()

    def __init__(self, token, artistName, albumsName):
        self.token = token
        self.artistName = artistName
        self.albumsName = albumsName
        self.genius = lg.Genius(
        self.token, 
        skip_non_songs=True,
        excluded_terms=["(Remix)", "(Live)"],
        remove_section_headers=True)
        self.discography_dict = self.fillDiscography(artistName, albumsName)

    def requestAlbum(self, artistName, album):
        try:
            album = self.genius.search_album(album, artistName)
            return album
        except:
            print("We didn't find lyrics for ", album )
        return None
        
    def fillDiscography(self, artistName, albumsName):
        discography = dict()
        for album in albumsName:
            albumInformation = self.requestAlbum(artistName, album)
            if albumInformation is not None:
                discography[album] = albumInformation.to_dict()
        return discography

    def clearLyrics(self, trackTitle, trackLyrics):
        text = trackLyrics.split("\n")
        text = text[1:]
        lastSentence = text[len(text)-1]
        
        # last sentence contains numbers
        index = 0
        for letter in lastSentence:
            if letter.isnumeric():
                break
            index = index + 1
        lastSentence = lastSentence[:index]
        text[len(text)-1] = lastSentence

        # delete extra endlines
        cleanedText = []
        endline = 0
        for sentence in text:
            if len(sentence):
                if endline > 2:
                    cleanedText.append('', 2)
                endline = 0
                cleanedText.append(sentence)
            else :
                endline = endline + 1
        return '\n'.join(text)

    def getDiscography(self):
        formatted = dict()

        for key, value in self.discography_dict.items():
            tracks = []
            for track in value['tracks']:
                if track['number']:
                    trackTitle = track['song']['title'].encode('latin-1', errors='ignore')
                    trackTitle = trackTitle.decode('latin-1', errors='ignore')
                    
                    trackLyrics = track['song']['lyrics'].encode('latin-1', errors='ignore')
                    trackLyrics = trackLyrics.decode('latin-1', errors='ignore')
                    
                    tracks.append({
                        'number': track['number'],
                        'title': trackTitle,
                        'lyrics': self.clearLyrics(trackTitle, trackLyrics),
                    })
            
            formatted[key] = {
                'tracks': tracks
            }
        #pprint.pprint(formatted)
        return formatted
    