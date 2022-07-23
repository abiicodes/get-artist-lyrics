from pdf import PDF
from discography import Discography 

albums = [
    "Taylor Swift",
    "Fearless Taylor's version",
    "Speak Now",
    "Red Taylor's version",
    "1989 deluxe",
    "Reputation",
    "Lover",
    "Folklore deluxe",
    "Evermore deluxe"
]

color = {
    "Taylor Swift" : [152, 245, 255],
    "Fearless Taylor's version": [255, 248, 220],
    "Speak Now": [255, 225, 255],
    "Red Taylor's version": [255, 218, 185],
    "1989 deluxe": [205, 150, 205],
    "Reputation": [209, 209, 209],
    "Lover": [255, 130, 171],
    "Folklore deluxe": [238, 233, 233],
    "Evermore deluxe": [238, 197, 145],
}

def formatImageName(name):
    name = name.split(" ")
    name = ''.join(name)
    name = name.lower()
    return name + ".jpg"


token = ''
discography = Discography(token, "Taylor Swift", albums)
discographyFormatted = discography.getDiscography()

pdf = PDF()

for key, value in discographyFormatted.items():
    pdf.printAlbum(key, formatImageName(key), value['tracks'], color[key])
pdf.generatePdf('Taylor Swift albums.pdf')