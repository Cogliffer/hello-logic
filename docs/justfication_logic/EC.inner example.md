

## 具体公式

### Example C.1
记命题逻辑公理系统$\mathbf{LP}$公式构成为
$$\begin{align*}
    P::=p\ |\ \hat{\neg} P\ |\ P\hat{\rightarrow} P\\
\end{align*}$$
公理系统$\text{hybrid-}\mathbf{S4_f}$的公式构成为
$$\begin{align*}
    F::=P\ |\ \neg F\ |\ F\rightarrow F\ |\ \Box F
\end{align*}$$
外化公理：$\hat{\neg} P\rightarrow\neg P,(P\hat{\rightarrow} Q)\rightarrow(P\rightarrow Q)$
$(1)$ 任给$\mathbf{LP}$语言中的公式$P$，在系统$\text{hybrid-}\mathbf{S4_f}$中证明，如果$P$在$\mathbf{LP}$中（$P$是$\mathbf{LP}$中的定理），那么对于任意$\mathbf{LP}$语言中的公式$Q$，在$\mathbf{LP}$中可证$Q\hat{\rightarrow}P$。这个陈述的正确性使用命题逻辑上的导出引理立即得到，即已知$\mathbf{LP}\vdash P,\mathbf{LP}\vdash P\hat{\rightarrow}(Q\hat{\rightarrow} P)$，由导出引理，得$\mathbf{LP}\vdash Q\hat{\rightarrow} P$。现在将用$\text{hybrid-}\mathbf{S4_f}$的公理系统证明这个陈述，Let $@_i$ be $@_\mathbf{LP}$, we try to proof $@_iP\rightarrow @_i\Box(Q\hat{\rightarrow} P)$ is a theorem.
**Proof.**
$$\begin{align*}
    &(1)\ @_i\big(P\hat{\rightarrow}(Q\hat{\rightarrow} P)\big)\quad TAUT\ on\ \mathbf{LP}\\
    &(2)\ (P\hat{\rightarrow}(Q\hat{\rightarrow} P))\rightarrow(P\rightarrow(Q\hat{\rightarrow} P))\quad (*)\\
    &(3)\ @_i(P\hat{\rightarrow}(Q\hat{\rightarrow} P))\rightarrow @_i(P\rightarrow(Q\hat{\rightarrow} P))\quad 2,@NEC,K_@\\
    &(4)\ @_iP\rightarrow @_i(Q\hat{\rightarrow} P)\quad 1,3,MP\\
    &(5)\ (Q\hat{\rightarrow} P)\rightarrow\Box(Q\hat{\rightarrow} P)\quad \text{fact checker}\\
    &(6)\ @_i(Q\hat{\rightarrow} P)\rightarrow @_i\Box(Q\hat{\rightarrow} P)\quad 5,@NEC,K_@\\
    &(7)\ @_iP\rightarrow @_i\Box(Q\hat{\rightarrow} P)\quad 4,6
\end{align*}$$

$(2)$ 任给$\mathbf{LP}$语言中的公式$P$，在系统$\text{hybrid-}\mathbf{S4_f}$中证明，如果$P$在$\mathbf{LP}$中（$P$是$\mathbf{LP}$中的定理），那么对于任意$\mathbf{LP}$语言中的公式$Q$，可证$Q\hat{\rightarrow}P$在$\mathbf{LP}$中。Let $@_i$ be $@_\mathbf{LP}$, we try to proof $@_iP\rightarrow \Box @_i(Q\hat{\rightarrow} P)$ is a theorem.
**Proof.**
$$\begin{align*}
    &(1)\ @_iP\rightarrow\Box @_iP\quad \text{dual back}\\
    &(2)\ @_i(P\hat{\rightarrow}(Q\hat{\rightarrow} P))\quad TAUT\ on\ \mathbf{LP}\\
    &(3)\ (P\hat{\rightarrow}(Q\hat{\rightarrow} P))\rightarrow(P\rightarrow(Q\hat{\rightarrow} P))\quad (*)\\
    &(4)\ @_iP\rightarrow @_i(Q\hat{\rightarrow} P)\quad 3,@NEC,K_@,2,MP\\
    &(5)\ \Box @_iP\rightarrow \Box @_i(Q\hat{\rightarrow} P)\quad 4,NEC,K\\
    &(6)\ @_iP\rightarrow \Box @_i(Q\hat{\rightarrow} P)\quad 1,5
\end{align*}$$

<!-- 借助具体公式进一步分析内部可证和外部可证。第一个例子可证是指$\mathbf{LP}$中的可证，。我们不严格的称为内部可证和外部可证的区别。

两个证明都是从$\mathbf{LP}$的公理$P\hat{\rightarrow}(Q\hat{\rightarrow} P)$通过外化定理，得到$\text{hybrid-}\mathbf{S4_f}$上的定理$P\rightarrow(Q\hat{\rightarrow} P)$。

混合算子能够做到，在一个公理系统中推理另一个公理系统的定理。就是需要内化和外化公理。混合算子相当于一个标签，标明了当前推理所在的公理系统

证明的思路是将$\mathbf{LP}$中的定理外化到$\text{hybrid-}\mathbf{S4_f}$中，然后利用$\text{hybrid-}\mathbf{S4_f}$中的公理和规则给出证明再用混合算子$@_\mathbf{LP}$内化到$\mathbf{LP}$中。 -->

### Example C.2
在$\text{hybrid-}\mathbf{S4_f}$上用公理系统证明$\mathbf{LP}$的导出引理的简化版。即证任给$\mathbf{LP}$语言中的公式$P,Q$，如果$P,P\hat{\rightarrow}Q$是$\mathbf{LP}$中的定理，那么$Q$也是$\mathbf{LP}$中的定理。注意到下面三种表达是等价的
$$\begin{align*}
    &(1)\ @_iP\rightarrow (@_i(P\hat{\rightarrow} Q)\rightarrow\Box @_iQ)\\
    &(2)\ @_iP\rightarrow (@_i(P\hat{\rightarrow} Q)\rightarrow @_iQ)\\
    &(3)\ @_iP\rightarrow (@_i(P\hat{\rightarrow} Q)\rightarrow @_i\Box Q)\\
\end{align*}$$
Let $@_i$ be $@_\mathbf{LP}$, we try to proof $@_iP\rightarrow (@_i(P\hat{\rightarrow} Q)\rightarrow @_iQ)$ is a theorem.
**Proof.**
$$\begin{align*}
    &(1)\ @_i\big(P\hat{\rightarrow}((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\big)\quad TAUT\ on\ \mathbf{LP}\\
    &(2)\ \big(P\hat{\rightarrow}((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\big)\rightarrow\big(P\rightarrow((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\big)\quad (*)\\
    &(3)\ @_iP\rightarrow @_i( (P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\quad 2,@NEC,K_@,1,MP\\
    &(4)\ ((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\rightarrow((P\hat{\rightarrow} Q)\rightarrow Q)\quad (*)\\
    &(5)\ @_i((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\rightarrow(@_i(P\hat{\rightarrow} Q)\rightarrow @_i Q)\quad 4,@NEC,K_@\\
    &(6)\ @_iP\rightarrow (@_i(P\hat{\rightarrow} Q)\rightarrow @_iQ)\quad 3,5
\end{align*}$$
进一步可以通过演绎定理，证明完整的导出引理，不过我们不再补充这些繁琐的细节，而是考虑如何在我们的语言中给出这个证明过程，也就是给出一个具体的闭项证明了导出引理，作为内化定理的一个例子。
### Example C.3
在证明之前先引入项上的函数来简化证明。设$F\rightarrow M$为公理，在$\text{hybrid-}\mathbf{LPS4_f}$中，我们有如下推理
$$\begin{align*}
    &(1)\ c:@_i(F\rightarrow M)\quad \text{Iterated remote axiom necessitation}\\
    &(2)\ d:\big(@_i(F\rightarrow M)\rightarrow (@_iF\rightarrow @_iM)\big)\quad K_@,\text{Iterated axiom necessitation}\\
    &(3)\ d:\big(@_i(F\rightarrow M)\rightarrow (@_iF\rightarrow @_iM)\big)\rightarrow\\
    &\qquad \big(   c:@_i(F\rightarrow M)  \rightarrow dc:(@_iF\rightarrow @_iM)  \big)\quad application\\
    &(4)\ c:@_i(F\rightarrow M)  \rightarrow dc:(@_iF\rightarrow @_iM)\quad 3,2,MP\\
    &(5)\ dc:(@_iF\rightarrow @_iM)\quad 4,1,MP\\
\end{align*}$$
根据推理规则，常项$c,d$的选择是任意的，特殊的引入函数$f_k(c)=cc$，将推理简化为
$$\begin{align*}
    &(1)\ c:@_i(F\rightarrow M)\quad \\
    &(2)\ f_k(c):(@_iF\rightarrow @_iM)\quad 1,f_k\\
\end{align*}$$
像 Example A.4 and B.4 中一样，每次对公理实例引入常项证明时都使用了$\text{Iterated axiom necessitation}\ and\ \text{Iterated remote axiom necessitation}$规则，为了简化书写在下述证明过程中省略了标注。

Let $@_i$ be $@_\mathbf{LP}$, we try to proof $h\big(f_k(d)c\big)f_k(e):\big(@_iP\rightarrow (@_i(P\hat{\rightarrow} Q)\rightarrow @_iQ)\big)$ is a theorem where $c,d,e,h$ defined as follow.
**Proof.** 
$$\begin{align*}
    &(1)\ c:@_i\big(P\hat{\rightarrow}((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\big)\quad TAUT\ on\ \mathbf{LP}\\
    &(2)\ d:@_i\Big(\big(P\hat{\rightarrow}((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\big)\rightarrow\big(P\rightarrow((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\big)\Big)\quad (*)\\
    &(3)\ f_k(d)c:\big(@_iP\rightarrow @_i( (P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\big)\quad 2,f_k,1,MP\\
    &(4)\ e:@_i\big(((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\rightarrow((P\hat{\rightarrow} Q)\rightarrow Q)\big)\quad (*)\\
    &(5)\ h:\Big(\big(@_iP\rightarrow @_i( (P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\big)\rightarrow\qquad\qquad\qquad\qquad TAUT\\
    &\qquad \Big(\big(@_i((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\rightarrow(@_i(P\hat{\rightarrow} Q)\rightarrow @_i Q)\big)\rightarrow\big(@_iP\rightarrow (@_i(P\hat{\rightarrow} Q)\rightarrow @_iQ)\big)\Big)\Big)\\
    &(6)\ h\big(f_k(d)c\big):\Big(\big(@_i((P\hat{\rightarrow} Q)\hat{\rightarrow} Q)\rightarrow(@_i(P\hat{\rightarrow} Q)\rightarrow @_i Q)\big)\rightarrow\\
    &\qquad \big(@_iP\rightarrow (@_i(P\hat{\rightarrow} Q)\rightarrow @_iQ)\big)\Big)\quad 5,3,application\\
    &(7)\ h\big(f_k(d)c\big)f_k(e):\big(@_iP\rightarrow (@_i(P\hat{\rightarrow} Q)\rightarrow @_iQ)\big)\quad 6,4,f_k,application
\end{align*}$$
