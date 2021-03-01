from time import sleep

# import pyscreenshot
from selenium import webdriver

number = int(input("number of sudokus:\t"))

options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(options=options)

parent_url = "https://sudoku.com/expert/"
browser.get(url=parent_url)

game_tip = browser.find_element_by_class_name('game-tip')

sleep(2)

browser.execute_script("document.getElementsByClassName('game-tip')[0].style.display = 'none';")

table = browser.find_element_by_class_name("game-table")
img = table.screenshot_as_png

with open('./outputs/1.png', 'wb') as file:
    file.write(img)

for i in range(number - 1):

    game_tip = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div[3]')

    sleep(2)

    browser.execute_script("document.getElementsByClassName('game-tip')[0].style.display = 'none';")

    table = browser.find_element_by_class_name("game-table")
    img = table.screenshot_as_png

    with open(f'./outputs/{i + 2}.png', 'wb') as file:
        file.write(img)


    new_game_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/nav/div[1]/div[1]")
    new_game_button.click()

    new_game_link = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/nav/div[1]/div[2]/ul/li[2]/a")
    new_game_link.click()
