# import line_up_page
# import food_menu
# import line_up_confirmation_dialogue
# import item_add_page
# import cart_page

from config import *

from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint
from lib.asserts.assert_check_point_jot_metadata import assertCheckPointJotMetadata

def run_check(json_metadata, browser):
  # init test json_metadata
  json_metadata['go_to_food_menu']={}
  json_metadata['go_to_food_menu'][TESTFIELD_STATUS] = TEST_TESTING

  # URL = 'http://192.168.88.105:8002/'
  # browser.get(URL)
  browser.get(LINE_UP_PAGE)

  # assert False, 'hello fail'

  # assertCheckPoint(browser, 'go_to_food_menu_1', ERROR_MESSAGE)
  assertCheckPointJotMetadata(json_metadata['go_to_food_menu'], browser, 'go_to_food_menu_1', ERROR_MESSAGE, 0.04)

  json_metadata['go_to_food_menu'][TESTFIELD_STATUS] = TEST_PASS
