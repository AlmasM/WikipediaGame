import wikipedia
from difflib import get_close_matches
import sys

class WikipediaScrapper():

    def __init__(self, articleName):
        self.articleName = articleName
        self.articleObject = object()


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



    def get_object(self):


        try:
            self.is_exists()

            self.articleObject = wikipedia.page(self.articleName, auto_suggest=False)
            # print("articleObject:{}".format(self.articleObject))
            self.is_connected()


        except wikipedia.exceptions.DisambiguationError as e:

            articleList = e.options
            # print("ArticleList: {}".format(articleList))
            articleModified = get_close_matches(self.articleName, articleList, n=1)

            if articleModified == []:
                articleModified = e.options[0]

            # print("articleName: {} || ArticleModified: {}".format(self.articleName, articleModified))

            self.articleObject = wikipedia.page(articleModified, auto_suggest=False)

        except wikipedia.exceptions.PageError:
            self.articleObject = []




    def get_url(self):
        return self.articleObject.links






