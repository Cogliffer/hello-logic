

## $\Box F$ and $t:F$
[Sergei Artemov, Elena Nogina, Logic of knowledge with justifications from the provability perspective., 2004]
[Sergei Artemov, Elena Nogina, Introducing Justification into Epistemic, 2005]
Language: 
$t::= c\ |\ x\ |\ (t\cdot t)\ |\ (t+t)\ |\ !t$
$F::= i\ |\ p\ |\ \neg F\ |\ F\rightarrow F\ |\ \Box F\ |\ t:F$
$\textbf{LPGL}$:
直觉：$\Box F$表达$F$可证，$t:F$表达$t$是$F$的证明
Axioms:
$$\begin{align*}
    & (TAUT)\\
    & (K,dual,4/\text{implicit proof checker})\\
    & (\text{Lob schema}) & \Box(\Box F\rightarrow F)\rightarrow\Box F\\
    & (\cdot,+,\text{Factivity})\\
    & (\text{proof checker}) & t:F\rightarrow !t:t:F \\
    & (\text{connection}) & t:F\rightarrow \Box F \\
    & (\text{weak negative introspection}) & \neg t:F\rightarrow \Box\neg t:F \\
    & (\text{weak reflexivity}) & t:\Box F\rightarrow F\\
\end{align*}$$
Rules: $(\text{MP, NEC, Iterated axiom necessitation})$
$\qquad\ ^*(\text{reflexivity rule}) \qquad \Box F/F$
$\text{Lob schema}$公理与$T$公理是不相容的，因为对于任意的$F$有证明序列$\Box F\rightarrow F,\Box(\Box F\rightarrow F),\Box(\Box F\rightarrow F)\rightarrow\Box F,\Box F,F$，但是$\textbf{LPGL}$中可以具有$\text{reflexivity rule}$（推测这个系统使用可能世界语义会有些奇怪）。
### 算数语义：
$$\begin{align*}
    \mathsf{PA}\vdash\varphi\ \Leftrightarrow\ \text{for some }n\in\omega\quad Prf(n,\ulcorner\varphi\urcorner)\text{holds}.\quad \ulcorner\varphi\urcorner\text{ is the Gödel number of }\varphi.
\end{align*}$$
存在可计算函数$\mathsf{m}(x,y),\mathsf{a}(x,y),\mathsf{c}(x)$使得
$$\begin{align*}
    Prf(k,\ulcorner\varphi\rightarrow\psi\urcorner)\land Prf(n,\ulcorner\varphi\urcorner)\rightarrow Prf(\mathsf{m}(k,n),\ulcorner\psi\urcorner)\\
    Prf(k,\ulcorner\varphi\urcorner)\rightarrow Prf(\mathsf{a}(k,n),\ulcorner\varphi\urcorner)\\
    Prf(n,\ulcorner\varphi\urcorner)\rightarrow Prf(\mathsf{a}(k,n),\ulcorner\varphi\urcorner)\\
    Prf(k,\ulcorner\varphi\urcorner)\rightarrow Prf(\mathsf{c}(k),\ulcorner Prf(k,\ulcorner\varphi\urcorner)\urcorner)\\
\end{align*}$$
翻译$F^*$
$$\begin{align*}
    (t\cdot s)^* = \mathsf{m}(t^*,s^*),\ (t+s)^* = \mathsf{a}(t^*,s^*),\  (!t)^* = \mathsf{c}(t^*),\\
    (t:F)^* = Prf(t^*,\ulcorner F^* \urcorner),\ (\Box F)^* = \exist x Prf(x,\ulcorner F^* \urcorner).\\
\end{align*}$$

$\textbf{LPS4}\text{ and }\textbf{LPS4}^{-}$:
直觉：$\Box F$表达潜在的（大概的，直觉上）知道（相信）$F$，$t:F$表达因为证据（推理）$t$（实际的，具体过程的，有理有据的）知道（相信）$F$
Axioms:
$$\begin{align*}
    & (TAUT)\\
    & (K,dual,T,4/\text{positive introspection})\\
    & (\cdot,+,\text{Factivity})\\
    & (\text{explicit positive introspection}) & t:F\rightarrow !t:t:F \\
    & (\text{connection}) & t:F\rightarrow \Box F \\
    & ^+(\text{weak negative introspection}) & \neg t:F\rightarrow \Box\neg t:F \\
\end{align*}$$
Rules: $\text{MP, NEC, Iterated axiom necessitation}$
$\textbf{LPS4}$不包含$\text{weak negative introspection}$公理，$\textbf{LPS4}$加入证据可判定原则$\Box t:F\lor\Box\neg(t:F)$可以得到$\text{weak negative introspection}$公理，即构成$\textbf{LPS4}^{-}$。

### 认知语义：

<!-- 但是又需要抽象的表达，需要统一语言而不关心具体的规则是什么 -->
$K_j F$ and $t:F$ [Sergei Artemov, Justified common knowledge, 2006]
Language:
$t::= c\ |\ x\ |\ t\cdot t\ |\ t+t$
$F::= P\ |\ \neg F\ |\ F\rightarrow F\ |\ K_j F\ |\ t:F$
$\mathbf{S4_nLP}$
Axioms: $TAUT,K_j,dual,T,$
$\qquad\quad \cdot,+,\text{Factivity},\text{explicit positive introspection},\text{connection}$
Rules: $\text{MP, NEC, Iterated axiom necessitation}$

$K_j F,t:F$ and $@_i F$
Language: 
$t::= c\ |\ x\ |\ t\cdot t\ |\ t+t\ |\ !t\ |\ f_i\ |\ !_it\ |\ ?_it$
$F::= i\ |\ P\ |\ \neg F\ |\ F\rightarrow F\ |\ K_j F\ |\ @_i F\ |\ t:F$
Axioms: $TAUT,K_j,dual,T,$
$\qquad\quad \cdot,+,\text{Factivity},\text{explicit positive introspection},\text{connection}$
$\qquad\quad K_@,self-dual,introduction,ref,sym,norm,agree,back$
$\qquad\quad \text{remote fact checker},\text{remote positive justification checker},\text{remote negative justification checker} $
Rules: $\text{MP, NEC, Iterated axiom necessitation},\text{Iterated remote axiom necessitation}$

模型$\mathcal{M}=(\mathcal{G},\mathcal{R_1},\mathcal{R_2},\cdots,\mathcal{R_n},\mathcal{R},\mathcal{E},\mathcal{V})$。一个认知状态是一些知识和证据的集合，证据指向的知识由证据函数$\mathcal{E}$给定。一个主体$j$在知识上不能区分的认知状态是一个二元关系$\mathcal{R_j}$，证据不分主体，一个证据的不可区分状态是一个二元关系$\mathcal{R}$。知识用命题符号表示，赋值函数$\mathcal{V}$确定了一个认知状态上为真的知识。

$\mathcal{M},\Gamma\vDash t:F$表达与$\Gamma$证据不可区分的认知状态中$F$都为真，并且$t$在$\Gamma$上是$F$的证据。



