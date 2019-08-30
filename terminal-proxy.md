Terminal设置代理：
export all_proxy=socks5://127.0.0.1:1086

mvn install:install-file -Dfile=vertica-jdbc-8.1.1-18.jar -DgroupId=com.vertica -DartifactId=vjdbc8 -Dversion=8.1.1 -Dpackaging=jar

打开内存数据库客户端
java -cp hsqldb.jar org.hsqldb.util.DatabaseManagerSwing

npm —registry https://npm.4paradigm.com install
