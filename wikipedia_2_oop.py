"""
    Name: wikipedia_2_oop.py
    Purpose: OOP method which can be integrated
    into main JARVIS project
"""
import wikipedia

class WikipediaApp:
    def __init__(self):
        pass
    
    def get_wikipedia(self):
        """Search Wikipedia
        """
        try:
            # Type in your search term
            result = input("Search Wikipedia: ")
            # Return a summary result of 3 sentences
            self.__summary = wikipedia.summary(result, sentences=3)
            
        except:
            # Use raise for troubleshooting exceptions
            # raise
            # If there is an exception, allow the user to try again.
            print("Try a different search term.")
            
    def display_wikipedia(self):
        """
            Display Wikipedia search results
        """
        print(self.__summary)
        
# Create a jarvis program object
wikipedia_app = WikipediaApp()
while True:
    wikipedia_app.get_wikipedia()
    wikipedia_app.display_wikipedia()