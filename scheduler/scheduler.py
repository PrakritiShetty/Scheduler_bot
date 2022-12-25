from twilio_func import *
from datetime import datetime
from datetime import date
from datetime import time
import apscheduler
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dateutil.parser import parse

s = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]

dt = date.today().strftime('%d/%m/%y')
now_date = datetime.strptime(dt, '%d/%m/%y')
rem_day = now_date.day
rem_month = now_date.month
rem_year = now_date.year

t = datetime(rem_year, rem_month, rem_day, 9, 0)
local = pytz.timezone("Asia/Kolkata")
local_dt = local.localize(t, is_dst=None)
utc_dt = local_dt.astimezone(pytz,utc)

scheduler = BlockingScheduler()
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json")
client = gspread.authorize(creds)

# logic is to traverse all dates and then if one of the dates correspond to today, we'll send a reminder
worksheet = client.open("Reminders").sheet1
list_of_lists = worksheet.get_all_values()
for row in list_of_lists:
    p=parse(row[0])
    parsed_date = p.strftime('%d/%m/%y')
    if parsed_date == dt:
        scheduler.add_job(send_rem, 'date', run_date = utc_dt, args=[row[0],row[1]])
    else:
        pass

scheduler.start()

# now, will deploy both apps on cloud(heroku)
# procfile is a mechanism for declaring what commands are run by our app's dynos on the heroku platform