<h2 style="text-align: center">描述逻辑简介</h2>

### 1. 概念

论域必须是非空的，可以是无穷集合。论域中的元素称为实例（instance）。

**概念名称（concept name）**：类名，外延是论域的有限子集，可以看作一元谓词。

**作用名称（role name）**：关系名，表示论域中的二元关系，可以看作二元谓词。

**概念描述（concept description）**：用概念名称和作用名称按照语法规则构成的句子，表示对一些实例的抽象描述/刻画。

**概念定义（defined concept）**：将概念描述定义为一个概念名称。

**专名（nominal concept）**：外延只有一个元素的概念名称。

**个体名称（individual name）**：个体名，只能出现在 $ABox$ 中，表示论域中的单个元素。

**实例断言（instance assertion）**：断言一个个体名称是一个概念名称的实例。

**概念模型（concept patterns）**：含有变量的概念描述。

### 2. $\mathcal{ALC}$ 语法

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

### 3. $\mathcal{ALC}$ 语义

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
    (\exists r . C)^{\mathcal{I}} & = \{ d \in \Delta^{\mathcal{I}} | 存在一个 e \in C^{\mathcal{I}} ，使得 (d,e) \in r^{\mathcal{I}} \},\\
    (\forall r . C)^{\mathcal{I}} & = \{ d \in \Delta^{\mathcal{I}} | 对于每一个 e \in \Delta^{\mathcal{I}} ，如果 (d,e) \in r^{\mathcal{I}} 那么 e \in C^{\mathcal{I}} \}。\\
\end{align*}
$$

### 4. 模态

描述逻辑 $\mathcal{ALC}$ 是多模态逻辑 $\mathcal{K}_m$ 的变体是由 Schild 于 1991 发现的。概念名称看作命题，作用名称看作可通达关系。 $\mathcal{ALC}$ 的解释就是一个克里普克结构，其中 $\Delta^{\mathcal{I}}$ 是世界集，$\cdot^{\mathcal{I}}$ 既提供世界集上的可通达关系集又给出对命题的赋值。于是基于可通达关系 $r$ ，全称约束 $\forall r.C$ 成为 $\Box_r C$ ，存在约束 $\exists r.C$ 成为 $\diamondsuit_r C$ 。将 $\mathcal{ALC}$ 翻译到一阶逻辑（FOL）的通常方法也和模态逻辑的标准翻译一致。

### 5. $Tbox$

一个 $TBox\ \mathcal{T}$ 是形如 $A \equiv C$ 的概念定义的有限集合，其中 $A$ 是概念名称， $C$ 是概念描述，并且同一个 $A$ 在 $\mathcal{T}$ 中只出现一次。这时， $A$ 称作 $\mathcal{T}$ 中的原始概念。如果概念名称 $B$ 在 $C$ 中出现，则称 $A$ 直接使用 $B$ ，将"使用"理解为"直接使用"的传递闭包。若 $\mathcal{T}$ 中存在一个原始概念使用了它本身，则称 $\mathcal{T}$ 含有循环（或一般的 $\mathcal{T}$），否则称为无环的 $\mathcal{T}$ 。

无环 $TBox$ 的模型：如果 $A^{\mathcal{I}} = C^{\mathcal{I}}$ 则解释 $\mathcal{I}$ 满足概念定义 $A \equiv C$ 。如果解释 $\mathcal{I}$ 满足 $TBox\ \mathcal{T}$ 中的所有概念定义，则解释 $\mathcal{I}$ 是 $\mathcal{T}$ 的模型。

一般的 $TBox$ 的模型：general concept inclusion axioms (GCIs)： $GCI$ 是形如 $C \sqsubseteq D$ 的形式，其中 $C,D$ 都是（复合）概念描述。如果 $C^{\mathcal{I}} \subseteq D^{\mathcal{I}}$ 则解释 $\mathcal{I}$ 满足 $C \sqsubseteq D$ 。如果解释 $\mathcal{I}$ 满足 $A \sqsubseteq C,\ C \sqsubseteq A$ 则解释 $\mathcal{I}$ 满足概念定义 $A \equiv C$ 。有限个 $GCI$ 构成的集合是 $\mathcal{T}$ 。如果解释 $\mathcal{I}$ 满足 $TBox\ \mathcal{T}$ 中的所有概念定义，则解释 $\mathcal{I}$ 是 $\mathcal{T}$ 的模型。

### 6. $Abox$

设有可数无穷个个体名称 $a,b,c$ 等等， $ABox$ 是形如 $C(a),\ r(a,b)$ 的断言的有限集合，其中 $C$ 是概念描述， $r$ 是作用描述。对每个个体 $a$ 解释为 $a^{\mathcal{I}} \in \Delta^{\mathcal{I}}$ ，通常遵守唯一名称假设（ $a \neq b 蕴涵 a^{\mathcal{I}} \neq b^{\mathcal{I}}$ ）。如果 $a^{\mathcal{I}} \in C^{\mathcal{I}}$ 则解释 $\mathcal{I}$ 满足概念断言 $C(a)$ 。如果 $(a^{\mathcal{I}},b^{\mathcal{I}}) \in r^{\mathcal{I}}$ 则解释 $\mathcal{I}$ 满足作用断言 $r(a,b)$ 。如果解释 $\mathcal{I}$ 满足 $ABox\ \mathcal{A}$ 中的所有断言，则解释 $\mathcal{I}$ 是 $\mathcal{A}$ 的模型。

### 7. 推理

T 推理(Terminological Reasoning)

- 可满足 (Satisfiability)：如果存在一个概念描述 $C$ 和一个 TBox $\mathcal{T}$ 的共同模型时，那么 $C$ 相对于 $\mathcal{T}$ 是可满足的。
- 包含 (Subsumption)：如果对于一个 TBox $\mathcal{T}$ 的任意模型 $\mathcal{I}$，均有 $C^{\mathcal{I}} \subseteq D^{\mathcal{I}}$ ，那么概念描述 $C$ 包含在概念描述 $D$ 中，记为 $C \sqsubseteq_{\mathcal{T}} D$ 。
- 相等 (equivalent)：如果对于一个 TBox $\mathcal{T}$ 的任意模型 $\mathcal{I}$，均有 $C^{\mathcal{I}} = D^{\mathcal{I}}$ ，那么概念描述 $C$ 与概念描述 $D$ 相等，记为 $C \equiv_{\mathcal{T}} D$ 。

A 推理(Assertional Reasoning)

- 一致性 (Consistency)：如果存在一个 ABox $\mathcal{A}$ 和一个 TBox $\mathcal{T}$ 的共同模型，那么 $\mathcal{A}$ 相对于 $\mathcal{T}$ 是一致的。
- 实例检测 (Instance Detection)：如果对于一个 TBox $\mathcal{T}$ 和一个 ABox $\mathcal{A}$ 的任意共同模型 $\mathcal{I}$ ，均有 $a^{\mathcal{I}} \in C^{\mathcal{I}}$，那么个体实例 $a$ 相对于 $\mathcal{T}$ 是概念描述 $C$ 的实例，记为 $\mathcal{A} \models_{\mathcal{T}} C(a)$ 。

复合推理问题(Compound Inference Problems)

- Classification (结构化)：给定一个 TBox $\mathcal{T}$ ，计算 $\mathcal{T}$ 中概念名称（抽象类）之间起约束作用的包含关系($\sqsubseteq_{\mathcal{T}}$)。
- Realization (抽象化)：给定一个 ABox $\mathcal{A}$ ，一个 TBox $\mathcal{T}$ 以及个体实例 $a$ ，计算 $\mathcal{T}$ 中满足 $\mathcal{A} \models_{\mathcal{T}} A(a)$ 的概念名称 $A$ 构成的集合，记为 $R_{\mathcal{A},\mathcal{T}}(a)$，并用包含关系 $\sqsubseteq_{\mathcal{T}}$ 找到最小的。
- Retrieval (实例化)：给定一个 ABox $\mathcal{A}$ ，一个 TBox $\mathcal{T}$ 以及概念 $C$ ，计算 $\mathcal{A}$ 中满足 $\mathcal{A} \models_{\mathcal{T}} C(a)$ 的个体实例 $a$ 构成的集合，记为 $\mathcal{I}_{\mathcal{A},\mathcal{T}}(C)$ 。

### 8. 具体域
- 抽象域 (abstract domain)：论域 $\Delta^{\mathcal{I}}$ 。
- 具体域 (concrete domain)：一个具体域 $\mathcal{D}$ 是一个有序对 $(\Delta^{\mathcal{D}}, \Phi^{\mathcal{D}})$ ，其中 $\Delta^{\mathcal{D}}$ 是非空集合， $\Phi^{\mathcal{D}}$ 是由谓词名称构成的集合，并且对于 $n$ 元谓词 $P \in \Phi^{\mathcal{D}}$ ，有 $P^{\mathcal{D}} \subseteq (\Delta^{\mathcal{D}})^{n}$ 。

将具体域 $\mathcal{D}$ 整合到 $\mathcal{ALC}$ 就得到 $\mathcal{ALC(D)}$

- 抽象特征：$g^{\mathcal{I}} : \Delta^{\mathcal{I}} \rightarrow \Delta^{\mathcal{I}}$
- 具体特征：$h^{\mathcal{I}} : \Delta^{\mathcal{I}} \rightarrow \Delta^{\mathcal{D}}$
- 谓词约束：$P(u_1, u_2, \cdots, u_n)$ ，其中 $u_i$ 是任意多个抽象特征和一个具体特征的复合，设 $u = g_1 \circ g_2 \cdots \circ g_k \circ h$ ，则 $u(d)^{\mathcal{I}} = h^{\mathcal{I}}\Big( g_{k}^{\mathcal{I}}\big( g_{k-1}^{\mathcal{I}} \cdots (g_1^{\mathcal{I}}(d)) \big) \Big), d \in \Delta^{\mathcal{I}}$ 。其解释定义如下：

$$
\begin{align*}
    & P(u_1, u_2, \cdots, u_n)^{\mathcal{I}} = \{ d \in \Delta^{\mathcal{I}}\ |\ \exists x_1, x_2,\cdots,x_n \in \Delta^{\mathcal{D}}\ 使得 \\
    & \qquad \qquad \qquad \qquad \qquad  u_i(d)^{\mathcal{I}} = x_i\ (1 \le i \le n)\ 并且\ (x_1,x_2,\cdots,x_n) \in P^{\mathcal{I}} \}
\end{align*}
$$

### 9. 属性描述逻辑 $\mathcal{ALCH}_@$

$\textsf{N}_\textsf{C}$ ： 概念名称的集合；$\textsf{N}_\textsf{R}$ ： 作用名称的集合；$\textsf{N}_\textsf{I}$ ： 个体名称的集合；$\textsf{N}_\textsf{V}$ ： 变量的集合

$\textbf{S}$ ：说明的集合，可以是如下表达式：

- 变量 $X \in \textsf{N}_\textsf{V}$
- 闭说明（closed specifiers）： $[a_1:v_1,\cdots,a_n:v_n]$
- 开说明（open specifiers）： $\lfloor a_1:v_1,\cdots,a_n:v_n \rfloor$

其中，$a_i \in \textsf{N}_\textsf{I}$ ， $v_i$ 要么 $\textsf{N}_\textsf{I}$ 中的个体名称，要么是形如 $X.c$ 的表达式，其中 $X \in \textsf{N}_\textsf{V}$ ， $c \in \textsf{N}_\textsf{I}$ 。

$\textbf{R}$ ：关系的集合，包括所有形如 $r@S$ 的表达式，其中 $r \in \textsf{N}_\textsf{R}$ ，$S \in \textbf{S}$ 。

$\textbf{C}$ ：概念描述的集合

$$
\textbf{C} := \top\ |\ \bot\ |\ \textsf{N}_\textsf{C} @ \textbf{S}\ |\ \neg \textbf{C}\ |\ \textbf{C} \sqcap \textbf{C}\ |\ \textbf{C} \sqcup \textbf{C}\ |\ \exists \textbf{R}.\textbf{C}\ |\ \forall \textbf{R}.\textbf{C}
$$

记 $\Phi^{\mathcal{I}} := \{\Sigma \subseteq \Delta^{\mathcal{I}} \times \Delta^{\mathcal{I}} |\ \Sigma 是有限集合 \}$ 为论域上的所有有限二元关系的集合。

$$
\begin{align*}
    & a^{\mathcal{I}} \in \Delta^{\mathcal{I}} \\
    & C^{\mathcal{I}} \in \Delta^{\mathcal{I}} \times \Phi^{\mathcal{I}}\quad \textrm{for}\quad C \in \textsf{N}_\textsf{C}\\
    & r^{\mathcal{I}} \in \Delta^{\mathcal{I}} \times \Delta^{\mathcal{I}} \times \Phi^{\mathcal{I}}\quad \textrm{for}\quad r \in \textsf{N}_\textsf{R}\\
\end{align*}
$$

任给变量指派 $\mathcal{Z} : \textsf{N}_\textsf{V} \rightarrow \Phi^{\mathcal{I}}$ ，一个说明 $S \in \textbf{S}$ 被解释到一个集合 $S^{\mathcal{I},\mathcal{Z}} \subseteq \Phi^{\mathcal{I}}$ 。通过定义 $X^{\mathcal{I},\mathcal{Z}} := \{\mathcal{Z}(X)\}, X \in \textsf{N}_\textsf{V}$ ，说明的语义定义为：

$$
\begin{align*}
    & [a:b]^{\mathcal{I},\mathcal{Z}} := \{ \{ (a^{\mathcal{I}},b^{\mathcal{I}}) \} \} \\
    & [a:X.b]^{\mathcal{I},\mathcal{Z}} := \{ \{ (a^{\mathcal{I}}, \delta)\ |\ (b^{\mathcal{I}}, \delta)\in \mathcal{Z}(X) \} \} \\
    & [a_1:v_1,\cdots,a_n:v_n]^{\mathcal{I},\mathcal{Z}} := \{ \cup_{i=1}^{n} F_i\}\textrm{where}\{F_i\} = [a_i:v_i]^{\mathcal{I},\mathcal{Z}}\ \textrm{for all}\ i \in \{1,\cdots,n\} \\
    & {\lfloor a_1:v_1,\cdots,a_n:v_n\rfloor}^{\mathcal{I},\mathcal{Z}} := \{ F\in \Phi^{\mathcal{I}}\ |\ F \supseteq G\ \textrm{for}\ \{G\} = [a_1:v_1,\cdots,a_n:v_n]^{\mathcal{I},\mathcal{Z}} \}
\end{align*}
$$

对于， $A \in \textsf{N}_\textsf{C}, r \in \textsf{N}_\textsf{R}, S \in \textbf{S}$ ，定义:
$(A@S)^{\mathcal{I},\mathcal{Z}} := \{ \delta \in \Delta^{\mathcal{I}}\ |\ \exists R\in S^{\mathcal{I},\mathcal{Z}}\textrm{ 使得 } (\delta, R)\in A^{\mathcal{I}} \}$
$(r@S)^{\mathcal{I},\mathcal{Z}} := \{ (\delta,\epsilon) \in \Delta^{\mathcal{I}} \times \Delta^{\mathcal{I}}\ |\ \exists R\in S^{\mathcal{I},\mathcal{Z}} \textrm{ 使得 } (\delta,\epsilon, R)\in r^{\mathcal{I}} \}$

$$
\begin{align*}
    \top^{\mathcal{I,Z}} & = \Delta^{\mathcal{I}}\\
    (C \sqcap D)^{\mathcal{I,Z}} & = C^{\mathcal{I,Z}} \cap D^{\mathcal{I,Z}},\\
    (C \sqcup D)^{\mathcal{I,Z}} & = C^{\mathcal{I,Z}} \cup D^{\mathcal{I,Z}},\\
    \neg C^{\mathcal{I,Z}} & = \Delta^{\mathcal{I}} \setminus C^{\mathcal{I,Z}} \\
    (\exists R . C)^{\mathcal{I,Z}} & = \{ d \in \Delta^{\mathcal{I}} | 存在一个 e \in C^{\mathcal{I,Z}} ，使得 (d,e) \in R^{\mathcal{I,Z}} \},\\
    (\forall R . C)^{\mathcal{I,Z}} & = \{ d \in \Delta^{\mathcal{I}} | 对于每一个 e \in \Delta^{\mathcal{I}} ，如果 (d,e) \in R^{\mathcal{I,Z}} 那么 e \in C^{\mathcal{I,Z}} \}。\\
\end{align*}
$$

### 10. 亚里士多德形而上学

**“是”的逻辑功能**

- 判断的联结词：其形式是“ S ”是“ P ”，直称判断是最简单、最基本的判断。
- 指称主词自身：“ S 是 ”在希腊文中是一个完整的句子，表示主词 S 是自身。
- 表示被定义的概念与定义的等同：定义的形式是“ S 是 Df ”。定义与判断不同，判断的谓词表述主词，不能交换，而被定义的词与定义的位置却可以交换而意义不变。定义的一般形式是“种 + 属差”。

**实体与属性**

主词和谓词分属两类逻辑范畴，主词所属的范畴是“实体”，谓词所属的范畴是“属性”。亚里士多德把范畴数量归纳为十个：除“实体”外，其他九个分别是实体的数量、性质、关系、位置、时间、姿态、状态、活动、受动。只有实体可以充当主词，其它九个范畴都是用来表述主词的谓词。就实体和属性的关系而言，实体是独立存在，不依赖其它东西而存在；属性必须依附于实体才能存在。

**第一实体和第二实体**

判断的主词可以被分为通名和专名：专名指示个别事物，是第一实体，而通名指示种和属，是第二实体。专名只能作为主词来使用；通名也可以用作谓词。

*本节所有内容摘抄自 赵敦华《西方哲学史》 pp. 79-82*

### 附录. 一些例子

**基于 $\mathcal{ALC}$ 的知识库的例子：**

$$
\begin{align*}
    & TBox : \\
    & \quad Teacher \equiv Person \sqcap \exists teaches.Course,\\
    & \quad Student \equiv Person \sqcap \exists attends.Course,\\
    & \quad \exists teaches.\top \sqsubseteq \neg Student,\\
    & \quad LazyStudent \equiv Student \sqcap \forall attends.\neg Course\\
\end{align*}
$$

$$
\begin{align*}
    & ABox : \\
    & \quad Person(\text{Plato}),\\
    & \quad Person(\text{Aristotle}),\\
    & \quad Course(\text{LogicFrontiers}),\\
    & \quad attends(\text{Aristotle}, \text{LogicFrontiers}),\\
    & \quad teaches(\text{Plato}, \text{LogicFrontiers})\\
\end{align*}
$$

**含有循环的 $Tbox$** ： $Human \equiv Adam \sqcup Eve \sqcup \exists parent.Human$

**$GCI$的例子** ： $Person \sqcap \exists uncle.Father \sqsubseteq \exists cousin.Person$ 表示：如果一个人的叔叔为人父，那这个人有表兄妹。

**具体域** $Q = (\mathbb{Q}, \Phi^{Q})$ ，其中 $\mathbb{Q}$ 是有理数域， $\Phi^{Q}$ 包含谓词：

1. 对任意 $P \in \{ <, \le, =, \ne, \ge, > \}$ 和任意 $q \in \mathbb{Q}$ 有一元谓词 $P_q$ ，且 $(P_q)^{Q} = \{q' \in \mathbb{Q} | q' P q \}$ 。
2. 二元谓词 $\{ <, \le, =, \ne, \ge, > \}$ 。
3. 三元谓词 $+$ ，且 $(+)^{Q} = \{(q_1, q_2, q_3) \in \mathbb{Q}^3 | q_1 + q_2 = q_3\}$ 。

在 $\mathcal{ALC}(Q)$ 中：

1. “ 青少年是 10 - 19 岁之间的人 ” 可以表示为： $Teenager \equiv Human\ \sqcap >_{10} (age)\ \sqcap <_{19} (age)$ 。

2. “ 所有人的年龄都比他父母的年龄小 ” 可以表示为： $\top \sqsubseteq\ ( <(age, mother \circ age)\ \sqcap <(age, father \circ age) )$ 。

**属性描述逻辑 $\mathcal{ALCH}_@$**

$ABox : \textrm{awarded}(\textrm{Agostini}, \textrm{Nobel Prize}) @[ \textrm{year}:2023]$

闭说明 $[\textrm{year} : R.\textrm{year} ]$ 表示将 R 中所有属性为 $\textrm{year}$ 的属性值对提取出来构成的关系的集合。

在通常描述逻辑中有公理： $\exists \textrm{awarded}.\textrm{Award} \sqsubseteq \exists \textrm{known_for}.\top$

在 $\mathcal{ALCH}_@$ 中 $\exists \textrm{awarded}@X.\textrm{Award}@X \sqsubseteq \exists \textrm{known_for}@ \lfloor \textrm{year} : X.\textrm{year} \rfloor .\top$ ，指派 $\mathcal{Z} = \{X\rightarrow \{(\textrm{year},2023)\} \}$ 。

在 2023 年获奖的人，都是在这一年因某个东西而著称的人。

给定论域 $\Delta^{\mathcal{I}} = \{ \textrm{Agostini},\textrm{Nobel Prize},\textrm{2023},\textrm{year},\textrm{attosecond pulses} \}$ 

$\textrm{Award}^{\mathcal{I}} = \{ (\textrm{Nobel Prize},\{(\textrm{year},2023)\}) \}$

$\textrm{awarded}^{\mathcal{I}} = \{ (\textrm{Agostini},\textrm{Nobel Prize},\{(\textrm{year},2023)\}) \}$

$\textrm{known_for}^{\mathcal{I}} = \{ (\textrm{Agostini},\textrm{attosecond pulses},\{(\textrm{year},2023)\}) \}$