aws s3 rm s3://covid.arjungandhi.com/ --recursive
aws s3 sync ./ s3://covid.arjungandhi.com
