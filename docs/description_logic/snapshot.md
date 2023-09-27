<h2 style="text-align: center">描述逻辑简介</h2>

### 1. 概念

论域必须是非空的，可以是无穷集合。
**个体名称（individual name）**：个体名，表示论域中的单个元素。
**概念名称（concept name）**：类名，外延是论域的有限子集，可以看作一元谓词。
**作用名称（role name）**：关系名，表示论域中的二元关系，可以看作二元谓词。
**概念描述（concept description）**：用概念名称和作用名称按照语法规则构成的句子，表示对一些实例的抽象描述/刻画。
**概念定义（defined concept）**：将概念描述定义为一个概念名称。
**实例断言（instance assertion）**：断言一个个体名称是一个概念名称的实例。
**概念模型（concept patterns）**：含有变量的概念描述。

### 2. 语法

$$
\begin{align*}
& \textbf{定义 }(\mathcal{ALC}语言) 记 \, \mathbf{C} \, 为概念名称的集合，\, \mathbf{R} \, 为作用名称的集合，\,\mathbf{C}\, 与 \,\mathbf{R}\, 不相交。\,\mathcal{ALC}\, \\
& 的概念描述集合递归定义如下：\\
& \bullet 所有的概念名称是 \,\mathcal{ALC}\, 概念描述。\\
& \bullet \top 和 \bot 是 \,\mathcal{ALC}\, 概念描述。\\
& \bullet 如果 \,C\, 和 \,D\, 是 \,\mathcal{ALC}\, 概念描述，并且 \,r\, 是一个作用名称，那么下面的也是 \,\mathcal{ALC}\, 概念描述：\\
& \qquad \,C\, \sqcap \,D\, (合取)，\\
& \qquad \,C\, \sqcup \,D\, (析取)，\\
& \qquad \neg \,C\, (非)，\\
& \qquad \exists r . C\, (存在约束)，\\
& \qquad \forall r . C\, (全称约束)。\\
\end{align*}
$$

### 3. 语义

$$
\begin{align*}
& \textbf{定义 }一个解释 \mathcal{I} = (\Delta^{\mathcal{I}}, \cdot^{\mathcal{I}}) 是由一个非空集合论域 \Delta^{\mathcal{I}} 和一个映射 \cdot^{\mathcal{I}} 构成，\\
& 其中映射定义如下：\\
& \bullet 每一个概念名称 A \in \mathbf{C} 都映射到一个集合 A^{\mathcal{I}} \subseteq \Delta^{\mathcal{I}}。\\
& \bullet 每一个作用名称 r \in \mathbf{R} 都映射到一个二元关系 r^{\mathcal{I}} \subseteq \Delta^{\mathcal{I}} \times \Delta^{\mathcal{I}}\\ 
\end{align*}
$$

$$
\begin{align*}
    \top^{\mathcal{I}} & = \Delta^{\mathcal{I}},\\
    \bot^{\mathcal{I}} & = \emptyset,\\
    (C \sqcap D)^{\mathcal{I}} & = C^{\mathcal{I}} \cap D^{\mathcal{I}},\\
    (C \sqcup D)^{\mathcal{I}} & = C^{\mathcal{I}} \cup D^{\mathcal{I}},\\
    (\neg C)^{\mathcal{I}} & = \Delta^{\mathcal{I}} \setminus C^{\mathcal{I}},\\
    (\exists r . C)^{\mathcal{I}} & = \{ d \in \Delta^{\mathcal{I}} | 存在一个 e \in \Delta^{\mathcal{I}} ，使得 (d,e) \in r^{\mathcal{I}} 并且 e \in C^{\mathcal{I}} \},\\
    (\forall r . C)^{\mathcal{I}} & = \{ d \in \Delta^{\mathcal{I}} | 对于每一个 e \in \Delta^{\mathcal{I}} ，如果 (d,e) \in r^{\mathcal{I}} 那么 e \in C^{\mathcal{I}} \}。\\
\end{align*}
$$

### 4. 模态

描述逻辑 $\mathcal{ALC}$ 是多模态逻辑 $\mathcal{K}_m$ 的变体是由 Schild 于 1991 发现的。概念名称看作命题，作用名称看作可通达关系。 $\mathcal{ALC}$ 的解释就是一个克里普克结构，其中 $\Delta^{\mathcal{I}}$ 是世界集，$\cdot^{\mathcal{I}}$ 既提供世界集上的可通达关系集又给出对命题的赋值。于是基于可通达关系 $r$ ，全称约束 $\forall r.C$ 成为 $\Box_r C$ ，存在约束 $\exists r.C$ 成为 $\diamondsuit_r C$ 。将 $\mathcal{ALC}$ 翻译到一阶逻辑（FOL）的通常方法也和模态逻辑的标准翻译一致。

### 5. $Tbox$

一个 $TBox\ \mathcal{T}$ 是形如 $A \equiv C$ 的概念定义的有限集合，其中 $A$ 是概念名称， $C$ 是概念描述，并且同一个 $A$ 在 $\mathcal{T}$ 中只出现一次。这时， $A$ 称作 $\mathcal{T}$ 中的原始概念。如果概念名称 $B$ 在 $C$ 中出现，则称 $A$ 直接使用 $B$ ，将"使用"理解为"直接使用"的传递闭包。若 $\mathcal{T}$ 中存在一个原始概念使用了它本身，则称 $\mathcal{T}$ 含有循环（或一般的 $\mathcal{T}$），否则称为无环的 $\mathcal{T}$ 。

无环 $TBox$ 的模型：如果 $A^{\mathcal{I}} = C^{\mathcal{I}}$ 则解释 $\mathcal{I}$ 满足概念定义 $A \equiv C$ 。如果解释 $\mathcal{I}$ 满足 $TBox\ \mathcal{T}$ 中的所有概念定义，则解释 $\mathcal{I}$ 是 $\mathcal{T}$ 的模型。

一般的 $TBox$ 的模型：general concept inclusion axioms (GCIs)： $GCI$ 是形如 $C \sqsubseteq D$ 的形式，其中 $C,D$ 都是（复合）概念描述。如果 $C^{\mathcal{I}} \subseteq D^{\mathcal{I}}$ 则解释 $\mathcal{I}$ 满足 $GCI\ \ C \sqsubseteq D$ 。如果解释 $\mathcal{I}$ 满足 $GCI\ \ A \sqsubseteq C,\ C \sqsubseteq A$ 则解释 $\mathcal{I}$ 满足概念定义 $A \equiv C$ 。有限个 $GCI$ 构成的集合是 $\mathcal{T}$ 。如果解释 $\mathcal{I}$ 满足 $TBox\ \mathcal{T}$ 中的所有概念定义，则解释 $\mathcal{I}$ 是 $\mathcal{T}$ 的模型。

### 6. $Abox$

设有可数无穷个个体名称 $a,b,c$ 等等， $ABox$ 是形如 $C(a),\ r(a,b)$ 的断言的有限集合，其中 $C$ 是概念描述， $r$ 是作用描述。对每个个体 $a$ 解释为 $a^{\mathcal{I}} \in \Delta^{\mathcal{I}}$ ，通常遵守唯一名称假设（ $a \neq b 蕴含 a^{\mathcal{I}} \neq b^{\mathcal{I}}$ ）。如果 $a^{\mathcal{I}} \in C^{\mathcal{I}}$ 则解释 $\mathcal{I}$ 满足概念断言 $C(a)$ 。如果 $(a^{\mathcal{I}},b^{\mathcal{I}}) \in r^{\mathcal{I}}$ 则解释 $\mathcal{I}$ 满足作用断言 $r(a,b)$ 。如果解释 $\mathcal{I}$ 满足 $ABox\ \mathcal{A}$ 中的所有断言，则解释 $\mathcal{I}$ 是 $\mathcal{A}$ 的模型。
