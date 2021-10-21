.. PlantUML:

PlantUML
====================

.. image:: ../_static/PlantUML/PlantUML_logo.png
   :height: 100
   :target: https://plantuml.com/zh/

PlantUML是一个开源项目，支持快速绘制：

- 时序图
- 用例图
- 类图
- 对象图
- 活动图
- 组件图
- 部署图
- 状态图
- 定时图

同时还支持以下非UML图：

- JSON 数据
- YAML 数据
- 网络图 (nwdiag)
- 线框图形界面
- 架构图
- 规范和描述语言 (SDL)
- Ditaa 图
- 甘特图
- 思维导图
- WBS 工作分解图
- 以 AsciiMath 或 JLaTeXMath 符号的数学公式
- 实体关系图

PlantUML 安装
-----------------

#. 安装 ``Java`` ， 并配置环境变量

#. 安装 ``Graphviz`` ， 并配置环境变量

#. 下载 ``PlantUML`` 应用包 `plantuml.jar <http://sourceforge.net/projects/plantuml/files/plantuml.jar/download>`_

#. 安装 VSCode ``PlantUML`` 插件

PlantUML VSCode 插件
--------------------------

Markdown
~~~~~~~~~

- 配置

  ``settings.json`` 例子

  .. code-block:: json
      
     {
        "plantuml.exportOutDir": "docs/images",
        "plantuml.diagramsRoot": "docs",
        "plantuml.exportFormat": "svg",
        "plantuml.jar": "D:\\tools\\Plantuml\\plantuml.jar"
     }

- 使用

  按 :guilabel:`F1`, 点击 :guilabel:`PlantUML:导出当前图表`

  .. code-block:: none

     <!--
     ```PlantUML
     @startuml 测试
     用户 -> 认证中心: 登录操作
     认证中心 -> 缓存: 存放(key=token+ip,value=token)token
     用户 <- 认证中心 : 认证成功返回token
     用户 -> 认证中心: 下次访问头部携带token认证
     认证中心 <- 缓存: key=token+ip获取token
     其他服务 <- 认证中心: 存在且校验成功则跳转到用户请求的其他服务
     其他服务 -> 用户: 信息
     @enduml
     ```
     -->

     ![测试](./images/sys/测试.svg "测试")


  生成的图形如下

  .. image:: ../_static/PlantUML/generated.svg

ReStructuredText
~~~~~~~~~~~~~~~~~~

- 配置

  ``conf.py`` 例子

  .. code-block:: python
      
     extensions = [
        'sphinx.ext.autosectionlabel',
        'recommonmark',
        'sphinxcontrib.plantuml',
     ]

     ## PlantUML
     plantuml = 'java -jar .\\_utils\\plantuml.jar'
     plantuml_output_format = 'png'

- 使用

  .. uml::

     Alice -> Bob: Hi!
     Alice <- Bob: How are you?
