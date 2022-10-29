import datetime
import os
from dotenv import load_dotenv

# botが始まる時間かどうかチェックする
def is_bot_time():

    start_time = set_start_time()
    end_time = set_end_time()    
    now = get_current_time()
    
    if start_time <= now <= end_time:
        return True
    
    return False

def set_start_time():
    
    load_dotenv()

    start_hour = os.environ["START_HOUR"]
    start_minute = os.environ["START_MINUTE"]
    start_second = os.environ["START_SECOND"]
 
    return datetime.time(int(start_hour), int(start_minute), int(start_second))

def set_end_time():

    load_dotenv()
    
    end_hour = os.environ["END_HOUR"]
    end_minute = os.environ["END_MINUTE"]
    end_second = os.environ["END_SECOND"]
       
    return datetime.time(int(end_hour), int(end_minute), int(end_second))

def get_current_time():
    
    JST = datetime.timezone(datetime.timedelta(hours=9), 'JST')
    return datetime.datetime.now(JST).time()
