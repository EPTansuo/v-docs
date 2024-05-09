# 二、VCS仿真框架搭建

华工微电子学院”Verilog HDL“这门课的贺老师推荐使用VCS进行仿真，为与课程内容契合，故在此讲解其仿真框架的搭建。同时VCS相比于iverilog，仿真速度更快，支持`DPI-C`，在后面的门级仿真中也支持导入sdf标准延迟文件。

为了方便仿真，在此使用了[make](https://www.gnu.org/software/make/)工具。如果你不知道make是什么，可上网查询。

## 1. 克隆代码

使用make来进行仿真，需要写一个`Makefile`文件，不过我已经写好了，并上传到了github仓库中：[https://github.com/EPTansuo/vcs_template](https://github.com/EPTansuo/vcs_template)。

将仓库克隆到服务器上，你应该可以看到如下的目录结构：

```
├── Makefile
├── README.md
├── tb
│   └── demo_tb.v
└── vsrc
    └── demo.v
```

如果你想编译并仿真，只需执行即可:

```shell
make sim
```

仿真后，示例工程会生成`build`文件夹，生成的波形文件便在其中。

你可以将`tb`和`vsrc`目录下的文件替换为自己的verilog代码，尝试进行仿真。

## 2. 进一步尝试

1. 如果你想在本地编写代码，并在本地执行`make remote_sim`，即可实现在服务器上仿真，并把仿真结果拉取到本地，如何进行？(学习Makefile，并了解rsync，你就可以做到这一点。)

2. 示例代码中使用了`$dumpfile("wave.vcd")`来生成波形，但是vcd文件没有进行压缩，当dump波形时间长，信号量多的情况下，会导致波形文件占用很多的磁盘空间，而fsdb波形文件就会好很多，那如何使用fsdb波形文件代替vcd文件呢？
3. 如何使用vscode进行远程开发呢？如何调用verdi来联合仿真呢…… 





