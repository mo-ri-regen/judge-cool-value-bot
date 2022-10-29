import random

import os
from dotenv import load_dotenv

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
    
def create_non_bot_time_text():
    
    load_dotenv()

    start_hour = os.environ["START_HOUR"]
    start_minute = os.environ["START_MINUTE"]
    start_second = os.environ["START_SECOND"]
 
    end_hour = os.environ["END_HOUR"]
    end_minute = os.environ["END_MINUTE"]
    end_second = os.environ["END_SECOND"]

    return f"{start_hour}:{start_minute}{start_second}〜{end_hour}:{end_minute}{end_second}までしかクール度は測りません😿\n明日、遊びにきてください😸"