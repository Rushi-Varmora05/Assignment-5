# MySQL
## Setting up Database in Docker
docker pull mysql

docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:latest

## Creating the database and Tables 
CRETE DATABASE school;

CREATE TABLE students (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(100) NOT NULL,
 age INT NOT NULL,
 grade VARCHAR(10) NOT NULL
);

## Installing the required modules for FastAPI application
pip install fastapi uvicorn
pip3 install mysql-connector-python           

## Running the Fast API
uvicorn main_mysql:app --reload  

//To start the database container's terminal
docker exec -it mysql-container bash 

# MongoDB
## Setting up Database in Docker

docker pull mongo:latest

docker run -d -p 27017:27017 --name=mongodb-container mongo:latest

## Installing the required modules for FastAPI application
pip3 install pymongo

## Running the Fast API
uvicorn main_mongo:app --reload   


# Elastic Search
## Setting up Database in Docker
docker network create elastic

docker pull docker.elastic.co/elasticsearch/elasticsearch:8.14.3

docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.14.3

## Running the Fast API
pip install elasticsearch   
uvicorn main_elastic:app --reload  

# Repo URL : https://github.com/Rushi-Varmora05/Assignment-5


# neo4j
docker pull neo4j
docker run --name neo4j-container \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=/Users/rahil/Documents/DBMS_Q1/Databases/neo4j/data:/data \
    neo4j
    
bin/cypher-shell -u neo4j -p <password>
