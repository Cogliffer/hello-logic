
## substructure
$\mathcal{M}\subseteq\mathcal{N}$ indicates that $\mathcal{M}$ is a substructure of $\mathcal{N}$ if and only if $M\subseteq N$ and the following conditions hold
(1) $if\ CS(c_i)\ then\ I(c_i)=J(c_i)$
(2) $if\ FS(F_i)$ then $I(F_i)$ is the restriction of $J(F_i)$ to $M^n,n=\rho(F_i)$
(3) $if\ PS(P_i)$ then $I(P_i)$ is equal to $J(P_i)\cap M^n,n=\rho(P_i)$

## substructure property
Theorem 4.5 Suppose that $\mathcal{M}=(M,I)$ and $\mathcal{N}=(N,I)$ are $\mathcal{L_\mathcal{A}}$-structures with $M\subseteq N$, Then the following are equivalent:
(1)$\mathcal{M}$ is a substructure of $\mathcal{N}$
(2)For all atomic $\mathcal{L_\mathcal{A}}$-formulas $\phi$ and for all $\mathcal{M}$-assignments $\nu$, there have $\mathcal{M},\nu\vDash\phi\Leftrightarrow\mathcal{N},\nu\vDash\phi$
**Proof.**
(1)$\Rightarrow$(2) is directly from the definition.
(2)$\Rightarrow$(1)
for $c_i$ is a constant symbol, then for any assignment $\nu$, there have $\mathcal{M},\nu\vDash x\hat{=}c_i\Leftrightarrow\mathcal{N},\nu\vDash x\hat{=}c_i$, that is $\overline{\nu}(x)=I(c_i)=J(c_i)$
for $F_i$ is a function symbol, then for any assignment $\nu$, there have $\mathcal{M},\nu\vDash x\hat{=}F_i(x_1,\cdots,x_n) \Leftrightarrow\mathcal{N},\nu\vDash x\hat{=}F_i(x_1,\cdots,x_n)$, that is $\nu(x)=I(F_i)(\overline{\nu}(x_1),\cdots,\overline{\nu}(x_n))=J(F_i)(\overline{\nu}(x_1),\cdots,\overline{\nu}(x_n))$, since that $M\subseteq N$ thus $I(F_i)$ is the restriction of $J(F_i)$ to $M^n$
for $P_i$ is a function symbol, then for any assignment $\nu$, there have $\mathcal{M},\nu\vDash P_i(x_1,\cdots,x_n) \Leftrightarrow\mathcal{N},\nu\vDash P_i(x_1,\cdots,x_n)$, that is $I(P_i)(\overline{\nu}(x_1),\cdots,\overline{\nu}(x_n))\Leftrightarrow J(P_i)(\overline{\nu}(x_1),\cdots,\overline{\nu}(x_n))$, since that $M\subseteq N$ thus $I(P_i)$ is the restriction of $J(P_i)$ to $M^n$
This conculsion could be extends to propositional cases directly by induction on the complexity of formulas.

## elementary substructure
if $\mathcal{M}\subseteq\mathcal{N}$, then $\mathcal{M}$ is called an elementary substructure of $\mathcal{N}$ if and only if for all $\mathcal{L_\mathcal{A}}$-formulas $\phi$ and for all $\mathcal{M}$-assignments $\nu$ $$\mathcal{M},\nu\vDash\phi\Leftrightarrow\mathcal{N},\nu\vDash\phi$$ denoted as $\mathcal{M}\preceq\mathcal{N}$

## identify the substructure
the nature question is: what kinds of conditions make sure different structure satisfy the same formula? How to identify the elementary substructure?
according to the substructure property, we notice that the different mainly caused by the quantifiers
Suppose that $\mathcal{M}=(M,I)$ is a substructure of $\mathcal{N}=(N,J)$, we notice that $M\subseteq N$ which means that $\mathcal{N}$ has a bigger universe than $\mathcal{M}$, thus the formula satisfied by $\mathcal{M}$ may not satisfied by $\mathcal{N}$ since the domain of quantifiers was put into a bigger universe.
The nature interesting is try to find a condition to make sure the quantifiers are satisfied in the new universe, the tarski theorem give the answer

## Tarski Theorem 
Suppose that $\mathcal{M}=(M,I)$ and $\mathcal{N}=(N,J)$ are $\mathcal{L_\mathcal{A}}$-structures, and $\mathcal{M}\subseteq\mathcal{N}$. The following are equivalent:
(1) $\mathcal{M}\preceq\mathcal{N}$
(2) $\mathcal{M} \subseteq \mathcal{N}$ and for each nonempty set $A\subseteq N$, if $A$ is deifnable in $\mathcal{N}$ with parameters from $M$, then $A\cap M\neq \emptyset$
**Proof.** $(1)\Rightarrow(2)$ is obvious.
$(2)\Rightarrow(1)$ Suppose that $\mathcal{M}\subseteq\mathcal{N}$ and for each nonempty set $A\subseteq N$, if $A$ is definable in $\mathcal{N}$ with parameters from $M$, then $A\cap M\neq \emptyset$. We prove by induction on the length of formulas $\phi$ that for all $\mathcal{M}$-assignments $\nu$, we have $\mathcal{M},\nu\vDash\phi\Leftrightarrow\mathcal{N},\nu\vDash\phi$
$(i)$ $\mathcal{M},\nu\vDash\phi\Leftarrow\mathcal{N},\nu\vDash\phi$ is obvious.
$(ii)$ we prove $\mathcal{M},\nu\vDash\phi\Rightarrow\mathcal{N},\nu\vDash\phi$. Assum that $\phi=\forall x_i\psi$.  for all $\mathcal{M}$-assignments $\mu$ agree with $\nu$ on $\phi$, we notice that a $\mathcal{M}$-assignment also is a $\mathcal{N}$-assignment, thus the set $Y$ defined by $\psi$ in $\mathcal{N}$ with parameters $\nu(x_{k_1}),\cdots,\nu(x_{k_m})$ from $M$ must have $M\subseteq Y\subseteq N$. Suppose that $N\setminus Y\neq\emptyset$, then $N\setminus Y$ is defined by $\neg\psi$ in $\mathcal{N}$ with parameters $\nu(x_{k_1}),\cdots,\nu(x_{k_m})$ from $M$, and $(N\setminus Y)\cap M=\emptyset$. However, the second condition means that there is no nonempty set $A\subseteq N$ deifnable in $\mathcal{N}$ with parameters from $M$ and $A\cap M=\emptyset$. Thus $N\setminus Y=\emptyset$, $Y = N$, and $\mathcal{N},\nu\vDash\phi$
$(iii')$ we also give a reverse proof. Assume that 




## definable property
Suppose that $\mathcal{M}=(M,I)$ and a set $A\subseteq M$ is defined by the formula $\phi$ in $\mathcal{M}$ with parameters from $M$, then the set $M\setminus A$ is defined by the formula $\neg\phi$ in $\mathcal{M}$ with the same parameters from $M$.
**Proof.** It is directly form the defination of definable.
