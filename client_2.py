from datetime import datetime, timedelta
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import time
import random
import json
import os

try:
    account_cookie_file = r"C:\\Users\\erfan\\InstaPy\\logs\\cyber_expo\\cyber_expo_cookie.pkl"
    os.remove(account_cookie_file)
except FileNotFoundError:
    pass

group_of_tags = ["cybersecurity", "coding", "hacking", "pythonprogramming", "kali_linux","linux", "hacker", "hackingnews", "growthhackking", "programming", "computerscience"]


rand_num_for_follow_h = random.randint(20,50)
rand_num_for_follow_d = random.randint(40,100)
rand_num_for_unfollow_h = random.randint(10,55)
rand_num_for_unfollow_d = random.randint(100,233)
#your login credentials


with open("./credentials.json") as file:
    config = json.load(file)

insta_username=config.get("username")
insta_password=config.get("password")

def agent_1():
  session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)

  session.set_quota_supervisor(enabled=True, sleep_after=["likes_d", "comments_d", "follows", "unfollows_d"], sleepyhead=True, stochastic_flow=True, notify_me=False,
                                peak_likes_hourly=57,
                                peak_likes_daily=135,
                                peak_follows_hourly=rand_num_for_follow_h,
                                peak_follows_daily=rand_num_for_follow_d,
                                peak_unfollows_hourly=rand_num_for_unfollow_h,
                                peak_unfollows_daily=rand_num_for_unfollow_d)
  with smart_run(session):

    session.set_dont_like(["naked", "sex"])
    session.set_comments(['Well done @{}!'])
    session.set_do_like(enabled=True, percentage=80)
    session.set_do_comment(enabled=True, percentage=67)
    session.set_do_story(enabled = True, percentage = 70, simulate = True)
    session.set_do_follow(enabled=True, percentage=83, times=2)
    session.set_skip_users(skip_private=True,
                       skip_business=True,
                       business_percentage=100)

    session.like_by_tags(group_of_tags, amount=9)


def agent_2():
    session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)

    session.set_quota_supervisor(enabled=True, sleep_after=["unfollows_d"], sleepyhead=True, stochastic_flow=True, notify_me=False,
                                  peak_unfollows_hourly=rand_num_for_unfollow_h,
                                  peak_unfollows_daily=rand_num_for_unfollow_d)
    with smart_run(session):
      session.unfollow_users(amount=200, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)          


"""

now = datetime.now()
time_finish = nine_hours_from_now = datetime.now() + timedelta(hours=4)
current_time = now.strftime("%H:%M")
time_to_finish = time_finish.strftime("%H:%M")

schedule.every().day.at("20:04").do(agent_1)
schedule.every().wednesday.at("13:01").do(agent_2)

while True:
  schedule.run_pending()

"""

agent_2()

