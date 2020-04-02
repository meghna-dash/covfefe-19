#!/bin/bash
npm run-script build
cd build
zip -r ../build.zip ./*
cd ..
aws s3 cp build.zip s3://covid.arjungandhi.com/
rm build.zip
