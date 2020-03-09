.. Conda:

Conda
====================

.. image:: ../_static/Conda/conda_logo.png
   :height: 100
   :target: Conda_

.. _Conda: https://conda.io/projects/conda/en/latest/

|   

Conda 是一个开源的软件包管理系统和环境管理系统，用于安装多个版本的软件包及其依赖关系，
并在它们之间轻松切换。Conda 是为 Python 程序创建的，适用于 Linux，OS X 和 Windows，
也可以打包和分发其他软件。

你可以使用 Conda 为不同的项目隔离开发环境，可以在不同的机器上重现开发环境。

Conda 安装
----------

Conda 分为两个大版本

* Miniconda 只包含 Conda 和它的依赖
* Anaconda 除了 Conda 还包含7500多个开源包

Anaconda 又包含命令行版本和图形版本。

.. tip::
   
   关于版本选用：我建议 Windows 环境下使用 Anaconda 图形版本。 Linux 环境下使用 Miniconda 。

系统需求
~~~~~~~~

* 32或64位计算机
* Miniconda---400 MB 硬盘空间
* Anaconda---3 GB 以上硬盘空间
* Windows, macOS, 或 Linux

安装步骤
~~~~~~~~~

Windows Anaconda 图形版
#########################

#. `下载 Anaconda 安装程序 <https://www.anaconda.com/download/#windows>`_
#. 双击打开安装程序
#. 点击 :guilabel:`Next`
#. 阅读使用许可协议，如果想继续安装点击 :guilabel:`I Agree`
#. 选择安装类型，为“所有用户”安装需要管理员权限，如非必要，选择 :guilabel:`Just Me` 点击 :guilabel:`Next`
#. 选择安装位置，默认在 "C:\\Users\\<USERNAME>\\Anaconda3", 点击 :guilabel:`Next`
#. 选择是否将 Anaconda 加入 PATH 环境变量。 Anaconda 的建议是不加到 PATH 环境变量，以免影响其他软件。
   作为替代，使用 
   :menuselection:`开始菜单 --> Anaconda Navigator` 和 :menuselection:`开始菜单 --> Anaconda Prompt` 。
   
   选择是否将 Anaconda 注册为默认的 Python 解释器。勾选，点击 :guilabel:`Install`。

   .. image:: ../_static/Conda/advance_option.png
      :scale: 80

#. 如果想了解 Anaconda 正在安装的包，点击 :guilabel:`Show Details`
#. 安装完成点击 :guilabel:`Next`
#. 可选项，如果需要安装 “PyCharm”，点击链接 https://www.anaconda.com/pycharm
    
   不需要的话，点击 :guilabel:`Next`
#. 如果安装成功，这是你将看到 “感谢安装 Anaconda3 ”， 如果不想看说明，取消勾选，点击 :guilabel:`Finish`。
#. 验证安装
    
   * :menuselection:`开始菜单 --> Anaconda Navigator`
   * :menuselection:`开始菜单 --> Anaconda Prompt`
      
     * 输入 ``conda list`` , 如果安装正常，会显示安装的包及它们的版本
     * 输入 ``python`` , 如果安装正常，版本信息会包含 Anaconda
     * 输入 ``anaconda-navigator``, 如果安装正常会启动 Anaconda 图形界面

Linux Miniconda
################

还没装，装的时候再说。

Conda 配置
----------

PowerShell
~~~~~~~~~~~

我习惯使用 PowerShell 而不是 Anaconda Prompt 。
由于我们没有把 Anaconda 加入 PATH 环境变量，当使用 PowerShell 的时候，出现找不到 Conda 的问题。

.. code-block:: shell

   Windows PowerShell
   Copyright (C) Microsoft Corporation. All rights reserved.

   Try the new cross-platform PowerShell https://aka.ms/pscore6
   PS C:\Users\yang> conda
   conda : The term 'conda' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
   the spelling of the name, or if a path was included, verify that the path is correct and try again.
   At line:1 char:1
   + conda
   + ~~~~~
      + CategoryInfo          : ObjectNotFound: (conda:String) [], CommandNotFoundException
      + FullyQualifiedErrorId : CommandNotFoundException

可以通过 ``conda init powershell`` 来初始化 PowerShell 环境变量。 Conda 可执行文件在安装目录的 Scripts 文件夹。

.. code-block:: shell

   PS C:\Users\yang> C:\Users\yang\Anaconda3\Scripts\conda init powershell
   no change     C:\Users\yang\Anaconda3\Scripts\conda.exe
   no change     C:\Users\yang\Anaconda3\Scripts\conda-env.exe
   no change     C:\Users\yang\Anaconda3\Scripts\conda-script.py
   no change     C:\Users\yang\Anaconda3\Scripts\conda-env-script.py
   no change     C:\Users\yang\Anaconda3\condabin\conda.bat
   no change     C:\Users\yang\Anaconda3\Library\bin\conda.bat
   no change     C:\Users\yang\Anaconda3\condabin\_conda_activate.bat
   no change     C:\Users\yang\Anaconda3\condabin\rename_tmp.bat
   no change     C:\Users\yang\Anaconda3\condabin\conda_auto_activate.bat
   no change     C:\Users\yang\Anaconda3\condabin\conda_hook.bat
   no change     C:\Users\yang\Anaconda3\Scripts\activate.bat
   no change     C:\Users\yang\Anaconda3\condabin\activate.bat
   no change     C:\Users\yang\Anaconda3\condabin\deactivate.bat
   modified      C:\Users\yang\Anaconda3\Scripts\activate
   modified      C:\Users\yang\Anaconda3\Scripts\deactivate
   modified      C:\Users\yang\Anaconda3\etc\profile.d\conda.sh
   modified      C:\Users\yang\Anaconda3\etc\fish\conf.d\conda.fish
   no change     C:\Users\yang\Anaconda3\shell\condabin\Conda.psm1
   modified      C:\Users\yang\Anaconda3\shell\condabin\conda-hook.ps1
   modified      C:\Users\yang\Anaconda3\Lib\site-packages\xontrib\conda.xsh
   modified      C:\Users\yang\Anaconda3\etc\profile.d\conda.csh
   modified      D:\Documents\WindowsPowerShell\profile.ps1

   ==> For changes to take effect, close and re-open your current shell. <==

重新打开 PowerShell ，输入 conda 验证

.. code-block:: shell

   Windows PowerShell
   Copyright (C) Microsoft Corporation. All rights reserved.

   Try the new cross-platform PowerShell https://aka.ms/pscore6

   Loading personal and system profiles took 1289ms.
   (base) PS C:\Users\yang> conda -V
   conda 4.7.12

如果不想每次一启动 PowerShell 就自动激活 Base 环境

.. code-block:: shell

   conda config --set auto_activate_base false

如果又想启动了

.. code-block:: shell

   conda config --set auto_activate_base true


下载频道
~~~~~~~~

下载频道就是选择从哪里下载包，国外的比较慢，推荐使用国内的源，比如清华的::

   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

可以使用三种方式配置：

* 图形界面
  
  :menuselection:`开始菜单 --> Anaconda Navigator`

  .. image:: ../_static/Conda/anaconda_navigator.png

  点击 :guilabel:`Channels`

  .. image:: ../_static/Conda/channels.png

  点击 :guilabel:`Add`， 并加入新的源地址

  .. image:: ../_static/Conda/channels_added.png

* 命令行

  使用 PowerShell

  .. code-block:: shell

     conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
     conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

* 修改配置文件

  配置文件一般位于 ``C:\\Users\\<USERNAME>\\.condarc``
  
  Channles 部分默认为::

     channels:
       - defaults

  修改为::

     channels:
       - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
       - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
       - defaults

环境位置
~~~~~~~~

Anaconda 创建的环境默认位置是 ``C:\Users\<USERNAME>\Anaconda3\envs`` ，
如果想修改创建环境的默认位置，可以通过修改配置文件 ``.condarc`` 来实现::

   ssl_verify: true
   channels:
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
     - defaults
   envs_dirs:
     - E:\conda\envs
     - C:\Users\yang\Anaconda3\envs

.. attention:: 

   文件夹位置很重要，使用 ``conda create`` 命令默认创建在 ``envs`` 的第一个文件夹，
   在上面例子里就是 ``E:\conda\envs``。 
   
   如果本例写成::

      envs_dirs:
        - C:\Users\yang\Anaconda3\envs
        - E:\conda\envs

   则使用 ``conda create --name <ENVNAME> python`` 会把环境创建在 ``C:\Users\yang\Anaconda3\envs``,
   想在 ``E:\conda\envs`` 中创建环境需要使用 ``conda create --prefix E:\conda\envs\<ENVNAME> python`` ,
   或者从命令行进入 ``E:\conda\envs`` 文件夹， 再使用 ``conda create --prefix <ENVNAME> python``


Conda 使用
----------

环境
~~~~~

创建环境
########

* 图形界面

  点击 :guilabel:`Environments`

  .. image:: ../_static/Conda/anaconda_env.png

  点击 :guilabel:`Create` ， 输入环境名，选择 Python 版本

  .. image:: ../_static/Conda/anaconda_create.png
  
  点击 :guilabel:`Create`

* 命令行

  使用 ``conda create --name <ENVNAME> python=3.7`` , 
  Python 的版本号根据需要更改， 在命令行询问 ``ProProceed ([y]/n)?`` 时，
  输入 ``y``

  .. code-block:: shell
     
     Windows PowerShell
     Copyright (C) Microsoft Corporation. All rights reserved.

     Try the new cross-platform PowerShell https://aka.ms/pscore6

     Loading personal and system profiles took 1183ms.
     (base) PS C:\Users\yang> conda create --name hello python=3.7
     Collecting package metadata (current_repodata.json): done
     Solving environment: done

     ==> WARNING: A newer version of conda exists. <==
     current version: 4.7.12
     latest version: 4.8.2

     Please update conda by running

        $ conda update -n base -c defaults conda

     ## Package Plan ##

     environment location: E:\conda\envs\hello

     added / updated specs:
        - python=3.7

     The following NEW packages will be INSTALLED:

     ca-certificates    anaconda/pkgs/main/win-64::ca-certificates-2020.1.1-0
     certifi            anaconda/pkgs/main/win-64::certifi-2019.11.28-py37_0
     openssl            anaconda/pkgs/main/win-64::openssl-1.1.1d-he774522_4
     pip                anaconda/pkgs/main/win-64::pip-20.0.2-py37_1
     python             anaconda/pkgs/main/win-64::python-3.7.6-h60c2a47_2
     setuptools         anaconda/pkgs/main/win-64::setuptools-45.2.0-py37_0
     sqlite             anaconda/pkgs/main/win-64::sqlite-3.31.1-he774522_0
     vc                 anaconda/pkgs/main/win-64::vc-14.1-h0510ff6_4
     vs2015_runtime     anaconda/pkgs/main/win-64::vs2015_runtime-14.16.27012-hf0eaf9b_1
     wheel              anaconda/pkgs/main/win-64::wheel-0.34.2-py37_0
     wincertstore       anaconda/pkgs/main/win-64::wincertstore-0.2-py37_0

     Proceed ([y]/n)? y

     Preparing transaction: done
     Verifying transaction: done
     Executing transaction: done
     #
     # To activate this environment, use
     #
     #     $ conda activate hello
     #
     # To deactivate an active environment, use
     #
     #     $ conda deactivate

查看环境
########

* 图形界面

  点击 :guilabel:`Environments`

  .. image:: ../_static/Conda/anaconda_env_check.png
  
  点击想查看的环境。

* 命令行

  使用 ``conda env list`` 或 ``conda info --envs`` 命令

  .. code-block:: shell

     (base) PS C:\Users\yang> conda env list
     # conda environments:
     #
     base                  *  C:\Users\yang\Anaconda3
     hello                    E:\conda\envs\hello

     (base) PS C:\Users\yang> conda info --envs
     # conda environments:
     #
     base                  *  C:\Users\yang\Anaconda3
     hello                    E:\conda\envs\hello
   
  其中带 ``*`` 的表示当前激活的环境。

激活环境
#########

* 图形界面
  
  在 :guilabel:`Environments` 中点击想要激活的环境， 
  :menuselection:`三角形 --> Open Terminal`
  或者 :menuselection:`三角形 --> Open Python` 

* 命令行

  使用 ``conda activate <env name>`` 激活环境， 使用 ``conda deactivate <env name>``
  去激活。

  .. code-block:: shell

     (base) PS C:\Users\yang> conda activate hello
     (hello) PS C:\Users\yang>

  括号内的是当前激活环境。

迁移环境
########

* 克隆
  
  如果只是想在本机上创建一个相同环境，可以克隆现有环境。
  例如克隆 base 环境::

     conda create --name <ENVNAME> --clone base

* 操作系统一致

  如果想在使用同一操作系统的不同计算机间迁移， 可以导出 ``spec list`` 文件。

  * 导出
    ::

       conda list --explicit > spec-list.txt
   
  * 导入
    ::

       conda create --name <ENVNAME> --file spec-list.txt

* 操作系统不一致

  使用不同操作系统间进行迁移，需要导出 ``environment.yml`` 文件。

  * 导出
    ::

       conda env export > environment.yml
  
  * 导入
    ::

       conda env create -f environment.yml

  .. important::

     事实上，这样导出是不行的， 因为这会导出所有包及依赖，很多都是操作系统不兼容的。。。

     要想使用非操作系统相关的，只需要导出你通过 ``install`` 命令安装的包，不含它们的依赖，
     不含创建环境的依赖。 这种情况下导出时要使用::
      
        conda env export --from-history > environment.yml
  
     然后要小修补一下，比如去掉 Prefix ，是否要去掉添加的国内加速频道，如果国内使用，就保留，
     如果放国外，可能默认的频道更快。
     以 Read the Docs 为例，使用清华的镜像频道比默认频道慢接近一个量级。

* 完全打包

  适合在没网或者网不好的情况下，把所有的二进制和安装的包都存档，这个默认安装不支持，
  需要安装 ``conda-pack`` 包。

  * 安装 ``conda-pack`` 包
    ::

       conda install -c conda-forge conda-pack
   
    或者::

       pip install conda-pack
  
  * 打包环境
    ::
   
       # Pack environment my_env into my_env.tar.gz
       $ conda pack -n my_env

       # Pack environment my_env into out_name.tar.gz
       $ conda pack -n my_env -o out_name.tar.gz

       # Pack environment located at an explicit path into my_env.tar.gz
       $ conda pack -p /explicit/path/to/my_env

  * 安装环境
    ::

       # Unpack environment into directory `my_env`
       $ mkdir -p my_env
       $ tar -xzf my_env.tar.gz -C my_env

       # Use Python without activating or fixing the prefixes. Most Python
       # libraries will work fine, but things that require prefix cleanups
       # will fail.
       $ ./my_env/bin/python

       # Activate the environment. This adds `my_env/bin` to your path
       $ source my_env/bin/activate

       # Run Python from in the environment
       (my_env) $ python

       # Cleanup prefixes from in the active environment.
       # Note that this command can also be run without activating the environment
       # as long as some version of Python is already installed on the machine.
       (my_env) $ conda-unpack

删除环境
########

* 图形界面
  
  在 :guilabel:`Environments` 中点击想要删除的环境， 点击 :guilabel:`Remove`

* 命令行
  ::
  
     conda remove --name <ENVNAME> --all

包
~~~~~

查看包
#######

* 图形界面

  在 :guilabel:`Environments` 中点击想要查看的环境，右侧有包列表，可以在下拉菜单中
  选择 :guilabel:`Installed`， :guilabel:`Not installed`， :guilabel:`Updatable`，
  :guilabel:`Selected`，及 :guilabel:`All` 进行过滤

* 命令行

  使用 ``conda list`` 命令

  .. code-block:: shell

     (hello) PS C:\Users\yang> conda list
     # packages in environment at E:\conda\envs\hello:
     #
     # Name                    Version                   Build  Channel
     ca-certificates           2020.1.1                      0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     certifi                   2019.11.28               py37_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     openssl                   1.1.1d               he774522_4    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     pip                       20.0.2                   py37_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     python                    3.7.6                h60c2a47_2    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     setuptools                45.2.0                   py37_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     sqlite                    3.31.1               he774522_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     vc                        14.1                 h0510ff6_4    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     vs2015_runtime            14.16.27012          hf0eaf9b_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     wheel                     0.34.2                   py37_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     wincertstore              0.2                      py37_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main

安装包
#######

* 图形界面

  在 :guilabel:`Environments` 中点击想要安装包的环境，在下拉菜单中选择 :guilabel:`Not installed`，
  然后在搜索栏搜索想要安装的包，比如 “numpy”

  .. image:: ../_static/Conda/package_search.png

  点击 :guilabel:`numpy`， 在选项菜单中选择 :guilabel:`mark for installation`
  
  点击 :guilabel:`Apply`

  .. image:: ../_static/Conda/package_install.png

  点击 :guilabel:`Apply`

  安装完毕后，在 :guilabel:`Environments` 中点击想要安装包的环境，在下拉菜单中
  选择 :guilabel:`Installed` 查看

* 命令行

  搜索包，使用命名 ``conda search PACKAGENAME``, 例如::

     (hello) PS C:\Users\yang> conda search beau
     Loading channels: done
     No match found for: beau. Search: *beau*
     # Name                       Version           Build  Channel
     beautiful-soup                 4.3.1          py26_0  anaconda/pkgs/free
     beautiful-soup                 4.3.1          py27_0  anaconda/pkgs/free
     ...

     beautifulsoup4                 4.8.2          py38_0  anaconda/pkgs/main
     beautifulsoup4                 4.8.2          py38_0  pkgs/main

  安装包，使用命令 ``conda install PACKAGENAME==Rev``, 例如:

  .. code-block:: shell

     (hello) PS C:\Users\yang> conda install beautifulsoup4

  Conda 不包含的包，可以用 ``pip install PACKAGENAME=Rev`` 安装, 例如:

  .. code-block:: shell

     doc) PS C:\Users\yang> pip install doc8

删除包
######

* 图形界面
  
  在 :guilabel:`Environments` 中点击想要安装包的环境，在下拉菜单中选择 :guilabel:`Installed`，
  然后在搜索栏搜索想要安装的包，比如 “numpy”

  点击 :guilabel:`numpy`， 在选项菜单中选择 :guilabel:`mark for removal`
  
  点击 :guilabel:`Apply`

* 命令行

  Conda 使用命令::
  
     conda uninstall PACKAGENAME

  pip 使用命令::
  
     pip uninstall PACKAGENAME

其他 Conda 命令
~~~~~~~~~~~~~~~

* 升级
  
  使用 ``conda update`` 命令

  升级 conda ::

     conda update conda
  
  升级 anaconda ::

     conda update anaconda

.. seealso::
   
   了解更多命令， 参见: 
   `conda cheat sheet`_

   .. only:: builder_html
     
      本地下载 :download:`conda cheat sheet <../_static/Conda/conda-cheatsheet.pdf>`

.. _`conda cheat sheet`: https://conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf

Conda vs. pip vs. virtualenv 命令
----------------------------------

.. list-table:: Conda vs. pip vs. virtualenv 命令
   :header-rows: 1

   * - 任务
     - Conda 包和环境管理器命令
     - Pip 包管理器命令
     - virtualenv 环境管理器命令
   * - 安装包
     - ``conda install $PACKAGE_NAME``
     - ``pip install $PACKAGE_NAME``
     - X
   * - 升级包
     - ``conda update --name $ENVIRONMENT_NAME $PACKAGE_NAME``
     - ``pip install --upgrade $PACKAGE_NAME``
     - X
   * - 升级包管理器
     - ``conda update conda``
     - Linux/macOS: ``pip install -U pip`` 
       Win: ``python -m pip install -U pip``
     - X
   * - 卸载包
     - ``conda remove --name $ENVIRONMENT_NAME $PACKAGE_NAME``
     - ``pip uninstall $PACKAGE_NAME``
     - X
   * - 创建环境
     - ``conda create --name $ENVIRONMENT_NAME python``
     - X
     - ``cd $ENV_BASE_DIR; virtualenv $ENVIRONMENT_NAME``
   * - 激活环境
     - ``conda activate $ENVIRONMENT_NAME`` [#f1]_
     - X
     - ``source $ENV_BASE_DIR/$ENVIRONMENT_NAME/bin/activate``
   * - 去激活
     - ``conda deactivate``
     - X
     - ``deactivate``
   * - 搜索可用包
     - ``conda search $SEARCH_TERM``
     - ``pip search $SEARCH_TERM``
     - X
   * - 从指定源安装包
     - ``conda install --channel $URL $PACKAGE_NAME``
     - ``pip install --index-url $URL $PACKAGE_NAME``
     - X
   * - 已安装包列表
     - ``conda list --name $ENVIRONMENT_NAME``
     - ``pip list``
     - X
   * - 创建依赖文件
     - ``conda list --export``
     - ``pip freeze``
     - X
   * - 环境列表
     - ``conda info --envs``
     - X
     - 安装 virtualenv wrapper, 然后 ``lsvirtualenv``
   * - 安装其他包管理器
     - ``conda install pip``
     - ``pip install conda``
     - X
   * - 安装 Python
     - ``conda install python=x.x``
     - X
     - X
   * - 升级 Python
     - ``conda update python`` [#f2]_
     - X
     - X

.. [#f1] ``conda activate`` 适用于 conda 4.6版本及以上。 4.6之前的版本:
          
   * Windows: ``activate``
   * Linux and macOS: ``source activate``

.. [#f2] ``conda update python`` 适用于同个大版本的 Python 更新，比如 Python 2.x 更新到 Python 2.x 最新版本，
   或者 Python 3.x 更新到 Python 3.x 最新版本




