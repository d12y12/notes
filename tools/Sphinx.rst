.. Sphinx:

Sphinx
=======

Docstring
-----------

三种风格：

* `reStructuredText 风格 <http://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists>`_

  类::

     """
     类描述
     
     :param 属性: 属性的描述
     :type 属性: 属性的类型
     """

  函数::

     """
     函数描述

     :arg 属性: 参数的描述
     :type 属性: 参数的类型

     :return: 返回值的描述
     :rtype: 返回值的类型

     :raises 返回值: 生成器返回值描述
     Returns/Yields:
         类型: 返回值的描述/生成器返回值描述
      
     Raises:
         异常名称: 异常描述
     """
  

* `Google 风格 <http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`_

  类::

     """
     类描述
      
     Attributes:
         属性(类型): 属性的描述
     """

  函数::

     """
     函数描述

     Args:
         参数(类型): 参数的描述

     Returns/Yields:
         类型: 返回值的描述/生成器返回值描述
      
     Raises:
         异常名称: 异常描述
     """

* `Numpy 风格 <https://numpydoc.readthedocs.io/en/latest/format.html#>`_

  类::

     """
     类描述

     Parameters
     ----------
     参数 : 类型
         参数的描述
      
     Attributes
     ----------
     属性 : 类型
         属性的描述
     
     Methods
     -------
     函数(参数列表)
         函数描述，注意不要把 self 放入参数列表
     """

  函数::

     """
     函数描述

     Parameters
     ----------
     参数 : 类型
         参数的描述

     Returns/Yields
     ---------------
     返回值 : 类型
         返回值的描述
      
     Raises
     ------
     异常名称
         异常描述

     Examples
     --------
     范例描述
     
     >>> 范例

     Note
     ----
     注释内容

     See Also
     --------
     参考内容

     Warnings
     --------
     警告内容
     """

我推荐使用 `Napoleon 扩展`_ 来支持 Google/Numpy 风格，毕竟 reStructuredText 风格太难看。

简单比较一下 Google/Numpy 的区别，至于如何选择看个人喜好:

+----------+-------------+----------------+
|          | Google 风格 |   Numpy 风格   |
+==========+=============+================+
| 分段方式 | 缩进分段    | 连续下划线分段 |
+----------+-------------+----------------+
| 空间需求 | 横向空间    | 纵向空间       |
+----------+-------------+----------------+
| 方便阅读 | 短小精干型  | 长而精细型     |
+----------+-------------+----------------+

扩展
-----

Napoleon 扩展
~~~~~~~~~~~~~~

Napoleon 扩展可以让 Sphinx 支持 Google/Numpy 风格的 docstring 。

* 使能

  将 ``sphinx.ext.napoleon`` 添加到扩展列表::

     extensions = [
         'sphinx.ext.autodoc',
         'sphinx.ext.napoleon',
     ]

* 配置

  默认值::

     # Napoleon settings
     napoleon_google_docstring = True # 是否支持解析 google 风格
     napoleon_numpy_docstring = True  # 是否支持解析 numpy 风格
     napoleon_include_init_with_doc = False    # 构造函数( __init___ )是否放入文档
     napoleon_include_private_with_doc = False # 私有成员(如  _membername)是否放入文档
     napoleon_include_special_with_doc = True  # 内置成员(如  __membername__)是否放入文档
     napoleon_use_admonition_for_examples = False # True  使用 .. admonition:: 指令展示示例
                                                  # False 使用 .. rubric:: 指令展示示例
     napoleon_use_admonition_for_notes = False # True  使用 .. admonition:: 指令展示注释
                                               # False 使用 .. rubric:: 指令展示注释
     napoleon_use_admonition_for_references = False # True  使用 .. admonition:: 指令展示引用
                                                    # False 使用 .. rubric:: 指令展示引用
     napoleon_use_ivar = False # True  使用 :ivar: 角色展示变量
                               # False 使用 .. attribute:: 指令展示变量
     napoleon_use_param = True # True  对每一个函数变量使用 :param: 角色展示
                               # False 函数的所有变量使用一个 :parameters: 角色展示
     napoleon_use_rtype = True # True  使用 :rtype: 角色展示返回变量类型
                               # False 将返回值类型内联入返回值描述， 
                               #       如 :returns: *bool* -- True if successful, False otherwise

  一般来说，我们只需要使用一种，比如 ``numpy``::

     napoleon_google_docstring = False    
     napoleon_numpy_docstring = True

autosectionlabel 扩展
~~~~~~~~~~~~~~~~~~~~~~

autosectionlabel 扩展允许使用章节标题进行引用。

* 使能

  将 ``sphinx.ext.autosectionlabel`` 添加到扩展列表::

     extensions = [
         'sphinx.ext.autosectionlabel',
     ]

* 配置

  默认值::

     autosectionlabel_prefix_document = False # True  使用文档名称作为章节标题标签的前缀，
                                              #       例如 index:Introduction，意思是 index.rst 中的 Introduction 章节
                                              # False 不使用前缀
                                              # 这个配置的主要作用是避免不同文章使用相同的标题导致引用混乱
     autosectionlabel_maxdepth = None # 选择允许到几级标题生成自动标签，可以被引用
                                      # 例如设成 1，那么只有文章大标题(最高级)可以被引用
                                      # None 不使能此功能，所有级别标题都可引用


