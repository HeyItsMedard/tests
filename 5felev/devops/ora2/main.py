print("Hello world")
#docker build -t myapp .
#docker run --rm -p 5000:5000 myapp 
#docker network create -d bridge my-net
#docker run -p 3306:3306 --network my-net --name db -e MYSQL_ROOT_PASSWORD=passowrd -d mysql
# docker run --rm --network my-net -p 81:5000 myapp