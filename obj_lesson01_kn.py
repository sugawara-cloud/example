
class Book:
    def __init__(self, title, writer):
        self.title = title
        self.writer = writer
        self.release_date = None

    def printBook(self):
        if self.release_date is None:
            print(f"本のタイトルは「{self.title}」、著者は「{self.writer}」です。")
        else:
            print(
                f"本のタイトルは「{self.title}」、著者は「{self.writer}」、発売日は「{self.release_date}」です。")

    def setReleaseDate(self, release_date):
        self.release_date = release_date


if __name__ == '__main__':
    b = Book("b", "w")
    b.printBook()
    b.setReleaseDate("d")
    b.printBook()
