from datetime import date
from datetime import time
from datetime import datetime, timedelta

today = date.today()
print(today)
tomorrow = today + timedelta(1)
print(tomorrow)