$$\begin{align*}
    &(0)\ (\neg (p \rightarrow \neg q))\rightarrow p \quad \text{(TAUT)} \\
    &(1)\ \Box((\neg (p \rightarrow \neg q))\rightarrow p) \quad \text{(NEC, 0)} \\
    &(2)\ \Box(p \rightarrow q) \rightarrow (\Box p \rightarrow \Box q) \quad \text{(Axiom, K)} \\
    &(3)\ \Box((\neg (p \rightarrow \neg q)) \rightarrow p) \rightarrow (\Box (\neg (p \rightarrow \neg q)) \rightarrow \Box p) \quad \text{(S, s1, 2)} \\
    &(4)\ \Box (\neg (p \rightarrow \neg q)) \rightarrow \Box p \quad \text{(MP, 1, 3)}\\
    &(5)\ (\neg (p \rightarrow \neg q))\rightarrow q \quad \text{(TAUT)} \\
    &(6)\ \Box((\neg (p \rightarrow \neg q))\rightarrow q) \quad \text{(NEC, 5)} \\
    &(7)\ \Box((\neg (p \rightarrow \neg q)) \rightarrow q) \rightarrow (\Box (\neg (p \rightarrow \neg q)) \rightarrow \Box q) \quad \text{(S, s2, 2)} \\
    &(8)\ \Box (\neg (p \rightarrow \neg q)) \rightarrow \Box q \quad \text{(MP, 6, 7)}\\
    &(9)\ (p \rightarrow q)\rightarrow ((p\rightarrow r)\rightarrow(p\rightarrow\neg(q\rightarrow\neg r))) \quad \text{(TAUT)} \\
    &(10)\ (\Box (\neg (p \rightarrow \neg q)) \rightarrow \Box p)\rightarrow ((\Box (\neg (p \rightarrow \neg q))\rightarrow \Box q)\rightarrow(\Box (\neg (p \rightarrow \neg q))\rightarrow\neg(\Box p\rightarrow\neg \Box q))) \quad \text{(S, s3, 9)} \\
    &(11)\ (\Box (\neg (p \rightarrow \neg q))\rightarrow \Box q)\rightarrow(\Box (\neg (p \rightarrow \neg q))\rightarrow\neg(\Box p\rightarrow\neg \Box q)) \quad \text{(MP, 4, 10)} \\
    &(12)\ \Box (\neg (p \rightarrow \neg q))\rightarrow\neg(\Box p\rightarrow\neg \Box q) \quad \text{(MP, 8, 11)} \\
\end{align*}$$
$$\begin{align*}\\
&(0)\ (¬(p → ¬q) → p)  \quad   (TAUT)\\
&(1)\ □_{x_{1}} (¬(p → ¬q) → p)  \quad   (T_Necessitation, 0)\\
&(2)\ (□_{x_{2}} (p → q) → (□_{x_{3}} p → □_{x_{2}·x_{3}} q))  \quad   (Axiom)\\
&(3)\ (□_{x_{4}} (¬(p → ¬q) → p) → (□_{x_{5}} ¬(p → ¬q) → □_{x_{4}·x_{5}} p))  \quad   (Substitution, s1, 2)\\
&(4)\ (□_{x_{5}} ¬(p → ¬q) → □_{x_{4}·x_{5}} p)  \quad   (Modus Ponens, 1, 3)\\
&(5)\ (¬(p → ¬q) → q)  \quad   (TAUT)\\
&(6)\ □_{x_{6}} (¬(p → ¬q) → q)  \quad   (T_Necessitation, 5)\\
&(7)\ (□_{x_{7}} (¬(p → ¬q) → q) → (□_{x_{8}} ¬(p → ¬q) → □_{x_{7}·x_{8}} q))  \quad   (Substitution, s2, 2)\\
&(8)\ (□_{x_{8}} ¬(p → ¬q) → □_{x_{7}·x_{8}} q)  \quad   (Modus Ponens, 6, 7)\\
&(9)\ ((p → q) → ((p → r) → (p → ¬(q → ¬r))))  \quad   (TAUT)\\
&(10)\ ((□_{x_{9}} ¬(p → ¬q) → □_{x_{10}} p) → ((□_{x_{9}} ¬(p → ¬q) → □_{x_{11}} q) → (□_{x_{9}} ¬(p → ¬q) → ¬(□_{x_{10}} p → ¬□_{x_{11}} q))))  \quad   (Substitution, s3, 9)\\
&(11)\ ((□_{x_{9}} ¬(p → ¬q) → □_{x_{11}} q) → (□_{x_{9}} ¬(p → ¬q) → ¬(□_{x_{10}} p → ¬□_{x_{11}} q)))  \quad   (Modus Ponens, 4, 10)\\
&(12)\ (□_{x_{9}} ¬(p → ¬q) → ¬(□_{x_{10}} p → ¬□_{x_{11}} q))  \quad   (Modus Ponens, 8, 11)
\end{align*}$$
$$\begin{align*}
&x_{1} = x_{4}\\
&x_{6} = x_{7}\\
&(x_{4} · x_{5}) = x_{10}\\
&(x_{7} · x_{8}) = x_{11}\\
&x_{8} = x_{9}\\
&x_{5} = x_{9}
\end{align*}$$
$$\begin{align*}
&□_{x_{1}} (¬(p → ¬q) → p)\\
&□_{x_{6}} (¬(p → ¬q) → q)\\
&(□_{x_{9}} ¬(p → ¬q) → ¬(□_{x_{1}\cdot x_{9}} p → ¬□_{x_{6}\cdot x_9} q))\\
\end{align*}$$


