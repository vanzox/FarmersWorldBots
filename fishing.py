from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://play.farmersworld.io/")
time.sleep(10)
login_button = driver.find_element_by_xpath("/html/body/div/div/div/div/button")
login_button.click()
time.sleep(1)
button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/button[1]")
button.click()
time.sleep(120)
button3 = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/section/div/section/img[1]")
button3.click()
t = time.time() + 7200
v = True
while True:
	try:
		button5 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/section/div/div/div[2]/div[3]/div[1]/button/div")
		button5.click()
		time.sleep(25)
		button4 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/button/div")
		button4.click()
		button8 = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/section/div/div/div[2]/div[3]/div[2]/button/div")
		button8.click()
		time.sleep(3600)
	except:
		try:
			button21 = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/img")
			button21.click()
			time.sleep(0.5)
		except:
			try:
				driver.refresh()
				time.sleep(10)
				login_button = driver.find_element_by_xpath("/html/body/div/div/div/div/button")
				login_button.click()
				time.sleep(1)
				button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/button[1]")
				button.click()
				time.sleep(25)
				button3 = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/section/div/section/img[1]")
				button3.click()
			except:
				driver.refresh()
				time.sleep(10)
				login_button = driver.find_element_by_xpath("/html/body/div/div/div/div/button")
				login_button.click()
				time.sleep(1)
				button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/button[1]")
				button.click()
				time.sleep(25)
				button3 = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/section/div/section/img[1]")
				button3.click()
	if v:
		e = time.time()
		s = t - e
		if s <= 0:
			driver.get("https://wax.atomichub.io/trading/transfer")
			time.sleep(10)
			ActionChains(driver).move_to_element(driver.find_element_by_xpath("//button[text()='Accept All']")).click().perform()
			time.sleep(2)
			driver.find_element_by_xpath('//*[@id="root"]/nav/div/div[4]/div/button').click()
			time.sleep(5)
			ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/button')).click().perform()
			time.sleep(15)
			buttons = driver.find_elements(By.CLASS_NAME, "small-card")
			for i in buttons:
				i.click()
				time.sleep(0.5)
			time.sleep(1)
			driver.find_element_by_class_name('form-input.form-control').send_keys("wgrjm.wam")
			time.sleep(2)
			driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[2]/div[2]/div[3]/form/div/div[2]/button').click()
			time.sleep(2)
			ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[text()="Confirm"]')).click().perform()
			time.sleep(10)
			for handle in driver.window_handles:
				driver.switch_to.window(handle)
				if driver.title == "WAX Cloud Wallet":
					try:
						driver.find_element_by_xpath('//*[@id="root"]/div/section/div[2]/div/div[5]/button').click()
					except:
						pass
			time.sleep(10)
			driver.get("https://wallet.wax.io/dashboard")
			time.sleep(10)
			driver.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/button[1]').click()
			time.sleep(2)
			buttons2 = driver.find_elements(By.CLASS_NAME, 'token-item.cursor-pointer.hover-highlight.col-md-12')
			for b in buttons2:
				ActionChains(driver).move_to_element(b).click().perform()
				time.sleep(5)
				span = driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div[2]/div[1]/div[2]/div[2]/span').text
				number = 0
				for word in span.split():
					if word.replace('.', '', 1).isdigit():
						number = str(word)
				if number != 0:
					time.sleep(2)
					driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div[2]/div[1]/div[2]/p[2]/input').send_keys(number)
					time.sleep(3)
					ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div[2]/div[3]/button')).click().perform()
					time.sleep(1)
					driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/input').send_keys('wgrjm.wam')
					time.sleep(1)
					ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div[2]/div[3]/button')).click().perform()
					time.sleep(3)
					for handle in driver.window_handles:
						driver.switch_to.window(handle)
						if driver.title == "WAX Cloud Wallet":
							try:
								driver.find_element_by_xpath('//*[@id="root"]/div/section/div[2]/div/div[5]/button').click()
							except:
								pass
					break
				else:
					break
			v = False
