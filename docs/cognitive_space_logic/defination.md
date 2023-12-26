## CSL
$\textsf{N}_\textsf{C}$ ： 概念名称的集合
$F$：原子体验的集合
$W$：对象的集合，对象被看作可能世界（泛对象）
$R$：对象上的二元关系
$I$：概念的解释
$V(C)$：概念 $C$ 所包含的对象的集合
$V(C\land D)$：概念 $C$ 与概念 $D$ 所包含的对象的交集
$V(C\lor D)$：概念 $C$ 与概念 $D$ 所包含的对象的并集
$I(C,\omega)$：概念 $C$ 在认识背景 $\omega$ 上的解释
$V(C\land D)$：概念 $C$ 和 $D$ 的交在认识背景 $\omega$ 上的解释
$V(C\lor D)$：概念 $C$ 和 $D$ 的并在认识背景 $\omega$ 上的解释

由于还是不太成熟的想法，我暂且称为认知空间逻辑（$Cognitive\ Space\ Logic,\ \mathbf{CSL}$），意义的解释还不清晰不充分，可以选择性略过并主要考虑形式系统。

给定原子概念集合 $\textsf{N}$ ，$\mathbf{CSL}$ 的语法定义如下，其中 $A\in \textsf{N}$
$C ::=A\ |\ \top\ |\ \bot\ |\ \neg C\ |\ C\land C\ |\ C\lor C\ |\ C\rightarrow C\ |\ \mathbf{T}C$
语法和命题模态逻辑是一样的
其中，合取读作概念的抽象，析取读作概念的概括，$\mathbf{T}C$ 读作可以想到概念 $C$ ，意思是在当前的意义理解中，想到了概念 $C$ ，或者概念 $C$ 的某个对象处于余跃状态。

在定义模型前，需要先定义概念的意义，或者说为概念指定对象。
（$\textbf{Cognitive Space}$）给定原子意义的集合 $F\cap\{\top,\bot\} = \emptyset$ ，意义（对象）的集合 $W \subseteq \mathcal{P}(F)$，一个认知空间是一个为概念赋予意义的函数 $V$ 定义如下：
$1）V(A) \neq \emptyset \subseteq W\ for\ any\ A\in \textsf{N}$ ，$V(\top) = W,V(\bot) = \emptyset$
$2）V(\neg C)=\{e\in W\ |\ \forall c\in V(C),c\cap e=\empty\}$
$3） V(C\land D)=\{ c\cap d\in W |\ (c,d)\in V(C) \times V(D) \}$
$4） V(C\lor D)=V(C) \cup V(D)$
$5）V(C\rightarrow D) \equiv_{def} V(\neg C \lor D)$ 缺乏一个直接定义
$6） V(\mathbf{T}C) = \{ e\in W\ |\ \exist c\in V(C)\ and\ \exist v\in W,s.t.eRv\ and\ c\supseteq v \}$
赋值函数 $V$ 为每个原子概念指定了一些意义（对象），对象被理解为具有一些意义的实体，对象可以是抽象观念也可以是具体实例。抽象概念的意义被指定为其组成概念的意义的交的集合，概括概念的意义被指定为其组成概念的意义的并的集合。通过抽象能得到已知对象以外的新对象，而概括无法得到新对象。
如果以单个对象为认识背景（可能世界），此时注意力集中到一个对象上

根据定义， $\land$ 的直观是乘法，$\lor$ 的直观是加法，类比引用数学性质有如下性质
德摩根律：$V(\neg (C\land D)) = V(\neg C\lor \neg D)$
以及 $V(\neg (C\lor D)) = V(\neg C\land \neg D)$
加法零元：$V(\bot \lor C) = V(C)$
加法逆元：$V(C \lor \neg C) = V(\top)$
加法交换律：$V(C\lor D) = V(D\lor C)$
加法结合律：$V((C\land D)\land E) = V(C\land (D\land E))$
（减法：$V(C-D) = V(C \lor \neg D)$，不符合直觉）
乘法零元：$V(\bot \land C) = \bot$
乘法没有幺元，没有逆元，没有除法
乘法交换律：$V(C\land D) = V(D\land C)$
乘法结合律：$V((C\lor D)\lor E) = V(C\lor (D\lor E))$
乘法分配律：$V(C\land (D\lor E)) = V((C\land D)\lor (C\land E))$
加法没有分配律：$V(C\lor (D\land E)) \subseteq V((C\lor D)\land (C\lor E))$
扩张：$V(C\land D)\supseteq V(C)\cap V(D)$ 特殊的 $V(C\land C)\supseteq V(C)$
逆元：$V(C \land \neg C) = V(\bot)$
封闭：$V(\top \land \top) = V(\top) = W$
意味着，可以用数学方法对概念进行计算。很像一个域但是乘法没有幺元，有限域加法

接下来分析算子的性质
$V(\mathbf{T}\neg C) \neq V(\neg \mathbf{T}C)$
$V(\mathbf{T}\bot) = \emptyset$，$V(\mathbf{T}\top) =\{e\in W\ |\ e不是死点\}$，
$V(\mathbf{T}(C\land D)) \subseteq V(\mathbf{T}C \land \mathbf{T}D)$
$V(\mathbf{T}(C\lor D)) = V(\mathbf{T}C \lor \mathbf{T}D)$
$V(\mathbf{T}(C\land(D\lor E))) = V(\mathbf{T}((C\land D)\lor(C\land E)))$
$V(\mathbf{T}(C\lor(D\land E))) \subseteq V(\mathbf{T}((C\lor D)\land(C\lor E)))$
$V(\mathbf{T}C) \subseteq V(\mathbf{T}(C\land C))$
$V(\mathbf{T}C) \subseteq V(\mathbf{T(C\lor D)})$
<!-- $V(\mathbf{T}) = V(\mathbf{T})$
$V(\mathbf{T}) = V(\mathbf{T})$ -->

对偶算子
$V(\mathbf{F}C) \equiv_{def} V(\neg \mathbf{T}\neg C)$

一个 $\mathbf{CSL}$ 的模型 $\mathcal{M}$是一个四元组，$\mathcal{M} = (V,W,R,I)$，其中 $V$ 是基于原子意义集合 $F$ 的认知空间，$W$ 是对象的集合，$R\subseteq W\times W$ 是对象上的二元关系，$I$ 将概念的意义限制在可能世界的对象上：
$1）I(A,\omega)=\{ c\in V(A)\ |\ c \supseteq \omega\}\subseteq V(A)$
$2）I(\neg C,\omega)=\{c\in V(\neg C)\ |\ c\supseteq \omega\} = \{e\in W\ |\ e\supseteq \omega\ and\ \forall c\in V(\neg C),c\cap e=\empty\}$ 补和约束不可交换
$3）I(C\land D,\omega)=\{ c\cap d\in W\ |\ (c,d)\in I(C,\omega) \times I(D,\omega) \}$
$4）I(C\lor D,\omega)=I(C,\omega)\cup I(D,\omega)$
$5）因为没有直接定义，所以不讨论关系$
$6）I(\mathbf{T}C,\omega)=\{c\in V(\mathbf{T}C)\ |\ c\supseteq \omega\}$
其中 $A \in \textsf{N}$ ， $C,D\in \mathbf{CSL}\ and\ \omega \in W$

之间的关系（事实关系，非定义，由定义决定好的关系）：
$\{ c\cap d\in W\ |\ (c,d)\in I(C,\omega) \times I(D,\omega) \}=\{ c\cap d\in W\ |\ c\cap d \supseteq \omega,(c,d)\in V(C) \times V(D) \}$
$I(C,\omega)\cup I(D,\omega)=\{ e\in V(C) \cup V(D)\ |\ e\supseteq \omega \}$
$I(\mathbf{T}C,\omega) = \{ e\in W\ |\ \exist c\in V(C)\ and\ \exist v\in W,s.t.eRv,e\supseteq \omega\ and\ c\supseteq v \}$

（$\mathbf{CSL}$的语义）对任意概念 $C\in \mathbf{CSL}$ 以及任意点模型 $\mathcal{M},\omega$，满足关系定义为
$\mathcal{M}, \omega \vDash \top$，$\mathcal{M}, \omega \nvDash \bot$
已经想到的语义：
$\mathcal{M}, \omega \vDash A \Longleftrightarrow I(A,\omega)\neq \emptyset$
$\mathcal{M},\omega \vDash \neg C \Longleftrightarrow \mathcal{M},\omega \nvDash C$
$\mathcal{M}, \omega \vDash (C \land D) \Longleftrightarrow \mathcal{M}, \omega \vDash C\ and\ \mathcal{M}, \omega \vDash D$
$\mathcal{M}, \omega \vDash (C \lor D) \Longleftrightarrow \mathcal{M}, \omega \vDash C\ or\ \mathcal{M}, \omega \vDash D$
$\mathcal{M},\omega \vDash C \rightarrow D \Longleftrightarrow \mathcal{M},\omega \nvDash C\ or\ \mathcal{M},\omega \vDash D$
可以想到的语义：
$\mathcal{M}, \omega \vDash \mathbf{T} C \Longleftrightarrow I(\mathbf{T}C,\omega) \neq \emptyset$
即$\mathcal{M}, \omega \vDash \mathbf{T} C \Longleftrightarrow there\ exist\ a\ e\ and\ a\ v\ where\ e\supseteq \omega,\ e R v\ and\ \exists c \in V(C) \ s.t. \ c\in I(C, v)$
即 $\mathcal{M}, \omega \vDash \mathbf{T} C \Longleftrightarrow there\ exist\ a\ e\ and\ a\ v\ where\ e\supseteq \omega,\ e R v\ and\ \mathcal{M}, v \vDash C$
严格可想到的语义：
$\mathcal{M}, \omega \vDash \mathbf{T^N} C \Longleftrightarrow there\ exist\ a\ v\ where\ \omega R v\ and\ \exists c \in V(C) \ s.t. \ c\in I(C, v)$
即 $\mathcal{M}, \omega \vDash \mathbf{T^N} C \Longleftrightarrow there\ exist\ a\ v\ where\ \omega R v\ and\ I(C,v)\neq \emptyset$
即 $\mathcal{M}, \omega \vDash \mathbf{T^N} C \Longleftrightarrow there\ exist\ a\ v\ where\ \omega R v\ and\ \mathcal{M}, v \vDash C $
宽泛可想到的语义：如果要求可能世界只能由概念的意义定义（不存在不在概念中的可能世界），并要求 $W$ 上的关系必须是概念之间的关系，即能够想到这种通达关系只能通过概念实现（语行、形式联系），而不能通过意义集合直接联系。定义概念上的二元关系为，存在一对意义之间的连通关系，则说一个概念可以想到另一个概念$(D,C)\in R^C$。
$\mathcal{M}, \omega \vDash \mathbf{T^W} C \Longleftrightarrow there\ exist\ a\ concept\ D\ where\ \mathcal{M},\omega \vDash D\ and\ (D,C)\in R^C$
显然的，严格可以想到则可以想到，可以想到则宽泛可以想到

这个逻辑是一种 $\exist\Diamond\exist$ 的打包，很弱，但是思维就是这么灵活。
是否可以用一长串 $\exist$ 来表示所有复杂的现象？

完全性是什么样的？读 Y. Wang 关于打包的判定性综合研究。

可视化，用超图表示概念关系

是否是 well-defined ？

满足推演定理。蕴涵式需要更深入的分析。

命题公理都成立

直接抽象为集合模型上的模态逻辑
附，证明这样的定义是唯一的。