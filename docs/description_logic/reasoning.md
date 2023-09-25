# 标准推理(Reasoning)

## T 推理(Terminological Reasoning)

- 可满足 (Satisfiability)：如果存在一个概念描述 $C$ 和一个 TBox $\mathcal{T}$ 的共同模型时，那么 $C$ 相对于 $\mathcal{T}$ 是可满足的。
- 包含 (Subsumption)：如果对于一个 TBox $\mathcal{T}$ 的任意模型 $\mathcal{I}$，均有 $C^{\mathcal{I}} \subseteq D^{\mathcal{I}}$ ，那么概念描述 $C$ 包含在概念描述 $D$ 中，记为 $C \sqsubseteq_{\mathcal{T}} D$ 。
- 可满足性推理是基本推理，其它推理问题归结为可满足性推理。

## A 推理(Assertional Reasoning)

- 一致性 (Consistency)：如果存在一个 ABox $\mathcal{A}$ 和一个 TBox $\mathcal{T}$ 的共同模型，那么 $\mathcal{A}$ 相对于 $\mathcal{T}$ 是一致的。
- 实例检测 (Instance Detection)：如果对于一个 TBox $\mathcal{T}$ 和一个 ABox $\mathcal{A}$ 的任意共同模型 $\mathcal{I}$ ，均有 $a^{\mathcal{I}} \in C^{\mathcal{I}}$，那么 $\mathcal{A}$ 中的个体实例 $a$ 相对于 $\mathcal{T}$ 是概念描述 $C$ 的实例，记为 $\mathcal{A} \models_{\mathcal{T}} C(a)$ 。
- 一致性推理和 TBox 的可满足性类似，都是基本推理，推理类其它推理问题归结为一致性推理。

## 复合推理问题(Compound Inference Problems)

- Classification (结构化)：给定一个 TBox $\mathcal{T}$ ，计算 $\mathcal{T}$ 中概念名称（抽象类）之间起约束作用的包含关系($\sqsubseteq_{\mathcal{T}}$)。
- Realization (抽象化)：给定一个 ABox $\mathcal{A}$ ，一个 TBox $\mathcal{T}$ 以及个体实例 $a$ ，计算 $\mathcal{T}$ 中满足 $\mathcal{A} \models_{\mathcal{T}} A(a)$ 的概念名称 $A$ 构成的集合，记为 $R_{\mathcal{A},\mathcal{T}}(a)$，并用包含关系 $\sqsubseteq_{\mathcal{T}}$ 最小化。
- Retrieval (实例化)：给定一个 ABox $\mathcal{A}$ ，一个 TBox $\mathcal{T}$ 以及概念 $C$ ，计算 $\mathcal{A}$ 中满足 $\mathcal{A} \models_{\mathcal{T}} C(a)$ 的个体实例 $a$ 构成的集合，记为 $\mathcal{I}_{\mathcal{A},\mathcal{T}}(C)$ 。

## 为何需要研究复合推理问题？


