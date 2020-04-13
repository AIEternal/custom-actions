# Eternal Custom Actions Repo

* Update code in actions/actions.py
* Login to aws ECR in the console
* Build the updated image: docker build -t custom-actions:staging .
* Tag the new image: docker tag custom-actions:staging 360773397712.dkr.ecr.ap-southeast-1.amazonaws.com/custom-actions:latest
* Push to AWS ECR Repo the new image: docker push 360773397712.dkr.ecr.ap-southeast-1.amazonaws.com/custom-actions:latest
