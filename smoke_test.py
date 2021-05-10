from selenium import webdriver
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(executable_path='drivers/chromedriver')
driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")

driver.maximize_window()

# LOGIN PAGE

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

# Alexander Yushkov -- 05/09/21
password_field = driver.find_element_by_id("input-password")
password_field.clear()
password_field.send_keys("123qwe123qweasdzc")

# Alexander Yushkov -- 05/09/21
login_btn = driver.find_element_by_xpath("//input[@value='Login']")

# Alexander Yushkov -- 05/09/21 (Optional)
background_color = login_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'

# Alexander Yushkov -- 05/09/21
login_btn.click()

# Alexander Yushkov -- 05/09/21
new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")

# getting the background color of the button
background_color = new_registrant_btn.value_of_css_property("background-color")
# converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
new_registrant_btn.click()

# Register Account PAGE

# Alexander Yushkov -- 05/09/21
fields = [("2", "firstname", "Alexander"), ("3", "lastname", "Yushkov"),
          ("4", "email", "test@test.com"), ("5", "telephone", "123-123-1231")]
# Alexander Yushkov -- 05/09/21
for field in fields:
    some_field = driver.find_element_by_xpath("//fieldset/div[%s]" % field[0])
    field_input = driver.find_element_by_id('input-%s' % field[1])
    field_class = some_field.get_attribute("class")
    assert "required" in field_class
    field_input.clear()
    field_input.send_keys("%s" % field[2])

# Alexander Yushkov -- 05/09/21
fax_field = driver.find_element_by_xpath("//fieldset/div[6]")
fax_input = driver.find_element_by_id('input-fax')
fax_field_class = fax_field.get_attribute("class")
assert "required" not in fax_field_class

# Alexander Yushkov -- 05/09/21
fax_input.clear()
fax_input.send_keys("321-543-9877")

driver.close()