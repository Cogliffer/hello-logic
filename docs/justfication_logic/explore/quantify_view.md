## Propositional Term modal logic

$F::= P\ |\ \neg F\ |\ F\rightarrow F\ |\ \Box_t F\ |\ \forall x F$

### 公理
$$\begin{align*}
    &\text{TAUT}\\
    &(\text{application}) & \Box_t(F\rightarrow M)\rightarrow(\Box_u F\rightarrow\Box_{t\cdot u}M)\\
    &(\text{weaking}) & \Box_t F\rightarrow\Box_{t+u} F
\end{align*}$$
$\exist x(\Box_x F)$: somebody knows $F$.
