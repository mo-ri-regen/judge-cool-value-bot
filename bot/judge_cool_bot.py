import random

def generate_random_number():
    return random.randrange(6)

def create_text(name, cool_value):

        text = f"{name}さんのクール度は"
        
        if cool_value == 0:
            text += "☆☆☆☆☆\n"
        elif cool_value == 1:
            text += "★☆☆☆☆\n"
        elif cool_value == 2:
            text += "★★☆☆☆\n"
        elif cool_value == 3:
            text += "★★★☆☆\n"
        elif cool_value == 4:
            text += "★★★★☆\n"
        else:
            text += "★★★★★\n"
        
        if cool_value == 0:
            text += "それでは、きょうは情熱的な1日を🔥"
        else:
            text += "それでは、きょうもCoolな1日を🆒"
        
        return text