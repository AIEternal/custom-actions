# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.9.0

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements
COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (otherwise comment this out)
RUN pip install -r requirements-actions.txt

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001
# docker build -t custom-actions:staging .
# docker tag custom-actions:staging 360773397712.dkr.ecr.ap-southeast-1.amazonaws.com/custom-actions:latest
# docker push 360773397712.dkr.ecr.ap-southeast-1.amazonaws.com/custom-actions:latest
