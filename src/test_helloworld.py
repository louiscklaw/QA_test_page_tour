import os,sys
from pprint import pprint

from lib.setupLocalChrome import setupLocalChrome
from lib.lib_helloworld import lib_helloworld
from lib.steps.steps_helloworld import steps_helloworld
from lib.pages.pages_helloworld import pages_helloworld

def test_helloworlds():
  print('test_helloworlds')
  lib_helloworld()
  steps_helloworld()
  pages_helloworld()