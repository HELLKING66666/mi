# zookeeper
export ZOOKEEPER_HOME=/opt/zookeeper-3.4.12

# apache-maven
export MAVEN_HOME=/opt/apache-maven-3.3.9

# marathon
export MARATHON_HOME=/opt/marathon-1.4.3

# mesos
export MESOS_HOME=/opt/mesos-1.6.0

export JAVA_HOME=/usr/local/jvm/jdk1.8.0_60
export JRE_HOME=${JAVA_HOME}/jre
export HADOOP_HOME=/usr/local/hadoop
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib:$($HADOOP_HOME/bin/hadoop classpath):$CLASSPATH


# global environment
export PATH=$PATH:$ZOOKEEPER_HOME/bin:$MAVEN_HOME/bin:$MARATHON_HOME/bin:$MESOS_HOME/build/bin
export ip=120.79.18.130
