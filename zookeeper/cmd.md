1. 配置文件
~~~
vi conf/zoo.cfg
~~~
2. 启动注册中心
~~~
sh bin/zkServer.sh start
sh bin/zkServer.sh status
sh bin/zkServer.sh stop
~~~
3. 启动客户端
~~~
sh zkCli.sh
sh zkCli.sh -server 172.27.128.33:2181,172.27.128.32:2181,172.27.128.31:2181
~~~
4. for client test
~~~
ls /
create /helloword "data"
ls /
get /helloword
set /helloword "data2"
get /helloword
stat /helloword
rmr /helloword
~~~


Ephemerals cannot have children

zk
临时节点
存储ip+port

getData()和exists()设置了内容watch，getChildren()设置了子节点watch
