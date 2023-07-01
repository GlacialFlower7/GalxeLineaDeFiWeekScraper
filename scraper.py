from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
url = 'https://galxe.com/Linea/campaign/GCfkeUSkbD'

i = 0
while i < 100:
	driver.get(url)

	time.sleep(7)
	try:
	    #points = driver.find_element(By.CLASS_NAME, "All participants")
	    q = driver.find_element(By.CLASS_NAME, 'participants-count')
	    #q = driver.find_element(By.CLASS_NAME, 'content')
	    print()
	    #print('test successful')
	    print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
	    print(q.text)
	    #print(q.is_displayed())
	    print()
	except NoSuchElementException:
	    print()
	    print('No participant block displayed yet T_T ')
	    print()
	s = str(q.text)
	N = s[18:-1]
	with open('./out.tab', 'a') as f:
		f.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + '\t' + str(N) + '\n'))

	## Comment out for an infinite loop:
	#i+=1
	time.sleep(1200)

driver.quit()
