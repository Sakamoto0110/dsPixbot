DD_BASE_URL = "https://ddragon.leagueoflegends.com/cdn/"


def GetChampionImageURL(champion_name, img_style : "valid values: centered | loading | spash | tiles" = "centered",  skin_index = 0):
    return "{0}img/champion/{1}/{2}_{3}.jpg".format(DD_BASE_URL,img_style,champion_name,skin_index)

    