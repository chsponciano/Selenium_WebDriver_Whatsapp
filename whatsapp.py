from selenium import webdriver

def load_driver():
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    return driver
    
_class_input_wapp = '_3FeAD'
_class_btn_wapp = '_3M-N-' 
_driver = load_driver()
input('Enter anuthing after scanning QR code')

while True:
    try:
        name = input('Enter the name of user or group: ')
        msg = input('Enter your message: ')

        _driver.find_element_by_xpath(f'//span[@title = "{name}"]').click()
        _driver.find_element_by_class_name(_class_input_wapp).send_keys(msg)
        _driver.find_element_by_class_name(_class_btn_wapp).click()
        
    except Exception as ex:
        print(f'Error: {ex}')
        _driver = load_driver()
        input('Enter anuthing after scanning QR code')
