import sys
import requests
#from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')
input_emo = sys.argv[1]
def Emoji_Detection(em1 = input_emo):
    html = requests.get("http://www.unicode.org/emoji/charts/full-emoji-list.html")
    emoji = BeautifulSoup(html.content, 'html.parser')
    emojis_icons = []
    emojis_desc = []
    try:
        for table_data in emoji.find_all('td', {'class': 'chars'}):
            emojis_icons.append(table_data.contents)
        emojis_list = [item for sublist in emojis_icons for item in sublist]

        for table_data in emoji.find_all('td', {'class': 'name'}):
            emojis_desc.append(table_data.contents)

        emojis_desc_list = [item for sublist in emojis_desc for item in sublist]


    except IndexError:
        print("Index value is reached")

    Emoji_List = pd.DataFrame(np.column_stack([emojis_list,emojis_desc_list]),columns=['Emoji_Symbol', 'Emoji_meaning'])
    print(Emoji_List.loc[Emoji_List['Emoji_Symbol'] == em1]['Emoji_Symbol'],'\n',Emoji_List.loc[Emoji_List['Emoji_Symbol'] == em1]['Emoji_meaning'])

if __name__ == "__main__":
    Emoji_Detection()