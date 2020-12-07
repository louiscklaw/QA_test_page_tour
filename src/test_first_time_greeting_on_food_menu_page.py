import os,sys
from pprint import pprint

from lib.steps import *
from lib.setupLocalChrome import setupLocalChrome

def test_first_time_greeting_on_food_menu_page():

  browser = setupLocalChrome()

  go_to_line_up_page.run_check({}, browser)

  return browser
