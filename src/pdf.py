from fpdf import FPDF

class PDF(FPDF):
    def albumName(self, albumName):
        # Line break
        self.ln(20)
        self.set_font('Times', 'B', 40)
        self.cell(0, 6, albumName, 0, 1, 'C', 0)
        self.set_font('')

    def trackName(self, trackName, color):
        self.set_fill_color(color[0], color[1], color[2])
        self.set_font('Times', 'B', 25)

        # Title
        self.multi_cell(0, 6, trackName, 0, 'C', 1)
        self.set_x(self.l_margin)
        self.set_font('')

        # Line break
        self.ln(4)

    def trackLyrics(self, trackLyrics):
        self.set_font('Times', '', 18)
        self.multi_cell(0, 6, trackLyrics, 0, 'C', False)
        self.set_x(self.l_margin)
        self.set_font('')

        # Line break
        self.ln(4)
        self.ln(4)
    
    def albumImage(self, albumImage):
        self.ln(20)
        albumImage = "../images/" + albumImage
        self.image(albumImage, w=190)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Times', 'I', 12)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'By @abiicodes', 0, 0, 'L')
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'R')

    def printAlbum(self, albumName, albumImage, tracks, color):
        self.set_font('Times', '', 12)
        self.add_page()
        self.albumImage(albumImage)
        self.albumName(albumName)
        self.add_page()

        for track in tracks:
            self.trackName(track['title'], color)
            self.trackLyrics(track['lyrics'])

    def generatePdf(self, pdfName):
        self.output(pdfName, 'F')
