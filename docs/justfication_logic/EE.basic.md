实现定理的例子

a proof of $\Box (p\land q)\rightarrow(\Box p\land \Box q)$ in $K$
$$\begin{align*}
    &(0)\ (p\land q)\rightarrow p \quad \text{(TAUT)} \\
    &(1)\ \Box((p\land q)\rightarrow p) \quad \text{(NEC, 0)} \\
    &(2)\ \Box(p \rightarrow q) \rightarrow (\Box p \rightarrow \Box q) \quad \text{(Axiom, K)} \\
    &(3)\ \Box((p\land q) \rightarrow p) \rightarrow (\Box (p\land q) \rightarrow \Box p) \quad \text{(S, s1, 2)} \\
    &(4)\ \Box (p\land q) \rightarrow \Box p \quad \text{(MP, 1, 3)}\\
    &(5)\ (p\land q)\rightarrow q \quad \text{(TAUT)} \\
    &(6)\ \Box((p\land q)\rightarrow q) \quad \text{(NEC, 5)} \\
    &(7)\ \Box((p\land q) \rightarrow q) \rightarrow (\Box (p\land q) \rightarrow \Box q) \quad \text{(S, s2, 2)} \\
    &(8)\ \Box (p\land q) \rightarrow \Box q \quad \text{(MP, 6, 7)}\\
    &(9)\ (p \rightarrow q)\rightarrow ((p\rightarrow r)\rightarrow(p\rightarrow(q\land r))) \quad \text{(TAUT)} \\
    &(10)\ (\Box (p\land q) \rightarrow \Box p)\rightarrow ((\Box (p\land q)\rightarrow \Box q)\rightarrow(\Box (p\land q)\rightarrow  (\Box p\land \Box q))) \quad \text{(S, s3, 9)} \\
    &(11)\ (\Box (p\land q)\rightarrow \Box q)\rightarrow(\Box (p\land q)\rightarrow(\Box p\land \Box q)) \quad \text{(MP, 4, 10)} \\
    &(12)\ \Box (p\land q)\rightarrow(\Box p\land \Box q) \quad \text{(MP, 8, 11)} \\
\end{align*}$$

a proof in $\Omega$
$$\begin{align*}
&(0)\ ((p ∧ q) → p)  \quad   (TAUT)\\
&(1)\ □_{x_{1}}  ((p ∧ q) → p)  \quad   (T_Necessitation, 0)\\
&(2)\ (□_{x_{2}}  (p → q) → (□_{x_{3}}  p → □_{(x_{2} · x_{3})}  q))  \quad   (Axiom)\\
&(3)\ (□_{x_{4}}  ((p ∧ q) → p) → (□_{x_{5}}  (p ∧ q) → □_{(x_{4} · x_{5})}  p))  \quad   (Substitution, s1, 2)\\
&(4)\ (□_{x_{5}}  (p ∧ q) → □_{(x_{4} · x_{5})}  p)  \quad   (Modus Ponens, 1, 3)\\
&(5)\ ((p ∧ q) → q)  \quad   (TAUT)\\
&(6)\ □_{x_{6}}  ((p ∧ q) → q)  \quad   (T_Necessitation, 5)\\
&(7)\ (□_{x_{7}}  ((p ∧ q) → q) → (□_{x_{8}}  (p ∧ q) → □_{(x_{7} · x_{8})}  q))  \quad   (Substitution, s2, 2)\\
&(8)\ (□_{x_{8}}  (p ∧ q) → □_{(x_{7} · x_{8})}  q)  \quad   (Modus Ponens, 6, 7)\\
&(9)\ ((p → q) → ((p → r) → (p → (q ∧ r))))  \quad   (TAUT)\\
&(10)\ ((□_{x_{9}}  (p ∧ q) → □_{x_{10}}  p) → ((□_{x_{9}}  (p ∧ q) → □_{x_{11}}  q) → (□_{x_{9}}  (p ∧ q) → (□_{x_{10}}  p ∧ □_{x_{11}}  q))))  \quad   (Substitution, s3, 9)\\
&(11)\ ((□_{x_{9}}  (p ∧ q) → □_{x_{11}}  q) → (□_{x_{9}}  (p ∧ q) → (□_{x_{10}}  p ∧ □_{x_{11}}  q)))  \quad   (Modus Ponens, 4, 10)\\
&(12)\ (□_{x_{9}}  (p ∧ q) → (□_{x_{10}}  p ∧ □_{x_{11}}  q))  \quad   (Modus Ponens, 8, 11)
\end{align*}$$
where
$$\begin{align*}
&x_{1} = x_{4}\\
&x_{6} = x_{7}\\
&(x_{4} · x_{5}) = x_{10}\\
&x_{5} = x_{9}\\
&x_{8} = x_{9}\\
&(x_{7} · x_{8}) = x_{11}
\end{align*}$$
so
$$\begin{align*}
&□_{x_1} (p\land q) → p\\
&□_{x_6} (p\land q) → q\\
&□_{x_9}(p\land q) → (□_{x_1\cdot x_9}p\land □_{x_6\cdot x_9}q)\\
\end{align*}$$

a proof in $\mathsf{J}$

$$\begin{align*}
    & c:((X\land Y)\rightarrow X)\in CS,\\
    & d:((X\land Y)\rightarrow Y)\in CS,\\
    & \textbf{Theorem. }s:(X\land Y)\rightarrow ((c\cdot s):X\land (d\cdot s):Y)
\end{align*}$$

A modal $\mathcal{M}$ given by

$\text{Lob schema}$公理与$T$公理是不一致的，因为对于任意的$F$有证明序列

$\Box F\rightarrow F,\Box(\Box F\rightarrow F),\Box(\Box F\rightarrow F)\rightarrow\Box F,\Box F,F$

$\mathcal{M} \vDash @_{\mathbf{GL}}\neg\Diamond P_T$, $P_T$ 为 $T$ 公式