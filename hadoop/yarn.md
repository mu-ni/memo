# Yarn
Yet Another Resource Negotiator

从Hadoop2.0开始引入的一个资源调度系统
替代Hadoop 1 中的TaskTracker 和 JobTracker

提供了资源管理，统一管理和调度集群资源，负责与客户端交互，处理客户端的请求

Master-Slave架构:Master即ResourceManager，Slave即NodeManager

ResourceManager负责全局资源管理和调度，NodeManager负责本机的资源管理

#### ResourceManager
整个集群只有一个，主要用来处理客户端请求，启动/监控ApplicationMaster，监控NodeManager，对资源进行分配和调度

#### NodeManager
每个节点只有一个，集群中一般与DataNode一一对应，在相同的机器上进行部署

主要功能：
1. 单个节点的资源监控和管理
2. 定时向ResourceManager汇报本机的资源使用情况
3. 处理ResourceManager的请求，为作业的执行分配Container
4. 处理来自ApplicationMaster的请求，启动和停止Container

#### ApplicationMaster
每个应用程序只有一个，负责应用程序的管理，资源的申请和任务调度

主要功能：
1. 与ResourceManager协商为应用程序申请资源
2. 与NodeManager通信启动/停止任务；监控任务的运行状态和失败处理

#### Container
任务运行环境的抽象，只有在分配任务的时候才会抽象出一个Container

主要功能
1. 描述一系列信息（任务运行资源如节点、CPU、内存等）
2. 管理任务的启停及任务的运行环境


## Yarn容错
Resource基于Zookeeper实现高可用

NodeManager故障会导致运行在该节点运行的任务失败，任务失败后:

ResourceManager将失败任务通知对应的ApplicationMaster

ApplicationMaster决定如何处理失败的任务

ApplicationMaster失败后，由ResourceManager负责重启

RMApplicationMaster会保存已经运行完成的Task,重启后不需要重新运行
