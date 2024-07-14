# MySQL
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:latest

CRETE DATABASE school;

CREATE TABLE students (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(100) NOT NULL,
 age INT NOT NULL,
 grade VARCHAR(10) NOT NULL
);

pip install fastapi uvicorn
pip3 install mysql-connector-python           

#to run the Fast API
uvicorn main_mysql:app --reload  

# docker exec -it mysql-container bash -- to run the container terminal
# MongoDB
pip3 install pymongo
docker pull mongo:latest
docker run -d -p 27017:27017 --name=mongodb-container mongo:latest


uvicorn main_mongo:app --reload  

# Elastic Search
uvicorn main_elastic:app --reload  

docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.14.3
docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.14.3


# Repo URL : https://github.com/Rushi-Varmora05/Assignment-5