# Readability
**(Lemma 1.11 Readability)** Suppose that $\varphi$ is a formula in $\mathcal{L_0}$, then exactly one of the following conditions applies.
(1) There is an $n$ such that $\varphi=\langle A_n\rangle $.
(2) There is a $\psi\in\mathcal{L_0}$ such that $\varphi = (\neg\psi)$
(3) There are $\psi_1$ and $\psi_2$ in $\mathcal{L_0}$ such that $\varphi = (\psi_1\rightarrow\psi_2)$.

(**readability conditions**) If $\varphi\in L\subseteq\mathcal{L_0}$, then only one of the following conditions applies.
(1) $\varphi=\langle A_n\rangle$, or
(2) $\exist \psi\in L,\varphi=(\neg\psi)$, or
(3) $\exist \psi_1,\psi_2\in L,\varphi=(\psi_1\rightarrow\psi_2)$,
then $L$ satisfy the readability conditions.

**Proof.** Obviously there exist not-empty $L$ and all the possible $L$ is a partial order by the $\subseteq$. So there is a bigest
$L_{max}\equiv_{def}\bigcup\{L\subseteq\mathcal{L_0}\mid L\text{ satisfy the readability conditions.}\}\subseteq\mathcal{L_0}$.
And $L_{max}$ also satisfy the readability conditions since the conjection doesn't destory the readability conditions. 
And we will prove that $L_{max}$ satisfy the conditions to be a propositional language (defination 1.3).
(1) The set $A = \{A_n\mid n\in\mathbb{N}\}$ satisfy the readability conditions so $A\subseteq L_{max}$.
(2) For any $\varphi,\psi\in L_{max}\subseteq\mathcal{L_0}$, then $\varphi,\psi\in\mathcal{L_0}$, so $(\neg\varphi),(\varphi\rightarrow\psi)\in\mathcal{L_0}$. Then the set $L_{max}\cup\{(\neg\varphi),(\varphi\rightarrow\psi)\}$ satisfy the readability conditions. So $(\neg\varphi),(\varphi\rightarrow\psi)\in L_{max}$.
Thus $L_{max}$ satisfy the conditions to be a propositional language, so $\mathcal{L_0}\subseteq L_{max}$, also we have $L_{max}\subseteq\mathcal{L_0}$, so $\mathcal{L_0}=L_{max}$, then $\mathcal{L_0}$ satisfy the readability conditions.$\Box$ 

**(Theorem 1.13 Unique Readability)** If $\varphi\in L\subseteq\mathcal{L_0}$, then only one of the following conditions applies.
(1) $\varphi=\langle A_n\rangle$, or
(2) $\exist \psi\in L,\varphi=(\neg\psi)$, or
(3) $\exist \psi_1,\psi_2\in L,\varphi=(\psi_1\rightarrow\psi_2)$,
Furthermore, the formula $\psi,\psi_1\psi_2$ is unique respectively.
