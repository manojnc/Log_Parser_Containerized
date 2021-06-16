# carta_solution

Introduction :
==============

This tool is designed to parse a given log file and aggregate the metrics around incoming client ips. The job is hosted on a webserver and containerized using docker and the output is made available through API access on port 8080 of the host running the container. 

Installation :
==============

Installing this tool requires docker to be pre installed in the system. Please follow the steps below to configure the webserver.

1) Copy the files carta_solution.py,nginx and Dockerfile to a system where docker is installed.
2) Build the docker image using the following commands from a user who is authorized to issue docker management commands.
docker build -t solution-image .				# Solution-image is a custom name and can be modified as per user convinience
3) Use the image that was built in step 2 to start the container.
docker image ls		--> get the image id for Solution-image  from this command and use it to start the container   
docker container run -it --name Solution-container -d -p 8080:5100 <Image Id>			# Solution-container is the custom name of the container and can be modified.

Using the Tool :
================

if using a unix based system try the following command
curl http://localhost:8080/
On windows :
open the browser and access the url http://localhost:8080/

The expected result is a json response with two top level keys, a list of ips and their occurence and the list of CIDR range and number of IP's falling in each range.

The logs of the script and the webserver  can be accessed using the following command. 
docker logs <container_id>

Stopping the Tool :
===================
To stop the tool, we can simply stop the container and remove it if its not necessary anymore. Use the following commands to stop or remove the container.

docker container stop <container_id>
docker container rm <containerId>

DESIGN DECISIONS :
==================

* The underlying script is written in python3.
* Flask module is used to create the webserver considering the simplicity of the requirement
* RE module is not used for log parsing but simpler python tools are employed to extract the required results. Usage of RE would be more appropriate if the requirement becomes complex.






