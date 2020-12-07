#!/usr/bin/env bash

set -ex

rm -rf /home/logic/_workspace/LynkedKK/QA_test_page_tour_master/src/actual/*.png

pipenv run pytest ./src
