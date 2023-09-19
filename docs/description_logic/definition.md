

# 单词
描述逻辑中有如下两种符号：

**概念**：

**作用**：

# 语法(Syntax)
$$\begin{align}
& \textbf{Definition. Attributive Language with Complements }(\mathcal{ALC}) \\
& 记 \, \mathbf{C} \, 为概念名称的集合，\, \mathbf{R} \, 为作用名称的集合，\,\mathbf{C}\, 与 \,\mathbf{R}\, 不相交。\,\mathcal{ALC}\, \\
& 的概念描述集合递归定义如下：\\
& \bullet 所有的概念名称是 \,\mathcal{ALC}\, 概念描述。\\
& \bullet \top 和 \bot 是 \,\mathcal{ALC}\, 概念描述。\\
& \bullet 如果 \,C\, 和 \,D\, 是 \,\mathcal{ALC}\, 概念描述，并且 \,r\, 是一个作用名称，那么下面的也是 \,\mathcal{ALC}\, 概念描述：\\
& \qquad \,C\, \sqcap \,D\, (合取)，\\
& \qquad \,C\, \sqcup \,D\, (析取)，\\
& \qquad \neg \,C\, (非)，\\
& \qquad \exists r . C\, (存在约束)，\\
& \qquad \forall r . C\, (全称约束)。\\
\end{align}$$

# 语义(Semantic)
$$
\begin{align}
& \textbf{Definition }一个解释 \mathcal{I} = (\Delta^{\mathcal{I}}, \cdot^{\mathcal{I}}) 是由一个非空集合论域 \Delta^{\mathcal{I}} 和一个映射 \Delta^{\mathcal{I}} 构成，\\
& 其中映射定义如下：\\
& \bullet 每一个概念名称 A \in \mathbf{C} 都映射到一个集合 A^{\mathcal{I}} \subseteq \Delta^{\mathcal{I}}。\\
& \bullet 每一个作用名称 r \in \mathbf{R} 都映射到一个二元关系 r^{\mathcal{I}} \subseteq \Delta^{\mathcal{I}} \times \Delta^{\mathcal{I}}\\ 
\end{align}
$$

映射 $\cdot^{\mathcal{I}}$ 可以扩展到 $\top, \bot$ 以及复杂概念中：

$$
\begin{align}
    \top^{\mathcal{I}} & = \Delta^{\mathcal{I}},\\
    \bot^{\mathcal{I}} & = \emptyset,\\
    (C \sqcap D)^{\mathcal{I}} & = C^{\mathcal{I}} \cap D^{\mathcal{I}},\\
    (C \sqcup D)^{\mathcal{I}} & = C^{\mathcal{I}} \cup D^{\mathcal{I}},\\
    (\neg C)^{\mathcal{I}} & = \Delta^{\mathcal{I}} \setminus C^{\mathcal{I}},\\
    (\exists r . C)^{\mathcal{I}} & = \{ d \in \Delta^{\mathcal{I}} | 存在一个 e \in \Delta^{\mathcal{I}} ，使得 (d,e) \in r^{\mathcal{I}} 并且 e \in C^{\mathcal{I}} \},\\
    (\forall r . C)^{\mathcal{I}} & = \{ d \in \Delta^{\mathcal{I}} | 对于每一个 e \in \Delta^{\mathcal{I}} ，如果 (d,e) \in r^{\mathcal{I}} 那么 e \in C^{\mathcal{I}} \}。\\
\end{align}
$$

通常，将 $C^{\mathcal{I}}$ 读作概念名称 $C$ 在解释 $\mathcal{I}$ 中的外延 ($extension$)，若 $b \in \Delta^{\mathcal{I}}, (a,b) \in r^{\mathcal{I}}$，则将 $b$ 称作 $a$ 在解释 $\mathcal{I}$ 下的$\,\textit{r-filler}$。

# 有向标号图(Directed Labeled Graph)

一个解释可以自然的用一个有向标号图来表示，其中每个节点表示一个概念名称，每个边表示一个作用名称。例如：

![image](assert/an%20example%20of%20directed%20labeled%20graph.png)

对应如下的解释：

$$
\begin{align}
    \Delta^{\mathcal{I}} & = \{ t, c1, c2, Aristotle \},\\
    Teacher^{\mathcal{I}} & = \{ t \},\\
    Course^{\mathcal{I}} & = \{ c1, c2\},\\
    Person^{\mathcal{I}} & = \{ Aristotle \},\\
    teaches^{\mathcal{I}} & = \{ (t,c1), (t,c2) \},\\
    attends^{\mathcal{I}} & = \{ (Aristotle, c1) \}.\\
\end{align}
$$