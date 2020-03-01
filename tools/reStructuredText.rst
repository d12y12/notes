.. reStructuredText:

reStructuredText
====================

reStructuredText_ 是 Docutils_ 和 Sphinx_ 使用的默认纯文本标记语言。

Docutils 提供基本的 reStructuredText 语法，而 Sphinx 则扩展此语法以支持其他功能。

.. _reStructuredText: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Sphinx: http://www.sphinx-doc.org/
.. _Docutils: http://docutils.sourceforge.net/

.. hint::

   本文所有展示效果只在 HTML 输出

标题和分隔线
------------

标题
~~~~~

定义标题的方式是在行的下面添加特殊符号，例如 “================”，但必须遵守一些原则：

1. 符号长度至少和文字行一样长, 更长也行
2. 相同级别必须使用统一的符号, 否则会被识别为更小的级别

通常没有专门的符号表示标题的等级，但是对于 Python 文档，可以这样认为:
   
* #， 及上划线表示部分
* \*， 及上划线表示章节
* =， 小章节
* -， 子章节
* ^， 子章节的子章节
* "， 段落

对于写其他文档，可以这样：

* =， 标题
* -， 章
* ~， 节
* #， 小节

.. note::

   这里为了避免目录生成出错，我就不举例了。

分隔线
~~~~~~~

连续4个以上的 ``-`` , ``~`` , ``=`` 等字符放在首尾空行之间。

:numref:`thematic_breaks` :

.. code-block::
   :caption: 分隔线
   :name: thematic_breaks

   ---------

.. only:: html or readthedocs 

   效果:

   ---------

段落和换行
----------

段落
~~~~~

段落是 reStructuredText 文档中最基础的部分，段落通过一个或者多个空行分隔开。左侧必须对齐(没有空格，或者有相同多的空格)。

普通的文本段落之间，还有块级元素之间，必须使用一个空行加以区分，否则会被 reStructuredText 折叠到上一行。

段落引述，使用缩进即可。

:numref:`quotes` :

.. code-block::
   :caption: 段落引述
   :name: quotes  

   这是个正常段落。

      这是个引述。
      
         这是个内嵌引述。

.. only:: html or readthedocs 

   效果:

   这是个正常段落。

      这是个引述。
            
         这是个内嵌引述。

换行
~~~~~

如果要换行，在行首显示使用 ``|`` 加一个空格, 只使用回车是不会形成换行的。

:numref:`line_breaks` :

.. code-block::
   :caption: 换行
   :name: line_breaks  
   
   | 《早发白帝城》
   | 朝辞白帝彩云间,
   | 千里江陵一日还。
   | 两岸猿声啼不住， 
   | 轻舟已过万重山。

   《黄鹤楼送孟浩然之广陵》
   故人西辞黄鹤楼，
   烟花三月下扬州。
   孤帆远影碧空尽，
   唯见长江天际流。

.. only:: html or readthedocs 

   效果:

   | 《早发白帝城》
   | 朝辞白帝彩云间,
   | 千里江陵一日还。
   | 两岸猿声啼不住， 
   | 轻舟已过万重山。

   《黄鹤楼送孟浩然之广陵》
   故人西辞黄鹤楼，
   烟花三月下扬州。
   孤帆远影碧空尽，
   唯见长江天际流。

代码
-----

缩进代码块
~~~~~~~~~~

在段落末尾添加 ``::`` ， 并且代码块需要与周围文本以空行分隔，代码的左侧必须缩进, 代码引用到没有缩进的行为止。

:numref:`code_with_double_colon` :

.. code-block::
   :caption: 缩进代码块
   :name: code_with_double_colon  

   这是一段代码::

      def hello(name):
          print("Hello", name.title())

.. only:: html or readthedocs 

   效果:

   这是一段代码::

      def hello(name):
          print("Hello", name.title())

这个 ``::`` 标记很优雅:

* 如果作为独立段落存在,则整段都不会出现在文档里.
* 如果前面有空白，则标记被移除.
* 如果前面是非空白，则标记被一个冒号取代.

栅栏代码块
~~~~~~~~~~~

使用 ``code`` 或 Sphinx 扩展的 ``code-block``，``highlight`` 指令。

:numref:`code_directive` :

.. code-block::
   :caption: code 指令
   :name: code_directive  

   .. code:: python
      :number-lines: 1

      def hello(name):
          print("Hello", name.title())

.. only:: html or readthedocs 

   效果：

   .. code:: python
      :number-lines: 1

      def hello(name):
          print("Hello", name.title())

:numref:`code_highlight_directive` :

.. code-block::
   :caption: code + highlight 指令
   :name: code_highlight_directive  

   .. highlight:: python
      :linenothreshold: 1
   
   .. code::

      def hello(name):
          print("Hello", name.title())
   
   .. highlight:: default

.. only:: html or readthedocs 
   
   效果：

   .. highlight:: python
      :linenothreshold: 1

   .. code::
      
      def hello(name):
         print("Hello", name.title())

   .. highlight:: default

:numref:`code_block_directive` :

.. code-block::
   :caption: code-block 指令
   :name: code_block_directive

   .. code-block:: python
      :linenos:

      def hello(name):
          print("Hello", name.title())

.. only:: html or readthedocs 
   
   效果：

   .. code-block:: python
      :linenos:

      def hello(name):
         print("Hello", name.title())

简单介绍一下这三个指令

* ``code``::

      .. code:: 高亮语言
         :number-lines: 第一行行号

* ``highlight``::

      .. highlight:: 高亮语言
         :linenothreshold: 此处给一个门限值，
                           当代码行数大于这个门限显示行数，
                           否则不显示

  这个指令是个全局命令。 如果这个命令选择的高亮语言失败了， ``code``  和  ``code-block`` 指令也不会高亮代码。
  如果一个文档只使用一种语言，可以在文档头部定义高亮语言，在文档的尾部设会默认。

* ``code-block``::

      .. code-block:: 高亮语言
         :linenos: 不带参数，有则显示行数，没有不显示
         :lineno-start: 第一行行号，这个会自动使能linenos
         :emphasize-lines: 强调某些行，如“3,5-8”，则第3行，第5到第8行斜体
         :caption: 代码块的标题，有这个才能编号
         :name: 代码块的名字，可以用来引用

所有支持的高亮语言，请参见 `Available lexers`_ 。

.. _Available lexers: https://pygments.org/docs/lexers/

内联代码段
~~~~~~~~~~

使用两个反引号 `````` 来包含，反引号前后要有空格。

:numref:`inline_code` :

.. code-block::
   :caption: 内联代码
   :name: inline_code

   这是一个内联 ``code`` 

.. only:: html or readthedocs 
   
   效果：

   这是一个内联 ``code`` 

包含源文件
~~~~~~~~~~

使用 ``literalinclude`` 指令::

   .. literalinclude:: 文件，通常使用相对路径，
                       如果使用绝对路径(以 ``/`` 开头)，则相对源文件顶级目录
      :language: 高亮语言
      :linenos: 是否显示行号
      :emphasize-lines: 强调某些行，如“3,5-8”，则第3行，第5到第8行斜体
      :encoding: 编码格式
      :lines: 指定哪些行被包含进文件，如“3,5-8”，则第3行，第5到第8行被包含
      :diff: 文件，展示两个文件的diff

:numref:`include_src_file` :

.. code-block::
   :caption: 包含源文件
   :name: include_src_file

      .. literalinclude:: ../_static/reStructuredText/example.py
         :language: python
         :linenos:
         :lines: 1-3

.. only:: html or readthedocs 
   
   效果：

   .. literalinclude:: ../_static/reStructuredText/example.py
      :language: python
      :linenos:
      :lines: 1-3


列表
----

无序列表
~~~~~~~~

无序列表使用 ``*`` 、 ``+`` 或是 ``-`` 作为列表标记。

:numref:`bulleted_list` :

.. code-block::
   :caption: 无序列表
   :name: bulleted_list

    * 李白
    * 杜甫
    * 白居易

.. only:: html or readthedocs 
   
   效果：

   * 李白
   * 杜甫
   * 白居易

列表可以嵌套，但是需跟父列表使用空行分隔。

:numref:`nested_list` :

.. code-block::
   :caption: 列表嵌套
   :name: nested_list

   * 这是一个列表

     * 嵌套列表
     * 子项

   * 父列表继续

.. only:: html or readthedocs 
   
   效果：

   * 这是一个列表

     * 嵌套列表
     * 子项

   * 父列表继续

有序列表
~~~~~~~~

有序列表则使用数字, 大小写字母，大小写罗马字母，或者 ``#`` (自动排序)接着一个 ``.`` ，
在列表标记上使用的数字必须递增，数字不必从一开始。

:numref:`numbered_list` :

.. code-block::
   :caption: 有序列表
   :name: numbered_list

   这个无法形成有序列表：

   1. 李白
   1. 杜甫
   1. 白居易

   下面的可以形成有序列表：

   #. 李白
   #. 杜甫
   #. 白居易

   1. 李白
   2. 杜甫
   3. 白居易
   
   a. 李白
   b. 杜甫
   c. 白居易
   
   3. 李白
   4. 杜甫
   5. 白居易

.. only:: html or readthedocs 
   
   效果：

   这个无法形成有序列表：

   1. 李白
   1. 杜甫
   1. 白居易

   下面的可以形成有序列表：

   #. 李白
   #. 杜甫
   #. 白居易

   1. 李白
   2. 杜甫
   3. 白居易
      
   a. 李白
   b. 杜甫
   c. 白居易

   3. 李白
   4. 杜甫
   5. 白居易

.. tip::

   推荐使用 ``#``  自动排序

任务列表
~~~~~~~~

reStructuredText 不支持生成带复选框的任务列表，但如下方式也能凑合看：

- [ ] 吃饭
- [x] 睡觉
- [ ] 打豆豆

定义列表
~~~~~~~~~

用来定义术语。

:numref:`definition_list` :

.. code-block::
   :caption: 定义列表
   :name: definition_list

   术语
      定义术语，必须缩进

      可以有多段组成
   
   *爬虫*
      一段自动抓取互联网信息的程序，从互联网上抓取对于我们有价值的信息。

.. only:: html or readthedocs 
   
   效果：

   术语
      定义术语，必须缩进

      可以有多段组成
      
   *爬虫*
      一段自动抓取互联网信息的程序，从互联网上抓取对于我们有价值的信息。

横向列表
~~~~~~~~

使用 ``hlist`` 指令::

   .. hlist::
      :columns: 每行几项

:numref:`horizontal_list` :

.. code-block::
   :caption: 横向列表
   :name:  horizontal_list

   .. hlist::
      :columns: 3

      * 这是
      * 一个
      * 横向
      * 列表
      * 每行三个

.. only:: html or readthedocs 

   效果：

   .. hlist::
      :columns: 3

      * 这是
      * 一个
      * 横向
      * 列表
      * 每行三个

.. attention::

   Latex PDF 不支持 ``hlist``

选项列表
~~~~~~~~

选项列表用来描述命令行或者程序的选项和描述。

:numref:`option_list` :

.. code-block::
   :caption: 选项列表
   :name: option_list

   -a         Output all.
   -b         Output both (this description is
              quite long).
   -c arg     Output just arg.
   --long     Output all day long.

   -p         This option has two paragraphs in the description.
              This is the first.

              This is the second.  Blank lines may be omitted between
              options (as above) or left in (as here and below).

   --very-long-option  A VMS-style option.  Note the adjustment for
                     the required two spaces.

   --an-even-longer-option
              The description can also start on the next line.

   -2, --two  This option has two variants.

   -f FILE, --file=FILE  These two options are synonyms; both have
                        arguments.

   /V         A VMS/DOS-style option.

.. only:: html or readthedocs 

   效果：

   -a         Output all.
   -b         Output both (this description is
            quite long).
   -c arg     Output just arg.
   --long     Output all day long.

   -p         This option has two paragraphs in the description.
            This is the first.

            This is the second.  Blank lines may be omitted between
            options (as above) or left in (as here and below).

   --very-long-option  A VMS-style option.  Note the adjustment for
                     the required two spaces.

   --an-even-longer-option
            The description can also start on the next line.

   -2, --two  This option has two variants.

   -f FILE, --file=FILE  These two options are synonyms; both have
                        arguments.

   /V         A VMS/DOS-style option.

表格
-----

简单表格
~~~~~~~~~

书写简单, 但有一些限制: 需要有多行，且第一列元素不能分行显示。

:numref:`simple_table_code` :

.. code-block::
   :caption: 简单表格
   :name: simple_table_code

   .. table:: Simple Table
      :name: simple_table

      =====  =====  ======
      Inputs        Output
      ------------  ------
      A      B      A or B
      =====  =====  ======
      False  False  False
      True   False  True
      False  True   True
      True   True   True
      =====  =====  ======

.. only:: html or readthedocs 

   效果：

   .. table:: Simple Table
      :name: simple_table

      =====  =====  ======
      Inputs        Output
      ------------  ------
      A      B      A or B
      =====  =====  ======
      False  False  False
      True   False  True
      False  True   True
      True   True   True
      =====  =====  ======

网格表格
~~~~~~~~

可以自定义表格的边框。 

:numref:`grid_table_code`

.. code-block::
   :caption: 网格表格
   :name: grid_table_code

   .. table:: Grid Table
      :name: grid_table
   
      +------------------------+------------+----------+----------+
      | Header row, column 1   | Header 2   | Header 3 | Header 4 |
      | (header rows optional) |            |          |          |
      +========================+============+==========+==========+
      | body row 1, column 1   | column 2   | column 3 | column 4 |
      +------------------------+------------+----------+----------+
      | body row 2             | Cells may span columns.          |
      +------------------------+------------+---------------------+
      | body row 3             | Cells may  | - Table cells       |
      +------------------------+ span rows. | - contain           |
      | body row 4             |            | - body elements.    |
      +------------------------+------------+---------------------+
      | body row 5             | Use the command ``ls | more``.   |
      +------------------------+------------+---------------------+

.. only:: html or readthedocs 

   效果：

   .. table:: Grid Table
      :name: grid_table

      +------------------------+------------+----------+----------+
      | Header row, column 1   | Header 2   | Header 3 | Header 4 |
      | (header rows optional) |            |          |          |
      +========================+============+==========+==========+
      | body row 1, column 1   | column 2   | column 3 | column 4 |
      +------------------------+------------+----------+----------+
      | body row 2             | Cells may span columns.          |
      +------------------------+------------+---------------------+
      | body row 3             | Cells may  | - Table cells       |
      +------------------------+ span rows. | - contain           |
      | body row 4             |            | - body elements.    |
      +------------------------+------------+---------------------+
      | body row 5             | Use the command ``ls | more``.   |
      +------------------------+------------+---------------------+

CSV表格
~~~~~~~

使用 ``csv-table`` 指令::

   .. csv-table:: 表名
      :header: 表头，如"Treat", "Quantity", "Description"
      :widths: 默认每列是同样宽度，这个选项可以指定每列相对宽度, 例如“15, 10, 30”
               也可以使用auto选项
      :width： 指定行宽度
      :header-rows: 指定表头行数，默认为0
      :stub-columns: 行标题列数, 默认为0
      :file：本地CSV文件, 使用相对路径
      :url: 网上CSV文件
      :delim: 分隔符，如“字符 | 制表符 | 空格”，默认为“，”

:numref:`csv_table_with_data` :

.. code-block::
   :caption: csv 表格 (数据)
   :name: csv_table_with_data

   .. csv-table:: Frozen Delights with data!
      :header: "Treat", "Quantity", "Description"
      :widths: 15, 10, 30
      :stub-columns: 1

      "Albatross", 2.99, "On a stick!"
      "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
      crunchy, now would it?"
      "Gannet Ripple", 1.99, "On a stick!"

.. only:: html or readthedocs 

   效果：

   .. csv-table:: Frozen Delights with data!
      :header: "Treat", "Quantity", "Description"
      :widths: 15, 10, 30
      :stub-columns: 1

      "Albatross", 2.99, "On a stick!"
      "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
      crunchy, now would it?"
      "Gannet Ripple", 1.99, "On a stick!"

加载文件:

:numref:`csv_table_with_file` :

.. code-block::
   :caption: csv 表格 (文件)
   :name: csv_table_with_file

   .. csv-table:: Frozen Delights with csv file!
      :file: ../_static/reStructuredText/example.csv
      :widths: 15, 10, 30
      :header-rows: 1

.. only:: html or readthedocs 

   效果：

   .. csv-table:: Frozen Delights with csv file!
      :file: ../_static/reStructuredText/example.csv
      :widths: 15, 10, 30
      :header-rows: 1

列表表格
~~~~~~~~

使用 ``list-table`` 指令::

   .. list-table:: 表名
      :widths: 默认每列是同样宽度，这个选项可以指定每列相对宽度, 例如“15, 10, 30”
               也可以使用auto选项
      :width： 指定行宽度
      :header-rows: 指定表头行数，默认为0
      :stub-columns: 行标题列数, 默认为0

:numref:`list_table` :

.. code-block::
   :caption: 列表表格
   :name: list_table

   .. _my_table:

   .. list-table:: Frozen Delights with list!
      :widths: 15 10 30
      :header-rows: 1

      * - Treat
      - Quantity
      - Description
      * - Albatross
      - 2.99
      - On a stick!
      * - Crunchy Frog
      - 1.49
      - If we took the bones out, it wouldn't be
         crunchy, now would it?
      * - Gannet Ripple
      - 1.99
      - On a stick!

.. only:: html or readthedocs 

   效果：

   .. _my_table:

   .. list-table:: Frozen Delights with list!
      :widths: 15 10 30
      :header-rows: 1

      * - Treat
        - Quantity
        - Description
      * - Albatross
        - 2.99
        - On a stick!
      * - Crunchy Frog
        - 1.49
        - If we took the bones out, it wouldn't be
          crunchy, now would it?
      * - Gannet Ripple
        - 1.99
        - On a stick!

链接
-----

.. _my-reference-label:

超链接
~~~~~~~

* 独立链接

  两种格式的独立链接会被生成自动链接，一个是邮件，另一个是以协议名比如 "http", "ftp", 
  "mailto", "telnet" 等开头的合法 URL。

  :numref:`individual_link` :

  .. code-block::
     :caption: 独立链接
     :name: individual_link

     | 访问 https://cn.bing.com/
     | 邮件 d12y12@hotmail.com
     | 这个 HTML 不会被转换，但 Latex PDF 会转换： www.google.com

  .. only:: html or readthedocs 

     效果：
     
     | 访问 https://cn.bing.com/
     | 邮件 d12y12@hotmail.com
     | 这个 HTML 不会被转换，但 Latex PDF 会转换： www.google.com

* 外部链接
  
  * 使用内联的方式， \`链接文本 <链接>\`_

    :numref:`external_link_inline` :

    .. code-block::
       :caption: 内联链接
       :name: external_link_inline

       使用 `必应 <https://cn.bing.com/>`_ 进行搜索。 

    .. only:: html or readthedocs 

       效果：

       使用 `必应 <https://cn.bing.com/>`_ 进行搜索。 

  * 使用引用的方式，```链接文本`_``, 在后面定义链接文本，当链接文本为单个词的时候，
    也可以不加反引号。

    :numref:`external_link_ref` :

    .. code-block::
       :caption: 引用外部链接
       :name: external_link_ref

       搜索只能使用 `微软 必应`_ 。

       .. _微软 必应: https://cn.bing.com/

       外部链接, 比如 Python_

       .. _Python: http://www.python.org/

    .. only:: html or readthedocs 

       效果：

       搜索只能使用 `微软 必应`_ 。

       .. _微软 必应: https://cn.bing.com/

       外部链接, 比如 Python_

       .. _Python: http://www.python.org/

* 内部链接
  
  内部链接可以被用来跳到文档指定位置。

  * 使用引用。

    :numref:`internal_link_ref` :

    .. code-block::
       :caption: 引用内部链接
       :name: internal_link_ref

       内部链接, 比如 点这里_

       .. _点这里: 

         点这里就到这里了。

    .. only:: html or readthedocs 

       效果：

       内部链接, 比如 点这里_

       .. _点这里: 

         点这里就到这里了。

  * 使用 ``ref`` 角色来跳到文档任意位置，Sphinx推荐。

    :numref:`internal_link_ref_role` :

    .. code-block::
       :caption: ref 角色内部链接
       :name: internal_link_ref_role

       .. _my-reference-label:

       超链接
       ~~~~~~~

       | 这里指向章节引用, 参见 :ref:`my-reference-label` 。
       | 这里指向图片引用, 参加 :ref:`my-figure` 。
       | 这里指向表格引用, 参加 :ref:`my_table`.

    .. only:: html or readthedocs 

       效果：
 
       | 这里指向章节引用, 参见 :ref:`my-reference-label` 。
       | 这里指向图片引用, 参加 :ref:`my-figure` 。
       | 这里指向表格引用, 参加 :ref:`my_table`. 
    
    .. note::

       为了避免目录混乱，这里并没有定义标题，my-reference-label定义在标题超链接

  * 使用自动产生链接，如章节标题, 注脚, 引文

    :numref:`internal_link_auto_generated` :

    .. code-block::
       :caption: 自动产生链接
       :name: internal_link_auto_generated

       | `超链接`_
       | `注脚4`_     Latex不支持
       | `CIT2002`_   Latex不支持
  
    .. only:: html or readthedocs 
       
       效果:

       | `超链接`_
       | `注脚4`_
       | `CIT2002`_

注脚
~~~~~

Sphinx 建议的使用方式是使用 ``[#name]_`` 来标记注脚，前后要有空格，
然后在文尾使用 ``rubric`` 加入注脚段，这个段不会进入文档结构。

:numref:`footnote_sphinx` :

.. code-block::
   :caption: Sphinx 注脚
   :name: footnote_sphinx

   到底是注脚[#f1]_还是脚注[#f2]_

   .. rubric:: 注脚

   .. [#f1] 这是注脚1
   .. [#f2] 这是注脚2

.. only:: html or readthedocs 
   
   效果:

   到底是注脚 [#f1]_ 还是脚注 [#f2]_ 

   .. rubric:: 注脚

   .. [#f1] 这是注脚1
   .. [#f2] 这是注脚2

当然也可以指定注脚号，或者不带名字自动编号注脚。

:numref:`footnote_more` :

.. code-block::
   :caption: 更多注脚
   :name: footnote_more

   | [3]_ 会是"3" (指定注脚号)
   | [#]_ 会是"5" (自动编号)
   | [#注脚4]_ 会是"4" (自动编号). 
   | 我们可以再次引用它 [#注脚4]_
   | 也可以这样引用它 注脚4_ (内部链接).   Latex不支持

   .. [3] 指定注脚号3
   .. [#注脚4] 第一这个在#f1和#f2之后，3被指定了，所以是4。这个序号是按定义注脚
      的顺序，不是按引用的顺序。这里注脚后面括号里的是只以注脚的方式被引用的地方。
   .. [#] 自动编号，所以是5 

.. only:: html or readthedocs 
   
   效果:

   | [3]_ will be "3" (指定注脚号)
   | [#]_ will be "5" (自动编号)
   | [#注脚4]_ will be "4" (自动编号). 
   | 我们可以再次引用它 [#注脚4]_
   | 也可以这样引用它 注脚4_ (内部链接).  

   .. [3] 指定注脚号3
   .. [#注脚4] 第一这个在#f1和#f2之后，3被指定了，所以是4。这个序号是按定义注脚
      的顺序，不是按引用的顺序。这里注脚后面括号里的是只以注脚的方式被引用的地方。
   .. [#] 自动编号，所以是5 

最后还有一种符号注脚, 但 Latex 不支持

:numref:`footnote_symbol` :

.. code-block::
   :caption: 符号注脚
   :name: footnote_symbol

   这是一个符号注脚引用: [*]_.

   .. [*] 符号注脚在这

.. only:: html or readthedocs 

   效果:

   这是一个符号注脚引用: [*]_.

   .. [*] 符号注脚在这

引文
~~~~~

引文与注脚类似，只是不用编号，使用 ``[name]_`` 来标记引文。

:numref:`citation` :

.. code-block::
   :caption: 引用文献
   :name: citation

   这是以一个引用文献: [CIT2002]_.

   .. [CIT2002] 这是引用文献，和注脚类似，只是不需要编号

.. only:: html or readthedocs 

   效果:

   这是以一个引用文献: [CIT2002]_.

   .. [CIT2002] 这是引用文献，和注脚类似，只是不需要编号

置换
~~~~~

置换能够替换文本、图片、链接、或者其它任何东西的组合。

* 文本置换
  
  :numref:`text_substitution` :

  .. code-block::
     :caption: 文本置换
     :name: text_substitution

     |RST|_ is a little annoying to type over and over, especially
     when writing about |RST| itself, and spelling out the
     bicapitalized word |RST| every time isn't really necessary for
     |RST| source readability.

     .. |RST| replace:: reStructuredText
     .. _RST: http://docutils.sourceforge.net/rst.html

  .. only:: html or readthedocs 

     效果:

     |RST|_ is a little annoying to type over and over, especially
     when writing about |RST| itself, and spelling out the
     bicapitalized word |RST| every time isn't really necessary for
     |RST| source readability.

     .. |RST| replace:: reStructuredText
     .. _RST: http://docutils.sourceforge.net/rst.html

* 图片置换

  :numref:`image_substitution` :

  .. code-block::
     :caption: 图片置换
     :name: image_substitution

     这只 |熊猫| 来自中国。

     .. |熊猫| image:: ../_static/reStructuredText/panda.png
        :height: 20
        :width: 20

  .. only:: html or readthedocs 

     效果:

     这只 |熊猫| 来自中国。

     .. |熊猫| image:: ../_static/reStructuredText/panda.png
        :height: 20
        :width: 20

* 默认置换
  
  Sphinx提供了三个默认置换。

  :numref:`default_substitution` :

  .. code-block::
     :caption: 默认置换
     :name: default_substitution

     | release |release|
     | version |version|
     | today   |today|

  .. only:: html or readthedocs 

     效果:

     | release |release|
     | version |version|
     | today   |today|

* 其他置换

  还可以置换对象，格式，模板，暂时用不上，以后再说。

文件链接
~~~~~~~~

* 引用文档

  使用 ``doc`` 角色，链接到文档引用，可以是绝对路径或者相对路径，注意这里是引用，不是文件。
  举个例子，如果引用 :doc:`Conda` 出现在文档 tools/contents， 那么引用路径为 tools/Conda 。
  例如我们想引用 Conda，它和我们在 tools/contents 里是同一级别，所以可以直接引用。

  :numref:`doc_role` :

  .. code-block::
     :caption: 引用文档
     :name: doc_role

     | 参考 :doc:`Conda <Conda>`  相对路径
     | 参考 :doc:`/tools/Conda`   绝对路径

  .. only:: html or readthedocs 

     效果:

     | 参考 :doc:`Conda <Conda>`  相对路径
     | 参考 :doc:`/tools/Conda`   绝对路径

* 下载文档

  使用 ``download`` 角色，用法同引用文档, 文件需要带扩展名。
  一般只有生成html页面支持下载，可以用 ``only`` 指令。
  
  :numref:`download_role` :

  .. code-block::
     :caption: 下载文档
     :name: download_role

      .. only:: html or readthedocs 

         下载 :download:`hello <../_static/reStructuredText/hello.txt>`

  .. only:: html or readthedocs 

     效果:

     下载 :download:`hello <../_static/reStructuredText/hello.txt>`

图片
----

内联式
~~~~~~~

* 使用 ``image`` 指令::

   .. image:: 文件，通常使用相对路径，
              如果使用绝对路径(以 ``/`` 开头)，则相对源文件顶级目录
              可以是URI
      :alt: 替代文字
      :height: 高度，如"100px", 当scale存在的时候要乘以scale，如scale为50%，则高度为"50px"
      :width: 宽度，如"200px", 当scale存在的时候要乘以scale，如scale为50%，则高度为"100px"
      :scale: 比例， 如"50 %", 这个"%"号可有可无，默认为100%
      :align: 对齐，"top", "middle", "bottom", "left", "center", "right"
      :target: 将图片指向一个链接，可以是URI，也可以是引用名。

  :numref:`image_directive` :

  .. code-block::
     :caption: image 指令
     :name: image_directive

      这是一个本地图片

      .. image:: ../_static/reStructuredText/apple_logo.png
         :alt: 本地图片
         :height: 200px
         :width: 200px
         :scale: 50
         :align: center
         :target: `图片`_
      
      这是一个网络图片

      .. image:: ../_static/reStructuredText/tesla_logo.jpg
         :alt: 网络图片
         :height: 200px
         :width: 200px
         :scale: 50
         :align: center

  .. only:: html or readthedocs 

     效果:

     这是一个本地图片

     .. image:: ../_static/reStructuredText/apple_logo.png
        :alt: 本地图片
        :height: 200px
        :width: 200px
        :scale: 50
        :align: center
        :target: `图片`_

     这是一个网络图片

     .. image:: ../_static/reStructuredText/tesla_logo.jpg
        :alt: 网络图片
        :height: 200px
        :width: 200px
        :scale: 50
        :align: center

* 使用 ``figure`` 指令，可以包含一个图片，图片标题，解释文字::

   .. figure:: 图片地址
      包含所有image选项
      :align: 对齐，"left", "center", "right"
      :figwidth: 可以是"image","长度"，"现有行长度的%百分比"，
                 "image"选项需要 Python Imaging Library，如果图片不存在或者库不存在，则此选项被忽略
         
                  +---------------------------+
                  |        figure             |
                  |                           |
                  |<------ figwidth --------->|
                  |                           |
                  |  +---------------------+  |
                  |  |     image           |  |
                  |  |                     |  |
                  |  |<--- width --------->|  |
                  |  +---------------------+  |
                  |                           |
                  |The figure's caption should|
                  |wrap at this width.        |
                  +---------------------------+

  :numref:`figure_directive` :

  .. code-block::
     :caption: figure 指令
     :name: figure_directive

      .. _my-figure:
      .. figure:: ../_static/reStructuredText/tesla_logo.jpg
         :scale: 50 %
         :alt: map to buried treasure
         :figwidth: 50 %
         :align: center

         This is the caption of the figure (a simple paragraph).

         The legend consists of all elements after the caption.  In this
         case, the legend consists of this paragraph and the following
         table:

         +---------------------------------------------------+-----------------------+
         | Symbol                                            | Meaning               |
         +===================================================+=======================+
         | .. image:: ../_static/reStructuredText/panda.png  | Panda                 |
         |    :scale: 25 %                                   |                       |
         +---------------------------------------------------+-----------------------+
         | .. image:: ../_static/reStructuredText/small.png  | Small                 |
         |    :scale: 25 %                                   |                       |
         +---------------------------------------------------+-----------------------+
         | .. image:: ../_static/reStructuredText/sad.png    | Sad                   |
         |    :scale: 25 %                                   |                       |
         +---------------------------------------------------+-----------------------+

  .. only:: html or readthedocs 

     效果:

     .. _my-figure:
     .. figure:: ../_static/reStructuredText/tesla_logo.jpg
        :scale: 50 %
        :alt: map to buried treasure
        :figwidth: 50 %
        :align: center

        This is the caption of the figure (a simple paragraph).

        The legend consists of all elements after the caption.  In this
        case, the legend consists of this paragraph and the following
        table:

        +---------------------------------------------------+-----------------------+
        | Symbol                                            | Meaning               |
        +===================================================+=======================+
        | .. image:: ../_static/reStructuredText/panda.png  | Panda                 |
        |    :scale: 25 %                                   |                       |
        +---------------------------------------------------+-----------------------+
        | .. image:: ../_static/reStructuredText/small.png  | Small                 |
        |    :scale: 25 %                                   |                       |
        +---------------------------------------------------+-----------------------+
        | .. image:: ../_static/reStructuredText/sad.png    | Sad                   |
        |    :scale: 25 %                                   |                       |
        +---------------------------------------------------+-----------------------+

引用式
~~~~~~~

参见 :numref:`image_substitution`


角色
-----

文字处理
~~~~~~~~

* 标记

  :numref:`text_markup` :

  .. code-block::
     :caption: 文字处理-标记
     :name: text_markup

     | 斜体 *italics*
     | 加粗 **bold**
     | 代码 ``code``

  .. only:: html or readthedocs 

     效果:

     | 斜体 *italics*
     | 加粗 **bold**
     | 代码 ``code``     

  .. attention::
   
     标记不能叠加

* 文本解释

  文本解释的语法为 ``:role:`text``` 或 ```text`:role:``, 功能是把文本(text)根据角色(role)进行解释。

  :numref:`text_roles` :

  .. code-block::
     :caption: 文字处理-解释
     :name: text_roles

     常用的文本处理角色：

     | 斜体: `text`:emphasis:
     | 粗体：`text`:strong:
     | 代码：`text`:code:
     | 下标：`text`:sub:
     | 上标：`text`:sup:

  .. only:: html or readthedocs 

     效果:

     | 斜体: `text`:emphasis:
     | 粗体：`text`:strong:
     | 代码：`text`:code:
     | 下标：`text`:sub:
     | 上标：`text`:sup:

*  自定义角色

  :numref:`customize_roles` :

  .. code-block::
     :caption: 文字处理-自定义
     :name: customize_roles

     .. role:: raw-html(raw)
        :format: html
     .. default-role:: raw-html

     `<U>` 下划线 `</U>` 、 `<S>` 删除线 `</S>`

     .. default-role:: title-reference

  .. only:: html or readthedocs 

     效果:

     .. role:: raw-html(raw)
        :format: html
     .. default-role:: raw-html

     `<U>` 下划线 `</U>` 、 `<S>` 删除线 `</S>`

     .. default-role:: title-reference     


用户界面交互
~~~~~~~~~~~~

* 用户界面互动，使用 ``:guilabel:`` 。 任何界面的标签都应该使用这个角色，包含
  按钮， 窗口标题，菜单，可选列表等等。

  :numref:`gui_lable` :

  .. code-block::
     :caption: 图形界面标签
     :name: gui_lable

     :guilabel:`Cancel`

  .. only:: html or readthedocs 

     效果:
  
     :guilabel:`Cancel`

* 菜单选择， 使用 ``:menuselection:`` 。 用来表示一连串的菜单选择项。

  :numref:`menu_selection` :

  .. code-block::
     :caption: 图形界面菜单选择
     :name: menu_selection

     :menuselection:`Start --> Programs`

  .. only:: html or readthedocs 

     效果:

    :menuselection:`Start --> Programs`

其他
~~~~~

* 缩写，使用 ``:abbr:``。

  :numref:`abbr_role` :

  .. code-block::
     :caption: 缩写
     :name: abbr_role

     :abbr:`LIFO (last-in, first-out)`.

  .. only:: html or readthedocs 

     效果:

     :abbr:`LIFO (last-in, first-out)`.

指令
----

提示
~~~~~

* 参见，使用 ``seealso`` 指令::

   .. seealso::

      这是一个参见事项。

  .. only:: html or readthedocs 

     效果:

     .. seealso::

        这是一个参见事项。 

* 注意，使用 ``attention`` 指令::

   .. attention::

      这是一个注意事项。

  .. only:: html or readthedocs 

     效果:

     .. attention::

        这是一个注意事项。

* 警告，使用 ``caution`` 指令::

   .. caution::

      这是一个警告事项。

  .. only:: html or readthedocs 

     效果:

     .. caution::

        这是一个警告事项。

* 危险，使用 ``danger`` 指令::

   .. danger::

      这是一个危险事项。

  .. only:: html or readthedocs 

     效果:

     .. danger::

        这是一个危险事项。

* 错误，使用 ``error`` 指令::

   .. error::

      这是一个错误事项。

  .. only:: html or readthedocs 

     效果:

     .. error::

        这是一个错误事项。

* 提示，使用 ``hint`` 指令::

   .. hint::

      这是一个提示事项。

  .. only:: html or readthedocs 

     效果:

     .. hint::

        这是一个提示事项。

* 重要，使用 ``important`` 指令::

   ..  important::

      这是一个重要事项。

  .. only:: html or readthedocs 

     效果:

     .. important::

        这是一个重要事项。

* 注释，使用 ``note`` 指令::

   .. note::

      这是一个注释事项。

  .. only:: html or readthedocs 

     效果:

     .. note::

        这是一个注释事项。

* 贴士，使用 ``tip`` 指令::

   .. tip::

      这是一个贴士事项。

  .. only:: html or readthedocs 

     效果:

     .. tip::

        这是一个贴士事项。

* 警告，使用 ``warning`` 指令::

   .. warning::

      这是一个警告事项。

  .. only:: html or readthedocs 

     效果:

     .. warning::

        这是一个警告事项。

* 定制，使用 ``admonition`` 指令::

   .. admonition:: 忠告名

      这是一个自定事项。

  .. only:: html or readthedocs 

     效果:

     .. admonition:: 忠告名

        这是一个自定事项。

* 版本添加， 使用 ``versionadded`` 指令::

   .. versionadded:: 2.5
      The *spam* parameter.

  .. only:: html or readthedocs 

     效果:

     .. versionadded:: 2.5
        The *spam* parameter.

* 版本修改， 使用 ``versionchanged`` 指令::

   .. versionchanged:: 2.5
      The *spam* parameter.

  .. only:: html or readthedocs 

     效果:

     .. versionchanged:: 2.5
        The *spam* parameter.

* 版本删除， 使用 ``deprecated`` 指令::

   .. deprecated:: 2.5
      Use :func:`spam` instead.

  .. only:: html or readthedocs 

     效果:

     .. deprecated:: 2.5
        Use :func:`spam` instead.

目录及目录树
~~~~~~~~~~~~

* 目录，使用 ``contents`` 指令::

   .. contents:: 目录名
      :depth: 目录深度，如“2”，只包含一级和二级标题
      :local: 如果存在，则只生成从contents指令开始的目录
              不存在，则生成整个文档的目录
      :backlinks: "entry" 生成返回目录条目的链接
                  "top" 生成返回目录本身的链接
                  "none" 不生成返回链接

* 目录树，使用 ``toctree`` 指令::

   .. toctree::
      :maxdepth: 最大深度，包含子文档
      :numbered: 是否给顶级目录章节编号
      :caption: 目录树名
      :titlesonly: 只给出子文档title
      :glob: 如果使用，则匹配文档名，
             如文档名使用"intro*",匹配所有以"intro"开头的文档，
             如"recipe/*", 则所有recip文件夹内的文档
      :reversed: 与glob同时使用，则反向选择glob匹配
      :hidden: 文档被包含在文档结构中，但是不会显示在目录树中

术语表
~~~~~~~

使用 ``glossary`` 指令包含一个定义列表。这些定义其后可被 ``term`` 引用。

:numref:`glossary` :

.. code-block::
   :caption: 术语表
   :name: glossary

   .. glossary::

      environment
         A structure where information about all documents under the root is
         saved, and used for cross-referencing.  The environment is pickled
         after the parsing stage, so that successive runs only need to read
         and parse new and changed documents.

      source directory
         The directory which, including its subdirectories, contains all
         source files for one Sphinx project.

   :term:`environment`

.. only:: html or readthedocs 

   效果:

   .. glossary::

      environment
         A structure where information about all documents under the root is
         saved, and used for cross-referencing.  The environment is pickled
         after the parsing stage, so that successive runs only need to read
         and parse new and changed documents.

      source directory
         The directory which, including its subdirectories, contains all
         source files for one Sphinx project.
      
   :term:`environment`

数学
~~~~~

使用 ``math`` 指令

:numref:`math_1` :

.. code-block::
   :caption: 数学 1
   :name: math_1

   .. math::
      :nowrap:

      \begin{eqnarray}
         y    & = & ax^2 + bx + c \\
         f(x) & = & x^2 + 2xy + y^2
      \end{eqnarray}

.. only:: html or readthedocs 

   效果:

   .. math::
      :nowrap:

      \begin{eqnarray}
         y    & = & ax^2 + bx + c \\
         f(x) & = & x^2 + 2xy + y^2
      \end{eqnarray}

:numref:`math_2` :

.. code-block::
   :caption: 数学 2
   :name: math_2

   .. math::

      (a + b)^2 = a^2 + 2ab + b^2

      (a - b)^2 = a^2 - 2ab + b^2

.. only:: html or readthedocs 

   效果:

   .. math::

      (a + b)^2 = a^2 + 2ab + b^2

      (a - b)^2 = a^2 - 2ab + b^2

:numref:`math_3` :

.. code-block::
   :caption: 数学 3
   :name: math_3

   .. math::

      (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2
   
   .. math:: (a + b)^2 = a^2 + 2ab + b^2

.. only:: html or readthedocs 

   效果:

   .. math:: 

         (a + b)^2  &=  (a + b)(a + b) \\
               &=  a^2 + 2ab + b^2

   .. math:: (a + b)^2 = a^2 + 2ab + b^2

:numref:`math_4` :

.. code-block::
   :caption: 数学 4
   :name: math_4

   .. math::

      α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)

.. only:: html or readthedocs 

   效果:

   .. math::

      α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)

关于如何写数学表达式，参见 AMS-LaTeX_

.. _AMS-LaTeX: https://www.ams.org/publications/authors/tex/amslatex

排版
~~~~~~

* 主题， 独立于文档大纲的章节，只可以包含一个章节，在无缩进的情况下使用 ``topic`` 指令。

  :numref:`topic_directive` :

  .. code-block::
     :caption: 主题指令
     :name: topic_directive

     .. topic:: Topic Title

        Subsequent indented lines comprise
        the body of the topic, and are
        interpreted as body elements.
  
.. only:: html or readthedocs 

   效果:

   .. topic:: Topic Title

      Subsequent indented lines comprise
      the body of the topic, and are
      interpreted as body elements.

* 侧边栏，在无缩进的情况下使用 ``sidebar`` 指令。

  :numref:`sidebar_directive` :

  .. code-block::
     :caption: 侧边栏指令
     :name: sidebar_directive

     .. sidebar:: Sidebar Title
        :subtitle: Optional Sidebar Subtitle

        Subsequent indented lines comprise
        the body of the sidebar, and are
        interpreted as body elements.

.. only:: html or readthedocs 

   效果:

   .. sidebar:: Sidebar Title
      :subtitle: Optional Sidebar Subtitle

      Subsequent indented lines comprise
      the body of the sidebar, and are
      interpreted as body elements.

注释
-----

任何以 ``..`` 标记开始，但不使用任何指令结构的文本，都视为注释::

   .. 这是一个注释。你看不到。

.. 这是一个注释你。看不到。

可以通过缩进产生多行注释::

   .. 
      你还是看不到。
      看不到。。。

      看不到。。。

.. 
      你还是看不到。
      看不到。。。

      看不到。。。

现在你能看到了，但这不是注释了。

参考
----

#. `reStructuredText Primer <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
#. `reStructuredText Directives <http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_
#. `docutils Directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_
#. `docutils rst reference <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext>`_
#. `The Docutils Document Tree <https://docutils.sourceforge.io/docs/ref/doctree.html>`_
