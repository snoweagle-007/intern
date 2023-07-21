from selenium import webdriver
from selenium.webdriver.common.by import By #Newer Version of selennium supports inline By.
from selenium.webdriver.support.ui import WebDriverWait #Helps in the case of Show-more-or-less
from selenium.webdriver.support import expected_conditions as EC #Waits until a certail condition is/are met

options = webdriver.ChromeOptions() #Removes the automatic closing of chrome
options.add_experimental_option("detach", True)

#Opens the website in chrome
website = "https://www.linkedin.com/jobs/view/3660532900/"
driver = webdriver.Chrome(options=options)
driver.get(website)

#Retrieves the data from the chrome as mentioned attributes from XPATH.

element = driver.find_element(By.XPATH,"//h3[contains(@class, 'base-main-card__title')]")
name = element.text.strip()
print("Job Poster's name:",name)

'''
Here, we need to extract the entire paragraph text i.e, Location, Skills, Job Description JD
But, here unlike the name tag, here the case is different.
We have the button called show more/ show less button that is included as a part of css

->Initially we need to find the Show more button 
-> Need to extract the data that is hidden this button
-> Wait for the expanded content to load via WebDriverWait and EC only terminates once of the condition is met.
-> Extract
->Print
->Terminate
'''

# 1. Finds the "Show more" button.
show_more_button = driver.find_element(By.CSS_SELECTOR,'button.show-more-less-html__button--more')

# 2. Clicks the "show more" button to reveal the hidden content.
show_more_button.click()

# Wait for the expanded content to load using WebDriverWait and EC).
wait = WebDriverWait(driver, 5)
expanded_content = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'show-more-less-html__markup')))

# Fetches text from  entire job description (JD).
job_description = expanded_content.text

# Prints the entire job description (JD).
print(job_description)

#Quits the driver.
driver.quit()