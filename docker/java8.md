apt-get update &&
apt-get install software-properties-common
add-apt-repository ppa:webupd8team/java
<!-- echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections -->
apt-get update
apt-get -y install oracle-java8-installer
apt-get install python2.7 python-pip
python -m pip install --upgrade pip
python -m pip install jupyter



CMD nohup java -jar featuredb-dbms-0.0.1-SNAPSHOT.jar & && nohup java -jar featuredb-web-0.0.1-SNAPSHOT.jar & && jupyter notebook --allow-root --ip=0.0.0.0 --port=4000 &
