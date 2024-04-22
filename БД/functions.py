import random
import datetime
from datetime import timedelta
import string

def random_date(start_date, end_date):
    random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date
    
def random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string