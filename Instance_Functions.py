import duolingo
from MyPlayer import Player

index = 0
logins = []

players = []


def player_generator(lingo):
    r = lingo.get_user_info()
    name = r.get('username')
    img = r.get('avatar')
    streak = lingo.get_streak_info()
    score = lingo.get_daily_xp_progress()
    lang = lingo.get_languages(abbreviations=True)
    temp_player = Player(name, img, streak, score, lang)
    return temp_player


def add_to_logins():
    username = input("Username: ")
    password = input("Password: ")
    return {'username': username, 'password': password}


def players_iterator(dict):
    username = dict['username']
    password = dict['password']
    lingo = duolingo.Duolingo(username, password)
    players.append(player_generator(lingo))


def player_gen_csv(x,y):
    lingo = players_iter_csv(x,y)
    r = lingo.get_user_info()
    name = r.get('username')
    img = r.get('avatar')
    big_streak = lingo.get_streak_info()
    streak = big_streak.get('site_streak')
    big_score = lingo.get_daily_xp_progress()
    score = big_score.get('xp_today')
    lang = lingo.get_languages()
    temp_player = Player(name, img, streak, score, lang)
    temp_dict = {
    'username':temp_player.name, 
    'avatar': temp_player.picture,
    'streak': temp_player.streak,
    'score': temp_player.score,
    'languages': temp_player.languages
    }
    return temp_dict

def players_iter_csv(x,y):
    username = x
    password = y
    bingo = duolingo.Duolingo(username, password)
    return bingo

print(players)