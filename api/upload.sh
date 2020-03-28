#!/bin/bash
pip install -r function/requirments.txt -t function/
zip -r ./lambda.zip function/*
mv function/lambda_function.py ./
mv function/requirments.txt ./
rm -r function/*
mv lambda_function.py function/
mv requirments.txt function/
aws lambda update-function-code --function-name covid-fact-check --zip-file fileb://lambda.zip
rm lambda.zip
