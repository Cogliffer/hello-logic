# **Proof.** system for $\mathcal{L_0}$

## axiom of propositional logic
(1) $(p\to p), (p\to(q\to p)), (p\to(\neg p\to q)), ((p\to\neg p)\to \neg p)$
(2) $(p\to(\neg q\to(\neg(p\to q))))$ means $p\land\neg q\leftrightarrow\neg(p\to q)$
(3) $((p\to (q\to r))\to((p\to q)\to(p\to r)))$ means $p\land q\land\neg r\leftrightarrow (p\to q)\land(p\to\neg r)\land(q\to\neg r)\leftrightarrow(p\to(q\to \neg r))\land((p\to q)\to(p\to\neg r))$

## $\Gamma$-proof
a set of formulas $\Gamma\subseteq\mathcal{L_0}$
a $\Gamma$-proof is a finite sequence of formulas for each $i$-th formula $\phi_i$ is a logical axiom, or $\phi_i\in\Gamma$ or $\exist j_1,j_2<i\ s.t.\ \phi_{j_2} = (\phi_{j_1}\to\phi_i)$. I say the the prove of $\phi_i$ is given by $\phi_{j_1}$ under $\phi_{j_2}$, and this sequence is a $\Gamma$-proof for $\phi_i$, denoted by $\Gamma\vdash\phi$.
a formula $\phi$ could be infferenced by $\Gamma$ if there exists a finite $\Gamma$-proof for $\phi$.

定义、命题可以模式化为更基本的单元，对象/背景/前提+对象/结论

## Inference Lamma
a set of formulas $\Gamma\subseteq\mathcal{L_0}$
$\forall\phi,\psi\in\mathcal{L_0}$
$\Gamma\vdash\phi,\Gamma\vdash(\phi\to\psi)\Rightarrow\Gamma\to\psi$
**Proof.** try to construct a relation $\phi_{j_2} = (\phi_{j_1} \to \psi)$ from the axiom and $\phi,(\phi\to\psi)$
let $\phi_{j_1} = \phi,\phi_{j_2} = (\phi\to\psi)$, then $\Gamma\vdash\psi$.

## soundness
a set of formulas $\Gamma\subseteq\mathcal{L_0}$
$\Gamma\vdash\phi$
a truth assignment $\nu:\{A_1,\cdots,A_n,\cdots\}\to\{T,F\}$
$\forall\psi\in\Gamma,\overline{\nu}(\psi)=T\Rightarrow\overline{\nu}(\phi)=T$
**Proof.**

## deduction Lemma
a set of formulas $\Gamma\subseteq\mathcal{L_0}$
$\Gamma\cup\{\phi\}\vdash\psi\Leftrightarrow\Gamma\vdash(\phi\to\psi)$
**Proof.** (left to right)

## Consistent
a set of formulas $\Gamma\subseteq\mathcal{L_0}$
$\overline{\mathrm{Cons}}(\Gamma)$ $\Gamma$ is inconsistent : $\exist\phi,\Gamma\vdash\phi\text{ and }\Gamma\vdash\neg\phi$
$\mathrm{Cons}(\Gamma)$ $\Gamma$ is consistnet : $\forall\phi,\Gamma\nvdash\phi\text{ or }\Gamma\nvdash\neg\phi$
consistent and inconsistetn negate each other.
$\Gamma$ is consistnet : $\forall\phi,\Gamma\vdash\phi\Rightarrow\Gamma\nvdash\neg\phi$
$\Gamma$ is consistnet : $\forall\phi,\Gamma\vdash\neg\phi\Rightarrow\Gamma\nvdash\phi$
$\mathrm{Cons}(\Gamma),\Gamma\vdash\phi\Rightarrow\mathrm{Cons}(\{\Gamma\cup\phi\})$
$\mathrm{Cons}(\Gamma),\Gamma'\subseteq\Gamma\Rightarrow\mathrm{Cons}(\Gamma')$

## explosion lamma
a set of formulas $\Gamma\subseteq\mathcal{L_0}$
$\overline{\mathrm{Cons}}(\Gamma)\Rightarrow\forall\phi,\Gamma\vdash\phi$
**Proof.**

## extension lemma
a set of formulas $\Gamma\subseteq\mathcal{L_0}$
$\mathrm{Cons}(\Gamma)$
$\forall\phi,\mathrm{Cons}(\Gamma\cup\{\phi\})\text{ or }\mathrm{Cons}(\Gamma\cup\{\neg\phi\})$
**Proof.** Suppose not, then $\exist\phi,\overline{\mathrm{Cons}}(\Gamma\cup\{\phi\})\text{ and }\overline{\mathrm{Cons}}(\Gamma\cup\{\neg\phi\})$.
$$\begin{align*}
    \overline{\mathrm{Cons}}(\Gamma\cup\{\phi\}) & \Rightarrow\Gamma\cup\{\phi\}\vdash\neg\phi \text{ by explosion lemma}\\
    & \Rightarrow\Gamma\vdash\phi\to\neg\phi \text{ by deduction lemma}\\
    & \Rightarrow\Gamma\vdash\neg\phi \text{ under the axiom }((\phi\to\neg \phi)\to\neg \phi) \\
    & \Rightarrow\mathrm{Cons}(\Gamma\cup\{\neg\phi\}) \\
    \text{which is contradictory to } &\overline{\mathrm{Cons}}(\Gamma\cup\{\neg\phi\})\text{, the inverse direction is similar.}
\end{align*}$$

## maximally consistent
a set of formulas $\Gamma\subseteq\mathcal{L_0}$
$\mathrm{Cons}(\Gamma)$
$\mathrm{MaxCons}(\Gamma)$ The following defination of *maximally consistent* of $\Gamma$ is equivalence:
$$\begin{align}
    \mathrm{MaxCons}(\Gamma) & \Leftrightarrow\mathrm{Cons}(\Gamma),\forall\phi(\mathrm{Cons}(\Gamma\cup\{\phi\})\Rightarrow\phi\in\Gamma)\quad(1)\\
    & \Leftrightarrow\mathrm{Cons}(\Gamma),\neg\exist\mathrm{Cons}(\Gamma'),\Gamma\subset\Gamma'\\
    & \Leftrightarrow\mathrm{Cons}(\Gamma),(\exist\mathrm{Cons}(\Gamma'),\Gamma\subseteq\Gamma'\Rightarrow\Gamma=\Gamma')\\
    & \Leftrightarrow\forall\phi(\phi\in\Gamma\text{ or (not both) }\neg\phi\in\Gamma).
\end{align}$$
**Proof.**
(1) $\Rightarrow$ (2,3)
Suppose not, that is $\mathrm{Cons}(\Gamma'),$
$$\begin{align*}
    \Gamma\subset\Gamma' & \Rightarrow\exist\phi\in\Gamma',\phi\notin\Gamma \\
    & \Rightarrow\mathrm{Cons}(\Gamma'\cup\{\phi\}) \\
    & \Rightarrow\mathrm{Cons}(\Gamma\cup\{\phi\}) \\
    & \Rightarrow\phi\in\Gamma\text{ by (1)} \\
    \text{where }&\phi\notin\Gamma\text{ is contradictory to }\phi\in\Gamma
\end{align*}$$
(3) $\Rightarrow$ (4)
$$\begin{align*}
    \mathrm{Cons}(\Gamma)& \Rightarrow\forall\phi,\mathrm{Cons}(\Gamma\cup\{\phi\})\text{ or }\mathrm{Cons}(\Gamma\cup\{\neg\phi\})\\
    & \Rightarrow\forall\phi,\Gamma\cup\{\phi\} = \Gamma\text{ or (not both) }\Gamma\cup\{\neg\phi\} = \Gamma \text{ by (2)}\\
    & \Rightarrow\forall\phi,\phi\in\Gamma\text{ or (not both) }\neg\phi\in\Gamma
\end{align*}$$
(4) $\Rightarrow$ (1)
Given $\phi$ suppose
$$\begin{align*}
    \mathrm{Cons}(\Gamma\cup\{\phi\}) & \Rightarrow\phi\in\Gamma\text{ or (not both) }\neg\phi\in\Gamma \text{ by (3)}\\
    & \text{if }\phi\in\Gamma\text{ then it is directly get (1)}\\
    & \text{if }\neg\phi\in\Gamma\text{ then }\Gamma\vdash\neg\phi\Rightarrow\overline{\mathrm{Cons}}(\Gamma\cup\{\phi\})\\
    & \text{where }\overline{\mathrm{Cons}}(\Gamma\cup\{\phi\})\text{ is a contradicty to }\mathrm{Cons}(\Gamma\cup\{\phi\})
\end{align*}$$
$$\begin{align*}
    \overline{\mathrm{MaxCons}}(\Gamma)\Leftrightarrow& \overline{\mathrm{Cons}}(\Gamma)\text{ or  }\exist\phi(\mathrm{Cons}(\Gamma\cup\{\phi\})\text{ and }\phi\notin\Gamma)\\
    \Leftrightarrow& \overline{\mathrm{Cons}}(\Gamma)\text{ or }\exist \mathrm{Cons}(\Gamma'),\Gamma\subset\Gamma'\\
    \Leftrightarrow& \exist\phi(\phi\notin\Gamma\text{ and }\neg\phi\notin\Gamma)
\end{align*}$$


**corollary** 
$\mathrm{MaxCons}(\Gamma)\Rightarrow\forall\phi(\Gamma\vdash\phi\Rightarrow\phi\in\Gamma)$, reverse is false.
**Proof.** $\forall\phi(\Gamma\vdash\phi\Rightarrow\mathrm{Cons}(\Gamma\cup\{\phi\})\Rightarrow\phi\in\Gamma)$ so $\forall\phi(\mathrm{Cons}(\Gamma\cup\{\phi\})\Rightarrow\phi\in\Gamma)$ is strength than $\forall\phi(\Gamma\vdash\phi\Rightarrow\phi\in\Gamma)$
**corollary** 
$\mathrm{MaxCons}(\Gamma)\Rightarrow((\phi\to\psi)\in\Gamma\Leftrightarrow\phi\notin\Gamma\text{ or }\psi\in\Gamma)$
**Proof.** $(\Rightarrow)$ directly inference
$$\begin{align*}
    \text{Assume (1) }&\mathrm{MaxCons}(\Gamma),(\phi\to\psi)\in\Gamma,\phi\in\Gamma\\
    &\Rightarrow \Gamma\vdash\psi\\
    &\Rightarrow\psi\in\Gamma\\
    \text{Assume (2) }&\mathrm{MaxCons}(\Gamma),(\phi\to\psi)\in\Gamma,\psi\notin\Gamma\\
    &\Rightarrow\neg\psi\in\Gamma\\
    &????????\\
    &\Rightarrow\neg\phi\in\Gamma\\
    &\Rightarrow\phi\notin\Gamma\\
\end{align*}$$
$(\Rightarrow)$ by contraction
Assume $\phi\in\Gamma,\psi\notin\Gamma\Rightarrow\Gamma\vdash(\neg(\phi\to\psi))$ under the axiom $(\phi\to(\neg\psi\to(\neg(\phi\to\psi))))$, where $\neg(\phi\to\psi)\in\Gamma$ and $(\phi\to\psi)\in\Gamma$ is contracted.

$(\Leftarrow)$
(1) assume $\phi\notin\Gamma\Rightarrow\neg\phi\in\Gamma\Rightarrow\Gamma\vdash(\phi\to\psi)$ under the axiom $(\neg\phi\to(\phi\to\psi))$ 
(2) assume $\psi\in\Gamma\Rightarrow\Gamma\vdash(\phi\to\psi)$ under the axiom $(\psi\to(\phi\to\psi))$<end>$\Box
$</end>

**Theorem**
$\mathrm{MaxCons}(\Gamma)\Rightarrow\mathrm{Satisfiable}(\Gamma),\Gamma\subseteq\mathcal{L_0}$

**Theorem**
$\mathrm{Cons}(\Gamma)\Rightarrow\exist\mathrm{MaxCons}(\Gamma^\ast),\Gamma\subseteq\Gamma^\ast\subseteq\mathcal{L_0}$

**Theorem Completeness**
$\mathrm{Cons}(\Gamma)\Rightarrow\mathrm{Satisfiable}(\Gamma),\Gamma\subseteq\mathcal{L_0}$

我们需要将多个命题合并为一个命题，但这样分情况的时候就会有大量重复
 
自动提示，具有一定的方便性，如何开发逻辑专用的自动补全系统，能够自动进行有限步的推理，并提示出来

建立一个直觉系统，赋予到每个公式上，可以灵活编辑
class 对象
·公式
·直觉

默认自动继承前提，例如
a set of formulas $\Gamma\subseteq\mathcal{L_0}$