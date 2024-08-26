#### From modal $K_t$ to $\mathsf{J}$

$G::= P\ |\ \neg G\ |\ G\rightarrow G\ |\ \Box_c G\ |\ \Box_x G$
$F::= G\ |\ \forall x_i F$

### 公理
$$\begin{align*}
    &(\text{application}) & \forall t \forall u(\Box_t(F\rightarrow M)\rightarrow(\Box_u F\rightarrow\Box_{t\cdot u}M))\\
    &(\text{weaking}) & \forall t \forall u(\Box_t F\rightarrow\Box_{t+u} F)
\end{align*}$$
$\forall x_1 \forall x_2\cdots \forall x_n (F\rightarrow G)\nrightarrow (\forall x_1 \forall x_2\cdots \forall x_n F\rightarrow \forall x_1 \forall x_2\cdots \forall x_n G)$
### 规则
$MP$: suppose that $\forall x_1 \forall x_2\cdots \forall x_n $ are all variable terms contain in $F$ and $M$, then from $\forall x_1 \forall x_2\cdots \forall x_n (F\rightarrow M)$, $\forall x_1 \forall x_2\cdots \forall x_n F$ infer $\forall x_1 \forall x_2\cdots \forall x_n M$.

$MP$: suppose that $\forall x_1 \forall x_2\cdots \forall x_n $ are all variable terms contain in $F$ and $M$, then from $\forall x_1 \forall x_2\cdots \forall x_n (F\rightarrow M)$, $\forall x_1 \forall x_2\cdots \forall x_n G$ and $\forall x_1 \forall x_2\cdots \forall x_n F \leftrightarrow \forall x_1 \forall x_2\cdots \forall x_n G$ infer $\forall x_1 \forall x_2\cdots \forall x_n M$.

**Theorem.** Suppose that a set of modal formula $F$ without constant term is provable in $K_t$, we try to proof that there is a justification formula $J$ provable in $\mathsf{J}$ such that $J^\Box = F$.
