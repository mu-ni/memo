# HDFS
Hadoop Distributed File System

### NameNode
管理命名空间，维护文件存储的元数据信息

将存储的数据按照固定大小切分成多块，分别存储多份数据，存放在不同的节点

默认存储的副本为3

#### ActiveNameNode
系统的主节点，只有一个，主要作用是管理HDFS文件系统的命名空间，维护文件元数据信息，管理HDFS的副本策略，处理客户端的读写请求
#### Standby NameNode
Active NameNode的热备节点，它会周期性同步edits的编辑日志，定期合并fsimage和eidts到本地磁盘
#### NameNode元数据文件
包括edits和fsimage：

edits保存客户端对文件的写操作记录，包括创建文件、删除文件

fsimage为文件系统元数据的检查点镜像文件，保存了文件系统中的所有目录和文件信息，如目录结构、文件副本数、文件的块信息等
#### DataNode
slave的工作节点，一般启动多个，可以灵活扩展

存储数据块和数据校验和（对数据内容进行校验，看数据内容是否完整）

通过心跳机制定期向NameNode汇报运行状态和所有块的列表信息

在集群启动时DataNode向NameNode提供存储的Block块的列表信息
#### Block数据块
文件写入HDFS会被切分成固定大小的Block块

数据块的大小固定，Hadoop2.0默认128M，1.0默认64MB，可自定义修改

默认每个Block有三个副本
#### Client
客户端，主要作用为文件切分，与NameNode交互获取文件元数据信息，与DataNode交互，读取或写入数据，管理HDFS
