~~~
查询引擎: Hive, Impala, Pig, Presto, Drill, Tajo, HAWQ, IBM Big SQL
计算框架: MapReduce, Spark, Cascading, Crunch, Scalding, Kite
数据模型: Avro, Thrift, Protocol Buffers, POJOs
~~~

~~~
parquet-format -> 定义了 Parquet 内部的数据类型、存储格式等
parquet-mr -> 外部对象模型与 Parquet 内部数据类型的映射
~~~

~~~
Row group(推荐1G)[Column chunk[Page]] -- Footer[FileMetaData]
~~~

For嵌套数据类型
~~~
Repetition Level(R): 有定义的level深度
Definition Level(D): 该field的值在哪一个深度上是重复的
~~~
