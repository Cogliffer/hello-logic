
## 附录
## 内部证明(close)

### Example A.1
任给命题符号$P$和系统$\Gamma$，在系统$\mathbf{S4_f}$中证明，如果$P$在$\Gamma$中（$P$是$\Gamma$中的定理），那么对于任意公式$F$，在$\Gamma$上可证$F\rightarrow P$。语言不能表达这个命题，但是能够从语义上用模型上的满足关系来表达，即证明，如果$\mathcal{M},\Gamma\vDash P$，那么$\mathcal{M},\Gamma\vDash\Box(F\rightarrow P)$，从而能够用公理系统给出证明。
**Proof.** $$\begin{align*}
    &(1)\ P\rightarrow \Box P\quad \text{fact checker}\\
    &(2)\ P\rightarrow(F\rightarrow P)\quad TAUT \\
    &(3)\ \Box(P\rightarrow(F\rightarrow P))\quad 2,NEC \\
    &(4)\ \Box(P\rightarrow(F\rightarrow P))\rightarrow(\Box P\rightarrow\Box(F\rightarrow P))\quad K \\
    &(5)\ \Box P\rightarrow\Box(F\rightarrow P)\quad 3，4,MP \\
    &(6)\ (P\rightarrow \Box P)\rightarrow((\Box P\rightarrow\Box(F\rightarrow P))\rightarrow(P\rightarrow\Box(F\rightarrow P)))\quad TAUT\\
    &(7)\ (\Box P\rightarrow\Box(F\rightarrow P))\rightarrow(P\rightarrow\Box(F\rightarrow P))\quad 1,6,MP\\
    &(8)\ P\rightarrow\Box(F\rightarrow P)\quad 5,7,MP
\end{align*}$$

### Example A.2
任给命题符号$P$和系统$\Gamma$，在系统$\text{hybrid-}\mathbf{S4_f}$中证明，如果$P$在$\Gamma$中（$P$是$\Gamma$中的定理），那么对于任意公式$F$，在$\Gamma$上可证$F\rightarrow P$。通过用混合算子表达满足关系，可以直接表达这一命题，并在公理系统上给出证明。Let $\mathcal{V}(i)=\Gamma$, We try to proof $@_iP\rightarrow @_i\Box(F\rightarrow P)$ is a theorem.

**Proof.** 
$$\begin{align*}
    &(1)\ \cdots\\
    &\ \ \vdots\qquad\ \ \  \vdots\\
    &(8)\ P\rightarrow\Box(F\rightarrow P)\quad \\
    &(9)\ @_i(P\rightarrow\Box(F\rightarrow P))\quad 8,@NEC\\
    &(10)\ @_i(P\rightarrow\Box(F\rightarrow P))\rightarrow(@_i P\rightarrow @_i\Box(F\rightarrow P))\quad K_@\\
    &(11)\ @_i P\rightarrow @_i\Box(F\rightarrow P)\quad 9,10,MP\\
\end{align*}$$

### Example A.3
任给命题符号$P$和系统$\Gamma$，在系统$\text{hybrid-}\mathbf{LPS4_f}$中证明，如果$P$在$\Gamma$中（$P$是$\Gamma$中的定理），那么对于任意公式$F$，在$\Gamma$上给出$F\rightarrow P$的证明。加入项后，能够将可证具体化为给出证明。Let $\mathcal{V}(i)=\Gamma$, We try to proof $@_iP\rightarrow @_i(c\cdot f_i):(F\rightarrow P)$ is a theorem, where $c:(P\rightarrow(F\rightarrow P)),f_i:P$.

**Proof.** 
$$\begin{align*}
    &(1)\ @_iP\rightarrow @_i f_i:P\quad \text{close fact checker} \\
    &(2)\ P\rightarrow(F\rightarrow P)\quad TAUT\\
    &(3)\ c:(P\rightarrow(F\rightarrow P))\quad 2,\text{Iterated axiom necessitation}\\
    &(4)\ c:(P\rightarrow(F\rightarrow P))\rightarrow(f_i:P\rightarrow(c\cdot f_i):(F\rightarrow P))\quad application\\
    &(5)\ f_i:P\rightarrow(c\cdot f_i):(F\rightarrow P)\quad 3,4,MP\\
    &(6)\ @_i(f_i:P\rightarrow(c\cdot f_i):(F\rightarrow P))\quad @NEC\\
    &(7)\ @_i(f_i:P\rightarrow(c\cdot f_i):(F\rightarrow P))\rightarrow(@_i f_i:P\rightarrow @_i(c\cdot f_i):(F\rightarrow P))\quad K_@\\
    &(8)\ @_i f_i:P\rightarrow @_i(c\cdot f_i):(F\rightarrow P)\quad 6,7,MP\\
    &(9)\ (@_iP\rightarrow @_i f_i:P)\rightarrow\\
    &\qquad ((@_i f_i:P\rightarrow @_i(c\cdot f_i):(F\rightarrow P))\rightarrow(@_iP\rightarrow @_i(c\cdot f_i):(F\rightarrow P)))\quad TAUT\\
    &(10)\ (@_i f_i:P\rightarrow @_i(c\cdot f_i):(F\rightarrow P))\rightarrow(@_iP\rightarrow @_i(c\cdot f_i):(F\rightarrow P))\quad 1,9,MP\\
    &(11)\ @_iP\rightarrow @_i(c\cdot f_i):(F\rightarrow P)\quad 8,10,MP
\end{align*}$$

### Example A.4
**Theorem.** (Internalization) If $F$ is a theorem of $\text{hybrid-}\mathbf{LPS4_f}$, then there is a closed justification term $t$ such that $t:F$ is also a theorem.
根据内化定理，既然 Example A.3 中的结论是$\text{hybrid-}\mathbf{LPS4_f}$上的定理，那么存在一个封闭项$t$使得$t:F$也是定理。我们现在就依据 Example A.3 中的证明给出一个这样的闭项。

**Proof.** 
$$\begin{align*}
    &(1)\ d:(@_iP\rightarrow @_i f_i:P)\quad \text{close fact checker},\text{Iterated axiom necessitation}\\
    &(2)\ c:@_i(P\rightarrow(F\rightarrow P))\quad TAUT,\text{Iterated remote axiom necessitation}\\
    &(3)\ @_ic:@_i(P\rightarrow(F\rightarrow P))\quad 2,@NEC\\
    &(4)\ !_ic:@_ic:@_i(P\rightarrow(F\rightarrow P))\quad 3,\text{remote positive justification checker}\\
    &(5)\ e:@_i\Big(c:(P\rightarrow(F\rightarrow P))\rightarrow\big(f_i:P\rightarrow(c\cdot f_i):(F\rightarrow P)\big)\Big)\quad\\
    &\qquad\qquad\qquad application,\text{Iterated remote axiom necessitation}\\
    &(6)\ h:\bigg(@_i\Big(c:(P\rightarrow(F\rightarrow P))\rightarrow\big(f_i:P\rightarrow(c\cdot f_i):(F\rightarrow P)\big)\Big)\rightarrow\\
    &\qquad \Big(@_ic:(P\rightarrow(F\rightarrow P))\rightarrow @_i \big(f_i:P\rightarrow(c\cdot f_i):(F\rightarrow P)\big)\Big)\bigg)\quad\\
    &\qquad\qquad\qquad\qquad\qquad\qquad\qquad K_@,\text{Iterated axiom necessitation}\\
    &(7)\ he!_ic:@_i \big(f_i:P\rightarrow(c\cdot f_i):(F\rightarrow P)\big)\quad 6,5,4,application\\
    &(8)\ j:\Big(@_i\big(f_i:P\rightarrow(c\cdot f_i):(F\rightarrow P)\big)\rightarrow\big(@_i f_i:P\rightarrow @_i(c\cdot f_i):(F\rightarrow P)\big)\Big)\quad\\
    &\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad K_@,\text{Iterated axiom necessitation}\\
    &(9)\ j(he!_ic):\big(@_i f_i:P\rightarrow @_i(c\cdot f_i):(F\rightarrow P)\big)\quad 8,7,application\\
    &(10)\ k:\Big((@_iP\rightarrow @_i f_i:P)\rightarrow\\
    &\qquad \Big(\big(@_i f_i:P\rightarrow @_i(c\cdot f_i):(F\rightarrow P)\big)\rightarrow\big(@_iP\rightarrow @_i(c\cdot f_i):(F\rightarrow P)\big)\Big)\Big)\quad \\
    &\qquad\qquad\qquad\qquad\qquad\quad\qquad TAUT,\text{Iterated axiom necessitation}\\
    &(11)\ kd\big(j(he!_ic)\big):@_iP\rightarrow @_i(c\cdot f_i):(F\rightarrow P)\quad 10,1,9,application
\end{align*}$$
