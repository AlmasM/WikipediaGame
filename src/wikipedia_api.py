import wikipedia


class WikipediaScrapper():

    def __init__(self, startPage, endPage):
        self.startPage = startPage
        self.endPage = endPage


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



    def get_url(self, articleName):
        articleName = self.is_exists(articleName)[0]

        articleObject = wikipedia.page(articleName)
        print(articleObject.links)



