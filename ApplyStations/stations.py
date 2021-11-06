from selenium import webdriver
import time
start_time = time.time()

# Apply stations
def applyStations():
    driver.find_element_by_id('select_all').click()
    buttons = driver.find_elements_by_css_selector("button")
    for button in buttons:
        if button.text.strip() == "Actions":
            button.click()
            driver.implicitly_wait(3)
    driver.find_element_by_id("openLoadingStationModal").click()
    driver.find_element_by_xpath('//*[@id="loadingStationModal"]/div/div/div[2]/div[2]/label/input').click()
    driver.find_element_by_xpath('//*[@id="loadingStationModal"]/div/div/div[3]/button[2]').click()
    driver.implicitly_wait(3)
    
# chrome browser settings
options = webdriver.ChromeOptions()
options.add_argument('--start-maxmimized')
options.add_argument('--log-level=3')

driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
driver.set_window_size(1920, 1080)

webPage = None
while webPage != 'Q':
    webPage = input("Enter the merchant's all items link: ")
    if webPage == 'Q' or webPage == 'q':
        driver.close()
        quit()
    driver.get(webPage)
    # find total pages
    totalPages = len(driver.find_element_by_class_name("pagination").find_elements_by_tag_name("li"))

    # go through pages
    if totalPages > 1:
        for i in range(totalPages):
            nextPageNum = str(i+2)
            applyStations()
            if i < totalPages-1:
                next_page = driver.find_element_by_class_name("pagination").find_element_by_link_text(nextPageNum)
                next_page.click()
            time.sleep(0.8)
    else:
        applyStations()
    webPage = ''
    print ('Enter Q to quit or another link')