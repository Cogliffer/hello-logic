# semantic
## Truth assignments
*truth assignment* for $\mathcal{L}_0$ is a function $\nu:\{A_n:n\in\mathbb{N}\}\to\{T,F\}$.
**Theorem.** If $\nu$ is a truth assignment for $\mathcal{L}_0$, then there is a unique function $\overline{\nu}$ defined on $\mathcal{L}_0$ such that 
(1) $\forall n, \nu(\langle A_n\rangle) = \nu(A_n)$.
(2) $$\forall\psi\in\mathcal{L_0},\overline{\nu}((\neg\psi))=\begin{cases}
    T & \overline{\nu}(\psi)=F\\
    F & \text{ otherwise.}
\end{cases}$$
(3) $$\forall\psi_1,\psi_2\in\mathcal{L_0},\overline{\nu}((\psi_1\rightarrow\psi_2))=\begin{cases}
    F & \overline{\nu}(\psi_1)=T\text{ and }\overline{\nu}(\psi_2)=F\\
    T & \text{ otherwise.}
\end{cases}$$
**Proof.**

## satisfies
$\nu\vDash\phi\text{ iff }\nu(\phi) = T$
$\nu\vDash\Gamma\text{ iff }\forall\phi\in\Gamma,\nu(\phi) = T$
*tautology* is a formula $\phi$ such that $\forall\nu,\nu\vDash\phi$.
*contradiction* is a formula $\phi$ such that $\forall\nu,\nu\nvDash\phi$.

## truth functions
*$n$-place truth function* $f:\{T,F\}^n\to\{T,F\}$
**Theorem 1.21** Any formula derived a truth function, and any truth function defined a formula.
