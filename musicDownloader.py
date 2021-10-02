# Copyright 2021 matjs
# --------------------
# For usage, see the documentation at: https://github.com/matjsilva/music-downloader
# 
# Change this code at YOUR own risk, this is not recommended, just use it, don't screw it.

import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

print("starting virtual browser...")
try:
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    print("virtual browser instance initialized.")
except:
    print("no virtual browser instance found, installing...")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

print("\n====== Music Downloader - by matjs ======")
print("\nsome error logs may appear now, this is normal.\n")

time.sleep(8)
print("\n\ntype 'help' for a list of commands\n")

while True:
    cmd = input('> ')

    if "single " in cmd:
        vidId = cmd.split(" ")[1].split("?v=")[1]

        try:
            print("\nsearching video...")
            driver.get(f"https://www.snappea.com/pt/videoInfo?key=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D{vidId}&searchType=link&source=seopage")
            button = driver.find_element_by_id('downloadBtn')
            print(f"video found!")
            button.click()
            print("music downloaded.")
        except:
            print("\nvideo not found!")

        print('\n')

    elif "mult " in cmd:
        links = cmd.split(" ")[1:]
        i = 0

        try:
            for vidId in links:
                i += 1

                try:
                    print(f"\nsearching video... ({i} of {len(links)})")
                    driver.get(f"https://www.snappea.com/pt/videoInfo?key=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D{vidId.split('?v=')[1]}&searchType=link&source=seopage")
                    button = driver.find_element_by_id('downloadBtn')
                    print("video found!")
                    button.click()
                    time.sleep(4)
                    print("music downloaded.")
                except:
                    print("video not found!")
        except:
            print("\nsomething went wrong, try again with another link.")

        print("\n")
    
    elif cmd == "help":
        print("\n====== Music Downloader Help ======")
        print("\nsingle [video link] => downloads only 1 song from a video link")
        print("mult [video link 1] [video link 2] ... [video link n] => downloads n songs from n video links")
        print("exit => shutdown the application\n")

    elif cmd == "exit":
        print("\nbye!\n")
        input("Press Any Key to Continue...")
        driver.quit()
        break