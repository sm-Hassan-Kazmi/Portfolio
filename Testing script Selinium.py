from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the webdriver (replace 'path/to/chromedriver' with your actual path)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Open the webpage
driver.get("file:///C:/Users/user/Desktop/minimalist-portfolio-master/index.html")

# Perform automated tests

# Test 1: Check if the title is correct
assert "Hassan Kazmi" in driver.title

# Test 2: Check if the social media links are present
twitter_link = driver.find_element(By.XPATH, "//a[contains(@href, 'twitter')]")
linkedin_link = driver.find_element(By.XPATH, "//a[contains(@href, 'linkedin')]")
github_link = driver.find_element(By.XPATH, "//a[contains(@href, 'github')]")

assert twitter_link.is_displayed()
assert linkedin_link.is_displayed()
assert github_link.is_displayed()

# Test 3: Check if the about section is present
about_section = driver.find_element(By.XPATH, "//h2[text()='About']")
assert about_section.is_displayed()

# Test 4: Check if the experience section is present
experience_section = driver.find_element(By.XPATH, "//h2[text()='Experience']")
assert experience_section.is_displayed()

# Test 5: Check if the skills section is present
skills_section = driver.find_element(By.XPATH, "//h2[text()='Skills']")
assert skills_section.is_displayed()

# Test 6: Check if the projects section is present
projects_section = driver.find_element(By.XPATH, "//h2[text()='Projects']")
assert projects_section.is_displayed()

# Test 7: Check if the contact section is present
contact_section = driver.find_element(By.XPATH, "//h2[text()='Contact']")
assert contact_section.is_displayed()

# Test 8: Check if the email is correct
email_element = driver.find_element(By.XPATH, "//p[text()='smkh760@gmail.com']")
assert email_element.is_displayed()

# Close the browser
driver.close()
