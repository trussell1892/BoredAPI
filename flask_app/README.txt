#Download and install Docker Desktop 
https://www.docker.com/products/docker-desktop/

#From the command line navigate to dir which contains the dockerfile
#Then run the below commands to build and run the 

docker build -t myimage1 .
docker run -d -p 5000:5000 myimage1

#confirm the container is running 
docker ps
 
#homepage
http://127.0.0.1:5000/
 
#to change the particpant number change the int on the end of the URL
http://127.0.0.1:5000/boredAPI/2