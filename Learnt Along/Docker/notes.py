# WHY CONTAINERS?
# so lets say i start a startup and i am the only one on the dev team can i even call that a team? Anyways, I developed an application
# or something sha. And when I was building this application, I downloaded some dependencies or libraries or i did some configurations
# and all. Then 1 month later we had enough fund to expand the dev team and we hired someone. Let's say Mosh. Mosh uses a mac but I the
# original developer uses a windows. So when Mosh wanted to run the application i developed on his machine, he had to install those
# libraries and dependencies and do the configurations. But due to like library mismatch or something, he couldn't run the app.
# Mosh complains to me, and sha I was able to help him figure out what was wrong. 3 months in, we were able to hire 3 more developers.
# and the same thing happens. Due to like installation mismatches, the application or some modules were not able to run on their own
# machine. So, I also have to help them figure out whats up. This is what happens without containers. Whenever we want to run our
# application in a new environment, we have to install the libraries manually. And this is a major issue. Because the other guys
# doing the setup might miss some libraries. They may not have the specific knowledge.

# SO WHAT EXACTLY IS DOCKER?
# It is an open platform for developing, shipping(moving packages to different environments.) and running applications or packages or containers.

# SO WHAT'S THE DIFFERENCE BETWEEN A DOCKER IMAGE AND A CONTAINER.
# Docker image is the package or articact that we can move or share accross environmets.

# when we run this docker image, it will start the application. And in order to run this application properly, it would create a container(which can be consiered
# as an environment), and install all the dependencies in the container. Then we would be able to run the application properly.


# DOCKER MOSH HAMEDANI
# Docker is a platform for building, running and shipping applications in a consistent manner. So, if your application runs on one machine, it can run and function the same way on other machines.
# WHY WOULD MY APP BE ABLE TO RUN ON ONE MACHINE AND NOT THE OTHER ONES.
# One or more files missing.
# Software version mismatch. Different versions of dependencies.
# Different configuration settings like if the environment variables are different across the machines.


# With Docker, we can easily package our application with everything it needs and run it on any machine that has docker on it.

# So, what happens when someone else wants to run my application. They just tell docker to bing up the application and docker itself automatically downloads the dependencies inside an isolated environment called a container.
# These container allows multiple applications to use different versions of a software side by side e.g one app is using fastapi version 5 and another is using fastapi version 3. And both would run side by side on the same machine without messing with each other.


# One more advantage of docker is that when we are done with a project and we no longer want to work on it, we can delete the app as well as all of its dependencies in one go. Without docker, as we work on different projects, our development machine gets cluttered with so many libraries and tools that are used by different applicatons and after a while, we don't know if we can remove one or more of these tools because we are always afraid that we would mess up with some applications.

# In a nutshell, DOCKER helps us to consistently build, run and ship applications.

# VIRTUAL MACHINES VS CONTAINERS
# Lemme just start by defininng a container. A container is an isolated environment for running an application.
# A VM is an abstraction of a machine or physical hardware. So, we can run several VMs on a real physical machine. So, on a machine running say mac, we can have 2 other VMs running windows and linux. And the tool used to make ths happen is HYPERVISOR. They are pretty much tools used for managint VMs. The benefit of these VMs is that as developers, we can run an application in isolation. And each application would have everything it needs. This is really great especially when working on different projects. But VMs also have their downsides:
# Each VM needs a full-blown OS. Which needs to be licensed, patched and monitored.
# They are slow to start since the entire OS has to be loaded just like starting a regular computer.
# They are resource intensive because each VM takes a slice of available hardware resources and at the end of the day, there is a limit to how many VMs we can run on a single machine.

# In contrast, CONTAINERS give us the same kind of isolation so we can run mulitple apps in isolation. But they
# Are more lightweight.
# Don't need a full OS. In fact all containers in a machine use the same OS of the host this means we only need to license, patch and monitor a single OS.
# Since containers use the host's OS and the OS has already started on the host, a container can start up very quickly
# They are also less hardware intensive. They need leeeessss. So, we can run 1000s of containers on the same machine.


# DOCKER ARCHITECTURE
# Docker has a client server architecture and the client talks to the server using REST API. This server is also callled the docker engine and it sits in the background and is responsible for building and running docker containers.

# Technically, a container is a process. But a special kind.
# Remember we said somn like all the containers on a machine share the OS of the host. Putting it more accurately, all containers share the KERNEL of the host.
# A kernel is the core of an OS. It is like an engine of a car, It is the part that manages applications and hardware resources.
# NB: Each OS has its own kernel or engine. And these kernels have different APIs. That is why we cannot run a windows application on LINUX. Beccuae, under the hood, this application needs to talk to the kernel of the underlying OS.
# This means on a LINUX machine, we can only run a LINUX container.
# But on a windows machine, we can run both a windows and a linux container. Because windows 10 is now bundled together with a custom built LINUX kernel in addition with the original windows kernel that has always been there. With this LINUX kernel, we can now run LINUX applications natively on windows. So, we can run both windows and LINUX containers on windows. The windows containers share the windows kernel and the LINUX containers share the LINUX kernel.
# On MacOS, there is an entirely different kernel and the rest and this kernel doesn't have support for containerized application. So, Docker on macs use a lightweight LINUX vm to run LINUX contianers.


# DEVELOPMENT WORKFLOW
# First of, we take an application, and dockerize it which means we make a small change so that it can be run by docker by adding a Dockerfile. Which is a plain text file that includes instructions that docker uses to package the application into an image.
# The image contains everything our application needs to run. Like
# A cut-down OS
# Runtime environment like Node, Python etc
# Application files
# 3rd party libraries
# Environment variables etc
# Once we have an image, we tell docker to start a container using that image and remember, we said a container is a special kind of a process because it has its own file system which is provided by the image.
# So, our application gets loaded into a container which is a process and this is how the application is run locally on our dev machine. So, instead of running a command like uvicorn app:app --reload and launching the application in a typical process, we tell docker to run it inside a container by doing something like docker run.


# Another advantage of docker is that once we have an image, we can push it to a docker registry like docker hub which is pretty much to docker what github is to git. It is a storage for docker images that anyone can use. Once our application is on docker hub, we can put it on any machine running docker. So anyone on our team can go there and download the image which contains our application and anything it needs.
# So, this other person would have the same image as the one on the development machine. So, this guy can start the application the same way we started the application on our development machine (telling docker to start a container using the image).

# With docker, we no longer need to maintain long complex release documents that have to be precisely followed. All the instructions for building the image of an application are written in a dockerfile. With that, we can package our application into an image and run it virtually anywhere.


# COMMANDS
# TO PACKAGE OUR APPLICATION INTO AN IMAGE, WE RUN THE COMMAND
# docker build -t first-image .
# -t is used to give our image a tag to identify it. And after that, we specify a name
# after giving the image a tag, we tell docker where to find the Dockerfile which is in the cwd. So, we do this
# docker build -t first-image .

# NB: The image is not stored in this cwd, it is stored somewhere else and the storage is complex and you don't
# need to know about it for now maybe sometimes later in the future when you are a senior senior dev.


# TO SEE ALL THE IMAGES ON THE COMPUTER
# docker images OR docker image ls (the ls there means list)
# REPOSITORY                 TAG       IMAGE ID       CREATED        SIZE
# first-image                latest    cc8923e0dd7d   33 hours ago   74.5MB
# docker/welcome-to-docker   latest    c1f619b6477e   3 weeks ago    18.6MB

# So, on this machine, we have 2 repos. Let's take the first one - first-image.
# repo first-image has an image with a tag "latest" which is. These tags are
# used for versioning images. So, each image can contain different versions of our application
# each image also has a unique identifier, date of creation and a size.


# TO RUN AN IMAGE IN A CONTAINER
# docker run first-image

# NOW, we can publish this image to a registry like docker hub and any other person on the team
# that needs to run the application only needs to go to docker hub and then pull the image.

# TO SEE THE CONTAINERS RUNNING LOCALLY
# docker ps (ps is short for processes)
# docker ps -a this shows all the containers on your computer even the ones that have stopped running except for the ones that have been deleted.


# NB: The docker image is portable


# # One thing that you should note is that when dealing with ports, you need to map your host port to your container port.
# Container Ports: These are the ports on which services inside the Docker container are running. When you run a service, like a web server, inside a Docker container, it listens on a specific port within the container.
# Host Ports: These are the ports on the host machine that you want to map to the container ports. The host port is the entry point from outside the Docker container.

# You can specify port mappings using the -p or --publish option when running a Docker container.
# So, the syntax is
# docker run -p <host-port>:<container-port> <image-name>

# example
# docker run -p 8080:80 nginx
# When you make a request to port 8080 on the host machine, Docker forwards that request to port 80 inside the container. Essentially, the mapping is saying, "Connect port 8080 on the host to port 80 in the container."
# So, if you open your web browser and navigate to http://localhost:8080, Docker will forward the request to the Nginx web server running inside the container on port 80. This allows you to access the web server and its services as if it were running directly on your host machine.


# TO STOP A RUNNING CONTAINER
# docker stop <container_id>

# TO DELETE AN IMAGE
# docker image rm -f <name-of-image> or <image-id>

# TO RENAME AN IMAGE
# docker tag <old-name> <new-name> # this creates a new image with the new name but you can go ahead and delte the old image if you have no need for it

# PUSHING OUR DOCKER IMAGE TO DOCKER HUB SO ANYONE CAN ACCESS IT
# We are going to be pushing the image to docker hub as a repo
# 1. docker login
# 2. docker push <image-name>:<tag> # the tag is pretty much used to specify the version of the image. I think it is usually latest
