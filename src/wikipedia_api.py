import wikipedia
import sys

class WikipediaScrapper():



    def is_exists(self, articleName):
        '''
        Given article name, search wikipedia and find if it exists

        :param articleName:
        :return: If exists, return list of (related) articles; otherwise
        '''

        try:
            return wikipedia.search(articleName)

        except:
            print('Article with the given name DNE')
            return []



    def get_article(self, articleName):

        articleName = wikipedia.suggest(articleName)
        print(articleName)
        sys.exit()

        if articleName != "":
            articleObject = wikipedia.page(articleName)
            print(articleObject.links)



