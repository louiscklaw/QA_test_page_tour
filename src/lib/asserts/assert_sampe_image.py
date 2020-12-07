import os,sys
from pprint import pprint
from diffimg import diff

def assertSameImageObsoleted(img_expected, img_actual,image_test_threshold=0.05, error_msg='same image is expected but diff image found', json_metadata={}):
  ''' exception if different image '''

  json_metadata['img_expected']=img_expected
  json_metadata['img_actual']=img_actual
  json_metadata['image_test_threshold']=image_test_threshold

  img_filename = os.path.basename(img_actual)
  # true = same image
  same_image = diff(img_expected, img_actual) < image_test_threshold
  json_metadata['same_image']=same_image

  print("debug: diff result {}".format(diff(img_expected, img_actual)))
  print("debug: image_test_threshold {}".format(image_test_threshold))
  print("debug: diff assert diff result {}, {}".format(same_image, img_filename))

  assert same_image, error_msg + "debug: diff result {} for file {}".format(diff(img_expected, img_actual))
