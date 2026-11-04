class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"{self.name} {self.author} {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, cheif_editor):
        self.cheif_editor = cheif_editor
        super().__init__(name)

    def print_information(self):
            print(f"{self.name} {self.cheif_editor}")    


magzine1 = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment NO. 6", "Rosa Liksom", 192)

magzine1.print_information()
book.print_information()