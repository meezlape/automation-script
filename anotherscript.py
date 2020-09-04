import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep

class firsttest (unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(time_to_wait=5)
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")
        sleep(3)

    def test_order(self):
        self.driver.find_element_by_id("search_query_top").send_keys("printed dress")     #searchbox
        self.driver.find_element_by_name("submit_search").click()   #searchbutton
        sleep(3)
        # productclickedon
        self.driver.find_element_by_css_selector(".block_content.products-block > li:nth-of-type(1) > .product-content > h5 > a").click()
        sleep(3)
        #quantity
        self.driver.find_element_by_css_selector(".icon-plus").click()
        sleep(2)
        #sizes(dropdown)
        self.sizes = self.driver.find_element_by_id("group_1")
        size = Select(self.sizes)
        size.select_by_index(1)
        sleep(2)
        #color
        self.driver.find_element_by_id("color_16").click()
        sleep(2)
        #Addtocart

        self.driver.find_element_by_name("Submit").click()
        sleep(3)
        #Checkout
        self.driver.find_element_by_css_selector("a[title='Proceed to checkout']").click()
        sleep(3)
        #ViewCart
        self.driver.find_element_by_css_selector("a[title='View my shopping cart']").click()
        #checkout
        #self.driver.find_element_by_css_selector("a#button_order_cart > span").click()
        #proceedtocheckout
        self.driver.find_element_by_css_selector("div#center_column  a[title='Proceed to checkout'] > span").click()
        sleep(3)
        #createaccount
        self.driver.find_element_by_id("email_create").send_keys("printed3@mailinator.com")
        self.driver.find_element_by_id("SubmitCreate").submit()
        sleep(3)

        # self.driver.find_element_by_css_selector("div#center_column > form[method='post']  button > span").click()
        # self.driver.find_element_by_css_selector("input#cgv").is_selected()
        # self.driver.find_element_by_css_selector("form#form  button > span").click()
        # self.driver.find_element_by_id("email_create").send_keys("lapee@mailinator.com")
        # self.driver.find_element_by_css_selector("button#SubmitCreate > span").click()
        #sleep(3)
        # fillform
        self.driver.find_element_by_id("id_gender2").click()
        self.driver.find_element_by_id("customer_firstname").send_keys("olape")
        self.driver.find_element_by_id("customer_lastname").send_keys("olape")
        self.driver.find_element_by_id("passwd").send_keys("Yellow100*")
        sleep(2)
        #DOB
        self.years = self.driver.find_element_by_id("days")
        year = Select(self.years)
        year.select_by_index(22)
        sleep(3)
        self.months = self.driver.find_element_by_id("months")
        month = Select(self.months)
        month.select_by_index(3)
        sleep(3)
        self.years = self.driver.find_element_by_id("years")
        year = Select(self.years)
        year.select_by_index(14)
        sleep(3)
        #Address
        self.driver.find_element_by_id("firstname").send_keys("shakirah")
        self.driver.find_element_by_id("lastname").send_keys("lape")
        self.driver.find_element_by_id("company").send_keys("wema bank")
        self.driver.find_element_by_id("address1").send_keys("No 10, Michael ogun")
        self.driver.find_element_by_id("address2").send_keys("Floor 10, suite 5, sheraton complex")
        self.driver.find_element_by_id("city").send_keys("orlando")
        self.states = self.driver.find_element_by_id("id_state")
        state = Select(self.states)
        state.select_by_index(10)
        self.driver.find_element_by_id("postcode").send_keys("32836")
        self.countries = self.driver.find_element_by_id("id_country")
        country = Select(self.countries)
        country.select_by_index(1)
        sleep(2)
        self.driver.find_element_by_id("other").send_keys("any other thing")
        self.driver.find_element_by_id("phone").send_keys("08097667543")
        self.driver.find_element_by_id("phone_mobile").send_keys("07085432167")
        self.driver.find_element_by_id("alias").send_keys("n0 5, Isaac ogun")
        sleep(3)
        self.driver.find_element_by_css_selector("button#submitAccount > span").click()
        sleep(3)
        #proceedtocheckout
        self.driver.find_element_by_css_selector("div#center_column > form[method='post']  button > span").click()
        sleep(3)
        #Tickontermsandcondition
        self.driver.find_element_by_id("cgv").click()
        sleep(3)
        #proceedtocheckout
        self.driver.find_element_by_css_selector("form#form  button > span").click()
        sleep(3)
        #Paywithbankwire
        self.driver.find_element_by_css_selector("a[title='Pay by bank wire'] > span").click()
        sleep(3)
        #comfirmmyorder
        self.driver.find_element_by_css_selector("p#cart_navigation  span").click()
        #self.driver.find_element_by_xpath("//p[@id='cart_navigation']//span").click()
        sleep(3)
        #Backtoorder
        self.driver.find_element_by_css_selector("a .icon-chevron-left").click()
        sleep(3)
        #Details
        self.driver.find_element_by_css_selector("table#order-list .btn.btn-default.button.button-small > span").click()
        sleep(3)
        #Backtobankaccount
        self.driver.find_element_by_css_selector("li:nth-of-type(1) > .btn.btn-default.button.button-small > span").click()
        sleep(3)
        #Backtohome
        self.driver.find_element_by_css_selector(".footer_links span").click()
        sleep(3)


        titleofwebpage = self.driver.title
        self.assertEqual("My Store", titleofwebpage, "Webpage title not same")


    def test_signin(self):
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_id("email").send_keys("printed3@mailinator.com")
        self.driver.find_element_by_id("passwd").send_keys("Yellow100*")
        self.driver.find_element_by_id("SubmitLogin").click()
        sleep(3)
        act = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 30)
        ele = self.driver.find_element_by_css_selector("#block_top_menu > ul:nth-child(2) > li:nth-of-type(2) .sf-with-ul")
        act.move_to_element(ele).click().perform()
        sleep(3)
        self.driver.find_element_by_xpath("//div[@id='subcategories']/ul//a[@title='Evening Dresses']/img").click()
        self.driver.find_element_by_css_selector("a[title='Printed Dress'] > img[alt='Printed Dress']").click()
        self.driver.find_element_by_id("wishlist_button").click()
        self.driver.find_element_by_css_selector(".fancybox-item.fancybox-close").click()
        sleep(1)

        titleofwebpage = self.driver.title
        self.assertEqual("Printed Dress - My Store", titleofwebpage, "Webpage title not same")

    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

