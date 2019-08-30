CAP - Consistency, Availability, Partition Tolerance
分区容错的意思是，区间通信可能失败
P总是成立，C和A无法同时做到

Zookeeper - CP
Spring Cloud Eureka - AP

ZooKeeper的核心实现算法Zab，解决了分布式系统下数据在多个服务之间保持同步问题
ZAB（ZooKeeper Atomic Broadcast ） 全称为：原子消息广播协议；ZAB可以说是在Paxos算法基础上进行了扩展改造而来的，ZAB协议设计了支持崩溃恢复，ZooKeeper使用单一主进程Leader用于处理客户端所有事务请求，采用ZAB协议将服务器数状态以事务形式广播到所有Follower上；由于事务间可能存在着依赖关系，ZAB协议保证Leader广播的变更序列被顺序的处理，：一个状态被处理那么它所依赖的状态也已经提前被处理；ZAB协议支持的崩溃恢复可以保证在Leader进程崩溃的时候可以重新选出Leader并且保证数据的完整性；过半数（>=N/2+1） 的Follower反馈信息后，Leader将再次向集群内Follower广播Commit信息，Commit为将之前的Proposal提交；

### 集群中的角色
1. 领导者(leader)，负责进行投票的发起和决议，更新系统状态
2. 学习者(learner)，包括跟随者（follower）和观察者（observer），
3. follower用于接受客户端请求并向客户端返回结果，在选主过程中参与投票
4. Observer可以接受客户端请求，将写请求转发给leader，但observer不参加投票过程，只同步leader的状态，observer的目的是为了扩展系统，提高读取速度。

### 每个znode由3部分组成:
1. stat：此为状态信息, 描述该znode的版本, 权限等信息.
2. data：与该znode关联的数据.
3. children：该znode下的子节点.

### 节点类型
节点的类型在创建时即被确定，并且不能改变。
1. ephemeral[ɪˈfemərəl] node：该节点的生命周期依赖于创建它们的会话。一旦会话结束，临时节点将被自动删除，当然可以也可以手动删除。另外，需要注意是，ZooKeeper的临时节点不允许拥有子节点。
2. persistent node：该节点的生命周期不依赖于会话，并且只有在客户端显示执行删除操作的时候，他们才能被删除。

### 基本操作
1. create: 创建Znode(父Znode必须存在)
2. delete: 删除Znode（Znode没有子节点）
3. exits: 测试Znode是否存在，并获取它的元数据
4. getACL/setACL: 为Znode获取/设置ACL（Access Control List）
5. getChildren: 获取Znode所有子节点的列表
6. getData/setData: 获取/设置Znode的相关数据
7. sync: 使客户端的Znode视图与Zookeeper同步

### 权限定义
1. create: 创建子节点
2. read: 从节点获取数据/列出节点的所有子节点
3. write: 设置节点数据
4. delete: 删除子节点
5. admin: 可以设置权限
