from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep

# tell top 10 operations to be done on HTML file using Python

# 1. E-commerce Product Monitoring:
#       Automatically extract product titles, prices, and star ratings from platforms like Amazon or Flipkart.
# 2. Competitor Price Tracking:
#       Save a scraping model for one site and apply it to another to compare prices across different online stores.
# 3. Job Market Analysis:
#       Scrape job titles, salaries, and company names from portals like LinkedIn or Indeed to build a custom job search dashboard.
# 4. Stock & Financial Data Extraction:
#       Pull real-time stock prices or financial metrics from sites like Yahoo Finance for portfolio tracking.
# 5. Sentiment Analysis of Reviews:
#       Collect thousands of customer reviews and ratings for specific products to analyze consumer sentiment.
# 6. Travel & Flight Price Alerts:
#       Regularly scrape flight or hotel booking sites (e.g., Expedia) and set up notifications for when prices drop.
# 7. News Aggregation:
#       Define a sample headline and URL to automatically pull the latest news from various media outlets into a single feed.
# 8. Real Estate Market Research:
#       Extract property listings, locations, and prices to identify trends in specific neighborhoods.
# 9. Media & Image Harvesting:
#       Use the library to specifically target image URLs across galleries or product pages to build your own datasets
# 10. News & Sentiment Tracking:
#       Aggregate news articles from multiple sources and process them through NLP libraries (like NLTK) for sentiment or trend analysis.






# 1. E-commerce Product Monitoring:
#       Automatically extract product titles, prices, and star ratings from platforms
url1 = "https://www.mollywoppy.co.nz/shop/category/foodservice-31"
xpath_search_icon = "//i[@class='oi oi-search fa-stack lh-lg']"
xpath_item_text = "//a[@class='text-primary text-decoration-none']"
xpath_item_price = "//*[@class='product_price']"
xpath_next_button = "//span[@title='Next']"
xpath_no_next = "//li[@class='page-item disabled']"
css_item_img = ".oe_product_image_img_wrapper>img"
main_time_out = 10

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url1)
wait = WebDriverWait(driver,main_time_out)
wait.until(EC.presence_of_element_located((By.XPATH, xpath_search_icon)))

no_next_elements = []

while len(no_next_elements) == 0:
    all_item_txt = driver.find_elements(By.XPATH, xpath_item_text)
    all_item_price = driver.find_elements(By.XPATH, xpath_item_price)
    all_item_img = driver.find_elements(By.CSS_SELECTOR, css_item_img)
    for one_item_txt, one_item_price, one_item_img in zip(all_item_txt, all_item_price, all_item_img):
        # print(one_item_txt.text)
        # print(one_item_price.text)
        # print(one_item_img.get_attribute("src"))
        print(one_item_txt.text + " " + one_item_price.text +  " "  + one_item_img.get_attribute("src"))

    ActionChains(driver).scroll_by_amount(0, 4000).perform()
    sleep(2)
    driver.find_element(By.XPATH, xpath_next_button).click()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_search_icon)))
    no_next_elements = driver.find_elements(By.XPATH, xpath_no_next)

driver.quit()









# 3. Job Market Analysis:
#       Scrape job titles, salaries, and company names from portals like LinkedIn or Indeed to build a custom job search dashboard.

email = "zondid@neert.com"
url1 = "https://nz.jora.com/j?sp=search&trigger_source=serp&q=python"
xpath_search_button = "//*[contains(text(), 'Search jobs')]"
xpath_item_title = "//h2[contains(@class,'job-title')]"
xpath_item_company = "//span[@class='job-company']"
xpath_item_location = "//a[contains(@class,'job-location')]"
xpath_next_button = "//a[@class='next-page-button']"
xpath_pop_up_dismiss = "//div[@class='dismiss']"
main_time_out = 10
page_iteration = 10

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url1)
wait = WebDriverWait(driver,main_time_out)
wait.until(EC.presence_of_element_located((By.XPATH, xpath_search_button)))

no_next_elements = []

for idx in range(0, page_iteration):
    all_item_title = driver.find_elements(By.XPATH, xpath_item_title)
    all_item_company = driver.find_elements(By.XPATH, xpath_item_company)
    all_item_location = driver.find_elements(By.XPATH, xpath_item_location)
    for one_item_title, one_item_company, one_item_location in zip(all_item_title, all_item_company, all_item_location):
        # print(one_item_title.text)
        # print(one_item_company.text)
        # print(one_item_location.text)
        print(one_item_title.text + " " + one_item_company.text +  " "  + one_item_location.text)

    ActionChains(driver).scroll_by_amount(0, 4000).perform()
    sleep(2)
    driver.find_element(By.XPATH, xpath_next_button).click()
    dismiss_elements = driver.find_elements(By.XPATH, xpath_pop_up_dismiss)
    if len(dismiss_elements) > 1:
        if dismiss_elements[0].is_displayed():
            dismiss_elements[0].click()
    sleep(2)

driver.quit()

