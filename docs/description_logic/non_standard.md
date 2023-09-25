
## 标准系统与非标准系统
对描述逻辑是重要的，但是在模态逻辑中没有直接的对应

# 非标准系统

## 非标准表达

### 具体域
- 抽象域 (abstract domain)：论域 $\Delta^{\mathcal{I}}$ 。
- 具体域 (concrete domain)：一个具体域 $\mathcal{D}$ 是一个有序对 $(\Delta^{\mathcal{D}}, \Phi^{\mathcal{D}})$ ，其中 $\Delta^{\mathcal{D}}$ 是非空集合， $\Phi^{\mathcal{D}}$ 是由谓词名称构成的集合，并且对于 $n$ 元谓词 $P \in \Phi^{\mathcal{D}}$ ，有 $P^{\mathcal{D}} \subseteq (\Delta^{\mathcal{D}})^{n}$ 。

!!! Example
    具体域 $Q = (\mathbb{Q}, \Phi^{Q})$ ，其中 $\mathbb{Q}$ 是有理数域， $\Phi^{Q}$ 包含谓词：
    1）对任意 $P \in \{ <, \le, =, \ne, \ge, > \}$ 和任意 $q \in \mathbb{Q}$ 有一元谓词 $P_q$ ，且 $(P_q)^{Q} = \{q' \in \mathbb{Q} | q' P q \}$ 。
    2）二元谓词 $\{ <, \le, =, \ne, \ge, > \}$ 。
    3）三元谓词 $+$ ，且 $(+)^{Q} = \{(q_1, q_2, q_3) \in \mathbb{Q}^3 | q_1 + q_2 = q_3\}$ 。

将具体域 $\mathcal{D}$ 整合到 $\mathcal{ALC}$ 就得到 $\mathcal{ALC(D)}$
- 抽象特征：

### 作用映射

作用路径是指由一系列作用名称构成的路径，记作 $r_1 \circ r_2 \circ \cdots \circ r_n$。其解释如下：

- $(r_1 \circ r_2 \circ \cdots \circ r_n)^{\mathcal{I}} = \{ (d, e) \in \Delta^{\mathcal{I}} \times \Delta^{\mathcal{I}} | \exists e_1, e_2, \cdots, e_{n-1} \in \Delta^{\mathcal{I}} st. (d, e_1) \in r_{1}^{\mathcal{I}}, (e_1, e_2) \in r_{2}^{\mathcal{I}}, \cdots, (e_{n-1}, e) \in r_{n}^{\mathcal{I}} \}$


如果 $R$ 和 $S$ 是两个作用路径，那么 $(R \subseteq S), (R = S)$ 是合法概念描述。其解释如下：

- $(R \subseteq S)^{\mathcal{I}} = \{ d \in \Delta^{\mathcal{I}} | \forall e.(d, e) \in R^{\mathcal{I}}\ 蕴含\ (d, e) \in S^{\mathcal{I}} \}$ ，
- $(R = S)^{\mathcal{I}} =  \{ d \in \Delta^{\mathcal{I}} | \forall e.(d, e) \in R^{\mathcal{I}}\ 当且仅当\ (d, e) \in S^{\mathcal{I}} \}$ 。

!!! Example
    $Person \sqcap (child \circ friend \subseteq knows)$ 描述了知道他的孩子所有朋友的人。

## 非标准推理

### Least common subsumers and most specific concepts
- 从实例抽象出新概念

**定义 **在一个描述逻辑 $\mathcal{L}$ 中，一个概念描述 $E$ 是概念描述 $C_1, C_2, \cdots, C_n$ 的最小公共类当且仅当：

1. 对所有的 $i = 1, \cdots, n$ ，$C_i \sqsubseteq E$ ，
2. 如果存在 $E'$ 使得对所有的 $i = 1, \cdots, n ，C_i \sqsubseteq E'$ ，则 $E \sqsubseteq E'$ 。

**定义 **在一个描述逻辑 $\mathcal{L}$ 中，一个概念描述 $E$ 是个体实例 $a$ 的最具体抽象当且仅当：

1. $\mathcal{A} \models E(a)$ ，
2. 如果存在 $E'$ 使得 $\mathcal{A} \models E'(a)$ ，则 $E \sqsubseteq E'$ 。

### Matching and unification
- 对概念改造获得新概念

**定义 **（概念模式）用概念变量（通常是 $X, Y, etc.$）替换某些概念名称后得到的概念描述称为**概念模式**。
- Q：概念变量是作为概念名称的吗，变量如何在论域中解释？

**定义 **（统一问题）在一个描述逻辑 $\mathcal{L}$ 中，
