# Kafka

Kafka是最初由Linkedin公司开发，用scala语言编写，Linkedin于2010年贡献给了Apache基金会并成为顶级开源项目
是一个分布式、支持分区的（partition）、多副本的（replica），基于zookeeper协调的分布式消息系统
由生产者，消费者，Broker三大部分组成，生产者会将消息写入到Broker，消费者会从Broker中读取出消息
kafka的数据，实际上是以文件的形式存储在文件系统的
topic下有partition，partition下有segment，segment是实际的一个个文件，topic和partition都是抽象概念
每个segment文件大小相等

#### 特性
- 高吞吐量、低延迟(hight throughput,low delay):kafka每秒可以处理几十万条消息，它的延迟最低只有几毫秒
- 可扩展性(Scalability)：kafka集群支持热扩展
- 持久性、可靠性（Persistence，Reliability）：消息被持久化到本地磁盘，并且支持数据备份防止数据丢失
- 容错性（Fault tolerance）：允许集群中节点失败（若副本数量为n,则允许n-1个节点失败）
- 高并发（High concurrency）：支持数千个客户端同时读写

#### 使用场景：
- 日志收集：日志通过kafka以统一接口服务的方式开放给各种consumer
- 消息系统：解耦和生产者和消费者、缓存消息等
- 用户活动跟踪：记录web用户或者app用户的各种活动
- 运营指标：K记录运营监控数据
- 流式处理：比如spark streaming和storm

#### 涉及概念
Producer & Consumer：消息生产者和消费者
Broker：组成Kafka集群的每个节点
Topic：相当于传统消息系统MQ中的一个队列queue
Partition：topic物理上的分组(保证有序)
Segment：partition物理上由多个segment组成
Partition replica：副本数目。不能大于kafka broker节点的数目。一个Leader, 其余follower
* 必须指定是发送到哪个topic，但是不需要指定topic下的哪个partition
* 一个partition只能被一个消费者消费, 但是一个消费者可以同时消费多个partition

#### partition的分配 & Broker Leader的选举
Kakfa Broker集群受Zookeeper管理, kafka使用zk在broker中选出一个controller，用于partition分配和leader选举
所有的Kafka Broker节点一起去Zookeeper上注册一个临时节点(ephemeral)，只有一个Kafka Broker会注册成功。
注册成功的broker -> Controller
注册失败的broker -> Follower

#### 消息投递语义
At most once：最多一次，消息可能会丢失，但不会重复
At least once：最少一次，消息不会丢失，可能会重复
Exactly once：只且一次，消息不丢失不重复，只且消费一次
