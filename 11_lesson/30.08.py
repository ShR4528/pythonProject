from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

url = 'https://www.youtube.com/c/visitestoniaofficial/videos'
driver = webdriver.Chrome()
driver.get(url)

agree_btn = driver.find_element('xpath',  '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button')
agree_btn.click()
time.sleep(5)
videos = driver.find_elements('class name', ' ytd-grid-video-renderer')


video_list = []
for video in videos:
    # '.' in front of xpath will search inside element not page
    title = video.find_element('xpath', './/*[@id="video-title"]').text
    views = video.find_element('xpath', './/*[@id="metadata-line"]/span[1]').text
    added = video.find_element('xpath', './/*[@id="metadata-line"]/span[2]').text
    link = video.find_element('xpath', './/*[@id="video-title"]').get_attribute('href')
    # print(title, views, added)

    vid_item = {
        'title': title,
        'views': views,
        'added': added,
        'link': link
    }
    video_list.append(vid_item)

print(video_list)
print(len(video_list))
# agree_btn = driver.find_element('xpath',  '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button')
# agree_btn.click()

# driver.switch_to.new_window('window')
# driver.get('http://github.com')
# second_window = driver.current_window_handle

# driver.switch_to.window(original_window)


# CDwindow-F625B06FE6DAE9FD4A89644493FE426B
# ==================================
# driver.refresh()
# element = driver.find_element('id', 'dismissible')
# element.screenshot('element_screenshot.png')
# driver.save_screenshot('page_screen.png')

# width = driver.get_window_size().get('width')
# height = driver.get_window_size().get('height')
# print(width)
# print(height)
# print(driver.get_window_size())
# driver.set_window_size(800, 600)
# driver.set_window_position(200, 200)


# link = driver.find_element('link text', 'Rohkem infot')
# link.click()
# link.sleep(5)
# link.back()
# driver.forward()
# table_data = driver.find_elements('tag name', 'td')
# for td in table_data:
#    print(td)


# print(driver.page_source)
# time.sleep(5)
# driver.close()
# print(driver.title)

# email_field = driver.find_element('name', 'user_email')
# email_field.send_keys('roman@example.com')
# email_field.send_keys(Keys.RETURN)
# time.sleep(10)
# continue_button = driver.find_element('xpath')
# continue_button = driver.find_element('class name', 'signup-continue-button')
# continue_button.click()


# email_field.is_enabled()
# email_field.is_selected()
# email_field.is_displayed()
# print(email_field.tag_name)
# print(email_field.parent)
