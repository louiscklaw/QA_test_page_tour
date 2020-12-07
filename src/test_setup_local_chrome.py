import os,sys
from pprint import pprint

from lib.setupLocalChrome import setupLocalChrome

def test_setup_local_chrome():

  browser = setupLocalChrome()

  return browser
