#!/usr/bin/env bash

echo "#########################################################################"
echo "################ Setting up Python Virtual Environment ##################"
echo "#########################################################################"
python3 -m venv ./venv
echo "Done!!!"

echo "#########################################################################"
echo "################ Activating Python Virtual Environment ##################"
echo "#########################################################################"
source ./activate.sh
echo "Done!!!"

echo "#########################################################################"
echo "#################### Installing PIP Dependencies ########################"
echo "#########################################################################"
pip3 install --no-cache-dir -q wheel
pip3 install --no-cache-dir -q -r ./requirements.txt
echo "Done!!!"

echo ""
echo "Executable Finished Running!!!"
echo ""
