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
Proof: Existence is true because the total set $\{s\mid s\text{ is any finite sequence}\}$ is exist and satisfy the conditions to be a propositional language. We need to prove that $\mathcal{L_0}$ satisfy the conditions to be a propositional language. For each $n\in\mathbb{N},A_n\in L$, so $A_n\in \mathcal{L_0}$. Suppose $s,t\in L_0$, then $s,t\in L$ for all $L$ satisfy the conditions to be a propositional language. So $(\neg s)\in L,(s\rightarrow t)\in L$, So that $(\neg s)$ and $(s\rightarrow t)$ alse belongs to the intersection of all $L$. So that $\mathcal{L_0}$ satisfy the conditions to be a propositional language. Another for all $L$ we have $\mathcal{L_0}\subseteq L$, so finished the proof. $\Box$

**(Lemma 1.11 Readability)** Suppose that $\varphi$ is a formula in $\mathcal{L_0}$, then exactly one of the following conditions applies.
(1) There is an $n$ such that $\varphi=\langle A_n\rangle $.
(2) There is a $\psi\in\mathcal{L_0}$ such that $\varphi = (\neg\psi)$
(3) There are $\psi_1$ and $\psi_2$ in $\mathcal{L_0}$ such that $\varphi = (\psi_1\rightarrow\psi_2)$.

(*readability conditions*) If $\varphi\in L\subseteq\mathcal{L_0}$, and only one of the following conditions applies.
(1) $\varphi=\langle A_n\rangle$, or
(2) $\exist \psi\in L,\varphi=(\neg\psi)$, or
(3) $\exist \psi_1,\psi_2\in L,\varphi=(\psi_1\rightarrow\psi_2)$,
then $L$ satisfy the readability conditions.

Proof. Obviously there exist not-empty $L$ and all the possible $L$ is a partial order by the $\subseteq$. So there is a bigest
$L_{max}\equiv_{def}\bigcup\{L\subseteq\mathcal{L_0}\mid L\text{ satisfy the readability conditions.}\}\subseteq\mathcal{L_0}$.
And $L_{max}$ also satisfy the readability conditions since the conjection doesn't destory the readability conditions. 
And we will prove that $L_{max}$ satisfy the conditions to be a propositional language (defination 1.3).
(1) The set $A = \{A_n\mid n\in\mathbb{N}\}$ satisfy the readability conditions so $A\subseteq L_{max}$.
(2) For any $\varphi,\psi\in L_{max}\subseteq\mathcal{L_0}$, then $\varphi,\psi\in\mathcal{L_0}$, so $(\neg\varphi),(\varphi\rightarrow\psi)\in\mathcal{L_0}$. Then the set $L_{max}\cup\{(\neg\varphi),(\varphi\rightarrow\psi)\}$ satisfy the readability conditions. So $(\neg\varphi),(\varphi\rightarrow\psi)\in L_{max}$.
Thus $L_{max}$ satisfy the conditions to be a propositional language, so $\mathcal{L_0}\subseteq L_{max}$, also we have $L_{max}\subseteq\mathcal{L_0}$, so $\mathcal{L_0}=L_{max}$, then $\mathcal{L_0}$ satisfy the readability conditions.$\Box$


**Lemma 0.1** The formula of propositional language has the same number of ( and ).

Proof.Let's apply induction on the construct of propositional formulas. It is clearly that the propositional symble $A_n$ where $n\in N$ has zero ( and ), so the propositional symble has the same number of ( and ).

Now, let's assume that the formula $s,t$ has the same number of ( and ), then we try to prove that the formula $(\neg s)$ and $(s\rightarrow t)$ also has the same number ( and ).

In the first case, $(\neg s) = <(,\neg,s,)>$, suppose the number of ( and ) in $s$ is $n$, then the number of ( and ) in $(\neg s)$ both is $n+1$. In the second case, $(s\rightarrow t) = <(,s,\rightarrow,t,)>$, suppose the number of ( and ) in $s$ and $t$ is $n$ and $m$, then the number of ( and ) in $(s\rightarrow t)$ both is $n+m+1$.

There we have the same number of ( and ) in the new formula $(\neg s)$ and $(s\rightarrow t)$.

**Corollary 0.2** If a consequence has diffent number of ( and ), then it is not a propositional formula.

Proof. Let's assume that the a consequence has diffent number of ( and ), then according to the lemma 0.1, the formula should has the same number of ( and ), which is contradict to the assumption.

**Lemma 0.3** The proper initial segment of propositional formula expect the propositional symble has different number of ( and ).

Proof. According to defination 1.3, there are two way to expand formula. We use the symble $I(\varphi)$ to represent a proper initial segment of $\varphi$. Let ${l}^{I(\varphi)}$ and $r^{I(\varphi)}$ are the number of ( and ) in $I(\varphi)$.

In the first case, assume $\varphi = (\neg A_n), n\in N$, there are three proper initial segment of $\varphi$:

$<(>,\quad <(,\neg>,\quad <(,\neg,A_n>$

In the second case, assume $\varphi = (A_n\rightarrow B_m), n,m\in N$, there are four proper initial segment of $\varphi$:

$<(>,\quad <(,A_n>,\quad <(,A_n,\rightarrow>,\quad <(,A_n,\rightarrow,B_m>,\quad$

We could find $l^{I(\varphi)}>r^{I(\varphi)}$ holds in different proper initial segment of $\varphi$.

So we assume that the propositional formula $\varphi,\psi$ hold $l^{I(\varphi)}>r^{I(\varphi)},l^{I(\psi)}>r^{I(\psi)}$, then to show that the constructed new formula $(\neg \varphi)$ and $(\varphi\rightarrow\psi)$ also holds.

In the first case, we can write the proper initial segment of $(\neg\varphi)$:

$<(>,\quad <(,\neg>,\quad <(,\neg>+I(\varphi),\quad <(,\neg,>+\varphi$

In the second case, we can write the proper initial segment of $(\varphi\rightarrow\psi)$:

$<(>,\quad <(>+I(\varphi),\quad <(>+\varphi+<\rightarrow>,\quad <(>+\varphi+<\rightarrow>+I(\varphi),\quad <(>+\varphi+<\rightarrow>+\varphi$

We can find that $l^{I((\neg\varphi))}>r^{I((\neg\varphi))}$ and $l^{I((\varphi\rightarrow\psi))}>r^{I((\varphi\rightarrow\psi))}$ holds. So that for any formula $\varphi$ of propositional language expect propositional symble , $l^{I(\varphi)}>r^{I(\varphi)}$ holds.

**Lemma 1.12** If $\varphi\in\mathcal{L}_0$, then no *proper initial segment* of $\varphi$ is an element of $\mathcal{L}_0$.

Proof. Assume that $\varphi$ is a proper initial segment of $\mathcal{L}_0$, then according to the Lemma 0.1, $\varphi$ has the same number of ( and ). 

Suppose $\varphi$ is propositional symble, then the proper initial segment of $\varphi$ is $<>$, and according to the Definition 1.3, $<>$ is not a formula.

If $\varphi$ is not a propositional symble, then according to corollary 0.2 and lemma 0.3, the proper initial segment of $\varphi$ is not formula of propositional language.

**Theorem 1.16** Suppose that $\varphi\in\mathcal{L}_0$ and that $v,\mu$ are truth assignments which agress on the propositional symbols which occur in $\varphi$, then $\bar{v}(\varphi) = \bar{u}(\varphi)$. 

Proof. According to the defination of unique readablilty, the formula $\varphi$ is either a propositional symble $<A_n>,n\in N$ or there exist a formula $\psi\in\mathcal{L}_0$ such that $\varphi = (\neg\psi)$ or there exist $\psi_1,\psi_2\in\mathcal{L}_0$ such that $\varphi = (\psi_1\rightarrow\psi_2)$.

In the first case, suppose $\varphi = <A_n>$, we have $v(A_n) = \mu(A_n)$, so that according to theorem 1.15, $\bar{v}(<A_n>) = v(A_n), \bar{\mu}(<A_n>) = \mu(A_n)$, so that $\bar{v}(\varphi) = \bar{u}(\varphi)$.

We induction on subformula to prove the theorem. 
**Base step.** For each $A_n\in\varphi, \bar{v}(A_n) = \bar{\mu}(A_n), n\in N$.
**Recursion step.** Suppose that the subformula $\psi_1,\psi_2$ of $\varphi$ satisfy $\bar{v}(\psi_1) = \bar{\mu}(\psi_1), \bar{v}(\psi_2) = \bar{\mu}(\psi_2)$, and $\varphi'$ is a new subformula of $\varphi$ such that $\varphi' = (\neg\psi_1)$ or $\varphi' = (\psi_1\rightarrow\psi_2)$.

In the first case, according theorem 1.15(2), $\bar{v}(\varphi') = \bar{v}((\neg\psi_1))$ has the opposite truth value of $\bar{v}(\psi_1)$, $\bar{\mu}(\varphi') = \bar{\mu}((\neg\psi_1))$ has the opposite truth value of $\bar{\mu}(\psi_1)$, so $\bar{v}(\varphi') = \bar{\mu}(\varphi')$.

In the second case, according theorem 1.15(2), $\bar{v}(\varphi') = \bar{v}((\psi_1\rightarrow\psi_2)) = \bar{\mu}((\psi_1\rightarrow\psi_2)) = \bar{\mu}(\varphi')$ because $\bar{v}(\psi_1) = \bar{\mu}(\psi_1), \bar{v}(\psi_2) = \bar{\mu}(\psi_2)$

So for any subformula $\psi$ of $\varphi$, $\bar{v}(\psi) = \bar{\mu}(\psi)$, and $\varphi$ is alse a subformula of $\varphi$, so $\bar{v}(\varphi) = \bar{\mu}(\varphi)$.




