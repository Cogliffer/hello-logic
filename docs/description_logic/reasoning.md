# 3. 标准推理(Reasoning)

## 3.1 T 推理(Terminological Reasoning)

- 可满足 (Satisfiability)：如果存在一个概念描述 $C$ 和一个 TBox $\mathcal{T}$ 的共同模型时，那么 $C$ 相对于 $\mathcal{T}$ 是可满足的。
- 包含 (Subsumption)：如果对于一个 TBox $\mathcal{T}$ 的任意模型 $\mathcal{I}$，均有 $C^{\mathcal{I}} \subseteq D^{\mathcal{I}}$ ，那么概念描述 $C$ 包含在概念描述 $D$ 中，记为 $C \sqsubseteq_{\mathcal{T}} D$ 。
- 相等 (equivalent)：如果对于一个 TBox $\mathcal{T}$ 的任意模型 $\mathcal{I}$，均有 $C^{\mathcal{I}} = D^{\mathcal{I}}$ ，那么概念描述 $C$ 与概念描述 $D$ 相等，记为 $C \equiv_{\mathcal{T}} D$ 。
- 相等推理 $C \equiv_{\mathcal{T}} D$ 可以自然的归为两次包含推理 $C \sqsubseteq_{\mathcal{T}} D$ ， $D \sqsubseteq_{\mathcal{T}} C$ 。
- 包含推理 $C \sqsubseteq_{\mathcal{T}} D$ 可以归结为 $C \sqcap \neg D$ 相对于 $\mathcal{T}$ 是不可满足的。

## 3.2 A 推理(Assertional Reasoning)

- 一致性 (Consistency)：如果存在一个 ABox $\mathcal{A}$ 和一个 TBox $\mathcal{T}$ 的共同模型，那么 $\mathcal{A}$ 相对于 $\mathcal{T}$ 是一致的。
- 实例检测 (Instance Detection)：如果对于一个 TBox $\mathcal{T}$ 和一个 ABox $\mathcal{A}$ 的任意共同模型 $\mathcal{I}$ ，均有 $a^{\mathcal{I}} \in C^{\mathcal{I}}$，那么个体实例 $a$ 相对于 $\mathcal{T}$ 是概念描述 $C$ 的实例，记为 $\mathcal{A} \models_{\mathcal{T}} C(a)$ 。
- 一个 ABox $\mathcal{A}$ 是一致的当且仅当对任意个体名称 $a$ 均有 $\mathcal{A} \nvDash_{\mathcal{T}} \bot(a)$ 。
- $\mathcal{A} \models_{\mathcal{T}} C(a)$ 当且仅当 $\mathcal{A}\ \cup \{ \neg C(a) \}$ 相对于 $\mathcal{T}$ 是不一致的，当且仅当 $C_{\mathcal{A}}\ \cup \{ \neg C(a) \}$ 相对于 $\mathcal{T}$ 是不一致的，当且仅当不存在一个 $C_{\mathcal{A}}\ \cup \{ \neg C(a) \}$ 和 $\mathcal{T}$ 的共同模型，当且仅当  $C_{\mathcal{A}}\ \cup \{ \neg C(a) \}$ 相对于 $\mathcal{T}$ 是不可满足的。

## 3.3 复合推理问题(Compound Inference Problems)

- Classification (结构化)：给定一个 TBox $\mathcal{T}$ ，计算 $\mathcal{T}$ 中概念名称（抽象类）之间起约束作用的包含关系($\sqsubseteq_{\mathcal{T}}$)。
- Realization (抽象化)：给定一个 ABox $\mathcal{A}$ ，一个 TBox $\mathcal{T}$ 以及个体实例 $a$ ，计算 $\mathcal{T}$ 中满足 $\mathcal{A} \models_{\mathcal{T}} A(a)$ 的概念名称 $A$ 构成的集合，记为 $R_{\mathcal{A},\mathcal{T}}(a)$，并用包含关系 $\sqsubseteq_{\mathcal{T}}$ 找到最小的。
- Retrieval (实例化)：给定一个 ABox $\mathcal{A}$ ，一个 TBox $\mathcal{T}$ 以及概念 $C$ ，计算 $\mathcal{A}$ 中满足 $\mathcal{A} \models_{\mathcal{T}} C(a)$ 的个体实例 $a$ 构成的集合，记为 $\mathcal{I}_{\mathcal{A},\mathcal{T}}(C)$ 。

## 3.4 为何需要研究复合推理问题？


