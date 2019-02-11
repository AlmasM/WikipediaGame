import sys
import process_input
import wikipedia_api


class WikipediaGame():

    def __init__(self, inputObject):
        self.inputObject = inputObject # contains 2 strings endPage and startPage
        self.searchPath = [] # path between startPage and endPage and their path
        self.visited = [] # list of all the visited pages

    def get_wiki_object(self, articleName):
        articleObject = wikipedia_api.WikipediaScrapper(articleName)
        articleObject.get_object()

        if articleObject.get_object() == []:
            return []

        return articleObject.get_url()

    def is_visited(self, item):
        '''
        Check if item was visited. If it was NOT visited, append to visited list
        :return: True if article was visited before, otherwise False
        '''
        if item not in self.visited:
            self.visited.append(item)
            return False
        else:
            return True


    def run_wikipedia_search(self, inputObject):


        # # starting article for the problem
        # startListURL = self.get_wiki_object(inputObject.startPage)
        #
        # # ending article [object] for the problem
        # endSearch = self.get_wiki_object(inputObject.endPage)
        #
        #
        # # base case: if two articles are connected directly - i.e. 1 click apart
        # if inputObject.endPage in startListURL:
        #     self.searchPath.append(inputObject.startPage)
        #     self.searchPath.append(inputObject.endPage)
        #
        #     return self.searchPath

        ''' 
        Try to find connection between articles using BFS
        Method: iterate over the list of links from the start page
                by BFS
        '''

        visited = []
        queue = []

        queue.append(inputObject.startPage)
        visited.append(inputObject.startPage)

        while queue:
            artName = visited.pop(0)
            print("articleName: {}".format(artName))
            for article in self.get_wiki_object(artName):

                if article not in visited:
                    queue.append(article)
                    visited.append(article)



        return self.searchPath




def run_string_manipulation():
    '''

    :return: object that contains two string parameters: startPage and endPage
    '''

    inputObject = process_input.ProcessInput()
    # inputObject.parse_input()

    return inputObject

def run_main():
    inputObject = run_string_manipulation()
    wikiAnswer = WikipediaGame(inputObject)
    answer = wikiAnswer.run_wikipedia_search(inputObject)

    print("Path: {}".format(answer))



if __name__ == '__main__':
    run_main()