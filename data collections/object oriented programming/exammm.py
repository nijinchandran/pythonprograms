class Book:
    def setvalue(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printvalue(self):
        print("library_name",self.library_name)
        print("book_name",self.book_name)
        print("author",self.author)
        print("pages",self.pages)

bk=Book()
bk.setvalue("luminar","My journey","Dr.A.P.J Abdul Kalam",132)
bk.printvalue()