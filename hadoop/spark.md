# spark

RDD(Resilient Distributed Datasets)
Spark 分布式计算的数据分片、任务调度都是以 RDD 为单位展开的，每个 RDD 分片都会分配到一个执行进程去处理

MapReduce 一个应用一次只运行一个map和一个reduce
Spark可以根据应用的复杂程度，分割成更多的计算阶段（stage），这些计算阶段组成一个有向无环图 DAG，Spark 任务调度器可以根据 DAG 的依赖关系执行计算阶段
负责 Spark 应用 DAG 生成和管理的组件是 DAGScheduler，DAGScheduler 根据程序代码生成 DAG，然后将程序分发到分布式计算集群，按计算阶段的先后关系调度执行
当 RDD 之间的转换连接线呈现多对多交叉连接的时候，就会产生新的阶段

其实从本质上看，Spark 可以算作是一种 MapReduce 计算模型的不同实现
Hadoop MapReduce 简单粗暴地根据 shuffle 将大数据计算分成 Map 和 Reduce 两个阶段，然后就算完事了。
而 Spark 更细腻一点，将前一个的 Reduce 和后一个的 Map 连接起来，当作一个阶段持续计算，形成一个更加优雅、高效地计算模型，虽然其本质依然是 Map 和 Reduce。但是这种多个计算阶段依赖执行的方案可以有效减少对 HDFS 的访问，减少作业的调度执行次数，因此执行速度也更快。
并且和 Hadoop MapReduce 主要使用磁盘存储 shuffle 过程中的数据不同，Spark 优先使用内存进行数据存储，包括 RDD 数据。除非是内存不够用了，否则是尽可能使用内存， 这也是 Spark 性能比 Hadoop 高的另一个原因。

#### Map & FlatMap
["hello you","hello me","hello word"]
- Map: hello you, hello me, hello word
- FlatMap: hello, you, hello, me, hello, word

#### SLA(Service-Level Agreement) 服务等级协议
1. Availability 可用性 -> 系统正常工作时间占比
2. Accuracy 准确性 -> 产生错误请求数/请求总数
3. Capacity 系统容量 -> 系统支持的负载量，QPS
4. Latency 延迟 -> 收到请求-响应请求 时间差

#### 可扩展性 Scalability
- 水平扩展Horizontal Scaling -> 加机器
- 垂直扩展Vertical Scaling -> 升级机器性能

#### 一致性 Consistency
- Strong Consistency 任何时刻一致
- Week Consistency 存在不一致窗口期
- Eventual Consistency 弱一致性的特殊形式

#### Batch & Stream
- Batch process - Bounded Data
- Stream process - Unbounded Data

#### Workflow 工作模式
1. Copier Pattern - 同一数据集，不同处理（youtube视频不同分辨率）
2. Filter Pattern - 过滤不符合条件的数据
3. Splitter Pattern - 不丢弃数据，对数据分类
4. Joiner Pattern - 不同数据集 - 集中 - 总数据集

#### Pub/Sub Pattern
- Loose Coupling 松耦合
- High Scalability 高伸缩
- Eventual Consistency 最终一致性

#### CAP Theorem[ˈθiːərəm]
- Consistency
- Availability
- Partition Tolerance 允许节点间通讯故障

* CP - HBase, MongoDB, Redis
* AP -
* CA - Kafka

#### Lambda Architecture
- Batch Layer
- Speed Layer
- Serving Layer
不足：两套分布式（批处理和流处理），难以维护

#### Kappa Architecture
- 去掉批处理层，只保留速度层
不足：1.处理大规模数据易出错 2.批/流处理两套逻辑必须一致

#### RDD - Resilient Distributed Dataset
- 分区： 数据存储在不同节点
- 不可变： 只读，只能做数据转换，不能更改。
- 并行操作： 不同节点的数据可以同时处理，并产生新的RDD

#### Narrow Dependency & Wide Dependency
- Narrow Dependency: RDD1 RDD2 一对一， 并行， map & filter
- Wide Dependency: RDD1 RDD2 一对多， RDD2依赖RDD1， join & groupBy

#### RDD & DataFrame & DataSet
- RDD - schema
- DataFrame - 优化RDD，DataSet[Row]
- DataSet - RDD+Schema, 基于DataFrame
在 Spark 2.0 中，DataFrame 和 DataSet被统一

#### Spark Streaming
- StreamingContext 所有streaming操作的入口
- DStream: 一个连续的RDD序列

#### Structured Streaming
- Complete Mode: 更新后，整个表 -> 外部存储
- Append Mode: 上一次触发后，新增的行 -> 外部存储
- Update Mode: 上一次触发后，更新的行 -> 外部存储
Structured Streaming 基于 Spark Streaming，更优

#### 滑动窗口
- window length 窗口长度
- sliding interval 滑动间隔
