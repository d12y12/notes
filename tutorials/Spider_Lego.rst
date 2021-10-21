.. spider_lego:

Lego手册爬虫
=============

创建爬虫项目
-------------

#. Conda 环境

   .. code-block:: shell

      conda create --name spider python
      conda activate spider
      python -m pip install --upgrade pip
      pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple/

   测试::

      scrapy

   输出::

      Scrapy 2.0.0 - no active project

      Usage:
        scrapy <command> [options] [args]

      Available commands:
        bench         Run quick benchmark test
        fetch         Fetch a URL using the Scrapy downloader
        genspider     Generate new spider using pre-defined templates
        runspider     Run a self-contained spider (without creating a project)
        settings      Get settings values
        shell         Interactive scraping console
        startproject  Create new project
        version       Print Scrapy version
        view          Open URL in browser, as seen by Scrapy

      [ more ]      More commands available when run from project directory

      Use "scrapy <command> -h" to see more info about a command

#. Scrapy 项目

   创建一个目录, 比如 ``spider``::

      mkdir E:\Git\spider
      cd E:\Git\spider

   创建 Scrapy 项目::

      scrapy startproject lego .

   .. attention::

      最后的 ``.``，代表在当前目录创建项目。
      不带 ``.`` 的话，它会在当前目录再创建一个 ``lego`` 目录并在其中创建项目。

   目录 ``spider`` 结构::

      scrapy.cfg
      lego/
         __init__.py
         items.py
         middlewares.py
         pipelines.py
         settings.py
         spiders/
            __init__.py



scrapy crawl category
scrapy crawl product -a categories="Technic,4 Juniors"

scrapy crawl download -a category="Technic"
