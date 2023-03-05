import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "http://menu.dining.ucla.edu/Menus/FeastAtRieber"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

wholepage = soup.find(id = "main-content")

recipelinks = wholepage.find_all("a", class_ = "recipelink")

dishnames = []
dishlinks = []

for recipelink in recipelinks:
    dishnames = dishnames + [recipelink.text]
    dishlinks = dishlinks + [recipelink['href']]

#print(dishnames, dishlinks)

data = {
    "dishname": dishnames,
    "dishlink": dishlinks
}

df = pd.DataFrame(data)
#print(df)

# for each food item:
    # long string of ingredients
    # carbon footprint(high, medium, low)
    # allergens
    # serving size
    # macros
        # calories
        # fat/saturated fat/trans fat
        # protein
        # sodium
        # fiber
        # carbs
        # cholesterol

food_fax = {

"ingredients": [],
"footprint": [],
"allergens": [],
"serving_size": [],
"calories": [],
"total fat" : [],
"saturated fat": [],
"trans fat": [],
"protein": [],
"sodium": [],
"fiber": [],
"carbs": [],
"cholesterol": []

}

URL = "http://menu.dining.ucla.edu/Recipes/977076/6"
page2 = requests.get(URL)

soup = BeautifulSoup(page2.content, "html.parser")


soup2 <- 

nutrients_page = soup.find(id = "main-content")

nutrients = nutrients_page.find_all("p", class_ = "nfserv")

print(nutrients_page)

for nutrient in nutrients:
    print(nutrient.text)


i = 1

#for dishlink in dishlinks:
    #for key in food_fax:
        #food_fax[key][i] <- 
    #df.index(dishlink)
       # print(i)
    #i = i + 1