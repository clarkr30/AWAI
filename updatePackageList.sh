#!/bin/sh
source .venv/bin/activate
rm packageList.txt
pip list >> packageList.txt
deactivate