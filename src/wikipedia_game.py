import process_input
import wikipedia_api



def run_wikipedia_search(inputObject):


    wikiSearch = wikipedia_api.WikipediaScrapper()

    wikiSearch.get_article("New York")
    # print(wikiSearch.is_exists("New York"))





def run_string_manipulation():

    inputObject = process_input.ProcessInput()
    inputObject.parse_input()

    return inputObject

def run_main():
    inputObject = run_string_manipulation()
    run_wikipedia_search(inputObject)


if __name__ == '__main__':
    run_main()