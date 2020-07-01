from selenium import webdriver
from csv import reader

contacts =[]
with open('contacts.csv',"r") as f:
    csv_reader = reader(f)
    for row in csv_reader:
        contacts.append(row[0])

driver=webdriver.Chrome()   # Selenium chromedriver path
driver.get("https://web.whatsapp.com/")

while True:
	for name in contacts:
		try:
			user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
			user.click()

			text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
			text_box.send_keys("Hello ",name)

		    
			sendbtn= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
			sendbtn.click()
		except Exception as e:
			# print('Keep Scrolling Your whatsapp Contacts')
			pass  
		else :
			print('Successfully msg sent to',name)
			print(len(contacts)-1, 'more msgs left to send')
			contacts.remove(name)

	if(len(contacts)==0):
		break

driver.close()

