import hashlib
import time

import requests
from bs4 import BeautifulSoup
from plyer import notification


class Site:
    """This class will store site details"""
    hash_value = None
    timer = 10


def calculate_hash(request):
    html = request.text
    soup = BeautifulSoup(html, "lxml")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines
              for phrase in line.split(" "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    hasher = hashlib.md5()
    new_md5sum = hasher.hexdigest()
    return new_md5sum


def notif(message):
    """This will be used to send notification"""
    notification.notify(
        title='site_checker',
        message=message,
        app_icon=None,
        timeout=5,
    )


def check_update(site):
    """This function will be used to check if there is any update on the given site"""
    request = requests.get(site)
    new_hash = calculate_hash(request)
    if Site.hash_value != new_hash:
        notif("The site has been updated.")
        Site.hash_value = new_hash

    time.sleep(Site.timer)
    check_update(site)


def check_site(site):
    """This function will be used to check the status of site"""
    try:
        request = requests.get(site)
        print(request.status_code)
        if request.status_code == 200:
            notif("Site is running.\n Website will be checked for updates.")
            Site.hash_value = calculate_hash(request)
            time.sleep(Site.timer)
            check_update(site)
        else:
            time.sleep(Site.timer)
            check_site(site)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        notif("Please enter correct url")
        raise SystemExit(e)


def check(site):
    """This is the function to check the site"""
    check_site(site)
