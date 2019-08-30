curator-framework：对zookeeper的底层api的一些封装
curator-client：提供一些客户端的操作，例如重试策略等
curator-recipes：封装了一些高级特性，如：Cache事件监听、选举、分布式锁、分布式计数器、分布式Barrier等


framework:
Path Cache：监视一个路径下1）孩子结点的创建、2）删除，3）以及结点数据的更新。产生的事件会传递给注册的PathChildrenCacheListener。
Node Cache：监视一个结点的创建、更新、删除，并将结点的数据缓存在本地。
Tree Cache：Path Cache和Node Cache的“合体”，监视路径下的创建、更新、删除事件，并缓存路径下所有孩子结点的数据。

recipes:
锁：包括共享锁、共享可重入锁、读写锁等。
选举：Leader选举算法。
Barrier：阻止分布式计算直至某个条件被满足的“栅栏”，可以看做JDK Concurrent包中Barrier的分布式实现。
缓存：前面提到过的三种Cache及监听机制。
持久化结点：连接或Session终止后仍然在Zookeeper中存在的结点。
队列：分布式队列、分布式优先级队列等。
