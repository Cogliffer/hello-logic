

## $\Box F$ and $t:F$
[Sergei Artemov, Elena Nogina, Logic of knowledge with justifications from the provability perspective., 2004]<br>
[Sergei Artemov, Elena Nogina, Introducing Justification into Epistemic, 2005]<br>
Language: <br>
$t::= c\ |\ x\ |\ (t\cdot t)\ |\ (t+t)\ |\ !t$<br>
$F::= i\ |\ p\ |\ \neg F\ |\ F\rightarrow F\ |\ \Box F\ |\ t:F$<br>
$\textbf{LPGL}$:<br>
直觉：$\Box F$表达$F$可证，$t:F$表达$t$是$F$的证明<br>
Axioms:<br>
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
Rules: $(\text{MP, NEC, Iterated axiom necessitation})$<br>
$\qquad\ ^*(\text{reflexivity rule}) \qquad \Box F/F$<br>
$\text{Lob schema}$公理与$T$公理是不相容的，因为对于任意的$F$有证明序列$\Box F\rightarrow F,\Box(\Box F\rightarrow F),\Box(\Box F\rightarrow F)\rightarrow\Box F,\Box F,F$，但是$\textbf{LPGL}$中可以具有$\text{reflexivity rule}$。<br>

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

$\textbf{LPS4}\text{ and }\textbf{LPS4}^{-}$:<br>
直觉：$\Box F$表达潜在的（大概的，直觉上）知道（相信）$F$，$t:F$表达因为证据（推理）$t$（实际的，具体过程的，有理有据的）知道（相信）$F$<br>
Axioms:<br>
$$\begin{align*}
    & (TAUT)\\
    & (K,dual,T,4/\text{positive introspection})\\
    & (\cdot,+,\text{Factivity})\\
    & (\text{explicit positive introspection}) & t:F\rightarrow !t:t:F \\
    & (\text{connection}) & t:F\rightarrow \Box F \\
    & ^+(\text{weak negative introspection}) & \neg t:F\rightarrow \Box\neg t:F \\
\end{align*}$$
Rules: $\text{MP, NEC, Iterated axiom necessitation}$<br>
$\textbf{LPS4}$不包含$\text{weak negative introspection}$公理，$\textbf{LPS4}$加入证据可判定原则$\Box t:F\lor\Box\neg(t:F)$可以得到$\text{weak negative introspection}$公理，即构成$\textbf{LPS4}^{-}$。

### $K_j F$ and $t:F$
[Sergei Artemov, Justified common knowledge, 2006]<br>
Language:

$t::= c\ |\ x\ |\ t\cdot t\ |\ t+t$<br>
$F::= P\ |\ \neg F\ |\ F\rightarrow F\ |\ K_j F\ |\ t:F$
$\mathbf{S4_nLP}$<br>
Axioms: $TAUT,K_j,dual,T,$<br>
$\qquad\quad \cdot,+,\text{Factivity},\text{explicit positive introspection},\text{connection}$<br>
Rules: $\text{MP, NEC, Iterated axiom necessitation}$<br>
