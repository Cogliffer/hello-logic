## 模态
尝试将 justification 还原到模态逻辑上

### 语言
$c,d,e$: constant term<br>
$x_i,x_j,x_k$: variable term<br>
$t,u,v$: any term<br>
$\mathbf{EVI}$：常项和变项对$\cdot,+$两个运算封闭的集合。其中<br>
$$\begin{align*}
    & t\cdot t = t\\
    & t+ t = t\\
    & u+v=v+u\\
\end{align*}$$
对任意的常项$t$，有对应的一个一元模态算子$\Box_t$

使用含有变项的公式作为一个记号，记的是一个公式模式，这个集合为将所有变项替换为任何常项后得到的公式的集合。当说含有变项的公式可证时，说的是这个集合中的所有公式可证。

### 模型
对任意的常项$t$，有对应的一个模型中的二元关系$R_t$

### 公理
$$\begin{align*}
    &(\text{application}) & \Box_t(F\rightarrow M)\rightarrow(\Box_u F\rightarrow\Box_{t\cdot u}M)\\
    &(\text{weaking}) & \Box_t F\rightarrow\Box_{t+u} F
\end{align*}$$
Axiom $K$ is a special case of $\text{application}$, Let $u=t$ and $t\cdot t = t$, we have $\Box_t(F\rightarrow M)\rightarrow(\Box_t F\rightarrow\Box_t M)$<br>
公理不仅要求每个算子$\Box_t$是正规模态算子，还给出了关系之间的约束关系，也就是能通过一个结构$\mathbf{EVI}$来刻画不同通达关系之间的关系。所以说 JSL 决定性的东西是$\mathbf{EVI}$结构，用来定义通达关系之间的关系，这相当于多模态算子的一个补充。完全可以有更多的结构来定义通达关系之间的关系。公理对通达关系的约束，起到了原来证据函数的功能。

### 规则
对任意的常项$t$，有规则$F/\Box_t F$

### 实现
将一个模态算子的公式扩展到多个模态算子的语言中，然后转为 justification 公式

在证明中，统一使用变项

设$\Lambda$上的替换为

$\sigma(P_1,P_2,\cdots,P_n) = (F_1,F_2,\cdots,F_n)$

将一个公式或一个公式序列中出现的$\Box$依次翻译为常项$\Box_c$，设$F_i$中出现了$m$个$\Box$，那么记$F_i(c_1,c_2,\cdots,c_m)$为将$F_i$中的$m$个$\Box$依次翻译为$\Box_{c_1},\Box_{c_2},\cdots,\Box_{c_m}$的结果。记$(F_1,F_2,\cdots,F_n)(c_1,c_2,\cdots,c_s)$为将$(F_1,F_2,\cdots,F_n)$中的$s$个$\Box$依次翻译为$\Box_{c_1},\Box_{c_2},\cdots,\Box_{c_s}$的结果。在$\Omega$上的一个替换记为

$\sigma(P_1,P_2,\cdots,P_n) = (F_1,F_2,\cdots,F_n)(c_1,c_2,\cdots,c_s)$

因为翻译的常项$\Box_c$是任意的，所以可以用变项来记所有翻译的集合，记$F_i(x_1,x_2,\cdots,x_m)$为将$F_i$中的$m$个$\Box$依次翻译为任意常项所得到的公式的集合。同样的，记$(F_1,F_2,\cdots,F_n)(x_1,x_2,\cdots,x_s)$为将$(F_1,F_2,\cdots,F_n)$中的$s$个$\Box$依次翻译为任意常项所得到的公式序列的集合。在$\Omega$上的一个自由替换记为

$\sigma'(P_1,P_2,\cdots,P_n) = (F_1,F_2,\cdots,F_n)(x_1,x_2,\cdots,x_s)$

$\sigma'$是一个替换集合，$F\sigma'$是公式$F$在所有$\sigma'$元素替换的结果的集合。

如果模态逻辑$\Lambda$中的公式$F$是命题逻辑公理$A$经过替换$\sigma$得到的，即$A\sigma=F$，那么$(A\sigma')^\circ = \{F\}$

#### From modal $K$ to $K_t$
**Theorem.** 如果公式$F$在$\Lambda$中可证，那么存在$\Omega$中的替换$\sigma'$使得$F\sigma'$可证并且$(F\sigma')^\circ = \{F\}$

**Proof.** Let $F_1,F_2,\cdots,F_n$ be a proof of $F$ in $\Lambda$, we try to prove for each $k\le n$ there is a free substitution $\sigma'_k$ in $\Omega$ such that $F_k\sigma'_k$ is provable and $(F_k\sigma'_k)^\circ = \{F_k\}$.<br>
**Axiom Case** Suppose that $F_k$ is an instance of axiom $A$ in PL, then there is a substitution $\sigma$ such that $A\sigma = F_k$, then $\sigma'$ is a free substitution such that $A\sigma'$ is provable and $(A\sigma')^\circ = \{F_k\}$<br>
**Modus Ponens Case** Suppose that $F_k$ is obtained from $F_{m}$ and $F_{n} = F_m\rightarrow F_k$ by modus ponens. Then by induction hypothesis there are free substitution $\sigma'_m,\sigma'_n$ such that $F_m\sigma'_m,F_n\sigma'_n$ are provable and $(F_m\sigma'_m)^\circ = \{F_m\},(F_n\sigma'_n)^\circ = \{F_n\}$. We first show that for every $J_1\rightarrow J_2\in F_n\sigma'_n$, $J_1\in F_m\sigma'_m$. Suppose that $\sigma'_n = \sigma'_n(x_1,x_2,\cdots,x_s)$ and $\sigma'_m = \sigma'_m(x_1,x_2,\cdots,x_l)$ where $l\le s$. Let $\sigma_n = \sigma'_n(x_1,x_2,\cdots,x_s;c_1,c_2,\cdots,c_s)$ such that $J_1\rightarrow J_2 = F_n\sigma_n$, then 
$$\begin{align*}
    J_1 &= F_m\sigma_n \\
    &= F_m\sigma'_n(x_1,x_2,\cdots,x_s;c_1,c_2,\cdots,c_s) \\
    &= F_m\sigma'_m(x_1,x_2,\cdots,x_l;c_1,c_2,\cdots,c_l)\in F_m\sigma'_m
\end{align*}$$
Since $F_m\sigma'_m,F_n\sigma'_n$ are provable so $J_1\rightarrow J_2,J_1$ are provable. Thus by modus ponens $J_2$ is provable and $J_2^\circ = F_k$. So there is a substitution $\sigma_k$ such that $F_k\sigma_k$ is provable and $F_k\sigma_k = J_2$. Since the substitution $\sigma_n$ is arbitary, there is free substitution $\sigma'_k$ such that $F_k\sigma'_k$ is provable and $(F_k\sigma'_k)^\circ = \{F_k\}$


**Theorem.** Suppose that modal formula $F$ is provable in $K$, we try to proof that there is a modal formula $J$ without constant term provable in $K_t$ such that $J^\circ = \{F\}$.

**Proof.** Let $F_1,F_2,\cdots,F_n$ be a proof of $F$ in $K$, we try to prove for each $k\le n$ there is a modal formula $J_k$ without constant term provable in $K_t$ such that $J_k^\circ = \{F_k\}$.

we proof by induction on $k$. For $k=1$, $F_k$ is an axiom of $K$. If $F_k$ is a tautology, then by theorem there is a free substitution $\sigma'$ such that $F_k\sigma'$ is a modal formula without constant term and is provable in $K_t$ and $(F_k\sigma')^\circ = \{F_k\}$. If $F_k$ is an instance of $K$ axiom, suppose that $F_k = \Box(F\rightarrow M)\rightarrow(\Box F\rightarrow \Box M)$ and that there are $s,l$ number $\Box$ in $F,M$. Let $i,j\ge s,l$ and $i\neq j$ then
$$\begin{align*}
    \Delta =\ &\Box_{x_i}(F(x_1,x_2,\cdots,x_s)\rightarrow M(x_1,x_2,\cdots,x_l))\rightarrow\\
    &\quad\quad (\Box_{x_j} F(x_1,x_2,\cdots,x_s)\rightarrow\Box_{x_i\cdot x_j}M(x_1,x_2,\cdots,x_s))
\end{align*}$$
is a modal formula without constant term and is an instance of $\text{application}$ axiom and $\Delta^\circ = F_k$

For $k\ge 1$, By induction hypothesis, suppose that for each $m\le k$ there is a modal formula $J_m$ without constant term and provable in $K_t$ such that $J_m^\circ = \{F_m\}$. <br>
**Case:Modus Ponens** Suppose that $F_k$ is obtained from $F_{m}$ and $F_{n} = F_m\rightarrow F_k$ by modus ponens. Then by induction hypothesis there are modal formula $J_m,J_n$ without constant term and provable in $K_t$ such that $J_m^\circ = \{F_m\},J_n^\circ = \{F_n\}$.<br>
**Case:Necessitation** Suppose that $F_k$ is obtained from $F_{m}$ by necessitation. Then by induction hypothesis there is a modal formula $J_m$ without constant term and provable in $K_t$ such that $J_m^\circ = \{F_m\}$. Let $x_i$ be a variable term not in $J_m$, then $\Box_{x_i}J_m$is a modal formula without constant term and is provable by $t\text{-}NEC$ in $K_t$ and $(\Box_{x_i}J_m)^\circ = F_k$.

