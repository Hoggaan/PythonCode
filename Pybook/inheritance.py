class Publication:
    def __init__(self, code, title, author):
        self._code = code
        self._title = title
        self._author = author

    def getCode(self):
        return self._code 
    
    def getBibEntry(self):
        return '[' + self.getCode() + '] "' + self._title + '" by ' + self._author
    
    def __str__(self):
        return str(self.getBibEntry())
    
class Book( Publication ):
    def __init__(self, code, title, author, publisher, year):
        super().__init__(code, title, author)

        self._publisher = publisher
        self._year = year

    def getBibEntry(self):
        return super().getBibEntry() + ', ' + self._publisher + ', ' + str(self._year)   

class Chapter(Book):
    def __init__(self, code, title, author, publisher, year, chapter, pages):
        super().__init__(code, title, author, publisher, year)

        self._chapter = chapter
        self._pages = pages
    
    def getBibEntry( self ) :
        return super().getBibEntry() + ', Chapter ' \
            + str(self._chapter) + ' pp. ' + str(self._pages) + '. ' \
                + self._publisher + ', ' + (self._year)
    def getCode(self):
        return super().getCode() + " Waaye"


pub = Publication("Test", "Just A test", "Faarah Garaad")
book = Book("bartamaha1", "Anay i tahay", "Galbayte", "Barbarhaad Publishing", 1990)
chapter = Chapter("balamaha1", "Yaa ii tahay", "Galbayte", "Barbarhaad Publishing", 1990, 1, 500)
print(chapter.getCode())
