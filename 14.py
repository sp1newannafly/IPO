from abc import ABC, abstractmethod
 
 
class Publication(ABC):
    
    @abstractmethod
    def get_info(self):
        print('Информация об издании...')
        
    def search(self, author):
        if author.lower() in self.author.lower():
            return True
        return False
 
 
class Book(Publication):
    
    def __init__(self, title, author, year_of_publication, publisher):
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.publisher = publisher
        
    def get_info(self):
        return ('Книга: "{}"\nАвтор: {}\nГод издания: {}\nИздательство: {}'.
              format(self.title, self.author, self.year_of_publication, self.publisher))
 
 
class Article(Publication):
    
    def __init__(self, title, author, magazine_title, magazine_number, year_of_publication):
        self.title = title
        self.author = author
        self.magazine_title = magazine_title
        self.magazine_number = magazine_number
        self.year_of_publication = year_of_publication
        
    def get_info(self):
        return ('Статья: "{}"\nАвтор: {}\n:Журнал "{}", {} за {} год'.
              format(self.title, self.author, self.magazine_title, self.magazine_number, self.year_of_publication))
 
 
class ElectronicResource(Publication):
    
    def __init__(self, title, author, url, annotation):
        self.title = title
        self.author = author
        self.url = url
        self.annotation = annotation
        
    def get_info(self):
        return ('Электронный ресурс: "{}"\nАвтор: {}\nСсылка: {}\nАннотация:\n{}'.
              format(self.title, self.author, self.url, self.annotation))
 
publications = []
 
publications.append(Book("Зов кукухи", "Шиз", "2020", "YA"))
publications.append(Book("Как получить зачет по ИПО?", "Максончик", "2022", "YТ"))
 
publications.append(Article("Гайд по получению зачетов", 
                            "Максончик", 
                            "СТУДЕНТЫ СГК", 
                            "1-2 (110-111)", "2021"))
publications.append(Article("Как вкусно покушать на ипо", 
                            "Поляков", 
                            "СТУДЕНТЫ СГК", 
                            "01 (104)", "2021"))
 
annotation = "Рассматривается возможность и условия получение зачета."
url = "https://vk.com/mkb10f31"
publications.append(ElectronicResource("Устойчивые зачеты", 
                                       "Максончик", 
                                       url, 
                                       annotation))
 
annotation = "Я люблю пахавать вкусно на ипо "
publications.append(ElectronicResource("Я не могу не думать о еде", 
                                       "Даник", 
                                       "https://vk.com/ovdanila", 
                                       annotation))
 
for publication in publications:
    print(publication.get_info())
    print()
    
search_word = "Шиз"
print('Результаты поиска по запросу "{}": '.format(search_word))
for publication in publications:
    if publication.search(search_word):
        print(publication.get_info())
        print()