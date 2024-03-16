

denotaion
$\mathscr{I}$ the set of all URM instructions
$\mathscr{P}$ the set of all URM programs

$Set(X),(Denumerable(X)\Leftrightarrow\exist f:X\to \mathbb{N},Bijection(f))$
$Set(X),(EffectivelyDenumerable(X)\Leftrightarrow\exist f:X\to\mathbb{N},Bijection(f),Computable(f),Computable(f^{-1}))$
$Set(X),Enumeration(X)\equiv_{def}(g:\mathbb{N}\to X,Surjection(g))$, donated by $X=\{x_0,x_1,\cdots\}$
$Set(X),(Denumerable(X)\Leftrightarrow Enumeration(X)WithoutRepetitions)$

$EffectivelyDenumerable(\mathbb{N}\times\mathbb{N})\Leftarrow\pi(m,n)=2^m(2n+1)-1$
$\pi^{-1}=(\pi_1(x),\pi_2(x)),\pi_1(x)=(x+1)_1,\pi_2(x)=((x+1)/2^{\pi_1(x)}-1)/2$


$EffectivelyDenumerable(\mathbb{N^+}\times\mathbb{N^+}\times\mathbb{N^+})\Leftarrow\zeta(m,n,q)=\pi(\pi(m-1,n-1),q-1)$
$\zeta^{-1}=(\pi_1(\pi_1(x))+1,\pi_2(\pi_1(x))+1,\pi_2(x)+1)$

$EffectivelyDenumerable(\bigcup_{k>0}\mathbb{N}^k)$
$\tau(a_1,a_2,\cdots,a_k)=2^{a_1}+2^{a_1+a_2+1}+2^{a_1+a_2+a_3+2}+\cdots+2^{a_1+a_2+\cdots+a_k+k-1}-1$
$x+1=2^{b_1}+2^{b_2}+\cdots+2^{b_k},0\le b_1<b_2<\cdots<b_k$
so $\tau^{-1}(x)=(a_1,a_2,\cdots,a_k)$


$EffectivelyDenumerable(\mathscr{I})$
$\beta(Z(n))=4(n-1)$
$\beta(S(n))=4(n-1)+1$
$\beta(T(m,n))=4\pi(m-1,n-1)+2$
$\beta(J(m,n,q))=4\zeta(m,n,q)+3$

$0\equiv\beta(x)\ mod\ 4\Rightarrow Z(x/4+1)$
$1\equiv\beta(x)\ mod\ 4\Rightarrow S((x-1)/4+1)$
$2\equiv\beta(x)\ mod\ 4\Rightarrow T\pi^{-1}((x-2)/4)$
$3\equiv\beta(x)\ mod\ 4\Rightarrow J\zeta^{-1}((x-3)/4)$

$EffectivelyDenumerable(\mathscr{P})$
$\gamma:\mathscr{P}\to\mathbb{N}$
for $P=(I_1,I_2,\cdots,I_k),\gamma(P)=\tau(\beta(I_1),\beta(I_2),\cdots,\beta(I_k))$
$\gamma(P)$ is the code number of $P$, or the $G\"odel$ number of $P$, or just the number of $P$
$P_n=\gamma^{-1}(n)$ is the program where code number is n, and $P_n$ is the $n$-th program
given a program $P$, we can effectively compute the code number $\gamma(P)$, and for any code number $n$, we can effectively compute the program $P_n=\gamma^{-1}(n)$

*URM without Transfer instruction
$\beta(Z(n))=3(n-1)$
$\beta(S(n))=3(n-1)+1$
$\beta(J(m,n,q))=3\zeta(m,n,q)+2$
$0\equiv\beta(x)\ mod\ 3\Rightarrow Z(x/3+1)$
$1\equiv\beta(x)\ mod\ 3\Rightarrow S((x-1)/3+1)$
$2\equiv\beta(x)\ mod\ 3\Rightarrow J\zeta^{-1}((x-2)/3)$

given the $a$-th program $P_a$
$\varPhi_a^{(n)}$ is the $n$-ary function computed by $P_a$, write $\varPhi_a$ for $\varPhi_a^{(1)}$ for convenience
$W_a^{(n)}=\{(x_1,x_2,\cdots,x_n)\mid P_a(x_1,x_2,\cdots,x_n)\downarrow\}$ is the domain of $\varPhi_a^{(n)}$
$E_a^{(n)}$ is the range of $\varPhi_a^{(n)}$
def $\mathscr{C}_a = \varPhi_a^\mathbb{N}=\{\varPhi_a^{(n)}\mid n\in\mathbb{N}\}$, is the function set corrsbound to $P_a$, $EffectivelyDenumerable(\varPhi_a^\mathbb{N})$.
a program is not a function bescause lack the variable field, the program corrsbound to a set of functions which assigment a variable field from $\empty,\mathbb{N},\mathbb{N}^2,\cdots$ by order

def $\mathscr{C}^n = \varPhi_\mathbb{N}^n=\{\varPhi_a^{(n)}\mid a\in\mathbb{N}\}$ means that the set of all $n$-ary computable functions, $Denumerable(\varPhi_\mathbb{N}^n)$
def $\mathscr{C} = \varPhi_\mathbb{N}^\mathbb{N}=\{\varPhi_a^{(n)}\mid a,n\in\mathbb{N}\}$, is the function set in the universe, $Denumerable(\varPhi_\mathbb{N}^\mathbb{N})$

the s-m-n theorem,simple form
$Computable(f(x,y))\Rightarrow\exist k,TC(k),f(x,y)\simeq\varPhi_{k(x)}(y)$

the s-m-n theorem
$\forall m,n\ge1,\exist s^m_n,TC(s^m_n),\varPhi_e^{m+n}(\boldsymbol{x,y})\simeq\varPhi^{(n)}_{s^m_n(e,\boldsymbol{x})}(\boldsymbol{y})$