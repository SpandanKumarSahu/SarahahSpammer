from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lyricwikia

lyrics = lyricwikia.get_lyrics('Travie McCoy', 'Billionaire')
lyrics = lyrics.split('\n')

url = 'https://ravir216.sarahah.com/'

for i in range(len(lyrics)):
    driver = webdriver.Firefox()
    driver.get(url)
    text_elem = driver.find_element_by_id("Text")
    button_elem = driver.find_element_by_id("Send")

    text_elem.clear()
    text_elem.send_keys(lyrics[i])
    text_elem.send_keys(Keys.RETURN)

    button_elem.click()
    driver.close()
