import wikipedia
import sys

class WikipediaScrapper():

<<<<<<< HEAD
=======
    def __init__(self, articleName):
        self.articleName = articleName
        self.articleObject = object()
>>>>>>> c722ff3c66202758b84fe99386f4b7c090fd297d


    def is_exists(self):
        '''
        Given article name, search wikipedia and find if it exists

        :param articleName:
        :return: If exists, return list of (related) articles; otherwise
        '''

        try:
            wikipedia.search(self.articleName)

        except:
            print('Article with the given name DNE')
            return []

    def is_connected(self):
        '''
        Check to see if article has any links (urls) on the page
        :return: True of False
        '''

        if len(self.articleObject.links) == 0:
            return False
        else:
            return True


    def normalize_input(self, inputString):

        # inputNorm = inputString.lower()
        inputNorm = inputString.replace(" ", "_")

        return inputNorm

    def get_object(self):

        artName = self.normalize_input(self.articleName)

        try:
            self.is_exists()

            self.articleObject = wikipedia.page(artName)
            self.is_connected()


        except wikipedia.exceptions.DisambiguationError as e:

            articleModified = e.options[0]
            self.articleObject = wikipedia.page(articleModified)



    def get_url(self):
        return self.articleObject.links


<<<<<<< HEAD
    def get_article(self, articleName):

        articleName = wikipedia.suggest(articleName)
        print(articleName)
        sys.exit()

        if articleName != "":
            articleObject = wikipedia.page(articleName)
            print(articleObject.links)
=======

>>>>>>> c722ff3c66202758b84fe99386f4b7c090fd297d



