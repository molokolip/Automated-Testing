# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestGithub():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_github(self):
    self.driver.get("https://github.com/")
    self.driver.set_window_size(1296, 1000)
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-sm:nth-child(8)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "molokolip/alx-low_level_programming").click()
    element = self.driver.find_element(By.LINK_TEXT, "molokolip/alx-system_engineering-devops")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "0x00-hello_world").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".d-none .js-path-segment span").click()
    self.driver.find_element(By.LINK_TEXT, "molokolip").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mb-3:nth-child(5) .repo").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input-group-button > .btn").click()
  
