
## 参考文献中的公理系统
## The basic hybrid language $\mathcal{H}(@)$
Language: 
$F::= i\ |\ p\ |\ \bot\ |\ \neg F\ |\ F\land F\ |\ \Box F\ |\ @_i F$
Axioms:
$$\begin{align*}
    & (TAUT) & \text{classical tautologies}\\
    & (K) & \Box(F\rightarrow M) \rightarrow (\Box F \rightarrow \Box M) \\
    & (dual) & \Diamond F\leftrightarrow\neg\Box\neg F \\
    & (K_@) & @_i(F\rightarrow M) \rightarrow (@_i F \rightarrow @_i M) \\
    & (self-dual) & @_i F \leftrightarrow \neg @_i \neg F \\
    & (introduction) & (i\land F)\rightarrow @_i F \\
    & (ref) & @_i i \\
    & (sym) & @_i j \leftrightarrow @_j i \\
    & (norm) & @_i j\land @_j F\rightarrow @_i F \\
    & (agree) & @_j@_i F \leftrightarrow @_i F \\
    & (back) & \Diamond @_iF\rightarrow @_iF\\
    & ^*(\text{dual back}) & @_iF\rightarrow\Box @_iF \\
\end{align*}$$
Rules:
$$\begin{align*}
    & (MP)\quad \text{Modus Ponens}\\
    & (NEC)\quad F/\Box F\\
    & (@NEC)\quad F/@F\\
\end{align*}$$


## $\mathcal{JH(@)}$ with $t:F$ and $@_i$
[Melvin Fitting, Justification logics and hybrid logics, 2010]
[Rui Zhu, Xinwen Liu, The Minimal System of Justification Logic with names, 2015]
Language: 
$t::= c\ |\ x\ |\ t\cdot t\ |\ t+t\ |\ f_i\ |\ !_it\ |\ ?_it$
$F::= i\ |\ P\ |\ \neg F\ |\ F\rightarrow F\ |\ @_i F\ |\ t:F$
Axioms:
$$\begin{align*}
    &(TAUT)\\
    &(K_@,self-dual,introduction)\\
    &(ref,sym,norm,agree)\\
    & (\cdot/application) & t:(F\rightarrow M)\rightarrow(u:F\rightarrow(t\cdot u):M) \\
    & (+/weakening) & t:F\rightarrow(t+u):F \\
    && u:F\rightarrow(t+u):F \\
    & ^+(\text{Factivity}) & t:F\rightarrow F \\
    & (\text{remote fact checker}) & @_i P \rightarrow f_i:@_i P \\
    && @_i\neg P\rightarrow f_i:@_i\neg P \\
    & (\text{remote positive justification checker}) & @_it:F\rightarrow(!_it):@_it:F\\
    & (\text{remote negative justification checker}) & @_i\neg t:F\rightarrow(?_i\neg t):@_i\neg t:F \\ 
\end{align*}$$
Rules:
$$\begin{align*}
    & (MP)\quad \text{Modus Ponens}\\
    & (@NEC)\quad F/@F\\
    & (\text{Iterated axiom necessitation})\quad\text{If }X\text{ is an axiom and }c_1, c_2,\cdots, c_n\text{ are constants, }\\
    &\text{then }c_1 : c_2 : \cdots : c_n : X\\
    & (\text{Iterated remote axiom necessitation})\quad \text{Let }i\text{ be any nominal. }\text{If }X\text{ is an axiom}\\
    &\text{and }c_1, c_2,\cdots, c_n\text{ are constants, }\text{then }c_1 : c_2 : \cdots : c_n : @_iX
\end{align*}$$
<!-- 
公理系统中并没有$\text{\text{dual back}}$公理，这是因为如果$@_iF$是定理，尽管是可证的，但是并没有公理能够给出具体的证明。不过存在证明的事实能够被下面的内化定理捕获。
**Theorem.** (Internalization) If $F$ is a theorem of basic hybird-$\mathsf{JT}$, then there is a closed justification term $t$ such that $t:F$ is also a theorem. 简写为：$Theorem(F)\Rightarrow(\exist t)(Colsed(t)\land Theorem(t:F))$
从与模态逻辑hybird-$\mathsf{T}$对应的角度看，内化定理对应必然化规则。从内化证明结构的角度来看，这个定理表明了basic hybird-$\mathsf{JT}$中的定理都有这个系统中项的语言可以表达的证明。

这也就是说，对于任意的系统$i$，如果公式$F$在系统$i$上为真，那么就存在一个项$t$，$t$是$F$在$i$上为真的证明。

内化定理表达了项语言对自身系统性质的刻画，一般的，公理系统的定理都有证明，在证明语义中，我们可以用项来刻画系统中的证明。

一般来说，Justification Logic的公理系统中，常量指定$CS$保证系统中的公理有常元证明，然后通过项上的函数记录规则的使用，从而系统中的定理都能有封闭的项来证明，即Justification Logic的内化定理。

这意味着，这里使用了这一结论，同样的，我们认为每个系统中的公理都有常元证明，并且我们的项语言有与系统中的规则对应的函数。这样以来，系统中所有的命题符号都能有封闭的项来证明，并且我们的项语言将包含所有系统规则的对应函数，但这些函数并不会冗余，反而是必要的。反之，如果我们直接给出所有命题符号的常元证明，并不在我们的项语言使用规则对应的函数（$\cdot,+$除外），则我们没法对已有的规则使用$\cdot,+$以外的规则，并且会使证明结构变得平凡，没法记录系统中给出证明的过程。如果这样，我们就只能抽象的讨论外部证明，而不能细致的分析内部证明。总而言之，对于系统中的一个定理，项内化了在这个系统中证明这个定理的过程（结构）。

[Fitting,2010]中，作者在含有$Factivity$公理的 basic hybird-$\mathsf{JT}$ 中证明了内化定理，并证明了 basic hybird-$\mathsf{JT}$ 与 basic hybrid-$\mathsf{T}$ 之间的实现定理，[Rui Zhu, Xinwen Liu,2015]中，作者不借助$Factivity$公理证明了 basic hybird-$\mathsf{J}$ 的内化定理。

这个系统可以作为一个逻辑的上层语义 -->