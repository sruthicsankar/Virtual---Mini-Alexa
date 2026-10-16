from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%I:%M%p")

def get_current_date():
    return datetime.now().strftime("%B%d,%Y")

def get_current_hour():
    return datetime.now().hour
