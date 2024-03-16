(\P0) we usually assume that the model have the same modal similarity type $\tau$, and use $\vartriangle$ for each one in $\tau$
(\P1) the denotion is as usual, $\omega$ is a state of model $\mathfrak{M}=(W,R,V)$, $\omega'$ is a state of model $\mathfrak{M'}=(W',R',V')$, and so on. Use $p,q,r$ to denota the proposition letter. Use $\phi,\varphi,\psi$ to denote formules according the context.

\def\P0\P1
$\omega\leftrightsquigarrow\omega'$ denote the modally equivalent of state of models if $\{\phi\mid\mathfrak{M},\omega\Vdash\phi\}=\{\phi\mid\mathfrak{M'},\omega'\Vdash\phi\}$l
$\mathfrak{M}\leftrightsquigarrow\mathfrak{M'}$ denote the modally equivalent of models if $\{\phi\mid\mathfrak{M}\Vdash\phi\}=\{\phi\mid\mathfrak{M'}\Vdash\phi\}$

disjoint unions, basic modal logic
two models are disjoint if their domians contain no common elements
For disjoint models $\mathfrak{M}_i=(W_i,R_i,V_i),i\in I$ their disjoint union is the structure $\biguplus_i\mathfrak{M_i}=(W,R,V)$, where $W$ is the union of sets $W_i$, $R$ is the union of relations $R_i$,and for each proposition letter $p,V(p)=\bigcup_{i\in I}V_i(p)$

modal satisfaction is invariant under disjoint unions
$\mathfrak{M_i},\omega\vDash\phi\ \text{iff}\ \biguplus_{i\in I}\mathfrak{M_i},\omega\vDash\phi$

$\mathfrak{M'}\rightarrowtail\mathfrak{M}$ denote that $\mathfrak{M'}$ is a generated submodel of $\mathfrak{M}$ if $W'\subseteq W,R'=R\cap(W'\times W'),\forall p,V'(p)=V(p)\cap W'$, we say that $R',V'$ is the restriction of $R,V$ on $\mathfrak{M'}$

modal satisfaction is invariant under generated submodels
$\mathfrak{M'}\rightarrowtail\mathfrak{M}\Rightarrow(\mathfrak{M},\omega\vDash\phi\ \text{iff}\ \mathfrak{M'},\omega\vDash\phi)$

\def\P0\P1
$f:\mathfrak{M}\to\mathfrak{M'}$ is a homomorphism from $\mathfrak{M}$ to $\mathfrak{M'}$ if $\omega\in V(p)\Rightarrow f(\omega)\in V'(p)$ and $(\omega_0,\cdots,\omega_n)\in R_\vartriangle\Rightarrow(f(\omega_0),\cdots,f(\omega_n))\in R'_\vartriangle$, for basic modal logic just $R\omega u\Rightarrow R'f(\omega)f(u)$
$f:\mathfrak{M}\to\mathfrak{M'}$ is a strong homomorphism if $f$ is a homomorphism from $\mathfrak{M}$ to $\mathfrak{M'}$ and modify $\Rightarrow$ to $\Leftrightarrow$
an embedding of $\mathfrak{M}$ into $\mathfrak{M'}$ is a stront homomorphism $f:\mathfrak{M}\to\mathfrak{M'}$ which is injective
$\mathfrak{M}\cong\mathfrak{M'}$ denote that $\mathfrak{M}$ is isomorphic to $\mathfrak{M'}$ if there is an isomorphism is a bijective strong homomorphism from $\mathfrak{M}$ to $\mathfrak{M'}$

\theorem\P0\P1
$f$ is a surjective strong homomorphism $\Rightarrow\omega\leftrightsquigarrow f(\omega)$ 
$\mathfrak{M}\cong\mathfrak{M'}\Rightarrow\mathfrak{M}\leftrightsquigarrow\mathfrak{M'}$

\def\P1
bounded morphism, basic modal logic
$f:\mathfrak{M}\to\mathfrak{M'}$ is a bounded morphism if $\omega\in V(p)\Leftrightarrow f(\omega)\in V'(p)$ and $R\omega u\Rightarrow R'f(\omega)f(u)$ and $R'f(\omega)u'\Rightarrow\exist u\ s.t.\ R\omega u,f(u)=u'$
\def\P0\P1
bounded morphism
$f:\mathfrak{M}\to\mathfrak{M'}$ is a bounded morphism if $\omega\in V(p)\Leftrightarrow f(\omega)\in V'(p)$ and $R_\vartriangle\omega u_1\cdots u_n\Rightarrow R'_\vartriangle f(\omega)f(u_1)\cdots f(u_n)$ and $R'_\vartriangle f(\omega)u'_1\cdots u'_n\Rightarrow\exist u_1\cdots u_n\ s.t.\ R_\vartriangle\omega u_1\cdots u_n,f(u_i)=u'_i$

\def\P0\P1
bisimulation, basic modal logicfe
$Z:\mathfrak{M}\ \overleftrightarrow{\_\_}\ \mathfrak{M'}$ denote a bisimulation between $\mathfrak{M}$ and $\mathfrak{M'}$ if 
(1) $\omega Z\omega'\Rightarrow(\omega\in V(p)\Leftrightarrow\omega'\in V'(p))$
(2) (the forth condition) $\omega Z\omega',R\omega u\Rightarrow\exist u'\ s.t.\ uZu',R'\omega'u'$
(2) (the back condition) $\omega Z\omega',R'\omega' u'\Rightarrow\exist u\ s.t.\ uZu',R\omega u$
bisimulation
$Z:\mathfrak{M}\ \overleftrightarrow{\_\_}\ \mathfrak{M'}$ denote a bisimulation between $\mathfrak{M}$ and $\mathfrak{M'}$ if 
(1) $\omega Z\omega'\Rightarrow(\omega\in V(p)\Leftrightarrow\omega'\in V'(p))$
(2) (the forth condition) $\omega Z\omega',R_\vartriangle\omega u_1\cdots u_n\Rightarrow\exist u'_1\cdots u'_n\ s.t.\ u_i Z u'_i,R_\vartriangle'\omega'u'_1\cdots u'_n$
(2) (the back condition) $\omega Z\omega',R_\vartriangle'\omega' u'_1\cdots u'_n\Rightarrow\exist u_1\cdots u_n\ s.t.\ u_i Z u'_i,R_\vartriangle\omega u_1\cdots u_n$

\theorem\P1
$\mathfrak{M}\cong\mathfrak{M'}\Rightarrow\mathfrak{M} \ \overleftrightarrow{\_\_}\ \mathfrak{M'}$
$\mathfrak{M_i},\omega\ \overleftrightarrow{\_\_}\ \biguplus_{i}\mathfrak{M_i},\omega$
$\mathfrak{M'}\rightarrowtail\mathfrak{M}\Rightarrow\mathfrak{M'},\omega\ \overleftrightarrow{\_\_} \ \mathfrak{M},\omega$
\theorem\P0\P1
(Hennessy-Milner Theorem) $\omega\ \overleftrightarrow{\_\_}\ \omega'\Rightarrow\omega\leftrightsquigarrow\omega'$ : modal formulas are invariant under bisimulation.

\def
(finite model property)
let $\tau$ be a modal similarity type
let $\mathsf{M}$ be a class of $\tau$-model
$\tau$ has the finite models property with respect to $\mathsf{M}$ if the following conditions hold:
if $\phi$ is a formula of similarity type $\tau$ and $\phi$ is satisfiable in some model in $\mathsf{M}$, then $\phi$ is satisfiable in a finite model in $\mathsf{M}$

\deg
degree definted by induction
$$\begin{align*}
    deg(p) &= 0,\\
    deg(\bot) &= 0,\\
    deg(\neg\phi) &= deg(\phi),\\
    deg(\phi\vee\psi) &= max({deg(\phi),deg(\psi)}),\\
    deg(\vartriangle(\phi_1,\cdots,\phi_n)) &= 1+max({deg(\phi_1),\cdots,deg(\phi_n)}).
\end{align*}$$

\def
$n$-bisimilar
$\omega\ \overleftrightarrow{\_\_}_n\ \omega'$ denote that $\omega,\omega'$ are $n$-bisimilar if there exists a sequence of binary relations $Z_n\subseteq\cdots\subseteq Z_0$ with the following properties:
(1) $\omega Z_n\omega'$
(2) $uZ_0u'\Rightarrow(u\in V(p)\Leftrightarrow u'\in V'(p))$
(3) $uZ_{i+1}u'\wedge Ruv\Rightarrow\exist v'(Ru'v'\wedge vZ_{i}v')$
(4) $uZ_{i+1}u'\wedge Ru'v'\Rightarrow\exist v(Ruv\wedge vZ_{i}v')$

$\omega\ \overleftrightarrow{\_\_}_n\ \omega'\Leftrightarrow\omega,\omega'$ agree on all modal formulas of degree at most $n$
