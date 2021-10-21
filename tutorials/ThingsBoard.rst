.. ThingsBoard:

ThingsBoard
====================

ThingsBoard Docker 部署
-----------------------------------

#. 在服务器上创建挂载目录

   .. code-block:: shell

      yang@ubuntu:~/workspace$ mkdir -p thingsboard/{data,logs}

#. 修改挂载目录权限

    .. code-block:: shell

       yang@ubuntu:~/workspace$ sudo chown -R 799:799 thingsboard/{data,logs}  

#. Docker-Compose Yaml

   .. code-block:: shell

     version: '3.7'
     services:
       thingsboard:
         image: thingsboard/tb-postgres
         container_name: thingsboard
         restart: always
         environment:
           TB_QUEUE_TYPE: in-memory
         ports:
           - 8080:9090
           - 3883:1883
           - 5683-5688:5683-5688/udp
         volumes:
           - ./data:/data
           - ./logs:/var/log/thingsboard
