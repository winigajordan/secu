from datetime import datetime

def get_current_time():
    return datetime.now().time().strftime("%H heures %M minutes %S secondes")

print(get_current_time())