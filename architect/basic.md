# Architect

KISS（Keep It Simple & Stupid）
#### Proxy
- Proxy -> client side
- Reverse Proxy -> server side

#### Nginx
- Http server
- Reverse Proxy

#### Nginx & Tomcat
- Static resource: Nginx
- Dynamic resource: Tomcat
- Load Balance: nginx send requests to different tomcat instances

#### Memcache & Redis
- memcache: Only memory
Memcache 只是把数据库的索引独立出来做成了一个缓存系统
- Redis: Memory & disk

#### Elestic Stack
1. ElasticSearch: Distributed search engine
2. Logstash: data collection & log analysis
3. Kibana: UI


## 高性能

#### 读写分离
- 主从复制延迟：用户刚注册完后立刻登录
1. 写操作后的读操作指定发给数据库主服务器
2. 读从机失败后再读一次主机
3. 关键业务读写操作全部指向主机，非关键业务采用读写分离
4. Redis缓存，登录的时候先查缓存再查库表

- 分配机制
1. 程序代码封装
2. 中间件封装

#### 分库分表

- 业务分库
- 分表：垂直&水平
水平分表路由:
1. 范围路由：分布不均，易扩展
2. Hash路由：分布均匀，难扩展
3. 配置路由：配置路由就是路由表，用一张独立的表来记录路由信息

#### NoSQL(Not Only SQL)
1. K-V 存储：解决关系数据库无法存储数据结构的问题 -> Redis
2. 文档数据库：解决关系数据库强 schema 约束的问题 -> MongoDB
3. 列式数据库：解决关系数据库大数据场景下的 I/O 问题 -> HBase
4. 全文搜索引擎：解决关系数据库的全文搜索性能问题 -> Elasticsearch

- Redis
string、hash、list、set、sorted set、bitmap 和 hyperloglog
Redis 的事务只能保证隔离性和一致性（I 和 C），无法保证原子性和持久性（A 和 D）

- MongoDB
JOSN， No schema, 自描述
不支持事务
无法进行join查询


#### 缓存
- 缓存穿透：缓存中没有数据，依然从数据库查询
- 缓存雪崩：缓存过期时，性能急剧下降 -> 缓存有效期设置为永久，后台线程更新缓存（而不是业务线程）
- 缓存热点：命中热点数据，缓存服务器压力大 -> 多副本，分布式存储（多副本过期时间不相同）

#### PPC & TPC
- PPC： Process Per Connection
1. fork创建新进程代价高
2. 父子进程通信复杂
3. 支持并发数有限

- TPC： Thread Per Connection
1. 轻量级，创建线程开销小
2. 多线程共享内存，线程间通信简单
3. 但是，多线程之间会互相影响

#### Reactor & Proactor
- Reactor：非阻塞同步网络模型
创建进程池 + I/O多路复用
只适用于业务处理非常快速的场景。单进程 -> Redis
- Proactor：非阻塞异步网络模型
来了事件我来处理，处理完了我通知你

#### select，poll，epoll -> I/O多路复用的具体实现
- select：遍历
- poll：遍历，与select类似，没有最大文件描述符数量的限制
- epoll：回调

#### 负载均衡
1. DNS负载均衡：地理位置级别
2. 硬件负载均衡：用于负载均衡的基础网络设备，集群级别
3. 软件负载均衡：Nginx，性能远低于硬件负载均衡，机器级别

#### 负载均衡算法
1. 轮询：按顺序轮流分配
2. 加权轮询：根据服务器权重分配（负载or性能）
3. Hash类

## 高可用

#### CAP （忽略延时）
1. Consistency: 一致性
2. Availability: 可用性
3. Partition Tolerance: 分区容错性，部分宕机不影响整体系统

#### BASE (对CAP的延伸和补充)
1. Basic Available: 分布式系统在出现故障时，允许损失部分可用性，即保证核心可用
2. Soft State: 允许系统存在中间状态，而该中间状态不会影响系统整体可用性
3. Eventual Consistency: 系统中的所有数据副本经过一定时间后，最终能够达到一致的状态

#### FMEA (Failure mode and effects analysis, 故障模式与影响分析)
<!-- 1. 功能点
2. 故障模式
3. 故障影响
4. 严重程度
5. 故障原因
6. 故障概率
7. 风险程度
8. 已有措施
9. 规避措施
10. 解决措施
11. 后续规划 -->

#### 双机架构
- 主备复制：硬件浪费
- 主从复制：主机负责读写，从机只读不写
- 双机切换
- 主主复制

#### 接口级故障解决方案
1. 降级 downgrade
2. 熔断 fuse
3. 限流 limit
4. 排队 queue

## 可扩展

#### 拆分方式
1. 面向流程拆分
2. 面向服务拆分
3. 面向功能拆分
