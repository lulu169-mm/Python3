### 1. Docker基础

#### (1). Docker相关概念

| 名称             | 含义                 |
| ---------------- | -------------------- |
| **CONTAINER ID** | 容器 ID              |
| **IMAGE**        | 使用的镜像           |
| **COMMAND**      | 启动容器时运行的命令 |
| **CREATED**      | 容器的创建时间       |
| **STATUS**       | 容器状态             |

#### (2). Docker状态

| 状态              | 含义       |
| ----------------- | ---------- |
| created           | 已创建     |
| restarting        | 重启中     |
| **running 或 Up** | **运行中** |
| removing          | 迁移中     |
| **paused**        | **暂停**   |
| **exited**        | **停止**   |
| dead              | 死亡       |

#### (3). 镜像操作

##### a. 拉取

```
docker pull [镜像名]
```

##### b. 删除

###### ①单个镜像

```
docker rmi [镜像名 or Id]
```

###### ②所有镜像

```
docker rmi $(docker images -q)
```

##### ③未使用镜像

```
docker image prune -a
```



##### c. 查询镜像列表

```
docker images
```

#### (4). 容器操作

##### a. 创建

###### ①仅创建

```
docker run [容器名]
```

###### ②终端执行

```
docker run -it [容器名] [脚本执行环境，例如/bin/bash]
```

##### b. 启动

###### ①指定容器

```
docker start [容器名 or Id]
```

###### ②所有容器

```
docker start $(docker ps -aq)
```

##### c. 停止

###### ①指定容器

```
docker stop [容器名 or Id]
```

###### ②所有容器

```
docker stop $(docker ps -aq)
```

##### d. 删除

###### ①指定容器

```
docker rm [容器名 or Id]
```

###### ②所有容器

```
docker rm $(docker ps -aq)
```

##### e. 查询

###### ①所有容器

```
docker ps -a
```

###### ②运行中容器

```
docker ps
```

### 2. Docker-Compose

* 前提是有一个 `docker-compose.yml` 文件。该文件定义了服务、网络、卷、以及各个容器的配置，通过该文件可以自动化管理和启动多个 Docker 容器。

#### (1). 相关资源

| 概念 | 解释                             |
| ---- | -------------------------------- |
| 容器 | 运行自镜像的实例                 |
| 镜像 | 容器的蓝图，包含应用及依赖       |
| 网络 | 连接容器，允许相互通信           |
| 卷   | 持久化容器数据，可在容器之间共享 |

#### (2). 镜像操作

* 在`docker-compose.yml` 文件同级目录下操作

##### a. 构建

```
docker-compose build
```

##### b. 删除

```
docker-compose down --rmi all
```

#### (3). 容器操作

##### a. 启动服务

###### ①启动服务

```
docker-compose start
```

###### ②创建并启动所有服务

```
docker-compose up
```

###### ③后台创建并启动服务

```
docker-compose up -d
```

##### b. 停止容器

###### ①仅停止服务

```
docker-compose stop
```

###### ②停止所有服务

```
docker-compose down
```

##### c. 删除容器

```
docker-compose rm
```

##### e. 查看所有服务

```
docker-compose ps
```

#### (4). 其他操作

a. 删除未使用的网络

```
docker network prune
```

b. 删除未使用的卷

```
docker volume prune
```

c. 一次性清理所有未使用的资源

```
docker system prune -a --volumes		//--volumes 选项会包括未使用的卷。
```



### 3. 配置docker代理

#### (1). 创建文件夹

在终端中运行以下命令创建所需的目录：

```
sudo mkdir -p /etc/systemd/system/docker.service.d
```

#### (2). 创建代理配置文件

然后，创建一个新的配置文件，例如 `http-proxy.conf`：

```
sudo vim /etc/systemd/system/docker.service.d/http-proxy.conf
```

在文件中添加以下内容（请替换为您的代理地址）：

```
[Service]
Environment="HTTP_PROXY=http://your-proxy-url:port/"
Environment="HTTPS_PROXY=http://your-proxy-url:port/"
```

#### (3). 重新加载系统守护进程

保存并退出后，重新加载系统守护进程以应用更改：

```
sudo systemctl daemon-reload
```

#### (4). 重启 Docker 服务

最后，重启 Docker 服务：

```
sudo systemctl restart docker
```





