# 4. 计算复杂性

## 4.1 可判定性

**希尔伯特判定问题：**是否存在算法，对于一阶逻辑中的任意语句 $A, B$ ，它能够判定是否可由 $A$ ，逻辑地推出 $B$ 。答案是否定的：一阶逻辑是不可判定的。

**停机问题：**图灵机停机问题是不可判定的。

**描述逻辑中的基本结论**：可满足性和包含推理在一般 $TBox$ 的 $\mathcal{ALC}$ 中 $^{[5]}$， $\mathcal{ALC}_{reg}$ 中 $^{[6]}$， $\mathcal{SHOIQ}$ 中 $^{[7]}$，均是可判定的。

## 4.2 计算复杂度

称一个图灵机判定一个语言 $L \subseteq \{ 0, 1 \}^*$ ，如果该图灵机计算函数 $f_L:\{0, 1\}^* \rightarrow \{0, 1\}$ ，其中 $f_L(x) = 1 \Leftrightarrow x \in L$ 。

**定义**（类 $\textbf{DTIME}$）设 $T: \mathbb{N} \rightarrow \mathbb{N}$ 是一个函数。称语言 $L \in \textbf{DTIME}(T(n))$ 当且仅当存在运行时间为 $c \cdot T(n)$ 的图灵机判定语言 $L$ ，其中 $c > 0$ 是常数。

**定义**（类 $\textbf{P}$）多项式时间复杂度

$$
\textbf{P} = \bigcup_{c \ge 1} \textbf{DTIME}(n^c)
$$

!!! Example
    在图连通性问题中，给定图 $G$ 和它的两个顶点 $s, t$ ，要求判定 $s$ 在 $G$ 上是否可以连通到 $t$ 。经过 $C_{n}^{2}$ 个步骤后所有的边要么已经被访问要么永远无法访问。这个问题属于 $\textbf{P}$ 。

**定义**（类 $\textbf{NP}$）语言 $L \subseteq \{0, 1\}^*$ 属于 $\textbf{NP}$ ，如果存在多项式 $p: \mathbb{N} \rightarrow \mathbb{N}$ 和一个多项式时间图灵机 $M$（称为 $L$ 的验证器），使得对于任意 $x \in \{0, 1\}^*$ 有

$$
x \in L \Leftrightarrow \exists u \in \{0, 1\}^{p(|x|)}\ 满足\ M(x, u) = 1
$$

称 $u$ 是 $x$ （关于语言 $L$ 和图灵机 $M$ ）的证明。

**定义**（类 $\textbf{EXP}$）

$$
\textbf{EXP} = \bigcup_{c \ge 1} \textbf{DTIME}(2^{n^c})
$$

**定义**（空间受限计算）设 $S:\mathbb{N} \rightarrow \mathbb{N}, L \subseteq \{0,1\}^*$ 。如果存在常数 $c$ 和判定 $L$ 的图灵机 $M$ ，使得对任意长度为 $n$ 的输入， $M$ 完成计算的过程中 $M$ 的带头至多只访问除输入带之外的各条工作带上的 $c \cdot S(n)$ 个储存单元，则称 $L \in \textbf{SPACE}(S(n))$ 。

**定义**（类 $\textbf{PSPACE}$）

$$
\textbf{PSPACE} = \bigcup_{c \ge 1} \textbf{SPACE}(n^c)
$$

**命题** $\textbf{P} \subseteq \textbf{NP}  \subseteq \textbf{PSPACE} \subseteq \textbf{EXP}$

## 4.3 描述逻辑中的基本结论

$\mathcal{ALC}$ 基本推理的复杂性

- 在 $TBox$ 无环或者为空的 $\mathcal{ALC}$ 中，概念可满足性计算和包含计算是 $\textbf{PSPACE}$ 完全的 $^{[1,2]}$。
<!-- 考虑是否加入一个简短的可判定性证明 -->
- 在一般 $TBox$ 的 $\mathcal{ALC}$ 中，概念可满足性计算和包含计算是 $\textbf{EXP}$ 完全的 $^{[3,4]}$。
<!-- - （直观的理解就是，随着知识库中概念的增加，计算复杂性呈指数级增长，这当然会有问题，至少难以应用）
- $\mathcal{ALC}$ 基本推理的复杂性和某些博弈论计算复杂性类似 [SC79] 。 -->

## 参考文献

- [1] Manfred Schmidt-Schauß and Gert Smolka. Attributive concept descriptions with unions and complements.Technical Report SR-88-21, Fachbereich Informatik, Universit¨at Kaiserslautern, Kaiserslautern(Germany), 1988.
- [2] Carsten Lutz. Complexity of terminological reasoning revisited. In Proc. of the 6th Int. Conf. on Logic for Programming and Automated Reasoning (LPAR’99), volume 1705 of Lecture Notes in Artificial Intelligence, pages 181–200. Springer-Verlag, 1999.
- [3] Klaus Schild. A correspondence theory for terminological logics: Preliminary report. In Proc. of the 12th Int. Joint Conf. on Artificial Intelligence (IJCAI’91), pages 466–471, 1991.
- [4] Klaus Schild. Terminological cycles and the propositional μ-calculus. In J. Doyle, E. Sandewall, and P. Torasso, editors, Proc. of the 4th Int. Conf. on the Principles of Knowledge Representation and Reasoning (KR’94), pages 509–520, Bonn (Germany), 1994. Morgan Kaufmann, Los Altos.
- [5] Klaus Schild. Terminological cycles and the propositional μ-calculus. In J. Doyle, E. Sandewall, and P. Torasso, editors, Proc. of the 4th Int. Conf. on the Principles of Knowledge Representation and Reasoning (KR’94), pages 509–520, Bonn (Germany), 1994. Morgan Kaufmann, Los Altos.
- [6] Giuseppe De Giacomo and Maurizio Lenzerini. Boosting the correspondence between description logics and propositional dynamic logics. In Proc. of the 12th Nat. Conf. on Artificial Intelligence (AAAI’94), pages 205–212. AAAI Press/The MIT Press, 1994.
- [7] Stephan Tobies. Complexity Results and Practical Algorithms for Logics in Knowledge Representation. PhD thesis, RWTH Aachen, 2001.