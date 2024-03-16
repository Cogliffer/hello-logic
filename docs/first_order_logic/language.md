
<h1>First Order Logic</h1>

# Language

*logical symbles* : $(,),\neg,\to,\forall$
*variable symble* : $x_i,i\in\mathbb{N}$
*constant symble* : $c_i,i\in\mathbb{N}$
*function symble* : $F_i,i\in\mathbb{N}$
*predicate symble* : $P_i,i\in\mathbb{N}$
*identity symble* : $=$
$\rho:\{F_i\}_{i\in\mathbb{N}}\to\mathbb{N}$
$\tau:\{P_i\}_{i\in\mathbb{N}}\to\mathbb{N}$

donation
$x_i$ is $\langle x_i \rangle$
$c_i$ is $\langle c_i \rangle$
$F_i(t_1,t_2,\cdots,t_n)$ is $\langle F_i \rangle+\langle ( \rangle+t_1+t_2+\cdots+t_n+\langle ) \rangle$
$P_i(t_1,t_2,\cdots,t_n)$ is $\langle P_i \rangle+\langle ( \rangle+t_1+t_2+\cdots+t_n+\langle ) \rangle$
$VS(x )$ means $x$ is a variable symbol
$CS(x)$ means $x$ is an constant symbol
$FS(x)$ means $x$ is a function symbol
$PS(x)$ means $x$ is a predicate symbol
$(\veebar: p_1\veebar: p_2\cdots\veebar: p_n)$ donate (case: $p_1$ case: $p_2\cdots$ case: $p_n$) means $p_1\text{ or }p_2\text{ or }\cdots\text{ or }p_n$ and $p_i\Rightarrow\text{ not } p_j,j\ne i$
<!-- 在不同的逻辑系统中，如何取非是需要定义的，neg操作取决于不同的系统 -->

*terms set* is the smallest set of finite sequences $T$ satisfying the following properties
(1) $\forall i\in\mathbb{N},x_i\in T,c_i\in T$ <!-- \forall i\in\mathbb{N},x_i,c_i\in T的写法不利于机器读取，具有含混的逗号，使用\text{ and }-->
(2) $n=\rho(F_i)\text{ and }t_1,t_2,\cdots,t_n\in T\Rightarrow F_i(t_1,t_2,\cdots,t_n)\in T$

*Term Readability*
$$\begin{align*}
    t \in T \Rightarrow &\veebar:\exist x, VS(x), t=x \\
    &\veebar:\exist c, CS(c), t=c \\
    &\veebar:\exist F, FS(F),\exist t_1,t_2,\cdots,t_{\rho(F)}\in T,t=F(t_1,t_2,\cdots,t_{\rho(F)})
\end{align*}$$

*Lemma*
$\forall t \in T$
no proper initial segment of $t$ is an element of $T$

*Unique Readability*
$\forall t \in T\Rightarrow$
$t$ is readability and unique

# Formulas

*formulas set* $\mathcal{L}$ is the smallest set of finite sequences of symbles satisfying the following properties
$PS(P)\text{ and }t_1,t_2,\cdots,t_{\rho(P)}\in T\Rightarrow P(t_1,t_2,\cdots,t_{\rho(P)})\in\mathcal{L}$
$t_1,t_2\in T\Rightarrow(t_1=t_2)\in\mathcal{L}$
$\phi\in\mathcal{L}\Rightarrow(\neg\phi)\in\mathcal{L}$
$\phi,\psi\in\mathcal{L}\Rightarrow(\phi\to\psi)\in\mathcal{L}$
$\phi\in\mathcal{L},VS(x)\Rightarrow(\forall x\phi)\in\mathcal{L}$

*Unique Readability*
$$\begin{align*}
    \phi\in\mathcal{L}\Rightarrow &\veebar: \exist P, PS(P),\exist t_1,t_2,\cdots,t_{\rho(P)}\in T,\phi=P(t_1,t_2,\cdots,t_{\rho(P)})\\
    & \veebar: \exist t_1,t_2\in T,\phi=(t_1=t_2)\\
    & \veebar: \exist\psi\in\mathcal{L},\phi=(\neg\psi)\\
    & \veebar: \exist\psi_1,\psi_2\in\mathcal{L},\phi=(\psi_1\to\psi_2)\\
    & \veebar: \exist x,VS(x),\exist\psi\in\mathcal{L},\phi=(\forall x\psi)\\
\end{align*}$$

*Lemma*
$\forall \phi \in \mathcal{L}$
no proper initial segment of $\phi$ is a formula of $\mathcal{L}$

## free variables and bound variables
$\forall\phi\in\mathcal{L},(VS(x),\phi=s+\langle\forall,x\rangle+t\Rightarrow\exist\psi\in\mathcal{L},\mathrm{Unique}(\psi),\exist s',t', s=s'+\langle(\rangle,\phi=s'+\langle(,\forall,x,)\rangle+\psi+t')$
$\psi$ is called the scope formula of variable symble $x$ in $\phi$, donated by $\mathrm{Scope}(\phi,x)$
$$\begin{align*}
    VS(x),\langle x\rangle\in\phi\in\mathcal{L}\Rightarrow&\mathrm{Free}(x)\equiv_{def}\forall\mathrm{Scope}(\phi,x),\langle x\rangle\notin\mathrm{Scope}(\phi,x)\\
    &\mathrm{Bound}(x)\equiv_{def}\exist\mathrm{Scope}(\phi,x),\langle x\rangle\in\mathrm{Scope}(\phi,x)\\
\end{align*}$$