原始直觉：If a function (problem) could be caculated by a program on Turing Machine, then the stete in this program is a abstract of some state in the method to solve the problem.

目的：给定外部状态之后，机械的确定出程序的内部状态以及转换关系。从内部状态生成外部状态是容易的，但是反向就有很多值得探讨的地方
主题：内容与形式
问题：图灵机的内部状态是纯粹的形式还是具有内容？
论点：图灵机的内部状态具有内容意义，并且这种意义对于设计程序是必要的。
论证：首先以正向的方向，分析几个具体的程序运行过程，表明内部状态是对一些外部状态的抽象。这个对应/意义是依赖于整个序列的/方法的/程序的。然后，以逆向方向，从外部状态序列中抽象出一些内部状态，从而构造出程序。
抽象：什么相关性下可以抽象？这依赖于这个问题的解决方法。即抽象的程度取决于方法的路径。
为何要辩护：内部状态不应该只是形式，而应该具有内容意义，否则我们人类的心灵、数学符号等都只是没有意义的形式。
PS：以下讨论均假设 TM 会停机


the *present outer state* of a TM is the present $(register,pointer)$
the *present inner state* of a TM is the present state of the TM.

the *general outer state space* of TM is the set of any tuple $(register,pointer)$ in the running of any program.
for a given program, the *outer state space* of this Truing Machine is the set of all the tuple $(register,pointer)$ in the running of the program with any 合法 input.

inner state and outer state
一般的，内部状态具有抽象性，和机器的状态没有直接对应。但在一个具体程序中，内部状态则由外部状态的确定而具有了内在的意义，而不再只是由关系确定的转换关系。当在设计程序中，设想如果有一个解决问题的程序，那么就可以从外部状态的抽象进而设计内部状态。
在一个程序中，内部状态能够对应到一定的外部状态，内部状态是对一些外部状态的抽象，这个抽象意义就是内容状态的意义

既然内部状态的意义依赖于程序/外部状态的完整序列，那么这个广泛的变化中，不变的是什么？
寻找到结构与外部状态序列之间的对应


问题，方法
问题是待解决的计算，方法是通过纸带与指针的移动和擦除实现的对问题的解决
有时一个程序可能不是解决某个问题，即不是某个方法，但仍然是一个过程，仍然具有一个外部状态序列
内部状态对应到：一些（外部状态，外部状态在全部状态序列中的位置）的集合/类
一个运行过程必然是一个线序，要划分出过程的不同成分，需要确定一个划分标准？
“外部状态在全部状态序列中的位置”可以用谓词进行刻画

当我们需要“移动到一端”时，我们能设计出“q1Rq”的指令给出一个循环，以抽象的完成移动，并给出一个跳出循环的条件。
使用循环和跳出循环的条件，来描述内部状态？
循环是唯一的抽象方式？
在图灵机中，抽象就是指循环
一个没有循环的程序，不具有抽象性

如何判断两个外部状态在同一个模式中？
首先依赖于整个序列

给出一个谓词，就能确定一个状态
优化程序就是将里面的谓词抽象，减少状态数

明确的，状态是和谓词对应的
谓词为真意味着，当前外部状态满足某个模式，并且这个外部状态在整个运行序列中满足某个模式

状态的意义依赖于具体的程序，进一步澄清，具体是如何依赖的？并从中发现一些不依赖具体程序的东西
局部结构与功能，以及这个局部在全局中的位置

我们确定了一些结构中状态的对应的谓词之后，在设计程序中，如果遇到这个谓词，我们就可以确定一个状态。
但由于程序是任意无限多的，无法将所有确定的谓词都列举出来。但是可以断言，每个内部状态都对应于某个谓词


一个外部状态序列，能够通过很多种内部状态结构来实现

Property.
(1) state is identify and 区别的 to other state in the space of $Register\times Pointer$
a state on the running of the program 对应到 a set of (register,pointer), we could find that there have some 内在的模式 on some subset of space of Machine.

(2) 所有带有循环的程序，都有一个无循环的展开，使得两个程序具有相同的输出

when we design a program, we need to decide when to create a new state and which state we are going to from present state.

the ordinary flow to design a program
(1) design a method for the problem in the general outer state space
(2) decide identify state on the progress of the method by some abstract
(3) decide some inner state to represent the abstract state set
(4) decide the transition relation of the inner state
(5) check every inner state is independent to each other in the outer state space
(6) run and debug the program

不可归约，独立于其它状态，所以需要确定出这样一个状态。状态之间具有区别，才能使之成为一个状态

核心问题：如何抽象出问题解决方法中的状态本体，如何区分出一个状态，关键是要确立一个状态，改区分的区分，该使用新状态的就创建新状态。要区分什么时候要用新状态。要明确什么状态在这个问题解决方法中是一个特殊的状态模式

一个内部状态上可以出现多个外部状态，所以对应关系并不是直接的。
