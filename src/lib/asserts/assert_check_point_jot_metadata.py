import os,sys

from time import sleep
from random import randrange
from diffimg import diff

from lib.asserts.assert_image import assertSameImage

def takeScreenshot(driver, sc_filename):
    driver.save_screenshot(sc_filename)

def getRandomString():
  return randrange(1,100)

def getActualScreenshotPath(test_number):
  random_string = getRandomString()
  # return 'tests/UI_test/functional/smoke_test_remote_parallel/actual/{}_sc.png'.format(test_number)
  return 'src/actual/{}_sc_{}.png'.format(test_number, random_string)

def getExpectedScreenshotPath(test_number):
  return 'src/expected/{}_sc.png'.format(test_number)

def assertCheckPointJotMetadata(json_metadata, driver ,check_point_name, error_message, fail_threshold=0.054, sleep_s=0.5, make_asserts=True ):
  sleep(sleep_s)
  actual_screenshot_path=getActualScreenshotPath(check_point_name)
  expected_screenshot_path=getExpectedScreenshotPath(check_point_name)

  takeScreenshot(driver, actual_screenshot_path)

  if make_asserts:
    img_expected=expected_screenshot_path
    img_actual=actual_screenshot_path
    image_test_threshold=fail_threshold
    error_msg=error_message

    # jot input
    json_metadata[check_point_name]={"hello":'world'}
    json_metadata[check_point_name]['img_expected']=img_expected
    json_metadata[check_point_name]['img_actual']=img_actual
    json_metadata[check_point_name]['image_test_threshold']=image_test_threshold

    # test
    img_diff_result = diff(img_expected, img_actual)
    verdict = img_diff_result < image_test_threshold
    img_filename = os.path.basename(img_actual)

    # jot output
    json_metadata[check_point_name]['check_point_name']=check_point_name
    json_metadata[check_point_name]['img_diff_result']=img_diff_result
    json_metadata[check_point_name]['verdict']=verdict

    DEBUG_MSG = "debug: file: {}, threshold {}, diff result {}, verdict {}".format(img_actual, image_test_threshold, img_diff_result, verdict)
    print(DEBUG_MSG)

    # assert False, 'hello fail'
    assert verdict, img_filename+' : ' +error_msg+', '+str(img_diff_result)+', '+str(image_test_threshold)

  # if make_asserts:
  #   assertSameImage(expected_screenshot_path, actual_screenshot_path,fail_threshold,  error_message, json_metadata)

  # os.remove(actual_screenshot_path)
