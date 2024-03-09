# structure
*relational structure* $\mathfrak{F} = (W,R),W\ne\empty\ne R\subseteq W^n, n\in\mathbb{N}$
*transitive closure* $R^+=\bigcap\{R'\mid R'\text{ is a transtive binary relation on }W\And R\subseteq R'\}$
*reflexive transtive closure* $R^\ast = \bigcap\{R'\mid R'\text{ is a reflexive transtive binary relation on }W\And R\subseteq R'\}$
*tree* is a relation structure $(T,S)$ where
(1) the *root* is a unique $r\in T$ such that $\forall t\in T, S^\ast rt$.
(2) $\forall t\ne r$ exist a unique $t', St't$.
(3) $S$ is acyclic, $\forall t\neg S^+tt$

## indistingguishable relation
$Ru_0u_1\cdots u_n$ is indistinguishable if $\forall i,j\le n,i\ne j\in\mathbb{N}, Ru_0u_1\cdots u_i\cdots u_j\cdots u_n \text{ iff }Ru_0u_1\cdots u_j\cdots u_i\cdots u_n$.
if $Ruv$ is indistinguishable, then $R$ is reflexive $Ruv\text{ iff }Rvu$.
there are many indistinguishable relations, for example, $Rabc$ means that $a,b,c$ are elements of a set.


# basic modal lanugage
propositional symble $p,q,r,\cdots\in\Phi$
a unary modal operator $\diamond$
$$\begin{align*}
    \phi ::= p\mid\bot\mid\neg\phi\mid\phi_1\lor\phi_2\mid\diamond\phi
\end{align*}$$
where $p$ ranges over elements of $\Phi$.

a frame for the basic modal language is a binary relation structure $\mathfrak{F} = (W,R)$.
a model for the basic modal language is a triple $\mathcal{M} = (W,R,V)$ where $(W,R)$ is a frame and $V$ is a assigment (valuation) function $V:\Phi\to \mathcal{P}(W)$
formula $\phi$ satisfied (or true) in model $\mathcal{M}$ at state $w$ inductively defined by follows
(1) $\mathcal{M},w \Vdash p \text{ iff } w\in V(p)$,
(2) $\mathcal{M},w \Vdash\bot$ never,
(3) $\mathcal{M},w \Vdash\neg\phi$ iff $\mathcal{M},w \nvDash\phi$,
(4) $\mathcal{M},w \Vdash\phi_1\lor\phi_2$ iff $\mathcal{M},w \Vdash\phi_1$ or $\mathcal{M},w \Vdash\phi_2$,
(5) $\mathcal{M},w \Vdash\diamond\phi$ iff for some $v\in W, wRv$ such that $\mathcal{M},v \Vdash\phi$ .

*the generated state set* of basic modal formulas
$m_R(X)=\{w\in W\mid Rwx\text{ for aome }x\in X\}$
$V(\diamond\phi) = m_R(V(\phi))$


# modal language

*modal similarity type* $\tau = (O,\rho), O\ne\empty, \rho:O\to\mathbb{N}$
*modal operators* is elements of $O$, denoded by $\vartriangle_0,\vartriangle_1,\dotsb$
*modal language* $ML(\tau,\Phi)$ form the formula set $Form(\tau,\Phi)$ by the rule
$$\begin{align*}
    \phi ::= p\mid\bot\mid\neg\phi\mid\phi_1\lor\phi_2\mid\vartriangle(\phi_1,\phi_2,\dotsb,\phi_{\rho(\vartriangle)})
\end{align*}$$
$\triangledown$ is the *dual* of $\vartriangle$ defined by $\triangledown(\phi_1,\phi_2,\dotsb,\phi_{\rho(\vartriangle)}) := \neg\vartriangle(\neg\phi_1,\neg\phi_2,\dotsb,\neg\phi_{\rho(\vartriangle)})$

## frame, modal and satisfied

a frame for the $\tau$-type modal language is a tuple $\mathfrak{F} = (W,\{R_{\vartriangle}\subseteq W^{\rho(\vartriangle)+1}\mid\vartriangle\in\tau\}),W\ne\empty$. 
a model for the $\tau$-type modal language is a tuple $\mathfrak{M} = (\mathfrak{F},V)$, where $V:\Phi\to\mathcal{P}(W)$ is a valuation.
formula $\phi$ satisfied (or true) in model $\mathcal{M}$ at state $w$ inductively defined by follows
(1,2,3,4) the same as basic modal logic.
(5) $\mathcal{M},w \Vdash\vartriangle(\phi_1,\phi_2,\dotsb,\phi_n)$ iff for some $v_1,v_2,\cdots,v_n\in W, R_\vartriangle wv_1v_2\cdots v_n$ such that $\mathcal{M},v_i \Vdash\phi_i$.

## valid on state, frame, class and global

A formula $\phi$ is *valid at a state* $w$ in a frame $\mathfrak{F}$ if $\phi$ is true at $w$ in every model $(\mathfrak{F},V)$ based on $\mathfrak{F}$, denoted by $\mathfrak{F},w\Vdash \phi$.
A formula $\phi$ is *valid at a frame* $\mathfrak{F}$ if it is valid at every state in $\mathfrak{F}$, denoted by $\mathfrak{F}\Vdash \phi$.
A formula $\phi$ is *valid on a class of frames* $\mathsf{F}$ if it is valid on every frame $\mathfrak{F}$ on $\mathsf{F}$, denoted by $\mathsf{F}\Vdash \phi$.
A formula $\phi$ is *valid* if it is valid on the class of all frames, denoted by $\Vdash \phi$.
The set of all formula that are valid on the class of frames $\mathsf{F}$ is called the *logic* of frame $\mathsf{F}$, donated by $\Lambda_\mathsf{F}$

## valuation of modal formulas
*the generated state set* of modal formulas
$m_R(X_1 ,X_2,\cdots,X_n) = \{w\in W\mid Rwx_1x_2\cdots x_n\text{ for some }x_1\in X_1,x_2\in X_2,\cdots,x_n\in X_n\}$

## general frame
a *general $\tau$-frame* is a pair $(\mathfrak{F},A),A\subseteq\mathcal{P}(W)$ where $A$ satisfy the following conditions:
(1) union: if $X,Y\in A$ then $X\cup Y\in A$,
(2) relative complement: if $X\in A$ then $W\backslash X\in A$,
(3) modal operations: if $X_1,X_2,\cdots,X_n\in A$ then $m_{R_\vartriangle}(X_1,X_2,\cdots,X_n)\in A,\forall\vartriangle\in\tau$.
The fitst condition make sure the valuation of $\phi_1\lor\phi_2$ could be difined by the $V(\phi_1)\cup V(\phi_2)$, the second condition make sure the valuation of $\neg\phi$ could be difined by the $W\backslash V(\phi)$, the third condition make sure the valuaion of $\vartriangle(w_1,w_2,\cdots,w_n)$ could be difined by the $m_{R_\vartriangle}(w_1,w_2,\cdots,w_n)$.

## general valid on state, frame, class and global
A formula $\phi$ is *valid at a state* $w$ in a general frame $(\mathfrak{F},A)$ if $\phi$ is true at $w$ in every admissable model $(\mathfrak{F},A,V)$ based on $(\mathfrak{F},A)$, denoted by $(\mathfrak{F},A),w\Vdash \phi$.
A formula $\phi$ is *valid at a general frame* $(\mathfrak{F},A)$ if it is valid at every state and any admissable models $(\mathfrak{F},A,V)$ based on $(\mathfrak{F},A)$, denoted by $(\mathfrak{F},A)\Vdash \phi$.
A formula $\phi$ is *valid on a class of general frames* $\mathsf{G}$ if it is valid on every general frame $(\mathfrak{F},A)$ on $\mathsf{G}$, denoted by $\mathsf{G}\Vdash \phi$.
A formula $\phi$ is *g-valid* if it is valid on the class of all general frames, denoted by $\Vdash_g \phi$.

## Local and Global Semantic Consequence
a similarity type $\tau$ 
$\mathsf{S}$ a class of structure of $\tau$ (a class of models, frames or general frames of $\tau$)
$\varSigma$ and $\phi$ be a set of formulas and a single formula from a language of type $\tau$
$\phi$ is *local semantic consequence* of $\varSigma$ over $\mathsf{S}$ if for all models $\mathcal{M}$ based on $\mathsf{S}$ for any state $w$ if $\mathcal{M},w\Vdash\varSigma$, then $\mathcal{M},w\Vdash\phi$, denoted by $\varSigma\Vdash_{\mathsf{S}}\phi$.
$\phi$ is *global semantic consequence* of $\varSigma$ over $\mathsf{S}$ if for all structure $\mathfrak{G}$ in $\mathsf{S}$ if $\mathfrak{G}\Vdash\varSigma$, then $\mathfrak{G}\Vdash\phi$, denoted by $\varSigma\Vdash_{\mathsf{S}}^g\phi$.

# frame extensions

(experimental) extend the define of modal satisfy as follow:
a $m$ length world line (state sequence) in the universe $W$ is a list of world $(w_1,w_2,\cdots,w_m)\in W^m$.
a frame for the $\tau$-type modal language is a tuple $\mathfrak{F} = (W,\{R_{\vartriangle}\subseteq W^{\rho(\vartriangle)+m}\mid\vartriangle\in\tau,m\in\mathbb{N}\}),W\ne\empty$. 
a model for the $\tau$-type modal language is a tuple $\mathfrak{M} = (\mathfrak{F},V)$, where $V:\Phi\to\mathcal{P}(W)$ is a valuation.
formula $\phi$ satisfied (or true) in model $\mathcal{M}$ at state sequence $\bm{w}=(w_1,w_2,\cdots,w_m)$ inductively defined by follows
(1) $\mathcal{M},\bm{w} \Vdash p \text{ iff } w_1,w_2,\cdots,w_m\in V(p)$,
(2) $\mathcal{M},\bm{w} \Vdash\bot$ never,
(3) $\mathcal{M},\bm{w} \Vdash\neg\phi$ iff $\mathcal{M},\bm{w} \nvDash\phi$,
(4) $\mathcal{M},\bm{w} \Vdash\phi_1\lor\phi_2$ iff $\mathcal{M},\bm{w} \Vdash\phi_1$ or $\mathcal{M},\bm{w} \Vdash\phi_2$,
(5) $\mathcal{M},\bm{w} \Vdash\vartriangle(\phi_1,\phi_2,\dotsb,\phi_n)$ iff for some state sequence $\bm{v}_1,\bm{v}_2,\cdots,\bm{v}_n, R_\vartriangle \bm{w}\bm{v}_1\bm{v}_2\cdots \bm{v}_n$ such that $\mathcal{M},\bm{v}_i \Vdash\phi_i$.
in the special case, if for some state sequence $v_1,v_2,\cdots,v_n\in W, R_\vartriangle \bm{w}v_1v_2\cdots v_n$ such that $\mathcal{M},v_i \Vdash\phi_i $ then $ \mathcal{M},\bm{w} \Vdash\vartriangle(\phi_1,\phi_2,\dotsb,\phi_n)$
just a model defined on the ordered $\mathcal{P}(W)$ ? any differnets with normal model?

## inner and extend view of state

a important inspiration
(1) the inner view, though the state $w$ is a character, when we want to know more specifics and details,it can represent a set of states $w = (s_1,s_2,\cdots)$, for example the vectors on line space.
(2) the extend view, we can add new character $s$ to $w$ and get new state $(w,s)$, so there need a extend universe $W'\subseteq W\times S$ and new relation $R' \subseteq R\times S^2$ to construct new frame and new valuation $V:\Phi\to W\times S$, there is a direct way to extend the model defined by the product of frames.
This is useful method to extend models exist to bigger models, so we can start our work with a simple model, and extend it step by step. We don't need to warry about the bigger models lost some original properties. This also expland why when we want to know something we had better to know from simple and small models. By product, there provide a method to consider the relationship between the new character $s$ and the old states $w$, and show how $S$ affect the properties of $W$.

## inner frames
Given two $\tau$-frame $\mathfrak{F}_1=(W_1,\{R_{\vartriangle}\subseteq W_1^{\rho(\vartriangle)+1}\mid\vartriangle\in\tau\}),W_1\ne\empty$ and $\mathfrak{F}_2=(W_2,\{R_{\vartriangle}\subseteq W_2^{\rho(\vartriangle)+1}\mid\vartriangle\in\tau\}),W_2\ne\empty$
a map $\eta:W_1\to W_2$
define $\mathcal{R} = \{R_{\vartriangle}\subseteq W_1^{\rho(\vartriangle)+1}\mid\vartriangle\in\tau\}$
then we get a new $\tau$-frame $\mathfrak{F}=(W_2,\{(\eta w_1,\eta w_2,\cdots,\eta w_{\rho(\vartriangle)+1}\mid w_1, w_2,\cdots,w_{\rho(\vartriangle)+1}\in R_{\vartriangle}\subseteq W_1^{\rho(\vartriangle)+1},\vartriangle\in\tau )\}\bigcup\{R_{\vartriangle}\subseteq W_2^{\rho(\vartriangle)+1}\mid\vartriangle\in\tau\})$, we say that $\mathfrak{F}$ is the frame $\mathfrak{F}_1$ explaned by $\mathfrak{F}_2$, and the $\mathfrak{F}_2$ is *inner frame* of $\mathfrak{F}$.

## frame product
*new frames by product (frame extension)*
Given a fimily $\tau$-frames $\{\mathfrak{F}_j\}j\in J$ where $\mathfrak{F}_j = (W_j,\{R_{\vartriangle}\subseteq W_j^{\rho(\vartriangle)+1}\mid\vartriangle\in\tau\}),W_j\ne\empty$. The product of this family frames is a new frame defined by $\mathfrak{F} = (\prod_{j\in J}W_j,\{R_\vartriangle\subseteq\prod_{j\in J}W_j^{\rho(\vartriangle)+1}\mid\vartriangle\in\tau\})$. In most case, we just work on the subframes of $\mathfrak{F}$.



# normal modal logic

A $\mathbf{K}$-$proof$ is a list of formulas which is an *axiom* or could be derived from the former formulas by the use of *rule of proof*, the axiom of $\mathbf{K}$ is all the instance of propositional tautologies puls:
(1) $\Box(\phi_1\to\phi_2)\to(\Box\phi_1\to\Box\phi_2)$
(2) $\diamond\phi\leftrightarrow\neg\Box\neg\phi$
rools of proof of $\mathbf{K}$ are:
(1) Modus ponens: given $\phi$ and $\phi\to\psi$, prove $\psi$,
(2) Uniform substitution: given $\phi$, prove $\psi$, where $\psi$ is obtained from $\phi$ by uniformly replacing propositions letters in $\phi$ by arbitaty formulas.
(3) Generalization: given $\phi$, prove $\Box\phi$.

Normal modal logic
A normal modal logic is a set of formulas that contains all tautologies, $\Box(\phi_1\to\phi_2)\to(\Box\phi_1\to\Box\phi_2)$, $\diamond\phi\leftrightarrow\neg\Box\neg\phi$ and that is colsed under *modus ponens*, *uniform substitution* and *generalization*. we call the smallest normal logic $\mathbf{K}$.