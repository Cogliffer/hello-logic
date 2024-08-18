
## 外部证明(remote)

### Example B.1
任给命题符号$P$和系统$\Gamma$，在系统$\mathbf{S4}$中证明，如果$P$在$\Gamma$中（$P$是$\Gamma$中的定理），那么对于任意公式$F$，可证$F\rightarrow P$在$\Gamma$上为真。语言不能表达这个命题，但是从模型上的满足关系来看这是显然的，即证明，如果$\mathcal{M},\Gamma\vDash P$，那么可证$\mathcal{M},\Gamma\vDash F\rightarrow P$，根据满足关系的定义立刻得到可证。

### Example B.2
任给命题符号$P$和系统$\Gamma$，在系统$\text{hybrid-}\mathbf{S4}$中证明，如果$P$在$\Gamma$中（$P$是$\Gamma$中的定理），那么对于任意公式$F$，可证$F\rightarrow P$在$\Gamma$上为真。通过用混合算子表达满足关系，可以直接表达这一命题，并在公理系统上给出证明。Let $\mathcal{V}(i)=\Gamma$, we try to proof $@_iP\rightarrow\Box @_i(F\rightarrow P)$ is a theorem.

**Proof.**
$$\begin{align*}
    &(1)\ P\rightarrow(F\rightarrow P) \quad TAUT \\
    &(2)\ @_iP\rightarrow @_i(F\rightarrow P) \quad 1,@NEC,K_@\\
    &(3)\ @_i(F\rightarrow P)\rightarrow\Box @_i(F\rightarrow P) \quad dual-back\\
    &(4)\ @_iP\rightarrow\Box @_i(F\rightarrow P) \quad 2,3\\
\end{align*}$$

### Example B.3
任给命题符号$P$和系统$\Gamma$，在系统$\text{hybrid-}\mathbf{LPS4}$中证明，如果$P$在$\Gamma$中（$P$是$\Gamma$中的定理），那么对于任意公式$F$，可证$F\rightarrow P$在$\Gamma$上为真。Let $\mathcal{V}(i)=\Gamma$, we try to proof $@_iP\rightarrow dcf_i:@_i(F\rightarrow P)$ is a theorem where $d:(@_i(P\rightarrow(F\rightarrow P))\rightarrow(@_iP\rightarrow @_i(F\rightarrow P))), c:@_i(P\rightarrow(F\rightarrow P)), f_i:@_iP$.

**Proof.**
$$\begin{align*}
    &(1)\ @_iP\rightarrow f_i:@_iP\quad \text{remote fact checker}\\
    &(2)\ c:@_i(P\rightarrow(F\rightarrow P))\quad TAUT,@NEC,\text{Iterated remote axiom necessitation}\\
    &(3)\ d:(@_i(P\rightarrow(F\rightarrow P))\rightarrow(@_iP\rightarrow @_i(F\rightarrow P)))\quad K_@,\text{Iterated axiom necessitation}\\
    &(4)\ dc:(@_iP\rightarrow @_i(F\rightarrow P))\quad 2,3,application\\
    &(5)\ dc:(@_iP\rightarrow @_i(F\rightarrow P))\rightarrow\\
    &\qquad (f_i:@_iP\rightarrow dcf_i:@_i(F\rightarrow P))\quad application\\
    &(6)\ f_i:@_iP\rightarrow dcf_i:@_i(F\rightarrow P)\quad 9,10,MP\\
    &(7)\ (@_iP\rightarrow f_i:@_iP)\rightarrow\\
    &\qquad ((f_i:@_iP\rightarrow dcf_i:@_i(F\rightarrow P))\rightarrow(@_iP\rightarrow dcf_i:@_i(F\rightarrow P)))\quad TAUT\\
    &(8)\ @_iP\rightarrow dcf_i:@_i(F\rightarrow P)\quad 12,1,11,MP
\end{align*}$$

### Example B.4
同样的，根据内化定理，依据 Example B.3 中的证明给出一个闭项。

**Proof.**
$$\begin{align*}
    &(1)\ e:(@_iP\rightarrow f_i:@_iP)\quad \text{remote fact checker},\text{Iterated axiom necessitation}\\
    &(2)\ (!c):c:@_i(P\rightarrow(F\rightarrow P))\quad \\
    &\qquad\quad TAUT,\text{Iterated remote axiom necessitation},\text{proof checker}\\
    &(3)\ (!d):d:(@_i(P\rightarrow(F\rightarrow P))\rightarrow(@_iP\rightarrow @_i(F\rightarrow P)))\quad \\
    &\qquad\qquad\qquad\qquad\qquad K_@,\text{Iterated axiom necessitation},\text{proof checker}\\
    &(4)\ h:\Big(d:\big(@_i(P\rightarrow(F\rightarrow P))\rightarrow(@_iP\rightarrow @_i(F\rightarrow P))\big)\rightarrow\\
    &\qquad \big(c:@_i(P\rightarrow(F\rightarrow P))\rightarrow dc:(@_iP\rightarrow @_i(F\rightarrow P))\big)\Big) \\
    &\qquad\qquad\qquad\qquad\qquad\qquad\qquad application,\text{Iterated axiom necessitation}\\
    &(5)\ h!d!c:dc:(@_iP\rightarrow @_i(F\rightarrow P))\quad 4,3,2,application\\
    &(6)\ j:\big(dc:(@_iP\rightarrow @_i(F\rightarrow P))\rightarrow(f_i:@_iP\rightarrow dcf_i:@_i(F\rightarrow P))\big)\quad \\
    &\qquad\qquad\qquad\qquad\qquad\quad\qquad application,\text{Iterated axiom necessitation}\\
    &(8)\ k:\big((@_iP\rightarrow f_i:@_iP)\rightarrow\\
    &\qquad ((f_i:@_iP\rightarrow dcf_i:@_i(F\rightarrow P))\rightarrow(@_iP\rightarrow dcf_i:@_i(F\rightarrow P)))\big)\quad \\
    &\qquad\qquad\qquad\qquad\qquad\qquad\qquad TAUT,\text{Iterated axiom necessitation}\\
    &(9)\ ke\big(j(h!d!c)\big):(@_iP\rightarrow dcf_i:@_i(F\rightarrow P))\quad 12,1,6,5,application
\end{align*}$$