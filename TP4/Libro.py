books=[]
authors=[]
prices=[]
class Book:
    def __init__ (self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def add(self):
        books.append(self.title)
        authors.append(self.author)
        prices.append(self.price)
    def view(self):
        for i in range(len(books)):
            print("name: ",books[i])
            print("author: ",authors[i])
            print("price: ",prices[i])
            print("------")