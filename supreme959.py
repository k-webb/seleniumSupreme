from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import re, time
from datetime import datetime


class target():
    def __init__(self):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #chrome_options.add_extension('Autofill.crx')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.email = 'EMAIL HERE'
        self.password = 'PASSWORD HERE'

    def UTCtoEST(self):
        current = datetime.now()
        return str(current) + " EST"

    def get_page(self,link):
        self.driver.get(link)
        return self.driver.page_source

    def parse(self,text):
        try:
            found = re.findall('<article><div class="inner-article"><a style="height:150px;"\s*href="(.*?)"><img width="150" height="150" src="(.*?)"\s*alt=(.*?)"\s\/><\/a><h1><a class="name-link" href="(.*?)">(.*?)<\/a><\/h1><p><a class="name-link"\shref="(.*?)">(.*?)<\/a><\/p><\/div><\/article',text)
            return found
        except Exception as e:
            print e

    def atc(self,size,link):
        page = self.get_page(link)
        try:
            if size == 'onesize':
                    atc = self.driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input')
                    atc.click()
                    cart = self.driver.find_element_by_xpath('//*[@id="cart"]/a[2]')
                    hover = ActionChains(self.driver).move_to_element(cart)
                    hover.perform()
                    time.sleep(.5)
                    cart.click()
            else:
                s = Select(self.driver.find_element_by_xpath('//*[@id="s"]'))
                s.select_by_visible_text(size)
                atc = self.driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input')
                atc.click()
                cart = self.driver.find_element_by_xpath('//*[@id="cart"]/a[2]')
                hover = ActionChains(self.driver).move_to_element(cart)
                hover.perform()
                time.sleep(.5)
                cart.click()
        except Exception as not_there:
            print not_there
            pass

    def chrome(self, email, password):
                login = self.driver.get('https://accounts.google.com/signin')
                email = self.driver.find_element_by_id('identifierId').send_keys(email)
                emailenter = self.driver.find_element_by_id('identifierNext').click()
                time.sleep(1)
                password = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
                passenter = self.driver.find_element_by_id('passwordNext').click()
                time.sleep(1)

    def s_keys(self, element, keys):
        for key in keys: element.send_keys(key)

    def autofill(self,name,email,phone,address1,address2,city,state,zipcode,card_num,month_exp,year_exp,last3):
        try:
            name_spot = self.driver.find_element_by_xpath('//*[@id="order_billing_name"]')
            name_spot.send_keys(name)
        except Exception as name_autofill_error:
            print 'Name Autofill Error\n'
            #print name_autofill_error
            pass
        try:
            email_spot = self.driver.find_element_by_xpath('//*[@id="order_email"]')
            email_spot.send_keys(email)
        except Exception as email_autofill_error:
            print 'Email Autofill Error\n'
            #print email_autofill_error
            pass
        try:
            phone_spot = self.driver.find_element_by_xpath('//*[@id="order_tel"]')
            self.s_keys(phone_spot, phone)
        except Exception as phone_autofill_error:
            print 'Phone Autofill Error\n'
            #print phone_autofill_error
            pass
        try:
            address1_spot = self.driver.find_element_by_xpath('//*[@id="bo"]')
            address1_spot.send_keys(address1)
        except Exception as address1_autofill_error:
            print 'Address1 Autofill Error\n'
            #print address1_autofill_error
            pass
        try:
            address2_spot = self.driver.find_element_by_xpath('//*[@id="oba3"]')
            address2_spot.send_keys(address2)
        except Exception as address2_autofill_error:
            print 'Address2 Autofill Error\n'
            #print address2_autofill_error
            pass
        try:
            zip_spot = self.driver.find_element_by_xpath('//*[@id="order_billing_zip"]')
            zip_spot.send_keys(zipcode)
        except Exception as zip_autofill_error:
            print 'Zip Month Autofill Error\n'
            #print zip_autofill_error
            pass
        try:
            city_spot = self.driver.find_element_by_xpath('//*[@id="order_billing_city"]')
            city_spot.send_keys(city)
        except Exception as city_autofill_error:
            print 'City Month Autofill Error\n'
            #print city_autofill_error
            pass
        try:
            state_spot = Select(self.driver.find_element_by_xpath('//*[@id="order_billing_state"]'))
            state_spot.select_by_visible_text(state)
        except Exception as state_autofill_error:
            print 'State Autofill Error\n'
            #print state_autofill_error
            pass
        try:
            card_spot = self.driver.find_element_by_xpath('//*[@id="cnb"]')
            self.s_keys(card_spot,card_num)
        except Exception as card_autofill_error:
            print 'CC Number Autofill Error\n'
            #print card_autofill_error
            pass
        try:
            month_spot = Select(self.driver.find_element_by_xpath('//*[@id="credit_card_month"]'))
            month_spot.select_by_visible_text(month_exp)
        except NoSuchElementException as month_autofill_error:
            print 'CC Month Autofill Error\n'
            #print month_autofill_error
            pass
        try:
            year_spot = Select(self.driver.find_element_by_xpath('//*[@id="credit_card_year"]'))
            year_spot.select_by_visible_text(year_exp)
        except Exception as year_autofill_error:
            print 'CC Year Autofill Error\n'
            #print year_autofill_error
            pass
        try:
            last_3_spot = self.driver.find_element_by_xpath('//*[@id="vval"]')
            last_3_spot.send_keys(last3)
        except Exception as last3_autofill_error:
            print 'Last 3 CC Autofill Error\n'
            #print last3_autofill_error
            pass
        try:
            accept_terms = self.driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins')
            accept_terms.click()
        except Exception as accept_terms_error:
            print 'Accept terms Error'
            pass
        print 'Autofill complete %s'%self.UTCtoEST()

    def run(self,pic_kw,size,catagory):
        print ('Getting catagory page .. %s'%self.UTCtoEST())
        #chrome = self.chrome(self.email,self.password)
        #supremecop = raw_input('Do you wish to continue?')
        page = self.get_page(catagory)
        page = page.encode('utf-8', 'ignore')
        while str(pic_kw) not in str(page):
            print 'Picture not on page, refreshing %s'%self.UTCtoEST()
            self.driver.refresh()
            time.sleep(4)
        info = self.parse(page)
        #print info
        for x in info:
            #print x
            link = 'https://www.supremenewyork.com%s'%x[0]
            product_name = str(x[4].lower())
            color = str(x[6].lower())
            pic = str(x[1])
            #print pic
            piclink = 'http:'+pic
            total = (product_name,color,link,str(piclink))
            if str(pic_kw) in str(total):
                print('found item : %s'%self.UTCtoEST())
                m = 'Item Name  : %s\nItem Color : %s\nItem Link  : %s\nItem Picture : %s\n'%(total[0],total[1],total[2],total[3])
                print (m)
                link = total[2]
                try:
                    self.atc(size,link)
                    if str(self.driver.current_url) == 'https://www.supremenewyork.com/checkout':
                        print 'Initializing Checkout :%s'%self.UTCtoEST()
                        self.autofill('Kleen Jawns','email@me.com','(123) 555-5555','1 St Rd',' ','City','KS','55555','1234567812345678','05','2018','882')
                except Exception as atc_error:
                    #print atc_error
                    print 'CLICK CHECKOUT MANUALLY NOW'
                    pass
            else:
                #print x
                pass
instance = target()
sweatshirts = 'http://www.supremenewyork.com/shop/all/sweatshirts'
t_shirts = 'http://www.supremenewyork.com/shop/all/t-shirts'
jackets = 'http://www.supremenewyork.com/shop/all/jackets'
accessories = 'http://www.supremenewyork.com/shop/all/accessories'
shoes = 'http://www.supremenewyork.com/shop/all/shoes'
hats = 'http://www.supremenewyork.com/shop/all/hats'
skate = 'http://www.supremenewyork.com/shop/all/skate'
tops_sweaters = 'http://www.supremenewyork.com/shop/all/tops_sweaters'
shirts = 'http://www.supremenewyork.com/shop/all/shirts'
pants = 'http://www.supremenewyork.com/shop/all/pants'
#EXAMPLE
#instance.run('PRODUCT NAME KEYWORD HERE','PRODUCT COLOR HERE',CATAGORY)
print'\nScript Loaded : %s\n'%instance.UTCtoEST()
instance.run('//d17ol771963kd3.cloudfront.net/137813/vi/Bd0-jT8Mrgs.jpg','Large',accessories)
