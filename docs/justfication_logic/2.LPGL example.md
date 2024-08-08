### Example D.1
记公理系统$\mathbf{LPGL}$的公式构成为
$$\begin{align*}
    &u::= c\ |\ x\ |\ (u\cdot u)\ |\ (u+u)\ |\ !u\\
    &P::= p\ |\ \neg P\ |\ P\rightarrow P\ |\ \Box P\ |\ u:P
\end{align*}$$
we try to proof $\mathbf{LPGL}\vdash u:\Box P\rightarrow P$
**Proof.**
$$\begin{align*}
    &(1)\ u:\Box P\rightarrow\Box P\quad Factivity\quad\\
    &(2)\ \neg\Box P\rightarrow\neg u:\Box P\quad 1\\
    &(3)\ \neg u:\Box P\rightarrow\Box(\neg u:\Box P)\quad \text{weak negative introspection}\\
    &(4)\ \Box(\neg u:\Box P)\rightarrow\Box(u:\Box P\rightarrow P)\quad TAUT,NEC,K\\
    &(5)\ \neg\Box P\rightarrow\Box(u:\Box P\rightarrow P)\quad 2,3,4\\
    &(6)\ \Box P\rightarrow\Box(u:\Box P\rightarrow P)\quad TAUT,NEC,K\\
    &(7)\ \Box(u:\Box P\rightarrow P)\quad 5,6\\
    &(8)\ u:\Box P\rightarrow P\quad 7,\text{reflexivity rule}
\end{align*}$$

### Example D.2
记公理系统$\text{hybrid-}\mathbf{S4_f}$的公式构成为
$$\begin{align*}
    F::= i\ |\ P\ |\ \hat{\neg} F\ |\ F\hat{\rightarrow} F\ |\ \hat{\Box} F\ |\ @_i F
\end{align*}$$
外化公理：$\neg P\rightarrow\hat{\neg} P,(P\rightarrow Q)\hat{\rightarrow}(P\hat{\rightarrow} Q)$
Let $@_i$ be $@_\mathbf{LPGL}$, we try to proof $@_i(u:\Box P\rightarrow P) $ is a theorem.
**Proof.** 
$$\begin{align*}
    &(1)\ @_i(u:\Box P\rightarrow\Box P) \quad Factivity\ on\ \mathbf{LPGL}\\
    &(2)\ @_i((u:\Box P\rightarrow\Box P)\rightarrow(\neg\Box P\rightarrow\neg u:\Box P)) \quad TAUT \ on\ \mathbf{LPGL}\\
    &(3)\ @_i(u:\Box P\rightarrow\Box P)\hat{\rightarrow}@_i(\neg\Box P\rightarrow\neg u:\Box P)\quad 2,(*),K_@\\
    &(4)\ @_i(\neg\Box P\rightarrow\neg u:\Box P)\quad 1,3,MP\\
    &(5)\ @_i(\neg u:\Box P\rightarrow\Box(\neg u:\Box P)) \quad \text{weak negative introspection} \ on\ \mathbf{LPGL}\\ 
    &(6)\ @_i(\neg u:\Box P\rightarrow(u:\Box P\rightarrow P)) \quad TAUT \ on\ \mathbf{LPGL} \\
    &(7)\ @_i(\Box(\neg u:\Box P)\rightarrow\Box(u:\Box P\rightarrow P)) \quad 6,NEC,K \ on\ \mathbf{LPGL}\\ 
    &(8)\ @_i\bigg((\neg\Box P\rightarrow\neg u:\Box P)\rightarrow\Big((\neg u:\Box P\rightarrow\Box(\neg u:\Box P))\rightarrow\notag\\
    &\qquad\big((\Box(\neg u:\Box P)\rightarrow\Box(u:\Box P\rightarrow P))\rightarrow(\neg\Box P\rightarrow\Box(u:\Box P\rightarrow P))\big)\Big)\bigg)\quad \\
    &\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad TAUT \ on\ \mathbf{LPGL} \\
    &(9)\ @_i(\neg\Box P\rightarrow\neg u:\Box P)\hat{\rightarrow}\Big(@_i(\neg u:\Box P\rightarrow\Box(\neg u:\Box P))\hat{\rightarrow}\notag\\
    &\qquad\big(@_i(\Box(\neg u:\Box P)\rightarrow\Box(u:\Box P\rightarrow P))\hat{\rightarrow}@_i(\neg\Box P\rightarrow\Box(u:\Box P\rightarrow P))\big)\Big)\quad \\
    &\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad 8,(*),K_@ \\
    &(10)\ @_i(\neg\Box P\rightarrow\Box(u:\Box P\rightarrow P))\quad 9,4,7,8,MP\\
    &(11)\ @_i(P\rightarrow(u:\Box P\rightarrow P))\quad TAUT \ on\ \mathbf{LPGL} \\
    &(12)\ @_i(\Box P\rightarrow\Box(u:\Box P\rightarrow P))\quad 11,NEC,K\ on\ \mathbf{LPGL} \\
    &(13)\ @_i\Big((\neg\Box P\rightarrow\Box(u:\Box P\rightarrow P))\rightarrow\\
    &\qquad \big((\Box P\rightarrow\Box(u:\Box P\rightarrow P))\rightarrow\Box(u:\Box P\rightarrow P)\big)\Big) TAUT \ on\ \mathbf{LPGL} \\
    &(14)\ @_i(\neg\Box P\rightarrow\Box(u:\Box P\rightarrow P))\hat{\rightarrow}\\
    &\qquad \big(@_i(\Box P\rightarrow\Box(u:\Box P\rightarrow P))\hat{\rightarrow}@_i\Box(u:\Box P\rightarrow P)\big) \quad 13,(*),K_@ \\ 
    &(15)\ @_i\Box(u:\Box P\rightarrow P)\quad 14,10,12,MP\\
    &(16)\ @_i(u:\Box P\rightarrow P)\quad \text{reflexivity rule}\ on\ \mathbf{LPGL}
\end{align*}$$

我们没法使用下层逻辑的规则，但是公理可以用，规则被外化到主语言中了，用term上的函数表示


用term内化了模型中系统的可证的公式的具体的证明过程，这是有趣的。因为term提供了一种证明的核心直觉，非常的简洁，清晰的刻画了证明的关键步骤。
term不仅能够内化外部证明，也能在给出下层系统之后，内化内部证明
成为可以用的推理规则

### Example D.3
下层逻辑$\mathbf{LPGL}$：
$\hat{u}::= c\ |\ x\ |\ (u\cdot u)\ |\ (u+u)\ |\ !u$
$P::= p\ |\ \neg P\ |\ P\rightarrow P\ |\ \Box P\ |\ \hat{u}:P$
函数：
$ f_{nec}(t)$ 对应$\mathbf{LPGL}$中的$NEC$规则；
$ f_{r}(t)$ 对应$\mathbf{LPGL}$中的$\text{reflexivity rule}$规则；
$ f_{k}(t)$ 对应$\mathbf{LPGL}$中的$K$规则；
$$\begin{align*}
    &(1)\ c:(\hat{u}:\Box P\rightarrow\Box P) \quad Factivity \\
    &(2)\ d:((\hat{u}:\Box P\rightarrow\Box P)\rightarrow(\neg\Box P\rightarrow\neg \hat{u}:\Box P)) \quad TAUT  \\
    &(3)\ dc:(\neg\Box P\rightarrow\neg \hat{u}:\Box P)\quad 2,1,Application\\
    &(4)\ h:(\neg \hat{u}:\Box P\rightarrow\Box(\neg \hat{u}:\Box P)) \quad \text{weak negative introspection}  \\ 
    &(5)\ j:(\neg \hat{u}:\Box P\rightarrow(\hat{u}:\Box P\rightarrow P)) \quad TAUT   \\
    &(6)\ f_kf_{nec}(j):(\Box(\neg \hat{u}:\Box P)\rightarrow\Box(\hat{u}:\Box P\rightarrow P)) \quad\\ 
    &(7)\ m:\bigg((\neg\Box P\rightarrow\neg \hat{u}:\Box P)\rightarrow\Big((\neg \hat{u}:\Box P\rightarrow\Box(\neg \hat{u}:\Box P))\rightarrow\notag\\
    &\qquad\big((\Box(\neg \hat{u}:\Box P)\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\rightarrow(\neg\Box P\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\big)\Big)\bigg)\quad \\
    &\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad TAUT   \\
    &(8)\ m(dc)h(f_kf_{nec}(j)):(\neg\Box P\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\quad 7,3,4,6,Application\\
    &(9)\ n:(P\rightarrow(\hat{u}:\Box P\rightarrow P))\quad TAUT   \\
    &(10)\ o:\Big((\neg\Box P\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\rightarrow\\
    &\qquad \big((\Box P\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\rightarrow\Box(\hat{u}:\Box P\rightarrow P)\big)\Big)\quad  TAUT   \\
    &(11)\ o\big(m(dc)h(f_kf_{nec}(j))\big)(f_kf_{nec}(n)):\Box(\hat{u}:\Box P\rightarrow P)\quad 10,8,9,application\\
    &(12)\ f_r\Big(o\big(m(dc)h(f_kf_{nec}(j))\big)(f_kf_{nec}(n))\Big):(\hat{u}:\Box P\rightarrow P)\quad 11,\text{reflexivity rule} 
\end{align*}$$

### Example D.4

上层逻辑$\text{hybrid-}\mathbf{LPS4_f}$：
$t::= c\ |\ x\ |\ t\cdot t\ |\ t+t\ |\ !t\ |\ !_it\ |\ ?_it\ |\ f_{nec}(t)\ |\ f_r(t)$
$F::= i\ |\ P\ |\ \hat{\neg} F\ |\ F\hat{\rightarrow} F\ |\ \hat{\Box} F\ |\ @_i F\ |\ t:F$
并使用函数$ g_{nec}(t)$,$ g_{k}(t)$简化证明过程：
$ g_{k}(t)$ 对应$\text{hybrid-}\mathbf{LPS4_f}$中的$K_@$规则；
同时为了书写的紧凑，使用符号$\underline{t}$表示函数$g_k(t)$，符号$\tilde{t}$表示函数$f_kf_{nec}(t)$
**Proof.** Let $@_i$ be $@_\mathbf{LPGL}$
$$\begin{align*}
    &(1)\ c:@_i(\hat{u}:\Box P\rightarrow\Box P) \quad Factivity\ on\ \mathbf{LPGL}\\
    &(2)\ d:@_i((\hat{u}:\Box P\rightarrow\Box P)\rightarrow(\neg\Box P\rightarrow\neg \hat{u}:\Box P)) \quad TAUT \ on\ \mathbf{LPGL}\\
    &(3)\ \underline{d}c:@_i(\neg\Box P\rightarrow\neg \hat{u}:\Box P)\quad 2,(*),g_k,1,Application\\
    &(4)\ h:@_i(\neg \hat{u}:\Box P\rightarrow\Box(\neg \hat{u}:\Box P)) \quad \text{weak negative introspection} \ on\ \mathbf{LPGL}\\ 
    &(5)\ j:@_i(\neg \hat{u}:\Box P\rightarrow(\hat{u}:\Box P\rightarrow P)) \quad TAUT \ on\ \mathbf{LPGL} \\
    &(6)\ \tilde{j}:@_i(\Box(\neg \hat{u}:\Box P)\rightarrow\Box(\hat{u}:\Box P\rightarrow P)) \quad\\ 
    &(7)\ m:@_i\bigg((\neg\Box P\rightarrow\neg \hat{u}:\Box P)\rightarrow\Big((\neg \hat{u}:\Box P\rightarrow\Box(\neg \hat{u}:\Box P))\rightarrow\notag\\
    &\qquad\big((\Box(\neg \hat{u}:\Box P)\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\rightarrow(\neg\Box P\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\big)\Big)\bigg)\quad \\
    &\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad TAUT \ on\ \mathbf{LPGL} \\
    &(8)\ \underline{\underline{\underline{m}\,\underline{d}c}h}\tilde{j}:@_i(\neg\Box P\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\quad \\
    &\qquad\qquad\qquad\qquad\qquad\qquad\qquad 7,(*),g_k,3,g_k,4,g_k,6,g_k,Application\\
    &(9)\ n:@_i(P\rightarrow(\hat{u}:\Box P\rightarrow P))\quad TAUT \ on\ \mathbf{LPGL} \\
    &(10)\ o:@_i\Big((\neg\Box P\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\rightarrow\\
    &\qquad\big((\Box P\rightarrow\Box(\hat{u}:\Box P\rightarrow P))\rightarrow\Box(\hat{u}:\Box P\rightarrow P)\big)\Big)\quad TAUT \ on\ \mathbf{LPGL} \\
    &(11)\ \underline{\underline{o}\,\underline{\underline{\underline{m}\,\underline{d}c}h}\tilde{j}}\tilde{n}: @_i\Box(\hat{u}:\Box P\rightarrow P)\quad\qquad 10,(*),g_k,8,g_k,9,application\\
    &(12)\ f_r\Big(\underline{\underline{o}\,\underline{\underline{\underline{m}\,\underline{d}c}h}\tilde{j}}\tilde{n}\Big): @_i\Box(\hat{u}:\Box P\rightarrow P)\quad\qquad\qquad 11,\text{reflexivity rule} \\
\end{align*}$$

这个例子体现出混合算子的必要性。让系统中的定理转化为公理系统中的定理。从而能够公理化方法推理。

四个例子构成平行关系，总结内化定理。

给出的证明项，要求都是从公理出发的，这保证了证明的可靠性，不会出现跳步