player_dict = {}
index=0

class Player:
    def __init__(self, name, picture, streak, score, languages):
        self.name = name
        self.picture = picture
        self.streak = streak
        self.score = score
        self.languages = languages

        def player_list(self, name):
            if (name) not in player_dict.values():
                player_dict[index].append(name)
                index+=1

        player_list(self, self.name)
    print(player_dict)
   



