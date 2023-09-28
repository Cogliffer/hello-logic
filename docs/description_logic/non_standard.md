# 5. 非标准系统

之前的表达与都在模态逻辑中有直接对应，称为标准系统，而在知识库的应用中，描述逻辑发展出了很多重要的非标准系统，但是在模态逻辑中没有直接的对应。

## 5.1 非标准表达

### 5.1.1 具体域
- 抽象域 (abstract domain)：论域 $\Delta^{\mathcal{I}}$ 。
- 具体域 (concrete domain)：一个具体域 $\mathcal{D}$ 是一个有序对 $(\Delta^{\mathcal{D}}, \Phi^{\mathcal{D}})$ ，其中 $\Delta^{\mathcal{D}}$ 是非空集合， $\Phi^{\mathcal{D}}$ 是由谓词名称构成的集合，并且对于 $n$ 元谓词 $P \in \Phi^{\mathcal{D}}$ ，有 $P^{\mathcal{D}} \subseteq (\Delta^{\mathcal{D}})^{n}$ 。

!!! Example
    具体域 $Q = (\mathbb{Q}, \Phi^{Q})$ ，其中 $\mathbb{Q}$ 是有理数域， $\Phi^{Q}$ 包含谓词：
    1）对任意 $P \in \{ <, \le, =, \ne, \ge, > \}$ 和任意 $q \in \mathbb{Q}$ 有一元谓词 $P_q$ ，且 $(P_q)^{Q} = \{q' \in \mathbb{Q} | q' P q \}$ 。
    2）二元谓词 $\{ <, \le, =, \ne, \ge, > \}$ 。
    3）三元谓词 $+$ ，且 $(+)^{Q} = \{(q_1, q_2, q_3) \in \mathbb{Q}^3 | q_1 + q_2 = q_3\}$ 。

将具体域 $\mathcal{D}$ 整合到 $\mathcal{ALC}$ 就得到 $\mathcal{ALC(D)}$

- 抽象特征：$g^{\mathcal{I}} : \Delta^{\mathcal{I}} \rightarrow \Delta^{\mathcal{I}}$
- 具体特征：$h^{\mathcal{I}} : \Delta^{\mathcal{I}} \rightarrow \Delta^{\mathcal{D}}$
- 谓词约束：$P(u_1, u_2, \cdots, u_n)$ ，其中 $u_i$ 是任意多个抽象特征和一个具体特征的复合，设 $u = g_1 \circ g_2 \cdots \circ g_k \circ h$ ，则 $u(d)^{\mathcal{I}} = h^{\mathcal{I}}\Big( g_{k}^{\mathcal{I}}\big( g_{k-1}^{\mathcal{I}} \cdots (g_1^{\mathcal{I}}(d)) \big) \Big), d \in \Delta^{\mathcal{I}}$ 。其解释定义如下：

$$
\begin{align}
    & P(u_1, u_2, \cdots, u_n)^{\mathcal{I}} = \{ d \in \Delta^{\mathcal{I}}\ |\ \exists x_1, x_2,\cdots,x_n \in \Delta^{\mathcal{D}}\ 使得 \\
    & \qquad \qquad \qquad \qquad \qquad  u_i(d)^{\mathcal{I}} = x_i\ (1 \le i \le n)\ 并且\ (x_1,x_2,\cdots,x_n) \in P^{\mathcal{I}} \}
\end{align}
$$

!!! Example
    在 $\mathcal{ALC}(Q)$ 中：

    $\bullet$ “ 青少年是 10 - 19 岁之间的人 ” 可以表示为： $Teenager \equiv Human\ \sqcap >_{10} (age)\ \sqcap <_{19} (age)$ 。

    $\bullet$ “ 所有人的年龄都比他父母的年龄小 ” 可以表示为： $\top \sqsubseteq\ ( <(age, mother \circ age)\ \sqcap <(age, father \circ age) )$ 。

### 5.1.2 作用映射

作用路径是指由一系列作用名称构成的路径，记作 $r_1 \circ r_2 \circ \cdots \circ r_n$。其解释如下：

$$
\begin{align}
    & (r_1 \circ r_2 \circ \cdots \circ r_n)^{\mathcal{I}} = \{ (d, e) \in \Delta^{\mathcal{I}} \times \Delta^{\mathcal{I}} | \exists e_1, e_2, \cdots, e_{n-1} \in \Delta^{\mathcal{I}} ,使得\\
    & \qquad \qquad \qquad \qquad \qquad (d, e_1) \in r_{1}^{\mathcal{I}}, (e_1, e_2) \in r_{2}^{\mathcal{I}}, \cdots, (e_{n-1}, e) \in r_{n}^{\mathcal{I}} \}
\end{align}
$$


如果 $R$ 和 $S$ 是两个作用路径，那么 $(R \subseteq S), (R = S)$ 是合法概念描述。其解释如下：

- $(R \subseteq S)^{\mathcal{I}} = \{ d \in \Delta^{\mathcal{I}} | \forall e.(d, e) \in R^{\mathcal{I}}\ 蕴含\ (d, e) \in S^{\mathcal{I}} \}$ ，
- $(R = S)^{\mathcal{I}} =  \{ d \in \Delta^{\mathcal{I}} | \forall e.(d, e) \in R^{\mathcal{I}}\ 当且仅当\ (d, e) \in S^{\mathcal{I}} \}$ 。

!!! Example
    $Person \sqcap (child \circ friend \subseteq knows)$ 描述了知道他的孩子所有朋友的人。

## 5.2 非标准推理

### 5.2.1 从实例抽象出新概念

**定义（Least common subsumers，lcs）**在一个描述逻辑 $\mathcal{L}$ 中，一个概念描述 $E$ 是概念描述 $C_1, C_2, \cdots, C_n$ 的 $lcs$ 当且仅当：

1. 对所有的 $i = 1, \cdots, n$ ，$C_i \sqsubseteq E$ ，
2. 如果存在 $E'$ 使得对所有的 $i = 1, \cdots, n ，C_i \sqsubseteq E'$ ，则 $E \sqsubseteq E'$ 。

**定义（Most specific concepts，msc）**在一个描述逻辑 $\mathcal{L}$ 中，一个概念描述 $E$ 是个体实例 $a$ 的 $msc$ 当且仅当：

1. $\mathcal{A} \models E(a)$ ，
2. 如果存在 $E'$ 使得 $\mathcal{A} \models E'(a)$ ，则 $E \sqsubseteq E'$ 。

!!! Example
    初始知识库 $K = (TBox,ABox)$ ：

    $\bullet$ $TBox : Man \equiv Human\ \sqcap Male, Woman \equiv Human\ \sqcap Famale$

    $\bullet\ ABox : Man(m),Woman(w),Man(m'),Woman(w'),child(m,w'),child(w,m')$

    $\bullet\ msc : Man\ \sqcup \exists child.Woman,\ Woman\ \sqcup \exists child.Man$

    $\bullet\ lcs : Parent \equiv Human\ \sqcup \exists child.Human$
### 5.2.2 基于 $TBox$ 重写概念（an instance of Rewriting）

!!! Example
    基于 $TBox : Woman \equiv Person\ \sqcap Female$

    重写概念描述 $Person\ \sqcap \forall child.Famale\ \sqcap \exists child.\top\ \sqcap \forall child.Person$ 得：

    $Parent\ \sqcap \forall child.Woman$

### 5.2.3 匹配（matching）

**定义（概念模型）**用概念变量（通常是 $X, Y, etc.$）替换某些概念名称后得到的概念描述称为概念模型。

!!! Example
    $D := P\ \sqcap X\ \sqcap \forall r.(Y\ \sqcap \forall r.X)$ 是一个以 $X,Y$ 为变量的概念模型。通过替换 $\sigma := (X \rightarrow Q, Y \rightarrow \forall r.P)$ 可以得到 $\sigma(D) = P\ \sqcap Q\ \sqcap \forall r.(\forall r.P\ \sqcap \forall r.Q)$ 。匹配就是在一个 $DL\ \mathcal{L}$ 中寻找所有使 $D^{\mathcal{I}}$ 不为空的 $\sigma$ 。

!!! Example
    寻找最接近的概念定义（approximation）：当一个 $DL\ \mathcal{L}_1$ 中的概念描述 $C_1$ 需要用另一个 $DL\ \mathcal{L}_2$ 中的概念描述 $C_2$ 来表达时，如果 $\mathcal{L}_1$ 比 $\mathcal{L}_2$ 表达能力更强，那么 $C_1$ 可能难以被 $C_2$ 表达，但是可以用 $\mathcal{L}_2$ 中的概念描述给出最近似的。一种可行的方法是先构造一个 $C_1$ 的概念模型，然后在 $\mathcal{L}_2$ 中匹配这个模型。

### 5.2.4 统一（unification）

!!! Example
    $C_1 \equiv \forall child.\forall child.Rich \sqcap \forall child.Rmr,\ C_2 \equiv Acr \sqcap \forall child.Acr \sqcap \forall child.\forall spouse.Rich$ 

    $D_1(X) := \forall child.\forall child.Rich \sqcap \forall child.X,\ D_2(Y) := Y \sqcap \forall child.Y \sqcap \forall child.\forall spouse.Rich$ 

    $\sigma := \{ X \rightarrow Rich \sqcap \forall child.\forall spouse.Rich,\ Y \rightarrow \forall child.Rich \}$

    $\sigma(D_1) = \forall child.\forall child.Rich \sqcap \forall child.Rich \sqcap \forall child.\forall spouse.Rich$

    $\sigma(D_2) = \forall child.Rich \sqcap \forall child.\forall child.Rich \sqcap \forall child.\forall spouse.Rich$ 