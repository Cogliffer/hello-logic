
*computable function*
- *zero function* $\mathbf{0}(x) = 0, \forall x\in\mathbb{N}$.
- *successor function* $s(x) = x + 1, \forall x\in\mathbb{N}$.
- *projection function* $\pi_{i}(x_1,x_2,\cdots,x_n) = x_{i}, x_i\in\mathbb{N}, \forall i = 1,2,\ldots,n$.

*standard program*
- If for every Jump instruction $J(a,b,c)$ on program $P = (p_1,p_2,\cdots,p_n)$ always holds that $c\le n+1$, then $P$ is a *standard program*.

*lemma*
- for every converge program $P$, there exists a standard program $P'$ such that they have the same computable function.
Proof. Assume $P=(p_1,p_2,\cdots,p_n)$, just replace the Jump instruction $J(a,b,c)$ with $J(a,b,n+1)$ if $c>n+1$. They are equal since $J(a,b,c),J(a,b,n+1)$ all lead to stop.
$P' = (p^{'}_1,p^{'}_2,\cdots,p^{'}_n), \text{where }
p^{'}_i = \begin{cases}
    J(a,b,n+1) & \text{if } p_i = J(a,b,c), c>n+1 \\
    p_i & \text{otherwise}.
\end{cases}$

*join*
- if program $P=(p_1,p_2,\cdots,p_n)$ and another program $Q=(q_1,q_2,\cdots,q_m)$, then program $PQ$ is defined by $PQ = (p^{'}_1,p^{'}_2,\cdots,p^{'}_n,q^{'}_1,q^{'}_2,\cdots,q^{'}_m)$ where $P' = (p^{'}_1,p^{'}_2,\cdots,p^{'}_n)$ is the standard program of $P$ and $q_{i}^{'} = \begin{cases}
    J(a,b,c+n) & \text{if } q_i = J(a,b,c) \\
    q_i & \text{otherwise}.
\end{cases}$

*subprogram*
- for every program $P=(p_1,p_2,\cdots,p_n)$, there exists a smallest number $\rho(P)$ such that $\forall u>\rho(P)$ register $R_u$ never used when the running of program $P$.
- $P[l_1,l_2,\cdots,l_n\rightarrow l] \equiv_{def} (T(l_1,1),T(l_2,2),\cdots,T(l_n,n),Z(n+1),Z(n+2),\cdots,Z(\rho(P)),P,T(1,l))$
(1) $T(l_1,1),T(l_2,2),\cdots,T(l_n,n)$
(2) $Z(n+1),Z(n+2),\cdots,Z(\rho(P))$
(3) $P$
(4) $T(1,l)$
generally, $\forall\rho\in\mathbb{N}, P[l_1,l_2,\cdots,l_n\rightarrow l:\rho] \equiv_{def} (T(l_1,1),T(l_2,2),\cdots,T(l_n,n),Z(n+1),Z(n+2),\cdots,Z(\rho),P,T(1,l))$

**Theorem** The composition of computable functions is computable.
Proof. Assume $\mathbf{x} = (x_1,x_2,\cdots,x_n),\mathbf{y} = (y_1,y_2,\cdots,y_m)$ and function $f(\mathbf{x})$ and $g_1(\mathbf{y}),g_2(\mathbf{y}),\cdots,g_n(\mathbf{y})$ are computabel. Assume program $P(\mathbf{x})\downarrow f(\mathbf{x})$ and $Q_1(\mathbf{y})\downarrow g_1(\mathbf{y}),Q_2(\mathbf{y})\downarrow g_2(\mathbf{y}),\cdots,Q_n(\mathbf{y})\downarrow g_n(\mathbf{y})$. We will show that the function $f(g_1(\mathbf{y}),g_2(\mathbf{y}),\cdots,g_n(\mathbf{y}))$ is computabel.

$\rho\equiv_{def} \mathrm{Max}\{\rho(P),\rho(Q_1),\rho(Q_2),\cdots,\rho(Q_n)\}$

set the $\mathbf{y}$ as initial configuration.

(1) $T(1,\rho+1),T(2,\rho+2),\cdots,T(m,\rho+m)$
(2) $Q_1[\rho+1,\rho+2,\cdots,\rho+m\rightarrow\rho+m+1:\rho],Q_2[\rho+1,\rho+2,\cdots,\rho+m\rightarrow\rho+m+2:\rho],\cdots,Q_n[\rho+1,\rho+2,\cdots,\rho+m\rightarrow\rho+m+n:\rho]$
(3) $P[\rho+m+1,\rho+m+2,\cdots,\rho+m+n\rightarrow 1:\rho]$

*recursion function*

**Theorem** computable