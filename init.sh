#!/bin/bash

set -e
# Any subsequent(*) commands which fail will cause the shell script to exit immediately

# Install all python packages
if [ -x "$(command -v pip3)" ]; then
    pip3 install -r api/requirements.txt --user
elif [ -x "$(command -v pip)" ]; then
    pip install -r api/requirements.txt --user
else
    echo "Could not find pip"
    echo "Quitting..."
    exit 1
fi

export FLASK_APP="api/flask_api.py"

if [ -x "$(command -v python3)" ]; then
    python3 -m flask run
elif [ -x "$(command -v python)" ]; then
    python -m flask run
else
    echo "Could not find python"
    echo "Quitting..."
    exit 1
fi

exit 0
