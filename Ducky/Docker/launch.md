<h1>How to use docker files ?</h1>

docker build -t flask-receiver . <br>
docker run -d -p 5000:5000 flask-receiver <br>
hostname -I | awk '{print $1}'
Change the IP in the ducky script with the IP of the docker container. <br>