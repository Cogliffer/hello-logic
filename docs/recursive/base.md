
<style>
    end {
        display: block;
        text-align: right;
        position: relative;
        top: -20px;
    }
</style>

*unlimited register machine (URM)* by Shepherdson & Sturgis [1963]
- *(URM)* A URM is a binary tuple $(R,P)$ where
- *(register)* A *register* $R$ is an infinite number of *unit register* labelled $R_1,R_2,\cdots$, each of which contains a natural number denoted by $r_1,r_2,\cdots$.
- *(program)* A *program* $P$ is a finite collection of *instructions*, there are four kind of instructions:
(1) *Zero instruction*. $Z(n),n\in\mathbb{N}$ change the content of $R_n$ to $0$, denoted by $r_n = 0$.
(2) *Successor instruction*. $S(n),n\in\mathbb{N}$ change the content of $R_n$ to $r_n+1$,denoted by $r_n = r_n+1$.
(3) *Transfer instruction*. $T(m,n),m,n\in\mathbb{N}$ change the content of $R_n$ by $r_m$,denoted by $r_n = r_m$.
(4) *Jump instruction*. $J(m,n,p),m,n,p\in\mathbb{N}$, to do judge if $r_m=r_n$ then go to the $p$th instruction otherwise go to the next instruction in $P$, denoted by $r_m=r_n\ ?\Rightarrow p\ ;\ \text{pass}$

*lemma* These four kind of instructions are independent of each other.
Proof. First, the last instruction Jump is independent of other three instructions since it is the only instruction that can change the running order of instructions on $P$. Second, the first instruction Zero is independent of other two instructions since (1) zero is not a successor of any natural number so Successor instruction can not generate a zero; (2) The Transfer instruction can transfer any unit register to zero only when there is a zero in register. Third, the second instruction Successor is independent of the third instruction Transfer since the Transfer instruction keep the number but can not transfer a number to the successor of itself. <end>$\Box$</end>

(more important question) weather there have a instructions could be a list of other instructions?
<!-- - I lost the most important question, why -->
If only use Zero and Successor, Transfer can not be constructed. If add the Jump, then Transfer can be constructed as following.

```
    #Transfer(m,n)
    1|Zero(n)
    2|Jump(m,n,5)
    3|S(n)
    4|Jump(m,m,2)
```

The intuition is that, if we want copy a number from register $m$ to register $n$, we can first Zero the number on register $n$ to zero, then successor the number until queal to the number on register $m$.

generally question, the equivalence of two programs.
- for converge program, the equivalence is that they have the same function.
- but for diverge program, it's a hard proplem.

相等判定和不等判定是同样复杂的吗，就是比较是否一样，如果都一样，则相等，如果不一样则不等。

*(flow diagram)* 

*donation*
- $P(a_1,a_2,\cdots)$ is the computation of P with initial configuration $a_1,a_2,\cdots$
- *(converge)* $P(a_1,a_2,\cdots)\downarrow b$ means that $P(a_1,a_2,\cdots)$ eventually stop and $r_1 = b$, when $b$ is unknow, then donate as $P(a_1,a_2,\cdots)\downarrow$.
- *(diverge)* $P(a_1,a_2,\cdots)\uparrow$ means that $P(a_1,a_2,\cdots)$ never stop.
- for simplfy the donation, we also use $P(a_1,a_2,\cdots,a_n)$ to present $P(a_1,a_2,\cdots,a_n,\cdots)$
- for $n\in\mathbb{N}$ define $f:\mathbb{N^n}\rightarrow\mathbb{N}$, useally we assume $Dom(f)\subset\mathbb{N^n}$

If there is a program that for every $(a_1,a_2,\cdots,a_n)\in Dom(f)$ and $f(a_1,a_2,\cdots,a_n) = b$, always $P(a_1,a_2,\cdots,a_n)\downarrow b$, then the program is a URM-computes of $f$, and the function $f$ is URM-computable.

If for some $(a_1,a_2,\cdots,a_n)$ the program holds $P(a_1,a_2,\cdots)\downarrow b$ then there is a function $f$ such that for these $(a_1,a_2,\cdots,a_n)\in Dom(f), f(a_1,a_2,\cdots,a_n) = b$.

<!-- $P(a_1,a_2,\cdots,a_n)\downarrow b$ if and only if $f(a_1,a_2,\cdots,a_n) = b$ -->

读书很容易不看例子，觉得浪费时间不如直接把握抽象形式，但貌似会缺少点什么

*predicates*
- $M(x_1,x_2,\cdots,x_n),n\in\mathbb{N}$ is an $n$-ary predicate of natural numbers.

*characteristic function*
- a *characteristic function* $c_M(\mathbf{x})$ of $M$ is a function where
$$
c_M(\mathbf{x})=
\begin{cases}
1, & \text{if } c_M \text{ is true.} \\
0, & \text{if } c_M \text{ is false.}\\
\end{cases}
$$
- The predicate $M$ is *decidable* if the function $c_M$ is computable. $M$ is *undecidable* if $M$ is not decidable.

*coding*
- A *coding* of a domain $D$ of objects is an explicit and effective injection $\alpha:D\rightarrow\mathbb{N}$.
- An object $d\in D$ is coded by the natural number $\alpha(d)$.
- If there is a function $f:D\rightarrow D$, then $f^{\star} = \alpha \circ f \circ \alpha^{-1}$ maps the code of any object $d\in Dom(f)$ to the code of $f(d)$.
