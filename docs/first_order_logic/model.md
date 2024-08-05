
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

## definable property
Suppose that $\mathcal{M}=(M,I)$ and a set $A\subseteq M$ is defined by the formula $\phi$ in $\mathcal{M}$ with parameters from $M$, then the set $M\setminus A$ is defined by the formula $\neg\phi$ in $\mathcal{M}$ with the same parameters from $M$.
**Proof.** It is directly form the defination of definable.
what is definalbe set?
exist a definable set means exist a formula and some parameters
exist a formula means there are many definable set with different parameters
thus the definable set is connect to formula closely

## identify the substructure
the nature question is: what kinds of conditions make sure different structure satisfy the same formula? How to identify the elementary substructure?
according to the substructure property, we notice that the different mainly caused by the quantifiers
Suppose that $\mathcal{M}=(M,I)$ is a substructure of $\mathcal{N}=(N,J)$, we notice that $M\subseteq N$ which means that $\mathcal{N}$ has a bigger universe than $\mathcal{M}$, thus the formula satisfied by $\mathcal{M}$ may not satisfied by $\mathcal{N}$ since the domain of quantifiers was put into a bigger universe.
The nature interesting is try to find a condition to make sure the quantifiers are satisfied in the new universe, the tarski theorem give the answer, it make sure that there is no definable set in the bigger universe generate by the original universe but independent to the original universe, means there is no formula could define a nonempty set in $N\setminus M$ with parameters form $M$, it means the definable set in $N\setminus M$ defined by any formulas is a empty set, then the definable set defined by the negation of that formula is $N$. Finally, ever extension to the original universe must extend to the new universe. That is there is no formula satisfied in $\mathcal{M}$ but not satisfied in $\mathcal{N}$ with the same assignment. 

## Tarski Theorem
Suppose that $\mathcal{M}=(M,I)$ and $\mathcal{N}=(N,J)$ are $\mathcal{L_\mathcal{A}}$-structures, and $\mathcal{M}\subseteq\mathcal{N}$. The following are equivalent:
(1) $\mathcal{M}\preceq\mathcal{N}$
(2) $\mathcal{M} \subseteq \mathcal{N}$ and for each nonempty set $A\subseteq N$, if $A$ is deifnable in $\mathcal{N}$ with parameters from $M$, then $A\cap M\neq \emptyset$
**Proof.** $(1)\Rightarrow(2)$ is obvious.
$(2)\Rightarrow(1)$ Suppose that $\mathcal{M}\subseteq\mathcal{N}$ and for each nonempty set $A\subseteq N$, if $A$ is definable in $\mathcal{N}$ with parameters from $M$, then $A\cap M\neq \emptyset$. We prove by induction on the length of formulas $\phi$ that for all $\mathcal{M}$-assignments $\nu$, we have $\mathcal{M},\nu\vDash\phi\Leftrightarrow\mathcal{N},\nu\vDash\phi$
$(i)$ $\mathcal{M},\nu\vDash\phi\Leftarrow\mathcal{N},\nu\vDash\phi$ is obvious.
$(ii)$ we prove $\mathcal{M},\nu\vDash\phi\Rightarrow\mathcal{N},\nu\vDash\phi$. Assum that $\phi=\forall x_i\psi$.  for all $\mathcal{M}$-assignments $\mu$ agree with $\nu$ on $\phi$, we notice that a $\mathcal{M}$-assignment also is a $\mathcal{N}$-assignment, thus the set $Y$ defined by $\psi$ in $\mathcal{N}$ with parameters $\nu(x_{k_1}),\cdots,\nu(x_{k_m})$ from $M$ must have $M\subseteq Y\subseteq N$. Suppose that $N\setminus Y\neq\emptyset$, then $N\setminus Y$ is defined by $\neg\psi$ in $\mathcal{N}$ with parameters $\nu(x_{k_1}),\cdots,\nu(x_{k_m})$ from $M$, and $(N\setminus Y)\cap M=\emptyset$. However, the second condition means that there is no nonempty set $A\subseteq N$ deifnable in $\mathcal{N}$ with parameters from $M$ and $A\cap M=\emptyset$. Thus $N\setminus Y=\emptyset$, $Y = N$, and $\mathcal{N},\nu\vDash\phi$
$(iii')$ we also give a reverse proof. Assume that $\mathcal{N},\nu\nvDash\phi$ and try to prove $\mathcal{M},\nu\nvDash\phi$. Then there is an $\mathcal{N}$-assignment $\mu$ which agree with $\nu$ on the free vriables of $\phi$ such that $\mathcal{N},\mu\nvDash\psi$, thus the set $Y$ defined by $\neg\psi$ in $\mathcal{N}$ with parameters $\mu(x_{k_1}),\cdots,\mu(x_{k_m})$ from $M$ must have $Y\neq\emptyset$ since $\mu(x_i)\in Y$. Now we use the assumption (2). By (2), $Y\cap M$ is not empty, and we let $b$ be an element of $Y\cap M$. Consequently, if $\rho$ is an $\mathcal{M}$-assignment such that $\rho$ agree with $\nu$ on the free variables of $\phi$ and $\rho(x_i)=b$, then $\mathcal{N},\rho\vDash\neg\psi$, by induction, $\mathcal{M},\rho\vDash\neg\psi$ and so $\mathcal{M},\nu\nvDash\phi$



