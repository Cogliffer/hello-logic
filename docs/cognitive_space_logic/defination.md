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
$C ::=A\ |\ \top\ |\ \bot\ |\ C\land C\ |\ C\lor C\ |\ \mathbf{T}C$

其中，合取读作概念的抽象，析取读作概念的概括，$\mathbf{T}C$ 读作可以想到概念 $C$ ，意思是在当前的意义理解中，想到了概念 $C$ ，或者概念 $C$ 的某个对象处于余跃状态。

在定义模型前，需要先定义概念的意义，或者说为概念指定对象。
（$\textbf{Cognitive Space}$）给定原子意义的集合 $F\cap\{\top,\bot\} = \emptyset$ ，意义（对象）的集合 $W \subseteq \mathcal{P}(F)$，一个认知空间是一个为概念赋予意义的函数 $V$ 定义如下：
$1) V(A) \neq \emptyset \subseteq W\ for\ any\ A\in \textsf{N}$
$2) V(C\land D)=\{ c\cap d\in W |\ (c,d)\in V(C) \times V(D) \}$
$3) V(C\lor D)=V(C) \cup V(D)$
$4) V(\mathbf{T}C) = \{ e\in W\ |\ \exist c\in V(C)\ and\ \exist v\in W,s.t.eRv\ and\ c\supseteq v \}$
赋值函数 $V$ 为每个原子概念指定了一些意义（对象），对象被理解为具有一些意义的实体，对象可以是抽象观念也可以是具体实例。抽象概念的意义被指定为其组成概念的意义的交的集合，概括概念的意义被指定为其组成概念的意义的并的集合。通过抽象能得到已知对象以外的新对象，而概括无法得到新对象。
如果以单个对象为认识背景（可能世界），此时注意力集中到一个对象上

一个 $\mathbf{CSL}$ 的模型 $\mathcal{M}$是一个四元组，$\mathcal{M} = (V,W,R,I)$，其中 $V$ 是基于原子意义集合 $F$ 的认知空间，$W$ 是对象的集合，$R\subseteq W\times W$ 是对象上的二元关系，$I$ 将概念的意义限制在可能世界的对象上：
$I(A,\omega)=\{ c\in V(A)\ |\ c \supseteq \omega\}\subseteq V(A)$
$I(C\land D,\omega)=\{ c\cap d\in \mathcal{P}(F)\ |\ (c,d)\in I(C,\omega) \times I(D,\omega) \}$
$I(C\lor D,\omega)=I(C,\omega)\cup I(D,\omega)$
$I(\mathbf{T}C,\omega)=\{c\in V(\mathbf{T}C)\ |\ c\supseteq \omega\}$
其中 $A \in \textsf{N}$ ， $C,D\in \mathbf{CSL}\ and\ \omega \in W$

之间的关系（事实关系，非定义，由定义决定好的关系）：
$\{ c\cap d\in \mathcal{P}(F)\ |\ (c,d)\in I(C,\omega) \times I(D,\omega) \}=\{ c\cap d\in \mathcal{P}(F)\ |\ c\cap d \supseteq \omega,(c,d)\in V(C) \times V(D) \}$
$I(C,\omega)\cup I(D,\omega)=\{ e\in V(C) \cup V(D)\ |\ e\supseteq \omega \}$
$I(\mathbf{T}C,\omega) = \{ e\in W\ |\ \exist c\in V(C)\ and\ \exist v\in W,s.t.eRv,e\supseteq \omega\ and\ c\supseteq v \}$

（$\mathbf{CSL}$的语义）对任意概念 $C\in \mathbf{CSL}$ 以及任意点模型 $\mathcal{M},\omega$，满足关系定义为
$\mathcal{M}, \omega \vDash \top$，$\mathcal{M}, \omega \nvDash \bot$
已经想到的语义：
$\mathcal{M}, \omega \vDash A \Longleftrightarrow I(A,\omega)\neq \emptyset$
$\mathcal{M}, \omega \vDash (C \land D) \Longleftrightarrow \mathcal{M}, \omega \vDash C\ and\ \mathcal{M}, \omega \vDash D$
$\mathcal{M}, \omega \vDash (C \lor D) \Longleftrightarrow \mathcal{M}, \omega \vDash C\ or\ \mathcal{M}, \omega \vDash D$
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

可视化，用超图表示概念关系

关于否定和蕴涵
$V(\neg C)=\{e\in W\ |\ \forall c\in V(C),c\cap e=\empty\}$
$V(\neg (C\land D)) = V(\neg C\lor \neg D)$
$V(\neg (C\lor D)) = V(\neg C\land \neg D)$
$I(\neg C,\omega)=\{c\in V(\neg C)\ |\ c\supseteq \omega\}$
$\mathcal{M},\omega \vDash \neg C \Longleftrightarrow \mathcal{M},\omega \nvDash C$
$C\rightarrow D \equiv_{def} \neg C \lor D$
$\mathcal{M},\omega \vDash C \rightarrow D \Longleftrightarrow \mathcal{M},\omega \nvDash C\ or\ \mathcal{M},\omega \vDash D$

是否是 well-defined ？

逻辑中还有很多细节没有考虑，