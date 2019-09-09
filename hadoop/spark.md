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
