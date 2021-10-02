import os

print("\ninstalling Music Downloader...\n")

try:
    import selenium

    print('selenium found.')
except:
    print('\nselenium not found, downloading...\n')
    os.system('pip install selenium')

try:
    import webdriver_manager

    print('webdriver_manager found.')
except:
    print('\nwebdriver_manager not found, downloading...\n')
    os.system('pip install webdriver_manager')

print("\nMusic Downloader succesfully installed.")

