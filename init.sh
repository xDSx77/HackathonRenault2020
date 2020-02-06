#!/bin/bash

set -e
# Any subsequent(*) commands which fail will cause the shell script to exit immediately

# Install all python packages
if [ -x "$(command -v pip3)" ]; then
    pip3 install -r api/requirements.txt --user
else
    pip install -r api/requirements.txt --user
fi

export FLASK_APP="api/flask_api.py"

flask run
