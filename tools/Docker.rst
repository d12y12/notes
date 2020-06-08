.. docker:

Docker
=======

.. image:: ../_static/Docker/docker_logo.png
   :height: 100
   :target: https://www.docker.com/

|

Docker 安装
-----------

#. 卸载旧版本::

      sudo apt-get remove docker docker-engine docker.io containerd runc

#. 更新apt包索引::

      sudo apt-get update

#. 安装以下包以使apt可以通过HTTPS使用源仓库::

      sudo apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common

#. 添加Docker官方的GPG密钥::

      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

   检查你现在有包含指纹 ``9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88`` 的密钥::

      sudo apt-key fingerprint 0EBFCD88

   检查输出::

      pub   rsa4096 2017-02-22 [SCEA]
            9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
      uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
      sub   rsa4096 2017-02-22 [S]

#. 设置源仓库版本::

      sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"
   
   参数：

   * ``arch``: amd64 (x86_64/amd64), armhf, arm64, ppc64el (IBM Power), s390x (IBM Z)
   * ``repository``: stable, nightly, test

#. 再更新一下apt包索引::

      sudo apt-get update

#. 安装最新版本的Docker CE::

      sudo apt-get install docker-ce docker-ce-cli containerd.io

   要安装指定版本，先列出你源仓库中的版本列表::

      apt-cache madison docker-ce
    
   输出::

      docker-ce | 5:18.09.1~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
      docker-ce | 5:18.09.0~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
      docker-ce | 18.06.1~ce~3-0~ubuntu       | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
      docker-ce | 18.06.0~ce~3-0~ubuntu       | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
      ...

   安装指定版本, 比如 ``5:18.09.1~3-0~ubuntu-xenial``, 将版本字符串替换下面名例中的 ``<VERSION_STRING>`` ::

      sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io

#. 验证安装

   * 检查服务状态::

        sudo systemctl status docker
   
   * 如服务未启动，启动服务::

        sudo systemctl start docker
   
   * 测试安装::

        sudo docker run hello-world

#. 建立 Docker 用户组，并将当前用户加入用户组::

      sudo groupadd docker
      sudo usermod -a -G docker $USER

   默认情况下，docker 命令会使用 Unix socket 与 Docker 引擎通讯。
   只有 root 用户和 docker 组的用户才可以访问 Docker 引擎的 Unix socket。
   出于安全考虑，一般 Linux 系统上不会直接使用 root 用户。
   因此，更好地做法是将需要使用 docker 的用户加入 docker 用户组。

#. 配置 Docker 在开机时启动::

      sudo systemctl enable docker

#. 国内加速

   修改 ``/etc/docker/daemon.json`` 文件，如果文件不存在就创建一个新的，添加如下内容::

      {
        "registry-mirrors": [
          "https://registry.docker-cn.com/",
          "http://hub-mirror.c.163.com"
        ]
      }

   然后重启 Docker 服务::

      sudo systemctl daemon-reload
      sudo systemctl restart docker

   .. list-table:: Docker 国内源列表
      :header-rows: 1

      * - 名称
        - 地址
      * - Docker 中国
        - ``https://registry.docker-cn.com``
      * - 网易
        - ``http://hub-mirror.c.163.com``
      * - 中国科技大学
        - ``https://docker.mirrors.ustc.edu.cn``

Docker 命令
-----------

镜像
~~~~

* 列出本地镜像::

     docker images

* 拉取镜像::

     docker pull <name:tag>

* 创建镜像::

     docker build -t <name:tag> .

  * ``-t``: 指定要创建的目标镜像名及标签
  * ``-f``: 指定要使用的Dockerfile路径，默认为当前目录
  * ``.`` : 上下文路径，是指 docker 在构建镜像，有时候想要使用到本机的文件（比如复制），
    docker build 命令得知这个路径后，会将路径下的所有内容打包。上下文路径下不要放无用的文件，
    因为会一起打包发送给 docker 引擎，如果文件过多会造成过程缓慢。

* 删除镜像::

     docker rmi <IMAGE ID>
  
  删除镜像前要先删除使用镜像的容器

容器
~~~~

* 列出所有容器::

     docker ps -a

* 启动容器::

     docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
   
  常用选项:

  * ``-d``: 后台运行容器，并返回容器ID
  * ``-i``: 以交互模式运行容器，通常与 -t 同时使用
  * ``-t``: 为容器重新分配一个伪输入终端，通常与 -i 同时使用
  * ``--name="<name>"``: 为容器指定一个名称
  * ``-P``: 随机端口映射，容器内部端口随机映射到主机的高端口
  * ``-p, --expose``: 指定端口映射，格式为：主机(宿主)端口:容器端口
  * ``--volume, -v``: 绑定一个卷
  * ``--hostname , -h``: 容器主机名
  * ``--network``: 连接到一个网络
  * ``--mount``: 挂载卷，主机目录和 tmpfs 到容器

  例如::

     yang@SkyLab:~$ docker run -it nginx:latest /bin/bash
     Unable to find image 'nginx:latest' locally
     latest: Pulling from library/nginx
     68ced04f60ab: Pull complete
     28252775b295: Pull complete
     a616aa3b0bf2: Pull complete
     Digest: sha256:2539d4344dd18e1df02be842ffc435f8e1f699cfc55516e2cf2cb16b7a9aea0b
     Status: Downloaded newer image for nginx:latest
     root@15730a99e735:/# exit
     exit
     yang@SkyLab:~$

* 进入容器::

     docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
  
  参数

  * ``-d``: 分离模式: 在后台运行
  * ``-i``: 即使没有附加也保持STDIN 打开
  * ``-t``: 分配一个伪终端
  
  例如::

    yang@SkyLab:~$ docker ps -a
    CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS                     PORTS               NAMES
    461eaeab82a7        nginx:latest            "/bin/bash"              7 seconds ago       Up 5 seconds               80/tcp              epic_driscoll
    yang@SkyLab:~$ docker exec -it 461eaeab82a7 /bin/bash
    root@461eaeab82a7:/# exit
    exit
    yang@SkyLab:~$

* 停止容器::

     docker stop <CONTAINER ID>

* 启动停止的容器::

     docker start <CONTAINER ID>

* 重启容器::

     docker restart <CONTAINER ID>

* 删除容器::

     docker rm <CONTAINER ID>

  删除所有已停止的容器::

     docker rm $(docker ps -qa)

* 获取容器的日志::

     docker logs [OPTIONS] CONTAINER

  常用选项:

  * ``-f``: 跟踪日志输出
  * ``--since``: 显示某个开始时间的所有日志
  * ``-t``: 显示时间戳
  * ``--tail``: 仅列出最新N条容器日志

* 获取容器/镜像的元数据::

     docker inspect [OPTIONS] NAME|ID [NAME|ID...]
  
  常用选项:

  * ``-f``: 指定返回值的模板文件。
  * ``-s``: 显示总的文件大小。
  * ``--type``: 为指定类型返回JSON。

网络
~~~~

* 列出所有网络::

     docker network ls

* 创建网络::

     docker network create [OPTIONS] NETWORK

  例如::

     $ docker network create \
       --driver=bridge \
       --subnet=172.28.0.0/16 \
       --ip-range=172.28.5.0/24 \
       --gateway=172.28.5.254 \
       br0

  * ``--driver``: 可以是 ``bridge`` 或 ``overlay``, 默认为 ``bridge``。 

     * ``bridge``: 依附于运行 Docker Engine 的单台主机上; 
     * ``overlay``: 网络能够覆盖运行各自 Docker Engine 的多主机环境中。
  
  * ``--subnet``: 子网设置
  * ``--ip-range``: IP段
  * ``--gateway``: 网关
  * ``--internal``: 禁止外部连接
  * ``--ipv6``: 使能 ipv6
  * ``--attachable``: 使能手动容器连接

* 查看网络信息::

     docker network inspect [OPTIONS] NETWORK [NETWORK...]

  例如::

      docker network inspect my-bridge

* 连接一个容器到网络::

     docker network connect [OPTIONS] NETWORK CONTAINER

  连接一个正在运行的容器::

     docker network connect multi-host-network container1

  在容器启动时连接一个网络::

     docker run -itd --network=multi-host-network busybox

  给容器指定一个 ip 地址::

     docker network connect --ip 10.10.36.122 multi-host-network container2

  使用 ``--link`` 选项，连接另一个容器

     docker network connect --link container1:c1 multi-host-network container2

* 断开容器与网络的连接::

     docker network disconnect [OPTIONS] NETWORK CONTAINER
  
  例如::

     docker network disconnect multi-host-network container1

* 删除网络::

     docker network rm NETWORK [NETWORK...]

  例如::

     docker network rm my-network

* 删除所有未用的网络::

     docker network prune [OPTIONS]
   
  例如::

     docker network prune

     WARNING! This will remove all networks not used by at least one container.
     Are you sure you want to continue? [y/N] y
     Deleted Networks:
     n1
     n2

数据卷
~~~~~~

``volumes`` 是 Docker 数据持久化机制。 ``bind mounts`` 依赖主机目录结构，``volumes`` 完全由Docker管理。
``volumes`` 有以下优点：

* Volumes 更容易备份和移植。
* 可以通过 Docker CLI 或 API 进行管理
* Volumes 可以无区别的工作中 Windows 和 Linux 下。
* 多个容器共享 Volumes 更安全。
* Volume 驱动可以允许你把数据存储到远程主机或者云端，并且加密数据内容，以及添加额外功能。
* 一个新的数据内容可以由容器预填充。
* volumes 不会增加容器的大小，生命周期独立与容器。

.. image:: ../_static/Docker/docker_volume.png

如果你的容器产生不需要持久化数据，请使用 ``tmpfs mount`` 方式，可以避免容器的写入层数据写入。

挂载卷：

* ``-v,--volume``: 由3部分参数组成，使用 ``:`` 间隔, 顺序不能颠倒
  
  * 第一个部分是volumes名字，在宿主机上具有唯一性。匿名卷名字系统给出。
  * 第二部分是挂载到容器里的文件或文件夹路径。
  * 第三部分是可选项列表分隔符

* ``—mount``: 由多个键值对组成，<key>=<value>。

  * ``type``: 可以是bind,volume或者tmpfs
  * ``source, src``: volumes的名字，匿名volume可以省略。
  * ``destination, dst, target``: 挂载到容器中的文件或目录路径
  * ``readonly``: 指定挂载在容器中为只读。
  * ``volume-opt``: 可选属性，可以多次使用。

  例如::

     docker run --read-only --mount type=volume,target=/icanwrite busybox touch /icanwrite/here
     docker run -t -i --mount type=bind,src=/data,dst=/data busybox sh

.. attention::

   Docker 建议使用 ``--mount`` 来挂载

卷命令：

* 列出所有卷::

     docker volume ls

* 创建卷::

     docker volume create [OPTIONS] [VOLUME]

  例如::

     $ docker volume create hello

     hello

     $ docker run -d -v hello:/world busybox ls /world

* 显示卷信息::

     docker volume inspect [OPTIONS] VOLUME [VOLUME...]

  例如::

     docker volume inspect hello

* 删除卷::

     docker volume rm [OPTIONS] VOLUME [VOLUME...]

  例如::

     docker volume rm hello

* 删除所有未用卷::

     docker volume prune [OPTIONS]

  例如::

     docker volume prune

     WARNING! This will remove all local volumes not used by at least one container.
     Are you sure you want to continue? [y/N] y
     Deleted Volumes:
     07c7bdf3e34ab76d921894c2b834f073721fccfbbcba792aa7648e3a7a664c2e
     my-named-vol

     Total reclaimed space: 36 B

Dockerfile
-----------

Dockerfile 是一个用来构建镜像的文本文件，文本内容包含了一条条构建镜像所需的指令和说明。

举个定制一个 nginx 镜像的例子, Dockerfile::

   FROM nginx
   RUN echo '这是一个本地构建的nginx镜像' > /usr/share/nginx/html/index.html

创建过程::

   yang@SkyLab:~/workspace$ mkdir docker_example
   yang@SkyLab:~/workspace$ cd docker_example/
   yang@SkyLab:~/workspace/docker_example$ ls
   yang@SkyLab:~/workspace/docker_example$ touch Dockerfile
   yang@SkyLab:~/workspace/docker_example$ vi Dockerfile
   yang@SkyLab:~/workspace/docker_example$ cat Dockerfile
   FROM nginx
   RUN echo '这是一个本地构建的nginx镜像' > /usr/share/nginx/html/index.html
   yang@SkyLab:~/workspace/docker_example$ docker build -t dockfile_demo .
   Sending build context to Docker daemon  2.048kB
   Step 1/2 : FROM nginx
   ---> 6678c7c2e56c
   Step 2/2 : RUN echo '这是一个本地构建的nginx镜像' > /usr/share/nginx/html/index.html
   ---> Running in 2386a741e098
   Removing intermediate container 2386a741e098
   ---> bf76644412f8
   Successfully built bf76644412f8
   Successfully tagged dockfile_demo:latest
   yang@SkyLab:~/workspace/docker_example$ docker images
   REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
   dockfile_demo           latest              bf76644412f8        11 seconds ago      127MB
   nginx                   latest              6678c7c2e56c        6 days ago          127MB

.. attention::
  
   Dockerfile 的指令每执行一次都会在 docker 上新建一层。所以过多无意义的层，会造成镜像膨胀过大。 
   可以用 ``&&`` 符号连接命令，这样执行后，只会创建 1 层镜像。

Dockerfile 格式
~~~~~~~~~~~~~~~~

通用格式为::

   # directive=value  解析指令（Parser directives）
   # 注释
   INSTRUCTION arguments

* 指令 (INSTRUCTION): 不区分大小写，习惯上使用大写，以便更容易和参数区分开。

  Docker 按顺序运行 Dockerfile 里的指令，Dockerfile 必须以 ``FROM`` 指令开始，在 ``FROM`` 指令前
  只可以存在注释，解析指令，或者全局变量（ARG 指令）。

* 注释: 以 ``#`` 开始的行，如果不是解析指令，就当作注释处理，注释中不支持行连接符 (``\``)。

* 解析指令： 目前只支持两种 
  
  * ``syntax``： 这个指令只有在使用 ``BuildKit`` 后端时才可以使用，用来指定本地的 Dockerfile builder，
    基本用不上::

       # syntax=[remote image reference]

       # syntax=docker/dockerfile
       # syntax=docker/dockerfile:1.0
       # syntax=docker.io/docker/dockerfile:1
       # syntax=docker/dockerfile:1.0.0-experimental
       # syntax=example.com/user/repo:tag@sha256:abcdef...
    
  * ``escape``: 用来设置 Dockerfile 中的转义符，默认转义符为 ``\``, 比如 Windows 下 ``\`` 会被用在路径,
    这时就需要更换转义符::

       # escape=`
   
    或者::

       # escape=\ 

* .dockerignore 文件: 用来定义哪些文件或者目录不被加入到 docker 镜像中。

Dockerfile 指令
~~~~~~~~~~~~~~~

* ``FROM``: 定制的镜像都是基于 FROM 的镜像。

  格式::

     FROM [--platform=<platform>] <image> [AS <name>]
     FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
     FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
  
  * 一个 Dockerfile 可以包含多行 ``FROM`` 指令来创建多个镜像或者一个作为另一的依赖项。
  * ``name`` 是一个可选项。这个名字可以用于后面的 ``FROM`` 或者 ``COPY --from=<name|index>``
    指令
  * ``ARG`` 是唯一一个可以放在 ``FROM`` 指令前的指令，例如::
  
       ARG  CODE_VERSION=latest
       FROM base:${CODE_VERSION}
       CMD  /code/run-app

       FROM extras:${CODE_VERSION}
       CMD  /code/run-extras 
   
    在 ``FROM`` 指令前的 ``ARG`` 指令不包含在构建阶段，所以不能被 ``FROM`` 后的指令使用，要想继续使用，
    需要在 ``FROM`` 后定义一个不带值的, 像这样::

       ARG VERSION=latest
       FROM busybox:$VERSION
       ARG VERSION
       RUN echo $VERSION > image_version        

* ``RUN``: 在现有镜像上的新层执行命令并提交结果，这个包含提交结果的新镜像将被用于下一步构建

  格式：

  * shell 格式::

       # <命令行命令> 等同于在终端操作的 shell 命令, Linux 的 /bin/sh -c， Windows 的 cmd /S /C
       RUN <命令行命令>
       
  * exec 格式::

       RUN ["可执行文件", "参数1", "参数2"]

    例如::

       RUN ["./test.php", "dev", "offline"] 

    等价于::

        RUN ./test.php dev offline

* ``CMD``: 主要目的是为执行容器提供默认值。这些默认值可以包括可执行文件，也可以省略可执行文件，
  在这种情况下，还必须指定 ``ENTRYPOINT`` 指令。 
  
  为启动的容器指定默认要运行的程序，程序运行结束，容器也就结束。 ``CMD`` 指令指定的程序可被 
  ``docker run`` 命令行参数中指定要运行的程序所覆盖。 如果 Dockerfile 中如果存在多个 ``CMD`` 
  指令，仅最后一个生效。

  格式::

     CMD <shell 命令> <param1> <param2>
     CMD ["<可执行文件或命令>","<param1>","<param2>",...] 
     CMD ["<param1>","<param2>",...]  # 该写法是为 ENTRYPOINT 指令指定的程序提供默认参数

  推荐使用第二种格式，执行过程比较明确。第一种格式实际上在运行的过程中也会自动转换成第二种格式运行，并且默认可执行文件是 sh。

  .. attention::

     ``CMD`` 和 ``RUN`` 指令区别在于，运行时间不同
     
     * ``CMD`` 在容器运行时运行。
     * ``RUN`` 在镜像构建时运行。

* ``ENTRYPOINT``: 类似于 ``CMD`` 指令，但其不会被 ``docker run`` 的命令行参数指定的指令所覆盖，
  而且这些命令行参数会被当作参数送给 ``ENTRYPOINT`` 指令指定的程序。 如果运行 ``docker run`` 时
  使用了 ``--entrypoint`` 选项，此选项的参数可当作要运行的程序覆盖 ``ENTRYPOINT`` 指令指定的程序。
  如果 Dockerfile 中如果存在多个 ``ENTRYPOINT`` 指令，仅最后一个生效。

  格式::

     ENTRYPOINT command param1 param2
     ENTRYPOINT ["<executeable>","<param1>","<param2>",...]

  可以搭配 ``CMD`` 命令使用：一般是变参才会使用 ``CMD`` ，这里的 ``CMD`` 等于是在给 ``ENTRYPOINT`` 传参，
  例如使用如下 dockerfile 生成镜像 nginx:test ::

     FROM nginx

     ENTRYPOINT ["nginx", "-c"] # 定参
     CMD ["/etc/nginx/nginx.conf"] # 变参 

  如果使用::

     docker run nginx:test

  容器内会默认运行以下命令，启动主进程::

     nginx -c /etc/nginx/nginx.conf

  如果使用::

     docker run  nginx:test -c /etc/nginx/new.conf
   
  容器内会默认运行以下命令，启动主进程(/etc/nginx/new.conf:假设容器内已有此文件)::

     nginx -c /etc/nginx/new.conf

* ``LABEL``: 用于给镜像添加元数据。

  格式::

     LABEL <key>=<value> <key>=<value> <key>=<value> ...

  例如::

     LABEL "com.example.vendor"="ACME Incorporated"
     LABEL com.example.label-with-value="foo"
     LABEL version="1.0"
     LABEL description="This text illustrates \
     that label-values can span multiple lines."

  要查看镜像的标签，可以使用 ``docker inspect`` 命令, 显示如下::

     "Labels": {
         "com.example.vendor": "ACME Incorporated"
         "com.example.label-with-value": "foo",
         "version": "1.0",
         "description": "This text illustrates that label-values can span multiple lines.",
         "multi.label1": "value1",
         "multi.label2": "value2",
         "other": "value3"
     },

* ``COPY``: 复制指令，从上下文目录中复制文件或者目录到容器里指定路径。

  格式::

     COPY [--chown=<user>:<group>] <源路径1>...  <目标路径>
     COPY [--chown=<user>:<group>] ["<源路径1>",...  "<目标路径>"]

  * ``[--chown=<user>:<group>]``: 可选参数，用户改变复制到容器内文件的拥有者和属组，只有生成 Linux 镜像时可用。
  * ``<源路径>``: 源文件或者源目录，这里可以是通配符表达式，其通配符规则要满足 Go 的 filepath.Match 规则。例如::

       COPY hom* /mydir/
       COPY hom?.txt /mydir/
  
  * ``<目标路径>``: 容器内的指定路径，该路径不用事先建好，路径不存在的话，会自动创建。

* ``ADD``: 与 ``COPY`` 指令的使用格式一致，区别为

  * ``<源文件>`` 为 ``tar`` 压缩文件的话，压缩格式为 gzip, bzip2 以及 xz 的情况下，
    会自动复制并解压到 ``<目标路径>``
  * ``<源文件>`` 为远程 ``URL`` 时会自动下载到 ``<目标路径>`` 或下载后复制到 ``<目标路径>``

  .. attention::

     推荐除了解压缩的情况，任何情况都使用 ``COPY``。

* ``ENV``: 设置环境变量，定义了环境变量，那么在后续的指令中，就可以使用这个环境变量。

  格式::

     ENV <key> <value>
     ENV <key1>=<value1> <key2>=<value2>...
  
  环境变量在 Dockerfile 中可以通过 ``$key`` 或者 ``${key}`` 来引用，``${key}`` 格式还支持两种修饰符：

  * ${key:-word}: 如果键值未被设置则设成 ``word``，否则使用设置值
  * ${key:+word}: 如果键值已被设置则改为 ``word``，否则使用空字符串

  例子::

     ENV NODE_VERSION 7.2.0

     RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
       && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc"

  使用 ``ENV`` 设置的环境变量会在保留在运行的容器中，可以用 ``docker inspect`` 查看，可以通过
  ``docker run --env <key>=<value>`` 来修改环境变量。

* ``ARG``: 构建参数。 

  格式::

       ARG <参数名>[=<默认值>]
  
  ``ARG`` 设置的环境变量仅对 Dockerfile 内有效，也就是说只对构建的过程中有效，构建好的镜像内不存在此环境变量。
  构建命令 ``docker build`` 中可以用 ``--build-arg <参数名>=<值>`` 来覆盖。
  
  .. attention::

     如果 ``ARG`` 和 ``ENV`` 定义了同样的变量，``ENV`` 定义的值会覆盖 ``ARG`` 定义的值。

* ``VOLUME``: 定义匿名数据卷。在启动容器时忘记挂载数据卷，会自动挂载到匿名卷。挂载数据卷的
  好处是避免重要的数据因容器重启而丢失和避免容器不断变大。

  格式::

     VOLUME ["<路径1>", "<路径2>"...]
     VOLUME <路径>

  在启动容器 ``docker run`` 的时候，也可以通过 ``-v`` 参数修改挂载点。

* ``EXPOSE``: 端口声明, 帮助镜像使用者理解这个镜像服务的守护端口，以方便配置映射。默认对外映射的
  是 ``TCP``协议，你可以指定 ``UDP`` 。

  格式::

     EXPOSE <端口1> [<端口2>/<协议>...]

  使用 ``docker run -P`` 时，会自动随机映射 EXPOSE 的端口。

* ``USER``: 用于指定执行后续命令的用户和用户组，这边只是切换后续命令执行的用户（用户和用户组必须提前已经存在）。

  格式::

     USER <用户名>[:<用户组>]
     USER <UID>[:<GID>]

* ``WORKDIR``: 指定工作目录。用 WORKDIR 指定的工作目录，会在构建镜像的每一层中都存在。 docker 构建镜像过程中的
  每一个 ``RUN`` 命令都是新建的一层。只有通过 ``WORKDIR`` 创建的目录才会一直存在。如果 ``WORKDIR`` 不存在，
  docker 会去创建一个。

  格式::

     WORKDIR <工作目录路径>

  ``WORKDIR`` 在 dockerfile 中可以被多次使用，例如::

     WORKDIR /a
     WORKDIR b
     WORKDIR c
     RUN pwd
  
  输出的 ``pwd`` 为 ``/a/b/c``

* ``HEALTHCHECK``: 用于指定某个程序或者指令来监控 docker 容器服务的运行状态。

  格式::

     HEALTHCHECK [选项] CMD <命令>：设置检查容器健康状况的命令
     HEALTHCHECK NONE：如果基础镜像有健康检查指令，使用这行可以屏蔽掉其健康检查指令

  可以用选项:

  * --interval=时长 (默认: 30s)
  * --timeout=时长 (默认: 30s)
  * --start-period=时长 (默认: 0s)
  * --retries=次数 (默认: 3)
  
  例如::

     HEALTHCHECK --interval=5m --timeout=3s \
       CMD curl -f http://localhost/ || exit 1

Docker Compose 安装
--------------------

#. 安装当前稳定版::

      sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  
   如果 GitHub 太慢了，可以使用国内 DaoCloud ::

      sudo curl -L https://get.daocloud.io/docker/compose/releases/download/1.25.4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

   如果更新版本了或者你想换个版本， 把 ``1.25.4`` 换成你指定的版本。

#. 设置运行权限::

      sudo chmod +x /usr/local/bin/docker-compose

#. 验证安装::

      docker-compose --version

#. 删除::

      sudo rm /usr/local/bin/docker-compose

Docker Compose 命令
-------------------

* 通用格式::

     docker-compose [-f …] [options] [COMMAND] [ARGS…]

  常用选项

  * ``-f, --file FILE``: 指定Compose模板文件，默认为docker-compose.yml可多次指定。
  * ``-p, --project-name NAME``: 指定项目名称，默认使用当前所在目录名称作为项目名称。
  * ``-verbose``: 输出更多调试信息
  * ``-v, --version``: 打印版本并退出

* ``docker-compose up``: 启动所有服务::

     docker-compose up [options] [–scale SERVICE=NUM…] [SERVICE…]
 
  命令选项

  * ``-d``: 指定在后台以守护进程方式运行服务容器
  * ``-no-color``: 设置不使用颜色来区分不同的服务器的控制输出
  * ``-no-deps``: 设置不启动服务所链接的容器
  * ``-force-recreate``: 设置强制重新创建容器，不能与 ``–no-recreate`` 选项同时使用。
  * ``–no-create``: 若容器已经存在则不再重新创建，不能与 ``–force-recreate`` 选项同时使用。
  * ``–no-build``: 设置不自动构建缺失的服务镜像
  * ``–build``: 设置在启动容器前构建服务镜像
  * ``–abort-on-container-exit``: 若任何一个容器被停止则停止所有容器，不能与选项 ``-d`` 同时使用。
  * ``-t, --timeout TIMEOUT``: 设置停止容器时的超时秒数，默认为10秒。
  * ``–remove-orphans`` 设置删除服务中没有在compose文件中定义的容器
  * ``–scale SERVICE=NUM`` 设置服务运行容器的个数，此选项将会负载在compose中通过scale指定的参数。

* ``docker-compose down``: 停止和删除容器、网络、卷、镜像::

     docker-compose down [options]

  命令选项

  * ``-rmi type``: 删除镜像类型，类型可选：

    * ``–rmi all``: 删除compose文件中定义的所有镜像
    * ``–rmi local``: 删除镜像名为空的镜像
  * ``-v, --volumes``: 删除已经在compose文件中定义的和匿名的附在容器上的数据卷
  * ``–remove-orphans``: 删除服务中没有在compose中定义的容器

* ``docker-compose ps``: 列出项目中当前的所有容器

* ``docker-compose logs``: 查看服务容器的输出，默认情况下 ``docker-compose``
  将对不同的服务输出使用不同的颜色来区分。可以通过 ``–no-color`` 来关闭颜色。

* ``docker-compose build``: 构建或重构项目中的服务容器，服务容器一旦构建后将会带上一个标记名称，
  可以随时在项目目录下运行docker-compose build来重新构建服务::

     docker-compose build [options] [–build-arg key=val…] [SERVICE…]

  命令选项

  * ``–compress``: 通过gzip压缩构建上下文环境
  * ``–force-rm``: 删除构建过程中的临时容器
  * ``–no-cache``: 构建镜像过程中不使用缓存
  * ``–pull``: 始终尝试通过拉取操作来获取更新版本的镜像
  * ``-m, --memory MEM``: 为构建的容器设置内存大小
  * –build-arg key=val``: 为服务设置build-time变量

* ``docker-compose restart``: 重启项目中的服务::

     docker-compose restart [options] [SERVICE…]

  命令选项

  * ``-t, --timeout TIMEOUT``: 指定重启前停止容器的超时时长，默认为10秒。

* ``docker-compose rm``: 删除所有停止状态的服务容器，推荐先执行 ``docker-compose stop``
  命令来停止容器::

     docker-compose rm [options] [SERVICE…]

  命令选项

  * ``-f, --force``: 强制直接删除包含非停止状态的容器
  * ``-v``: 删除容器所挂载的数据卷

* ``docker-compose start/stop``: 启动/停止已经存在的服务容器

* ``docker-compose pause/unpause/kill``: 暂停/恢复/强行终止服务容器

* ``docker-compose config``: 验证并查看compose文件配置::

     docker-compose config [options]
  
  命令选项
  
  * ``–resolve-image-digests``: 将镜像标签标记为摘要
  * ``-q, --quiet``: 只验证配置不输出，当配置正确时不输出任何容器，当配置错误时输出错误信息。
  * ``–services``: 打印服务名称，一行显示一个。
  * ``–volumes``: 打印数据卷名称，一行显示一个。

* ``docker-compose run``: 在指定服务上执行一条命令::

     docker-compose run [options] [-v VOLUME…] [-p PORT…] [-e KEY=VAL…] SERVICE [COMMAND] [ARGS…]

  例如, 在test容器上运行ping命令10次::
  
     docker-compose run testping www.baidu.com -c 10

* ``docker-compose exec``: 进入服务::

     docker-compose exec [options] SERVICE COMMAND [ARGS…]

  命令选项

  * ``-d``: 分离模式，以后台守护进程运行命令。
  * ``–privileged``: 获取特权
  * ``-T``: 禁用分配TTY，默认docker-compose exec分配TTY。
  * ``–index=index``: 当一个服务拥有多个容器时可通过该参数登录到该服务下的任何服务  

  例如::

     docker-compose exec --index=1 web /bin/bash

* ``docker-compose port``: 显示某个容器端口所映射的公共端口::

     docker-compose port [options] SERVICE PRIVATE_PORT

  命令选项

  * ``–protocol=proto``: 指定端口协议，默认为TCP，可选UDP。
  * ``–index=index``: 若同意服务存在多个容器，指定命令对象容器的索引序号，默认为1。

Docker Compose 文件
-------------------

Docker Compose 文件格式
~~~~~~~~~~~~~~~~~~~~~~~~

Compose 是用于定义和运行多容器 Docker 应用程序的工具。通过 Compose，您可以使用 ``YML`` 文件
来配置应用程序需要的所有服务，网络及数据卷。然后，使用一个命令，就可以从 ``YML`` 文件配置中创建并启动所有服务。
Compose 使用的三个步骤：

* 使用 Dockerfile 定义应用程序的环境。
* 使用 docker-compose.yml 定义构成应用程序的服务，这样它们可以在隔离环境中一起运行。
* 最后，执行 docker-compose up 命令来启动并运行整个应用程序。

当前最新的 Compose file 格式版本为 ``3.7``。下面是个例子::

   version: '3.7'
   services:
     web:
       build: .
       ports:
         - "5000:5000"
     redis:
       image: "redis:alpine"

Docker Compose 文件指令
~~~~~~~~~~~~~~~~~~~~~~~~

**版本** 配置指令

* ``version``：指定本 yml 依从的 compose 哪个版本制定的。

**服务** 配置指令

* ``build``: 指定为构建镜像上下文路径

  例如 webapp 服务，指定为从上下文路径 ./dir/Dockerfile 所构建的镜像::

     version: "3.7"
     services:
       webapp:
         build: ./dir

  或者，作为具有在上下文指定的路径的对象，以及可选的 Dockerfile 和 args ::

     version: "3.7"
     services:
     webapp:
       build:
         context: ./dir
         dockerfile: Dockerfile-alternate
         args:
           buildno: 1
         labels:
           - "com.example.description=Accounting webapp"
           - "com.example.department=Finance"
           - "com.example.label-with-empty-value"
         target: prod

  * ``context``: 上下文路径。
  * ``dockerfile``: 指定构建镜像的 Dockerfile 文件名。
  * ``args``: 添加构建参数，在 Dockerfile 中定义的 ARG
  * ``labels``: 设置构建镜像的标签。
  * ``target``: 多层构建，可以指定构建哪一层, Dockerfile 中 ``FROM`` 指令中定义的 ``AS`` 名字

* ``image``: 指定容器运行的镜像。以下格式都可以::

     image: redis
     image: ubuntu:14.04
     image: tutum/influxdb
     image: example-registry.com:4000/postgresql
     image: a4bc65fd # 镜像id    
  
* ``container_name``: 指定自定义容器名称，而不是生成的默认名称::

     container_name: my-web-container

* ``command``: 覆盖容器启动的默认命令::
     
     command: ["bundle", "exec", "thin", "-p", "3000"]   

* ``depends_on``: 设置依赖关系::

     version: "3.7"
     services:
       web:
         build: .
         depends_on:
           - db
           - redis
       redis:
         image: redis
       db:
         image: postgres

  * ``docker-compose up``: 以依赖性顺序启动服务。在上面示例中，先启动 db 和 redis ，才会启动 web。
  * ``docker-compose up SERVICE``: 自动包含 SERVICE 的依赖项。
  * ``docker-compose stop``: 按依赖关系顺序停止服务。在以下示例中，web 在 db 和 redis 之前停止。    

* ``configs``: 对每个服务使用不同的配置，例如::

     version: "3.7"
     services:
     redis:
       image: redis:latest
       deploy:
         replicas: 1
       configs:
         - my_config
         - my_other_config
   configs:
     my_config:
       file: ./my_config.txt
     my_other_config:
       external: "true"

* ``devices``: 指定设备映射列表::

     devices:
       - "/dev/ttyUSB0:/dev/ttyUSB0"

* ``dns``: 自定义 DNS 服务器，可以是单个值或列表的多个值::

     dns: 8.8.8.8

     dns:
       - 8.8.8.8
       - 9.9.9.9

* ``dns_search``: 自定义 DNS 搜索域。可以是单个值或列表::

     dns_search: example.com

     dns_search:
       - dc1.example.com
       - dc2.example.com

* ``entrypoint``: 覆盖容器默认的 ``entrypoint``::

     entrypoint: /code/entrypoint.sh

  也可以用类似 Dockerfile 的格式::

     entrypoint:
         - php
         - -d
         - zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20100525/xdebug.so
         - -d
         - memory_limit=-1
         - vendor/bin/phpunit

* ``env_file``: 从文件添加环境变量。可以是单个值或列表的多个值::

     env_file: .env

  也可以是列表格式::

     env_file:
       - ./common.env
       - ./apps/web.env
       - /opt/secrets.env

* ``environment``: 添加环境变量。您可以使用数组或字典、任何布尔值，
  布尔值需要用引号引起来，以确保 YML 解析器不会将其转换为 True 或 False ::

     environment:
       RACK_ENV: development
       SHOW: 'true'

* ``expose``: 暴露端口，但不映射到宿主机，只被连接的服务访问。仅可以指定内部端口为参数::

     expose:
      - "3000"
      - "8000"

* ``extra_hosts``: 添加主机名映射::

     extra_hosts:
       - "somehost:162.242.195.82"
       - "otherhost:50.31.209.229"

  以上会在此服务的内部容器中 /etc/hosts 创建一个具有 ip 地址和主机名的映射关系::

     162.242.195.82  somehost
     50.31.209.229   otherhost   

* ``healthcheck``: 用于检测 docker 服务是否健康运行::

     healthcheck:
       test: ["CMD", "curl", "-f", "http://localhost"] # 设置检测程序
       interval: 1m30s # 设置检测间隔
       timeout: 10s # 设置检测超时时间
       retries: 3 # 设置重试次数
       start_period: 40s # 启动后，多少秒开始启动检测程序

* ``logging``: 服务的日志记录配置。

  driver：指定服务容器的日志记录驱动程序，默认值为json-file。有以下三个选项

  * driver: "json-file"
  * driver: "syslog"
  * driver: "none"

  仅在 json-file 驱动程序下，可以使用以下参数，限制日志得数量和大小::

     logging:
       driver: json-file
       options:
         max-size: "200k" # 单个文件大小为200k
         max-file: "10" # 最多10个文件

  当达到文件限制上限，会自动删除旧得文件。

  syslog 驱动程序下，可以使用 syslog-address 指定日志接收地址::

     logging:
       driver: syslog
       options:
         syslog-address: "tcp://192.168.0.42:123"

* ``restart``: 重启策略::

     restart: "no"
     restart: always
     restart: on-failure
     restart: unless-stopped

  * no：是默认的重启策略，在任何情况下都不会重启容器。
  * always：容器总是重新启动。
  * on-failure：在容器非正常退出时（退出状态非0），才会重启容器。
  * unless-stopped：在容器退出时总是重启容器，但是不考虑在Docker守护进程启动时就已经停止了的容器

* ``secrets``: 存储敏感数据，例如密码::

     version: "3.1"
     services:

     mysql:
       image: mysql
       environment:
         MYSQL_ROOT_PASSWORD_FILE: /run/secrets/my_secret
       secrets:
         - my_secret

     secrets:
       my_secret:
         file: ./my_secret.txt

* ``network_mode``: 设置网络模式::

     network_mode: "bridge"
     network_mode: "host"
     network_mode: "none"
     network_mode: "service:[service name]"
     network_mode: "container:[container name/id]"

* ``networks``: 配置容器连接的网络，引用顶级 ``networks`` 下的条目::

     services:
       some-service:
         networks:
           some-network:
             aliases:
              - alias1
           other-network:
             aliases:
              - alias2
     networks:
       some-network:
         # Use a custom driver
         driver: custom-driver-1
       other-network:
         # Use a custom driver which takes special options
         driver: custom-driver-2

* ``port``: 端口映射, 有两种格式。

  短格式::

     ports:
       - "3000"
       - "3000-3005"
       - "8000:8000"
       - "9090-9091:8080-8081"
       - "49100:22"
       - "127.0.0.1:8001:8001"
       - "127.0.0.1:5000-5010:5000-5010"
       - "6060:6060/udp"

  长格式::

     ports:
       - target: 80
         published: 8080
         protocol: tcp
         mode: host
     
  * target: 容器内端口
  * published: 映射端口
  * protocol: 协议
  * mode: 模式
    
    * host: 在每一个 node 上映射端口
    * ingress: ``swarm`` 模式时，负载均衡

* ``volumes``: 将主机的数据卷或着文件挂载到容器里。 如果你不需要重用卷，那么这样定义就可以了。
  如果需要重用卷，需要在顶级 ``volumes`` 下引用。 数据卷映射有两种格式。

  短格式::

     version: "3.7"
     services:
       db:
         image: postgres:latest
         volumes:
           - "/localhost/postgres.sock:/var/run/postgres/postgres.sock"
           - "/localhost/data:/var/lib/postgresql/data"

  长格式::

     version: "3.7"
     services:
       web:
         image: nginx:alpine
         ports:
           - "80:80"
         volumes:
           - type: volume
             source: mydata
             target: /data
             volume:
               nocopy: true
           - type: bind
             source: ./static
             target: /opt/app/static

     networks:
       webnet:

     volumes:
       mydata:

  * type： volume, bind, tmpfs 或 npipe
  * source：需要映射的主机目录或者顶级 ``volumes`` 里定义的名字
  * target: 容器内的目录
  * read_only: 是否只读
  * bind: bind 模式的其他选项
  * volume: volume 模式的其他选项
    
    * nocopy: 在创建卷的时候不进行拷贝

  * tmpfs: tmpfs 模式的其他选项

    * size: tmpfs 的大小

  * consistency: 挂载的一致性要求

    * consistent: 主机和容器内容一致
    * cached: 读取缓存，主机内容权威
    * delegated: 读写缓存，容器内容权威

**卷** 配置指令

顶级 ``volumes`` 块是为了共享卷使用的, 例如::

   version: "3.7"

   services:
     db:
       image: db
       volumes:
         - data-volume:/var/lib/db
     backup:
       image: backup-service
       volumes:
         - data-volume:/var/lib/backup/data

   volumes:
     data-volume:

此例中 db 服务和 backup 服务共用卷 data-volume 。

**网络** 配置指令

顶级 ``networks`` 块是为了创建服务指定的虚拟网络，服务在这个虚拟网络中独立运行，主要
看你的服务需不需要隔离。例如::

   version: "3"
   services:

   proxy:
      build: ./proxy
      networks:
         - frontend
   app:
      build: ./app
      networks:
         - frontend
         - backend
   db:
      image: postgres
      networks:
         - backend

   networks:
   frontend:
      # Use a custom driver
      driver: custom-driver-1
   backend:
      # Use a custom driver which takes special options
      driver: custom-driver-2
      driver_opts:
         foo: "1"
         bar: "2"

这里 ``driver`` 需要你创建，例如::

   docker network create --driver weave mynet
