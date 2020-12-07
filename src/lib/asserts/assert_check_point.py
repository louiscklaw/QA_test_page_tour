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
  return 'tests/UI_test/functional/smoke_test_remote_parallel/actual/{}_sc_{}.png'.format(test_number, random_string)

def getExpectedScreenshotPath(test_number):
  return 'tests/UI_test/functional/smoke_test_remote_parallel/expected/{}_sc.png'.format(test_number)


def assertCheckPoint(driver ,check_point_name, error_message, fail_threshold=0.054, sleep_s=0.5, make_asserts=True, json_metadata={}):
  # assume scoped by the caller, e.g. jsom_metadata['TID_004]['TID_004_1]
  json_metadata={}

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
    json_metadata[check_point_name]='helloworld'
    # local_metadata=json_metadata[check_point_name]
    # local_metadata['img_expected']=img_expected
    # local_metadata['img_actual']=img_actual
    # local_metadata['image_test_threshold']=image_test_threshold

    # test
    img_diff_result = diff(img_expected, img_actual)
    verdict = img_diff_result < image_test_threshold
    check_point_name = os.path.basename(img_actual).replace('.png','')

    # jot output
    # local_metadata['check_point_name']=check_point_name
    # local_metadata['img_diff_result']=img_diff_result
    # local_metadata['verdict']=verdict

    DEBUG_MSG = "debug: file: {}, threshold {}, diff result {}, verdict {}".format(img_actual, image_test_threshold, img_diff_result, verdict)
    print(DEBUG_MSG)

    # assert False, 'hello fail'
    assert verdict, check_point_name+' : ' +error_msg

  # if make_asserts:
  #   assertSameImage(expected_screenshot_path, actual_screenshot_path,fail_threshold,  error_message, json_metadata)

  # os.remove(actual_screenshot_path)
