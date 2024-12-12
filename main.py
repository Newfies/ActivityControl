## Imports
import os # Interaction with the operating system
import requests # Adds ability to make HTTP requests
import time # Adds ability to use things like sleep
import warnings # Adds warnings
import argparse # Adds the ability to use arguments for parsing

from pystyle import Center, Colors, Colorate # Adds centering, colors, and combinations of colors and styles for the visual end
from colorama import Fore # Adds Foreground color text customization

from selenium import webdriver # Adds Seleniums library for automating browser actions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Fixed missing alias for expected_conditions

from selenium.webdriver.common.keys import Keys # Adds Seleniums library for simulating keyboard input on the page for the webdriver
from selenium.webdriver.common.by import By # Adds Seleniums library for finding elements on the page for the webdriver

## Script
def main(): # Function called main to make sure it can be ran when called

    ### Proxy List
    PROXY_LIST = {
        1: "https://www.blockaway.net"
    }

    ### Argument Parsing
    parser = argparse.ArgumentParser(description="Control Activity On The Desired Website.") # Shows description when running the script with the "--help" argument

    ### Arguments
    parser.add_argument("--default", action="store_true", help="Use the default values for the script, skipping the prompts") # Adds a new argument "--default" that shows when running the "--help" argument, followed by the help description

    ### Parse Arguments
    args = parser.parse_args() # It processes the arguments and maps them for use in calling them 

    ### Script Default Variables - These are used if the prompts below recieve no input
    DEFAULT_URL = "https://gmt.gvnx.xyz/LRP"
    DEFAULT_DELAY = 1
    DEFAULT_AMOUNT = 999999
    DEFAULT_PROXY = 1

    ### Set Variables - These are used to prompt for input, however not entering anything results in using the DEFAULT values above
    if args.default: # If using the argument "--default", it will use the DEFAULT values and skip the prompts
        URL = DEFAULT_URL
        DELAY = DEFAULT_DELAY
        AMOUNT = DEFAULT_AMOUNT
        PROXY = DEFAULT_PROXY
    else:
        os.system("cls")
        print(Center.XCenter(f"Activity Control - Getting Information, Entering Nothing Uses DEFAULT Values"))
        URL = input("URL? > ")
        os.system("cls")
        print(Center.XCenter(f"Activity Control - Getting Information, Entering Nothing Uses DEFAULT Values"))
        DELAY = input("DELAY? > ")
        os.system("cls")
        print(Center.XCenter(f"Activity Control - Getting Information, Entering Nothing Uses DEFAULT Values"))
        AMOUNT = int(input("AMOUNT TO SEND? > "))
        os.system("cls")
        print(Center.XCenter(f"Activity Control - Getting Information, Entering Nothing Uses DEFAULT Values"))
        PROXY = int(input("WHICH PROXY? > "))
    
    ### Checking For Input - If nothing was entered in the prompts, they will be set to the DEFAULT values
    if not URL:
        URL = DEFAULT_URL
    elif not DELAY:
        DELAY = DEFAULT_DELAY
    elif not AMOUNT:
        AMOUNT = DEFAULT_AMOUNT
    elif not PROXY:
        PROXY = DEFAULT_PROXY

    ### Selenium
    os.system("cls")

    chrome_path = 'C:\Program Files\Chrome4Driver\chrome.exe'
    driver_path = r'E:\GitHub\Newfies\ActivityControl\chromedriver.exe'


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    extension_path1 = 'adblock.crx'
    chrome_options.add_extension(extension_path1)
    service = Service(driver_path)  # Pass the path to the driver via Service
    driver = webdriver.Chrome(service=service, options=chrome_options)

    proxy_url = PROXY_LIST.get(PROXY)  # Get the selected proxy URL
    driver.get(proxy_url)  # Open the selected proxy

    for i in range(AMOUNT):

        driver.execute_script("window.open('" + proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])

        try:
            # Wait for the element with the ID 'url' to appear on the proxy page
           # text_box = WebDriverWait(driver, DELAY).until(
           # EC.presence_of_element_located((By.ID, 'url'))
           # )

            # Input the actual target URL into the proxy page's text box and submit it
            text_box = driver.find_element(By.ID, 'url')
            text_box.send_keys(URL)  # Enter the URL to be accessed
            text_box.send_keys(Keys.RETURN)  # Submit the form

        except Exception as e:
            print(f"Error interacting with the proxy page: {e}")

        # time.sleep(DELAY)  # Wait before opening a new proxy tab

    driver.quit()



if __name__ == '__main__': # __name__ is a built in variable for Python that gets set to a value depending on how this Python script is ran, running it directly using "python main.py" sets it to "__main__", but if its imported its set to the name of the script/module that imported it
    main() # This runs the main function defined above only if it is ran directly, which is managed by the if statement




















## VARIABLES HERE
# DEFAULT_URL = https://gmt.gvnx.xyz/LRP
# DEFAULT_DELAY = 5
# DEFAULT_AMOUNT = INFINITE
# DEFAULT_VISIBLE = N 

## PROMPTS HERE
# URL = PROMPT WHERE TO GO, IF NO ANSWER THEN USE DEFAULT_URL
# DELAY = PROMPT DELAY BETWEEN NEW TAB, IF NO ANSWER USE DEFAULT_DELAY
# AMOUNT = PROMPT TOTAL AMOUNT OF TABS, IF NO ANSWER USE DEFAULT_AMOUNT
# VIsIBLE = PROMPT IF USER WANTS TO SEE THE TAB (Y/N), IF NO ANSWER USE DEFAULT_VISIBLE

## WHAT PROXY
# LIST OF PROXYS HERE
# PROMPT USER WHICH PROXY TO USE

## OPENING TABS
# ALL THAT STUFF HERE


