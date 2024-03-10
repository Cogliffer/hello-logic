
# language
*symble*
- *logic symble*:$(,),\neg,\rightarrow$
- *propositional symble*:$A_n,\in\mathbb{N}$

*symble sequence*
- a list of symble: $\langle s_1,s_2,\cdots,s_n\rangle $

*operation on symble sequence*
- if $s = \langle s_1,s_2,\cdots,s_n\rangle , t = \langle t_1,t_2,\cdots,t_m\rangle $, then $s+t = \langle s_1,s_2,\cdots,s_n,t_1,t_2,\cdots,t_m\rangle $

(*block-subsequence*) A finite sequence $t$ is a *block-subsequence* of a finite sequence $s = \langle s_1,s_2,\cdots,s_n\rangle $ if there exist non-negative intergers $i$ and $j$ such that
(1) $i+j \le n$
(2) $t = \langle s_i,s_{i+1},\cdots,s_{i+j}\rangle $

**(subformula)** A *subformula* of formula $\varphi$ is a formula and a block-subsequence of $\varphi$.

(*initial segment*) A sequence $\langle a_1,\cdots,a_n\rangle $ is an *inital segment* of another sequence $\langle b_1,\cdots,b_m\rangle $ if and only if $n\le m$, and for all $i\le n, a_i = b_i$.
(*proper initial segment*) If $m$ is greater than $n$, we say that $\langle a_1,\cdots,a_n\rangle $ is a *proper initial segment* of $\langle a_1,\cdots,a_n,b_{n+1},\cdots,b_m\rangle $

**(Defination 1.3) propositional language $\mathcal{L_0}$**
Let $L$ be a set of symble sequences satisfying the following conditions:
(1) propositional symbles $A_n\in L,n\in\mathbb{N}$.
(2) if finite symble sequences $s,t\in L$, then $(\neg s)\in L, (s\rightarrow t)\in L$.
propositional language $\mathcal{L_0}$ defined be the smallest $L$ by the $\subseteq$ order.
we write this kind of $L$ satisfy the conditions to be a propositional language.

construct of the propositional language
Q:dose $\mathcal{L_0}$ 可枚举？
这里给出的是公式的构造过程，是从单元向复杂的过程，是公式结构中的生成方向

**(Theorem 1.4)** $\mathcal{L_0} = L_0 \equiv_{def} \bigcap\{L\mid\forall n\in\mathbb{N},A_n\in L\text{ and if finite }s,t\in L,\text{ then }(\neg s)\in L,(s\rightarrow t)\in L\}$
**Proof.**: Existence is true because the total set $\{s\mid s\text{ is any finite sequence}\}$ is exist and satisfy the conditions to be a propositional language. We need to prove that $\mathcal{L_0}$ satisfy the conditions to be a propositional language. For each $n\in\mathbb{N},A_n\in L$, so $A_n\in \mathcal{L_0}$. Suppose $s,t\in L_0$, then $s,t\in L$ for all $L$ satisfy the conditions to be a propositional language. So $(\neg s)\in L,(s\rightarrow t)\in L$, So that $(\neg s)$ and $(s\rightarrow t)$ alse belongs to the intersection of all $L$. So that $\mathcal{L_0}$ satisfy the conditions to be a propositional language. Another for all $L$ we have $\mathcal{L_0}\subseteq L$, so finished the proof. $\Box$

 **Theorem** the propositional language $\mathcal{L_0}$ is countable.



<div style="height:300px"></div>