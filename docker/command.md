### Command
1. 创建Dockerfile
~~~
touch Dockerfile
~~~
2. 使用当前目录的 Dockerfile 构建镜像(-t -> --tag, . -> 当前目录)
~~~
docker build -t muniooo/featuredb:v1 .
~~~
3. 启动容器
~~~
docker run -it -p 8123:8123 -p 8124:8124 -p 4000:4000 -p 3000:3000 -d develop-registry.4pd.io/featuredb:0.6
docker run -it -p 8888:8888 -p 3000:3000 -p 4000:4000 -d muniooo/featuredb:v1
docker logs {containerid}
docker run -it -p 8123:8123 -p 8124:8124 -p 8125:8125 -p 4000:4000 -d featuredb:0.8.5
~~~

*. 进入容器
~~~
docker exec -it {containerid} /bin/bash
~~~

4. List all images
~~~
docker images
~~~

5. Remove image
~~~
docker image rm -f featuredb:v4
~~~

*. 查看端口映射
~~~
docker ps
~~~

6. List all containers
~~~
docker container ls -a
docker stop {containerid}
docker logs {containerid}
~~~

docker container prune

docker commit c3f279d17e0a  featuredb:base3
docker tag e5002b1f10f1 develop-registry.4pd.io/featuredb:base3
docker push develop-registry.4pd.io/featuredb:base3

http://develop-registry.4pd.io/v2/featuredb/tags/list



docker tag 1a271f19d8e0 develop-registry.4pd.io/featuredb:0.8.5
docker push develop-registry.4pd.io/featuredb:0.8.5
