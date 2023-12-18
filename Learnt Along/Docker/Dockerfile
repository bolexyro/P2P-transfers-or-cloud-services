# in this Dockerfile, we are writing instructions for packaging our applications

# THINGS WE NEED TO DO
# 1. install an OS
# 2. Install python. 
# 3. Copy our application files
# 4. run uvicorn app:app --reload --host 0.0.0.0 --port 8000

# FROM baseImage. This baseImage is the first layer in our container and it should be a linux image. This would try and pull this image from docker hub
FROM python:3.10-alpine

# to copy the application files in the current directory i.e the same directory where the dockerfile is into the /app directory of the image
# so the image has a file system and in that file systemm, we are going to copy the files in our cwd into the app directory.
COPY . /app

# we are setting the working directory to this directory. And when we do this, all the subsequent instructions assume that we are 
# in that directory.
WORKDIR /app

# installing the dependencies
RUN pip install -r requirements.txt

# we are using the CMD command to run a command 
# if we hadn't set our working directory to /app, our command would have to be 
# CMD ["uvicorn", "app/app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "app.py"]

# In the context of Docker, a "base image" refers to the initial, starting point for a Docker container. It serves as the foundation or core layer 
# upon which additional layers are built. A base image typically contains a minimal operating system environment along with certain pre-installed 
# software or dependencies. When you create a Docker image, you start with a base image and then add or modify its contents based on your application's requirements.
# Base images are specified in the FROM instruction in a Dockerfile. For example, in the Dockerfile I provided earlier:

# Dockerfile
# FROM python:3.8-slim

# Here, python:3.8-slim is the base image. It's an official Docker image maintained by the Python Software Foundation. 
# The image is built on top of a minimal Debian-based operating system and includes a minimal Python runtime environment (in this case, version 3.8).
# Choosing an appropriate base image is crucial because it determines the environment in which your application will run. 
# Different base images provide different levels of functionality and size. For example, some base images include only the essentials needed to run 
# a specific programming language, while others might include a more complete operating system. Commonly used base images include ones for popular 
# programming languages (like Python, Node.js, Java) or minimalistic operating systems (such as Alpine Linux). When building Docker images, 
# it's a good practice to start with a base image that aligns with your application's needs and then customize it as necessary.