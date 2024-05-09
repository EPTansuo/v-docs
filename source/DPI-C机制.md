# 四、DPI-C机制 

## DPI-C的介绍

DPI-C(Direct Programming Interface for C) 是允许SystemVerilog与C或C++代码交互的接口。虽然是SystemVerilog的内容，但是许多Verilog仿真器也支持。

## VCS使用DPI-C示例

我们使用[VCS仿真框架搭建](VCS仿真框架搭建.html)一节中的示例，进行修改。

首先，需要修改`Makefile`文件，使得vcs支持SystemVerilog语法，只需在下面添加`-sverilog`即可：

```makefile
VCS_FLAGS = -full64 -notice -kdb -lca -debug_acc+all \
                +dmptf +warn=all +libext+.v+v2k+acc -sverilog
```

