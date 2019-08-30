### Dockerfile

1. FROM: 指定基础镜像
  + 如果不以任何镜像为基础 -> FROM scratch
* RUN: 执行命令
  + 尽量合并为一行，减少层数
* CMD: 指定默认的容器主进程的启动命令
  + 出现多次以最后一次为准
  + ex. CMD [ "npm", "start" ]（以前台形式运行）
* LABEL: 设置镜像标签
  + 如果base image中也有标签，则继承，如果是同名标签，则覆盖
  + LABEL <key\>=<value\>
  + 查看镜像标签：docker inspect ubuntu:latest -f={{.Config.Labels}}
* EXPOSE: 声明端口
  + 声明容器打算使用什么端口而已，并不会自动在宿主进行端口映射
  + Default -> tcp（EXPOSE 80/tcp，EXPOSE 80/udp）
  + docker run -P (自动映射EXPOSE端口到宿主机，80/tcp -> 0.0.0.0:49156)
* ENV: 设置环境变量
  + ENV <key\>=<value\>
  + 查看环境变量：docker inspect ubuntu:latest -f={{.Config.Env}}
* ADD: 复制文件
  + ADD <源路径\> <目标路径\>
  + 解压压缩文件并把它们添加到镜像中
  + 从url拷贝文件到镜像中
* COPY: 复制本地文件
  + COPY <源路径\> <目标路径\> (COPY package.json /usr/src/app/)
  + 源路径只能是本地路径
  + 目标路径可以是容器内的绝对路径，也可以是相对于工作目录的相对路径（工作目录可以用 WORKDIR 指令来指定）
* WORKDIR: 指定工作目录
* USER: 为接下来的Dockerfile指令指定用户
  + 受到影响的指令有：RUN、CMD、ENTRYPOINT
* HEALTHCHECK: 健康检查
* ARG: 构建参数
  + 构建参数和 ENV 的效果一样，都是设置环境变量
  + 所不同的是， ARG 所设置的构建环境的环境变量，在将来容器运行时是不会存在这些环境变量的
  + docker build --build-arg <varname\>=<value\>
* ENTRYPOINT: 入口点
  + 实际执行时，将变为：<ENTRYPOINT\> "<CMD\>"
* VOLUME: 镜像中创建挂载点
  + ex. VOLUME /data
  + 在运行时自动挂载为匿名卷
  + 任何向 /data 中写入的信息都不会记录进容器存储层，从而保证了容器存储层的无状态化
  + 查看挂载点：docker inspect ubuntu:latest -f={{.Config.Volumes}}
* ONBUILD
  + 它后面跟的指令，在当前镜像构建时并不会被执行。只有当以当前镜像为基础镜像，去构建下一级镜像的时候才会被执行
  + ONBUILD只会继承给子节点的镜像，不会再继承给孙子节点
* STOPSIGNAL: 设置停止容器所要发送的系统调用信号
  + ex. STOPSIGNAL signal
  + 默认：STOPSIGNAL SIGTERM
* SHELL
  + 更改后续的Dockerfile指令中所使用的shell
  + Windows下通常会有cmd和powershell两种shell
  + ex. SHELL ["powershell", "-command"]
  + 默认的shell是["bin/sh", "-c"]
