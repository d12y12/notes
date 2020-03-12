# Markdown

Markdown 是一种全文本格式，用来写作结构化文档。 Markdown 的语法全由一些符号所组成，
这些符号经过精挑细选，其作用一目了然。Markdown 的缺点在于没有标准，只有一个最初的格式描述，
CommonMark 在做标准化的事，但目前为止还没有如 reStructuredText 一样的标准。

- GitHub Flavored Markdown (GFM)

    由于 Markdown 没有明确的标准，所以存在各种味道( Flavored )的 Markdown ，
    简单地说就是各自增加的自己的一些语法或者渲染的方式不一样。

    GitHub 味的 Markdown 就是 GitHub 在 [CommonMark][CommonMark] 规格基础上，
    对语法格式和语义的定义，文档请见 [GitHub Flavored Markdown Spec][GitHub Flavored Markdown Spec] 。

> **注**： Sphinx 插件 recommonmark 支持使用 CommonMark 的 Markdown 语法，不支持 GFM ，所以本文中很多示例在 Sphinx 显示不正常。

## 生成目录

GFM 支持的目录方式如下:

    1. [Example](#example)
    2. [Example2](#example2)
    3. [Third Example](#third-example)
    4. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)
    5. [第五个中文例子](#第五个中文例子)

    这里是你的章节标题

    # Example
    # Example2
    # Third Example
    # [Fourth Example](http://www.fourthexample.com) 
    # 第五个中文例子

还有很多生成目录的工具，比如在 VSCode 里用 markdown-all-in-one 扩展。

## 标题

### 章节标题

类 `Atx` 形式，在行首插入1到6个 `#`，对应到标题1到6阶。
例如：

    # 这是一级标题
    
    ## 这是二级标题
    
    ###### 这是六级标题

> **注**:
>
> 1. 还有一种 `Setext` 形式，使用少于3个空格缩进的连续 `=` (一级标题)和 `-` (二级标题)，
>    任何数量的 `=` 和 `-` 都可以有效果， `-` 数量必须大于1个，单一的 `-` 会被处理成列表。
>    例如：
>
>           这是一级标题
>           ===========
>
>           这是二级标题
>           -----------
>
>    我个人建议不使用`Setext`形式，尽量使用`ATX`形式.
>
> 2. 此处我使用代码块来展示标题，为的是不让自动生成目录出错。。。

### 分隔线

你可以在一行中用3个以上的星号、减号、底线来建立一个分隔线( Thematic breaks )，行内不能有其他东西。
你也可以在星号或是减号中间插入空格。
例如：

    * * *
    
    ***
    
    *****
    
    - - -
    
    ---------------------------------------

下面就是一个分割线
***

## 段落和换行

### 段落

一个 Markdown 段落是由一个或多个连续的文本行组成，它的前后要有一个以上的空行(空行的定义是显示上看起来像是空的，
便会被视为空行。 比方说，若某一行只包含空格和制表符，则该行也会被视为空行)。 普通段落不该用空格或制表符来缩进。

### 换行

如果要换行，可以在行尾加2个以上空格( space )或者显示使用 `\`。
例如：

    朝辞白帝彩云间，  
    千里江陵一日还。\
    两岸猿声啼不住，  
    轻舟已过万重山。

朝辞白帝彩云间，  
千里江陵一日还。\
两岸猿声啼不住，  
轻舟已过万重山。

> **注**： 此处 HTML builder 可以正常输出换行， Latex PDF 只输出一行。

只使用回车是不会形成换行的。
例如：

    朝辞白帝彩云间，
    千里江陵一日还。
    两岸猿声啼不住，
    轻舟已过万重山。

朝辞白帝彩云间，
千里江陵一日还。
两岸猿声啼不住，
轻舟已过万重山。

## 代码

### 缩进代码块

要在 Markdown 中建立代码区块很简单，只要简单地缩进4个空格或是1个制表符就可以，
一个代码区块会一直持续到没有缩进的那一行(或是文件结尾。
例如：

    这是一段代码：

        def hello(name):
            print("Hello", name.title())

这是一段代码：

    def hello(name):
        print("Hello", name.title())

### 栅栏代码块

使用大于3个 `` ` `` 或 `~` ，将代码包围起来。
例如：

    ```python
    def hello(name):
        print("Hello", name.title())
    ```

```python
def hello(name):
    print("Hello", name.title())
```

GFM 支持的所有语言请参考 [GFM支持语言列表][GFM支持语言列表]。

### 内联代码段

使用1个或多个 `` ` `` 。
例如：

    `foo`

    ``foo ` bar``

    ` `` `

`foo`

``foo ` bar``

` `` `

## 引用

Markdown 标记区块引用是使用类似电子邮件中用 `>` 的引用方式。 如果你还熟悉在邮件中的引言部分，
你就知道怎么在Markdown文件中建立一个区块引用，那会看起来像是你自己先断好行，然后在每行的最前面加上 `>`：

    > 这个引用包含两个段落。
    >
    > 《早发白帝城》：
    > 朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。
    >
    > 《静夜思》：
    > 床前明月光，疑是地上霜。举头望明月，低头思故乡。

> 这个引用包含两个段落。
>
> 《早发白帝城》：
> 朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。
>
> 《静夜思》：
> 床前明月光，疑是地上霜。举头望明月，低头思故乡。

区块引用可以嵌套(例如：引用内的引用)，只要根据层次加上不同数量的 `>`：

    > 这是第一层引用。
    >
    > > 这是一个嵌套引用。
    >
    > 回到第一层引用

> 这是第一层引用。
>
> > 这是一个嵌套引用。
>
> 回到第一层引用

引用的区块内也可以使用其他的 Markdown 语法，包括标题、列表、代码区块等。
例如：

    >
    > 1. 这是第一行列表项。
    > 2. 这是第二行列表项。
    >
    > 给出一些例子代码：
    >
    >     return shell_exec("echo $input | markdown_script");

>
> 1. 这是第一行列表项。
> 2. 这是第二行列表项。
>
> 给出一些例子代码：
>
>     return shell_exec("echo $input | markdown_script");

## 列表

Markdown 支持有序列表和无序列表。

### 无序列表

无序列表使用`*`、`+`或是`-`作为列表标记。
例如：

    - 李白
    - 杜甫
    - 白居易

- 李白
- 杜甫
- 白居易

### 有序列表

有序列表则使用数字接着一个 `.` ，在列表标记上使用的数字并不会影响输出的结果。
例如：

    1. 李白
    2. 杜甫
    3. 白居易

1. 李白
2. 杜甫
3. 白居易

列表项目标记通常是放在最左边，但是其实也可以缩进，最多3个空格，项目标记后面则一定要接着至少一个空格或制表符。

列表项目可以包含多个段落，每个项目下的段落都必须缩进4个空格或是1个制表符。
例如：

    1. 这个列表包含两个段落。

        《早发白帝城》：

        朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。

    2. 《静夜思》：

        床前明月光，疑是地上霜。举头望明月，低头思故乡。

1. 这个列表包含两个段落。

    《早发白帝城》：

    朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。

2. 《静夜思》：

    床前明月光，疑是地上霜。举头望明月，低头思故乡。

如果要在列表项目内放进引用，那 `>` 就需要缩进。
例如：

    - 列表项包含一个引用区块:
        > 这个引用区块在列表内部。

- 列表项包含一个引用区块:
    > 这个引用区块在列表内部。

如果要放代码区块的话，该区块就需要缩进两次，也就是8个空格或是2个制表符。
例如：

    - 列表项包含一个代码区块：

            printf("hello")

- 列表项包含一个代码区块：

        printf("hello")

### 任务列表

**GFM 扩展项**，在列表项上增加了复选框。在列表标识(-，*，+)后加空格再加[ ]及1个空格，
[ ]中如果是空格则复选框未被选中，如为 `x` 则复选框被选中。
例如：

    - [ ] 吃饭
    - [x] 睡觉
    - [ ] 打豆豆

> **注**: 这里不展示了， 因为 recommonmark 不支持 GFM 扩展项。

## 表格

**GFM 扩展项**，并非所有 Markdown 都支持，我们以 GFM 为例。 一个列表包括表头，分隔符行，表数据。
例如：

    | 序号 | 日期      | 内容       |
    | ---- | --------- | ---------- |
    | 1    | 2020-2-17 | 文档初始化 |
    | 2    | 2020-2-18 | 文档完成   |

在分隔符行，可以使用`：`来定义对齐方式：

    | 对齐方式 | 语法  |
    | -------- | ----- |
    | 居中     | :---: |
    | 左对齐   | :---  |
    | 右对齐   | ---： |

> **注**: 这里不展示了， 因为 recommonmark 不支持 GFM 扩展项。

## 链接

### 普通链接

Markdown 支持两种形式的链接语法： 内联式和引用式两种形式。

不管是哪一种，链接文字都是用 [方括号] 来标记。

- 内联式

  要建立一个行内式的链接，只要在方块括号后面紧接着圆括号并插入网址链接即可，
  如果你还想要加上链接的 title 文字，只要在网址后面，用双引号把 title 文字包起来即可。
  例如：

      This is [an example](http://example.com/ "Title") inline link.

      [This link](http://example.net/) has no title attribute.

  > **注**： recommonmark 不支持 title 。

  如果你是要链接到同样主机的资源，你可以使用相对路径。
  例如：

      这只[熊猫](../_static/markdown/panda.png)来自中国。
  
  > **注**： 我不推荐这种方式，因为生成 PDF 可能无法使用。

- 引用式

  引用式的链接是在链接文字的括号后面再接上另一个方括号，
  而在第二个方括号里面要填入用以辨识链接的标记。
  例如：
  
      This is [an example][id] reference-style link.

  接着，在文件的任意处，你可以把这个标记的链接内容定义出来：

      [id]: http://example.com/  "Optional Title Here"

  链接的定义可以放在文件中的任何一个地方，我比较偏好把它放在文件最后面.

  > **注**： recommonmark 不支持 title 。

- 独立链接

  独立链接是指把链接直接放进 <> 尖括号内，如果支持自动链接扩展，可以不加 <>。
  例如：

      visit <https://cn.bing.com/>

      <d12y12@hotmail.com>

      如支持扩展， 可直接链接， 如 www.google.com

  > **注**： 此处 HTML 中 www.google.com 不是链接， Latex PDF 中 www.google.com 是链接

### 注脚

GFM 并不支持注脚( footnotes )， 但鉴于其作用， 还是把它写出来了， 注脚的定义与引用链接一样，
只是在[]方括号及引用定义内加上 `^` 。
例如:

    这是一个链接到谷歌的[^注脚]。

    [^注脚]: http://www.google.com

> 注：这里不展示了，因为 CommonMark 和 GFM 都不支持注脚。

## 图片

Markdown 使用一种和链接很相似的语法来标记图片，同样也允许两种样式：内联式和引用式。
到目前为止， Markdown 还没有办法指定图片的宽高。

- 内联式

  行内式的图片语法是一个惊叹号 `!`，接着一个方括号，里面放上图片的替代文字，
  接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上 选择性的 'title' 文字。
  例如：

      ![本地图片](/_static/markdown/apple_logo.png)

      ![网上图片](https://github.com/d12y12/notes/blob/master/_static/markdown/tesla_logo.jpg?raw=true "Optional title")

  ![本地图片](/_static/markdown/apple_logo.png)

  ![网上图片](https://github.com/d12y12/notes/blob/master/_static/markdown/tesla_logo.jpg?raw=true "Optional title")

  > **注**： recommonmark 不支持 title 。

- 引用式

  引用式的图片语法则长得像这样：

      ![Alt text][img_id]

  [img_id] 是图片参考的名称，图片参考的定义方式则和连结参考一样：

       [img_id]: /_static/markdown/tesla_logo.jpg  "Optional title attribute"

## 文字处理

### 强调

Markdown使用星号 `*` 和下划线 `_` 作为标记强调字词的符号

- 斜体

  被1个 `*` 或 `_` 包围的字词会被转成斜体，例如：

      - *single asterisks*
      - _single underscores_

  - *single asterisks*
  - _single underscores_

- 加粗

  用2个 `*` 或 `_` 包起来的话，则会被转成加粗，例如：

      - **double asterisks**
      - __double underscores__

  - **double asterisks**
  - __double underscores__

你可以随便用你喜欢的样式，唯一的限制是，你用什么符号开启标签，就要用什么符号结束。

强调也可以直接插在文字中间。
例如：

    un*frigging*believable

un*frigging*believable

但是如果你的 `*` 和 `_` 两边都有空白的话，它们就只会被当成普通的符号。
例如：

    a * foo bar*

a * foo bar*

如果要在文字前后直接插入普通的星号或底线，你可以用反斜线。
例如：

    \*this text is surrounded by literal asterisks\*

\*this text is surrounded by literal asterisks\*

### 删除线

**GFM 扩展项**，使用2个 `~`。
例如：

    ~~Hi~~ Hello, world!

> **注**: 这里不展示了， 因为 recommonmark 不支持 GFM 扩展项。

### 反斜杠转义

Markdown 可以利用反斜杠来插入一些在语法中有其它意义的符号，
Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

    \   反斜线
    `   反引号
    *   星号
    _   底线
    {}  花括号
    []  方括号
    ()  括弧
    #   井字号
    +   加号
    -   减号
    .   英文句点
    !   惊叹号

## 参考

- [GitHub Flavored Markdown Spec][GitHub Flavored Markdown Spec]
- [GFM支持语言列表][GFM支持语言列表]
- [CommonMark][CommonMark]
  
[GFM支持语言列表]: https://github.com/github/linguist/blob/master/lib/linguist/languages.yml "GFM支持语言列表"
[CommonMark]: https://spec.commonmark.org/ "CommonMark Spec"
[GitHub Flavored Markdown Spec]: https://github.github.com/gfm/ "GitHub Flavored Markdown Spec"
