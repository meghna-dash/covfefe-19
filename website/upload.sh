aws s3 rm s3://covid.arjungandhi.com/ --recursive
eval "$(conda shell.bash hook)"
conda activate covid-image-creation
python ../website-image-gen/function/lambda_function.py

aws s3 sync ./ s3://covid.arjungandhi.com
 aws cloudfront create-invalidation \
    --distribution-id E3O2DL46NY90CX\
    --paths "/*"
