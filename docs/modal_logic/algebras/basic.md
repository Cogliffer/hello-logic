Similarity Type
*similarity type* $\mathcal{F} = (F,\rho), F \ne \emptyset, \rho:F\rightarrow \mathbb{N}$
*function symble* $f\in F$
*arity or rank* of $f$ is $\rho(f)$
*constant* $c,\rho(c) = 0$
denote $f\in \mathcal{F}$ means $f\in F$

Algebra
*algebra* of type $\mathcal{F}$ is $\mathfrak{A}=(A,I),A\ne\empty$
*carrier* of $\mathfrak{A}$ is $A$
*interpretation* $I:F\rightarrow\{f\mid\forall n\in\mathbb{N},f:A^n\rightarrow A\}$ for $f\in F,\rho(f)=\mathrm{rank}(I(f))$
denote $\mathfrak{A}=(A,f_\mathfrak{A})_{f\in\mathcal{F}}$ means $\mathfrak{A}$ defined above

Homomorphisms
type $\mathcal{F}$
algebra $\mathfrak{A}=(A,f_\mathfrak{A})_{f\in\mathcal{F}}$ and $\mathfrak{B}=(B,f_\mathfrak{B})_{f\in\mathcal{F}}$
*homomorphisms* is a map $\eta:A\rightarrow B$ where
$$\begin{align*}
    & \forall f\in\mathcal{F}, \forall x_1,x_2,\cdots,x_n\in A, n=\rho(f),\\
    & \eta(f_{\mathfrak{A}}(x_1,x_2,\cdots,x_n)) = f_{\mathfrak{B}}(\eta(x_1),\eta(x_2),\cdots,\eta(x_n))
\end{align*}$$
for constant $\eta(c_\mathfrak{A})=c_{\mathfrak{B}}$
??? *kernel* of homomorphisms from $\mathfrak{A}$ to $\mathfrak{B}$ is the relation $ker$ $f=\{(a,a')\in A^2\mid f(a)=f(a')\}$
*homomorphic image* of $\mathfrak{A}$ is $\mathfrak{B}$ if $\eta$ is surjective, denoted by $\mathfrak{A}\twoheadrightarrow\mathfrak{B}$, $\mathbf{H}\mathsf{C}$ is the class of homomorphic images of algebra in class $\mathsf{C}$ of algebras.
*isomorphisms* is a bijective homomorphisms, two algebra is *isomorphic* if there is an isomorphism between them.

Subalgebras
$\mathfrak{B}=(B,f_\mathfrak{A}\upharpoonright_B)_{f\in\mathcal{F}}$ is a *subalgebra* of $\mathfrak{A}=(A,f_\mathfrak{A})_{f\in\mathcal{F}}$ if $B\subseteq A$ and $B$ is closed under $f_\mathfrak{A}$.
*embedding* is a isomorphisms from $\mathfrak{C}$ to the subalgebra of $\mathfrak{A}$, denoted by $\mathfrak{C}\rightarrowtail\mathfrak{A}$, $\mathbf{S}\mathsf{C}$ is the class of isomorphic copied of subalgebras of algebra in class $\mathsf{C}$ of algebras.

Products
a family of algebras $(\mathfrak{A_j})_{j\in J}$
*products* of the family $\prod_{j\in J}\mathfrak{A_j}$ is the algebra $\mathfrak{A}=(A,f_\mathfrak{A})_{f\in\mathcal{F}}, A=\prod_{j\in J}A_j, f_\mathfrak{A}$ defined by
$$\begin{align*}
    & \forall x_1,x_2,\cdots,x_n\in A, \forall j\in J, \\
    & f_{\mathfrak{A}}(x_1,x_2,\cdots,x_n)_j = f_{\mathfrak{A}_j}(x_{1,j},x_{2,j},\cdots,x_{n,j})
\end{align*}$$
when all the algebras $\mathfrak{A}_j$ are the same, we call $\mathfrak{A}^J$ a power of $\mathfrak{A}$.
$\mathbf{P}\mathsf{C}$ is the class of isomorphic copied of products of algebra in class $\mathsf{C}$ of algebras.

Varieties
a *variety* is a class of algebras which is closed under taking subalgebras, homomorphic images, and products.
$\mathbb{V}\mathsf{C}$ is the variety generated by a class $\mathsf{C}$ of algebras, that is the smallest variety containing $\mathsf{C}$.

Congruences
$\mathcal{F}$-algebra $\mathfrak{A}=(A,f_\mathfrak{A})_{f\in\mathcal{F}}$
*congruences* is an equivalence relation $\sim$ on $A$ satisfies
$$\begin{align*}
    & \forall f\in F, \forall a_1,a_2,\cdots,a_n,b_1,b_2,\cdots,b_n\in A, n=\rho(f) \\
    & \text{if }a_1\sim b_1 \And a_2\sim b_2 \And \cdots \And a_n\sim b_n, \\
    & \text{then }f_\mathfrak{A}(a_1,a_2,\cdots,a_n)\sim f_\mathfrak{A}(b_1,b_2,\cdots,b_n).
\end{align*}$$
*natural map* is the function $\pi:a\mapsto[a],a\in A$ associated with the congruence. 

Quotient ALgebras
$\mathcal{F}$-algebra $\mathfrak{A}=(A,f_\mathfrak{A})_{f\in\mathcal{F}}$ with congruences $\sim$
*quotient algebra* of $\mathfrak{A}$ by $\sim$ is the algebra $\mathfrak{A}/\hspace{-1mm}\sim = (A/\hspace{-1mm}\sim,f_{\mathfrak{A}/\sim})$ where
$$\begin{align*}
    & A/\hspace{-1mm}\sim = \{[a]\mid a\in A\} \\
    & f_{\mathfrak{A}/\sim}([a_1],[a_2],\cdots,[a_n]) = [f_\mathfrak{A}(a_1,a_2,\cdots,a_n)].
\end{align*}$$

Themorem. Homomorphisms and Congruences
$\mathcal{F}$-algebra $\mathfrak{A}$, then
(1) If $f:\mathfrak{A}\rightarrow\mathfrak{B}$ is a homomorphisim, its kernel is a congruences on $\mathfrak{A}$.
(2) If $\mathfrak{A}/\hspace{-1mm}\sim$ is a quotient algebra, then its associated natural map $\pi$ is a surjective homomorphism from $\mathfrak{A}$ to $\mathfrak{A}/\hspace{-1mm}\sim$.







