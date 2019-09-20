Yahoo，Google 的 3 篇大数据论文（Bigtable/Map- Reduce/GFS）开启了一个大数据的时代
Yahoo 开源的 Hadoop 系列（HDFS、HBase 等），基本上垄断了开源界的大数据处理

# HDFS

1. DataNode: 存储、读写data block
2. NameNode: Metadata管理 （文件路径名、数据块的ID以及存储位置等信息）
DataNode 会通过心跳和 NameNode 保持通信
NameNode 采用主从热备的方式提供高可用服务

# MapReduce
MapReduce 既是一个编程模型，又是一个计算框架
1. split
2. map
3. shuffle
4. reduce
5. final output

# JobTracker & TaskTracker
JobTracker 进程在整个 Hadoop 集群全局唯一
MapReduce 的主服务器就是 JobTracker，从服务器就是 TaskTracker

Hive 能够直接处理我们输入的 SQL 语句

# YARN
Yet Another Resource Negotiator

1. Resource Manager：进程负责整个集群的资源调度管理，通常部署在独立的服务器上
2. Node Manager：进程负责具体服务器上的资源和任务管理，在集群的每一台计算服务器上都会启动
Yarn 进行资源分配的单位是容器（Container）

框架在架构设计上遵循一个重要的设计原则叫“依赖倒转原则”(IOC - Inversion of Control)
依赖倒转原则是高层模块不能依赖低层模块，它们应该共同依赖一个抽象，这个抽象由高层模块定义，由低层模块实现

Je ne parle pas bien français maintenant
