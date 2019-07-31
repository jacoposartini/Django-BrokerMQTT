#!/bin/bash
pip3 install -r requirements.txt
git clone https://github.com/jacoposartini/SQLite3_HBMQTT_Plugins.git
cd SQLite3_HBMQTT_Plugins
python3 setup.py install

echo "give me a bottle of rum!"
