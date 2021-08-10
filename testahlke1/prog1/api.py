import requests

class CocktailApi():
    def __init__(self):
        self.url = "https://thecocktaildb.com/api/json/v1/"

    def get_cocktails(self, cocktailname):
        cocktail = requests.get(self.url + "/1/search.php?s=" + cocktailname)
        return cocktail.json()["drinks"]