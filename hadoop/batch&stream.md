## Batch Only
有界，持久，大量。批处理不适合对处理时间要求较高的场合

#### Apache Hadoop
从HDFS文件系统读取数据集
将数据集拆分成小块并分配给所有可用节点
针对每个节点上的数据子集进行计算（计算的中间态结果会重新写入HDFS）
重新分配中间态结果并按照键进行分组
通过对每个节点计算的结果进行汇总和组合对每个键的值进行“Reducing”
将计算而来的最终结果重新写入 HDFS

优缺点：
严重依赖持久存储，速度慢
磁盘廉价，可以处理海量数据集
极高的缩放潜力，数万个节点的应用
MapReduce的学习曲线较为陡峭


## Stream Only
流处理系统可以处理几乎无限量的数据，但同一时间只能处理一条（真正的流处理）或很少量（微批处理，Micro-batch Processing）数据

#### Apache Storm
Storm的流处理可对框架中名为Topology（拓扑）的DAG（Directed Acyclic Graph，有向无环图）进行编排
拓扑包含：
Stream：持续抵达系统的无边界数据
Spout：产生待处理的数据
Bolt：需要消耗流数据

默认情况下Storm提供了“至少一次”的处理保证，这意味着可以确保每条消息至少可以被处理一次，但某些情况下如果遇到失败可能会处理多次。
Storm无法确保可以按照特定顺序处理消息。

Core Storm：不使用Trident的Storm
Trident：实现严格的一次处理，即有状态处理。会增加延迟

#### Apache Samza
Apache Samza是一种与Apache Kafka消息系统紧密绑定的流处理框架
获得“至少一次”的交付保障
目前Samza只支持JVM语言
直接写入Kafka还可避免回压（Backpressure）问题。
回压是指当负载峰值导致数据流入速度超过组件实时处理能力的情况，这种情况可能导致处理工作停顿并可能丢失数据。

## Batch & Stream

#### Apache Spark
Spark可作为独立集群部署（需要相应存储层的配合），或可与Hadoop集成并取代MapReduce引擎
内存 -> 批计算，Resilient Distributed Dataset（弹性分布式数据集），即RDD的模型来处理数据
RDD -> 只位于内存中，永恒不变的结构

流处理能力是由Spark Streaming实现的(micro-batch)
Spark本身在设计上主要面向批处理工作负载

内存通常比磁盘空间更贵，因此相比基于磁盘的系统，Spark成本更高
相比Hadoop MapReduce，Spark的资源消耗更大
Spark更不适合与Hadoop堆栈的其他组件共存一处

#### Apache Flink
Kappa架构：流处理为先(Apache Flink)
Lambda架构：批处理为先

自行管理内存，无需依赖原生的Java垃圾回收机制，还可进行“增量迭代”
Flink提供了基于Web的调度视图
非常“年幼”的项目。现实环境中该项目的大规模部署尚不如其他处理框架那么常见
