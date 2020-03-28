#!/bin/bash
cd function 
pip install -r requirments.txt -t . 
zip -r ../lambda.zip .
mv lambda_function.py ../
mv requirments.txt ../
mv data ,,/
rm -r ./*
cd ..
mv lambda_function.py function/
mv requirments.txt function/
mv data function/data
aws lambda update-function-code --function-name covid-fact-check --zip-file fileb://lambda.zip
rm lambda.zip
