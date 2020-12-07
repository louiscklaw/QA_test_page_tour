import os,sys
from pprint import pprint
from diffimg import diff

def assertSameImage(img_expected, img_actual,image_test_threshold=0.05, error_msg='same image is expected but diff image found', json_metadata={}):
  ''' exception if different image '''

  # jot input
  json_metadata['img_expected']=img_expected
  json_metadata['img_actual']=img_actual
  json_metadata['image_test_threshold']=image_test_threshold

  img_diff_result = diff(img_expected, img_actual)
  verdict = img_diff_result < image_test_threshold
  check_point_name = os.path.basename(img_actual).replace('.png','')

  # jot output
  json_metadata['check_point_name']=check_point_name
  json_metadata['img_diff_result']=img_diff_result
  json_metadata['verdict']=verdict

  DEBUG_MSG = "debug: file: {}, threshold {}, diff result {}, verdict {}".format(img_actual, image_test_threshold, img_diff_result, verdict)
  print(DEBUG_MSG)

  assert verdict, check_point_name+' : ' +error_msg
