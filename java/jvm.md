## Reflection:
Knowing which class/method should be called according to the string during runtime.

Normally used by framework, like Spring.

~~~
Apple apple = new Apple();
apple.setPrice(4);
~~~
~~~
Class clazz = Class.forName("com.muni.reflect.Apple");
Method method = clazz.getMethod("setPrice", int.class);
Constructor constructor = clazz.getConstructor();
Object object = constructor.newInstance();
method.invoke(object, 4);
~~~

#### Get Object
~~~
// method 1
Class clazz = Class.forName("java.lang.String");

// method 2
Class clazz = String.class;

// method 3
String str = new String("");
Class clazz = str.getClass();
~~~

#### Create Object
~~~
// method 1
// Class.newInstance()
Class clazz = Apple.class;
Apple apple = (Apple)clazz.newInstance();

// method 2
// Constructor.newInstance(opt params)
Class clazz = Apple.class;
Constructor constructor = clazz.getConstructor();
Apple apple = (Apple)constructor.newInstance();
~~~

#### Get Attributes
~~~
// method 1(exclude private attributes)
Class clazz = Apple.class;
Field[] fields = clazz.getFields();

// method 2(include private attributes)
Class clazz = Apple.class;
Field[] fields = clazz.getDeclaredFields();
~~~


## Annotation:


Spring boot: Convention is more important than configuration.

## GC
## Decorator
## AOP/IOC
## dynamic programming
将复杂问题拆分成多个较简单的子问题
对每个子问题只计算一次，然后使用数据结构（数组，字典等）在内存中存储计算结果
子问题的计算结果按照一定规则进行排序（如，基于输入参数）
当需要再次运算子问题时直接使用已存储的计算结果而非再次运算以提升求解性能

这种存储计算结果以备再次使用称之为：Memoization（这个词，不知道怎么翻译好）
