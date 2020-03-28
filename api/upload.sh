#!/bin/bash
cd function
pip install -r requirements.txt -t .
zip -r ../lambda.zip ./*
pip uninstall -r requirements.txt -t .
cd ..
aws lambda update-function-code --function-name covid-face-check --zip-file fileb://lambda.zip
