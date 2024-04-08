# Semantics


**substitution**
Let $\mathcal{M}=(M,I)$ be an $\mathcal{L}_\mathcal{A}$-structure and $\nu$ be an $\mathcal{M}$-assignment.
(1) if $\tau(x_1,x_2,\cdots,x_n)$ is an $\mathcal{L}_\mathcal{A}$-term and $\tau_1,\cdots,\tau_n$ are $\mathcal{L}_\mathcal{A}$-terms, then
$$\begin{align*}
    & \overline{\nu}(\tau(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n))\\
    & = \tau[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)]\\
    & = \overline{\mu}(\tau(x_1,\cdots,x_n)),\overline{\mu}(x_i)=\overline{\nu}(\tau_i)\\
\end{align*}$$
(2) if $\phi(x_1,x_2,\cdots,x_n)$ is an $\mathcal{L}_\mathcal{A}$-formula, $\tau_1,\cdots,\tau_n$ are $\mathcal{L}_\mathcal{A}$-terms and for each $i\le n,\tau_i$ is free for $x_i$ in $\phi$, then 
$$\begin{align*}
    & \mathcal{M},\nu\vDash\phi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)\\
    & \Leftrightarrow \mathcal{M}\vDash\phi[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)]\\
    & \Leftrightarrow \mathcal{M},\mu\vDash\phi(x_1,\cdots,x_n),\overline{\mu}(x_i)=\overline{\nu}(\tau_i)\\
\end{align*}$$
**Proof.** 
(1)
atomic term.
constants symbols are obversily.
variables: 
$\overline{\nu}(x_i(x_i;\tau_i)) = \overline{\nu}(\tau_i) = x_i[\overline{\nu}(\tau_i)]$
function symbols: 
$$\begin{align*}
    & \overline{\nu}(F_i(t_1,\cdots,t_m)(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n))\\
    & = \overline{\nu}(F_i(t_1(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n),\cdots,t_m(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)))\\
    & = I(F_i)(\overline{\nu}(t_1(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)),\cdots,\overline{\nu}(t_m(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)))\\
    & = I(F_i)(t_1[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)],\cdots,t_m[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)])\\
    & = F_i(t_1,\cdots,t_m)[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)]\\
\end{align*}$$
(2)
atomic formula.
predicate formula is similar to function symbols.
equivalence formula is a special predicate formula:
$$\begin{align*}
    & \mathcal{M},\nu\vDash(t_1\hat{=}t_2)(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)\\
    & \Leftrightarrow \mathcal{M},\nu\vDash t_1(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)\hat{=}t_2(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)\\
    & \Leftrightarrow \overline{\nu}(t_1(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)) = \overline{\nu}(t_2(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n))\\
    & \Leftrightarrow t_1[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)] = t_2[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)]\\
    & \Leftrightarrow (t_1 = t_2)[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)]\\
    & \Leftrightarrow \mathcal{M},\nu\vDash(t_1 \hat{=} t_2)[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)]\\
\end{align*}$$
negation of formula
implication of formula
quantifier of formula: suppose $\phi=(\forall x_i\psi)$
aim (LO$\Leftrightarrow$RO): $$\begin{align*}
    & \mathcal{M},\nu\vDash\phi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n) \Leftrightarrow \mathcal{M}\vDash\phi[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)]\\
\end{align*}$$
the structure of proof.
$$\begin{align*}
    &LO\Leftrightarrow_4 RO\\
    &\Updownarrow_1\quad\qquad\Updownarrow_3\\
    &LU\Leftrightarrow^2 RU\\
\end{align*}$$
$$\begin{align*}
    \mathcal{M},\nu\vDash\phi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n) &\Leftrightarrow_4 \mathcal{M}\vDash\phi[\overline{\nu}(\tau_1),\cdots,\overline{\nu}(\tau_n)]\\
    \Updownarrow_1\qquad\qquad\qquad&\qquad\qquad\qquad\Updownarrow_3\\
    \begin{matrix}
        \forall\mu,\mu(x_i)=\nu(x_i),i\le n,for\ all\\
        x_j\ is\ free\ variable\ in\ \phi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)\\
        \Rightarrow\mathcal{M},\mu\vDash\psi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)\\
    \end{matrix}&\Leftrightarrow_2\begin{matrix}
        \forall\mu,\mu(x_i)=\nu(x_i),i\le n,for\ all\\
        x_j\ is\ free\ variable\ in\ \phi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)\\
        \Rightarrow\mathcal{M}\vDash\psi[\overline{\mu}(\tau_1),\cdots,\overline{\mu}(\tau_n)]\\
    \end{matrix}\\
\end{align*}$$

we suppose that $1\le i\le n$ since that $x_i$ may be occurence freely in $\psi$. we assume that $\tau_i=x_i$ since that we should keep the occerence of $x_i$ in $\psi$ is bounded by the scope of $\forall x_i$ to prevent change the meaning of $\phi$. formulaly speaking, we have to make sure $(\forall x_i(\psi(x_1,\cdots,x_n,\tau_1,\cdots,\tau_n)))=(\forall x_i\psi)(x_1,\cdots,x_n,\tau_1,\cdots,\tau_n)$

$x_1,\cdots,x_n$ is free variable in $\psi$
$x_j,1\le j\le n,j\neq i$ is free variable in $\phi$, thus $x_j$ is free variable in $\phi(x_1,\cdots,x_n,\tau_1,\cdots,\tau_n)$ since that 
$x_i$ is bound variable in $\phi$, thus $x_i$ is bound variable in $\phi(x_1,\cdots,x_n,\tau_1,\cdots,\tau_n)$ since that $\tau_i=x_i$
Let $Var(\tau_1)\cup\cdots\cup Var(\tau_n)\subseteq\{x_1,x_2,\cdots,x_m\}$

(LU) LO$\Leftrightarrow$LU means for all $\mathcal{M}$-assignments $\mu$, if $\mu$ and $\nu$ agree on the free variables of $\phi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)$, then 
$$\begin{align*}
    & \mathcal{M},\mu\vDash\psi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)
\end{align*}$$
(RU) LU$\Leftrightarrow$RU in the underling form, for all $\mathcal{M}$-assignments $\mu$, if $\mu$ and $\nu$ agree on the free variables of $\phi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)$, then 
$$\begin{align*}
    & \mathcal{M}\vDash\psi[\overline{\mu}(\tau_1),\cdots,\overline{\mu}(\tau_n)]
\end{align*}$$
(RO) we want to show on the overling form of Right, for all $\mathcal{M}$-assignments $\rho$, for each $j$ such that $x_j$ appears freely in $\phi$, $\rho(x_j)=\overline{\nu}(\tau_j)$, then $\mathcal{M},\rho\vDash\psi$
RU$\Rightarrow$RO
def $$\mu_\rho(x_j)=\begin{cases}
    \nu(x_j),\ if\ x_j\ occurs\ freely\ in\ \phi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)\\
    \rho(x_j),\ otherwise
\end{cases}$$
since $\mu_\rho$ and $\nu$ agreed on the free varibales of $\phi(x_1,\cdots,x_n,\tau_1,\cdots,\tau_n)$ and RU thus $$\begin{align*}
    & \mathcal{M}\vDash\psi[\overline{\mu_\rho}(\tau_1),\cdots,\overline{\mu_\rho}(\tau_n)]
\end{align*}$$
according to lemma 3.5, $\overline{\mu_\rho}(\tau_j)=\overline{\nu}(\tau_j)=\rho(x_j),1\le j\le n,j\neq i$
$x_i$ is not freely occuring in $\phi(x_1,\cdots,x_n;\tau_1,\cdots,\tau_n)$ so $\mu_\rho(x_i)=\rho(x_i)$
Since $\mathcal{M}\vDash\psi[\overline{\mu_\rho}(\tau_1),\cdots,\overline{\mu_\rho}(\tau_n)]$, it follows from theorem 3.7 that $\mathcal{M},\rho\vDash\psi$

RO$\Rightarrow$RU
def
$$\rho_\mu(x_j)=\begin{cases}
    \overline{\mu}(\tau_j) & if\ x_j\ occurs\ freely\ in\ \phi\\
    \mu(x_j) & otherwise
\end{cases}$$
notice that $\tau_i$ is free for $x_i$ in $\phi$, so if $x_j$ is free in $\phi$, then $\overline{\mu}(\tau_j)=\overline{\nu}(\tau_j)=\rho_\mu(x_j)$ according to lemma 3.5
By condition 3, $\mathcal{M},\rho_\mu\vDash\psi$, that is $\mathcal{M}\vDash\psi[\rho_\mu(x_1),\cdots,\rho_\mu(x_n)]$
if $x_i$ is not free in $\phi$, then $\rho_\mu(x_i)=\mu(x_i)=\overline{\mu}(\tau_i)$ since $\tau_i=x_i$
so $\lang\rho_\mu(x_1),\cdots,\rho_\mu(x_n)\rang$ is equal to $\lang\overline{\mu}(\tau_1),\cdots,\overline{\mu}(\tau_n)\rang$, thus $\mathcal{M}\vDash\psi[\overline{\mu}(\tau_1),\cdots,\overline{\mu}(\tau_n)]$