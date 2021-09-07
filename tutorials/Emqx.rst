.. Emqx:

EMQX
====================

EMQ X (Erlang/Enterprise/Elastic MQTT Broker) 是基于 Erlang/OTP 平台开发的开源物联网 MQTT 消息服务器。

详细文档参见: https://docs.emqx.cn/broker/latest/

EMQX Docker 部署
----------

#. 在服务器上创建临时容器

   .. code-block:: shell
      
      docker run -d --name emqx -p 1883:1883 -p 8081:8081 -p 8083:8083 -p 8883:8883 -p 8084:8084 -p 18083:18083 emqx/emqx

#. 在服务器上创建挂载目录

   .. code-block:: shell

      yang@ubuntu:~/workspace$ mkdir -p emqx/{etc,lib,data,log}

#. 将临时容器的文件拷贝到服务器
   
   .. code-block:: shell

      yang@ubuntu:~/workspace$ docker cp emqx:/opt/emqx/etc emqx
      yang@ubuntu:~/workspace$ docker cp emqx:/opt/emqx/lib emqx
      yang@ubuntu:~/workspace$ docker cp emqx:/opt/emqx/data emqx
      yang@ubuntu:~/workspace$ docker cp emqx:/opt/emqx/log emqx

   检查配置目录

   .. code-block:: shell
      
      yang@ubuntu:~/workspace$ ls emqx/etc/
      acl.conf       certs/         emqx.conf      lwm2m_xml/     plugins/       psk.txt        ssl_dist.conf  vm.args

#. 修改挂载目录权限

   .. code-block:: shell

      yang@ubuntu:~/workspace$ chown -R 1000:1000 emqx
      yang@ubuntu:~/workspace$ chmod -R 755 emqx

   .. note::

      如果像我这里一样在用户目录创建，此步骤可以省略

#. 重新启动并挂载目录到服务器

   .. code-block:: shell

      docker run -d \
      --name emqx \
      -p 1883:1883 \
      -p 8081:8081 \
      -p 8083:8083 \
      -p 8883:8883 \
      -p 8084:8084 \
      -p 18083:18083 \
      -v /home/yang/workspace/emqx/etc:/opt/emqx/etc \
      -v /home/yang/workspace/emqx/data:/opt/emqx/data \
      -v /home/yang/workspace/emqx/lib:/opt/emqx/lib \
      -v /home/yang/workspace/emqx/log:/opt/emqx/log \
      emqx/emqx

#. Docker-Compose Yaml

   .. code-block:: shell
      
      version: '3.7'
      services:
        emqx:
          image: emqx/emqx
          container_name: emqx
          restart: always
          ports:
            - 1883:1883
            - 8081:8081
            - 8083:8083
            - 8883:8883
            - 8084:8084
            - 18083:18083
          volumes:
            - ./etc:/opt/emqx/etc
            - ./data:/opt/emqx/data
            - ./lib:/opt/emqx/lib
            - ./log:/opt/emqx/log

#. 查看Dashboard: ``http://{your ip}:18083``
  
   默认用户名: ``admim``
   默认密码  : ``public``

   .. code-block:: shell
   
      http://192.168.146.128:18083

   .. note::
      
      这里要把我的IP ``192.168.146.128`` 替换成你自己的。

#. 禁止客户端匿名登录

   修改 ``emqx.conf`` 文件, 将 ``allow_anonymous``设置为 `false`

   .. code-block:: shell

      yang@ubuntu:~/workspace$ vi emqx/etc/emqx.conf

      allow_anonymous = false

#. 添加客户端用户名密码

   修改 ``emqx_auth_mnesia.conf`` 文件

   例如

   .. code-block:: shell

      yang@ubuntu:~/workspace$ vi emqx/etc/plugins/emqx_auth_mnesia.conf
      
      添加
      auth.user.1.username = test
      auth.user.1.password = yang

   .. attention::
      
      第一次初始化启动时候配置的账号密码会写入到mnesia数据库里面。
      如果要从配置文件改，就要先清空一下 ``data/mnesia`` 目录，否则修改无效。
      建议用 ``API`` 进行修改。

#. 通过API修改密码

   .. code-block:: shell

      PUT api/v4/auth_username/${username}
      {
        "password": "xxxx"
      }

EMQX 默认端口
-------------------

.. list-table:: EMQX 默认端口
      :header-rows: 1

      * - 端口
        - 服务
      * - 1883
        - MQTT TCP
      * - 8883
        - MQTT SSL
      * - 8083
        - MQTT Websocket
      * - 8084
        - MQTT Websocket SSL
      * - 8081
        - HTTP API
      * - 18083
        - Dashboard
