# 计算复杂性

## 可计算性
（由于我不太熟练，就花几分钟简单回忆一下关键点）

**希尔伯特判定问题：**是否存在算法，对于一阶逻辑中的任意语句 $A, B$ ，它能够判定是否可由 $A$ ，逻辑地推出 $B$ 。答案是否定的：一阶逻辑是不可判定的。

**递归函数**

**图灵机**

**停机问题：**图灵机停机问题是不可判定的。

## 复杂性类别

称一个图灵机判定一个语言 $L \subseteq \{ 0, 1 \}^*$ ，如果该图灵机计算函数 $f_L:\{0, 1\}^* \rightarrow \{0, 1\}$ ，其中 $f_L(x) = 1 \Leftrightarrow x \in L$ 。

**定义**（类 $\textbf{DTIME}$）设 $T: \mathbb{N} \rightarrow \mathbb{N}$ 是一个函数。称语言 $L \in \textbf{DTIME}(T(n))$ 当且仅当存在运行时间为 $c \cdot T(n)$ 的图灵机判定语言 $L$ ，其中 $c > 0$ 是常数。

**定义**（类 $\textbf{P}$）多项式时间复杂度

$$
\textbf{P} = \bigcup_{c \ge 1} \textbf{DTIME}(n^c)
$$

**定义**（类 $\textbf{NP}$）语言 $L \subseteq \{0, 1\}^*$ 属于 $\textbf{NP}$ ，如果存在多项式 $p: \mathbb{N} \rightarrow \mathbb{N}$ 和一个多项式时间图灵机 $M$（称为 $L$ 的验证器），使得对于任意 $x \in \{0, 1\}^*$ 有

$$
x \in L \Leftrightarrow \exists u \in \{0, 1\}^{p(|x|)}\ 满足\ M(x, u) = 1
$$

称 $u$ 是 $x$ （关于语言 $L$ 和图灵机 $M$ ）的证明。

**定义**（类 $\textbf{EXP}$）

$$
\textbf{EXP} = \bigcup_{c \ge 1} \textbf{DTIME}(2^{n^c})
$$

**命题** $\textbf{P} \subseteq \textbf{NP} \subseteq \textbf{EXP}$

## 描述逻辑中的基本结论

