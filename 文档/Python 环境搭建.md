#资料

python 官网：<https://www.python.org/>

网友整理的学习资料：[单击访问](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

官网上挂在的Python`2.7.12`和`3.5.2`两个版本。

我自己一直使用的`Python2.7.12`，Python3发布已经有8年之久。但是目前Linux的发行版里面内置的Python版本大都是`2.7`。

#python的使用方向

##Web方向

有很多优秀的Python web框架可供驱使。我自己使用[Django]("https://www.djangoproject.com/")，Django通过Pip安装还是很简单的，后面的文章说如何安装Django。

##大数据方向

Python 同样有很多很优秀的用于科学计算的包。

##网络采集（数据爬虫）

得力于Python的包的众多，有很多优秀的爬虫框架也就应运而生，目前我接触到的爬虫框架是：[Scrapy]("https://scrapy.org/")。

Scrapy的中文文档手册：<http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html>

#Windows下配置Python开发环境

首先从官方网站下载Python的`msi`安装包，记得安装过程中要安装`pip`，这是Python的一个包管理器。
然后看看安装程序是否将Python.exe添加到了path，接下来就是一路Next了。

![python icon](http://www.liaoxuefeng.com/files/attachments/0014222393965540081463bf8a9499094bdda24b6fdf2d6000)

好了，运行`CMD`，直接输入Python。可以看到如下的内容了:

![python icon](http://www.liaoxuefeng.com/files/attachments/0013868165417047ec57a2e466e4861a525d106e0b7e6b6000/0)

到这里Python的安装也就完成了。

#Linux/Mac下的Python

一般情况下，市面上流行的 Linux发行版，都是自带了`Python 2.7`的，Mac也是一样。我只需要直接使用就可以了。

若是需要对本地的Python进行升级，可以通过系统自带的软件包管理器去安装，这样还可以自动解决所有的依赖问题。

例如：Ubuntu内置的`apt-get`，CentOs内置的`yum`，Mac下推荐安装`brew`
