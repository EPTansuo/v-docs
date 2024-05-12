# 四、DPI-C机制 

## 1. DPI-C的介绍

DPI-C(Direct Programming Interface for C) 是允许SystemVerilog与C或C++代码交互的接口。虽然是SystemVerilog的内容，但是许多Verilog仿真器也支持。

## 2. VCS使用DPI-C示例

我们使用[VCS仿真框架搭建](VCS仿真框架搭建.md)一节中的示例，进行修改。

### 2.1 创建C文件

创建`csrc`文件夹，并在此文件夹下创建`dpi.c`文件：

```c
#include <svdpi.h>
#include <stdbool.h>


#define SIZE 3

//检测101
const char series[SIZE] = {1,0,1};

static int count = 0;
static char buf[SIZE] = { 0 };

void demo_difftest(char out){
        static diff_out_last=false; //存储上一次的结果
        bool diff_out = true;;
        if(count < SIZE)
                return;

        for(int i=0; i<SIZE; i++){
                if(buf[(count-SIZE+i)%SIZE] != series[i]){
                        diff_out = false;
                        break;
                }
        }
        if(diff_out_last != out)
                printf("\e[1;31m" "ERROR at count = %d" "\e[0m" "\n", count);
        diff_out_last = diff_out;

}

void catch_in(char in){
        buf[count%SIZE] = in;
        count++;
}

```

### 2.2 修改`tb/demo_tb`文件：

```systemverilog
`timescale 1ns/1ns

import "DPI-C" function void catch_in(byte);
import "DPI-C" function void demo_difftest(byte);

module demo_tb();
    reg clk;
    reg rst;
    reg input_;
    wire output_;

    demo demo_dut(
            .clk(clk),
            .rst(rst),
            .a(input_),
            .w(output_)
        );

     //生成波形文件
    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, demo_tb);
    end


    //生成时钟
    initial begin
        #5
        clk = 1'b0;
        forever #5 clk = ~clk;
    end

    //difftest
    always @(posedge clk) demo_difftest(output_);

    //生成输入测试信号
    initial begin
        forever begin 
                        #10 input_ = $random % 2;
                        catch_in(input_);
                end
    end

    //生成复位信号和设置仿真时长
    initial begin
        rst = 1;  //使能复位
        #15  rst = 0;
        #200 $finish;   //停止仿真
    end

endmodule
```

在上面的代码中，要尤其注意`import "DPI-C"`这两行以及对两个函数的使用部分。

### 2.3 修改Makefile文件

使得vcs支持SystemVerilog语法，只需在下面的语句最后添加`-sverilog`即可：

```makefile
VCS_FLAGS = -full64 -notice -kdb -lca -debug_acc+all \
                +dmptf +warn=all +libext+.v+v2k+acc -sverilog
```

将C文件添加到编译中，则添加：

```makefile
CSRC = $(shell find $(abspath $(./csrc)) -name "*.c")
```

同时，修改下面的代码，增加`$(CSRC)`,注意增加了两处：

```makefile
$(BIN): $(FILE_LIST_F) $(CSRC)
        vcs     $(INC_FLAGS) -l $(VCS_LOG) $(VCS_FLAGS)\
                -P $(VERDI_HOME)/share/PLI/VCS/$(PLATFORM)/novas.tab\
                $(VERDI_HOME)/share/PLI/VCS/$(PLATFORM)/pli.a\
                 -f $(FILE_LIST_F) $(CSRC)\
                -Mdir=$(OBJ_CSRC_DIR) -o $(BIN)
```

### 2.3尝试仿真

执行`make sim`， 如果正常的话，调用的c代码不会有任何报错的输出。

尝试注入错误，如将`vsrc/demo.v`中：

```verilog
assign w = (buffer == 3'b101);
```

改为：

```verilog
assign w = (buffer == 3'b111);
```

此时将会输出：

```
ERROR at count = 5
ERROR at count = 6
ERROR at count = 7
ERROR at count = 8
ERROR at count = 10
ERROR at count = 13
ERROR at count = 16
ERROR at count = 18
ERROR at count = 20
```

说明硬件描述代码有错误。

## 3. 总结

DPI-C其中一个很有用的地方就是用于芯片验证，在上面的例子中，就可以看到，我们用C语言实现了一个101序列检测器（假如可以确定C代码是正确的话），然后通过Verilog与C进行比较(difftest),就可以得出Verilog代码的逻辑是否正常。
