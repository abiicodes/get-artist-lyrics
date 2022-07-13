from dis import disco
from pdf import PDF
from discography import Discography 

albums = [
    #"Taylor Swift",
    #"Fearless Taylor's version",
    #"Speak Now",
    #"Red Taylor's version",
    #"1989 deluxe",
    "Reputation",
    #"Lover deluxe",
    #"Folklore deluxe",
    #"Evermore deluxe"
]

token = ''
discography = Discography(token, "Taylor Swift", albums)
discographyFormatted = discography.getDiscography()

pdf = PDF()

for key, value in discographyFormatted.items():
    pdf.printAlbum(key, value['tracks'])
pdf.generatePdf('test.pdf')