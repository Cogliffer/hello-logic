# 6. 描述逻辑的发展前景 — (a little peek)

当今描述逻辑通常被视作本体语言（Ontology language，用于构建本体的形式语言）的重要逻辑基础，基于描述逻辑的知识库现在多被称为本体知识库（Ontology Knowledge Base）。很有前景的趋势是将符号计算和深度学习结合的研究，例如概念学习（Concept Learning）。

## 6.1 传统路线

### 6.1.1 DLs 表达能力的扩展：集成其他逻辑

- 20世纪末21世纪初：时间描述逻辑、模糊描述逻辑、分布式描述逻辑、模态描述逻辑、概率描述逻辑、分布式动态描述逻辑等众多结合。
- 近几年：模糊空间描述逻辑 $^{[8,2022]}$、类比推理的描述逻辑 $^{[9,2021]}$、非分布式描述逻辑 $^{[10,2023]}$。

### 6.1.2 DLs 表达能力和算法的平衡

- Franz Baader $^{[11,2023]}$：大多数 DL 都是一阶逻辑（FOL）的可判定片段，即它们的表达能力弱于 FOL ，但也有一些可判定的 DL，其知识库（KBs）并不能总是由 FOL 句子表示 $^{[12,2019]}$。具体域的 DL 就是一个例子，带具体域的 $\mathcal{ALC}$ 或者说一阶逻辑（FOL）的扩展具有和 FOL 相同的形式属性，如紧致性和 Löwenheim-Skolem 属性。

## 6.2 新生路线

### 6.2.1 语义网络的当代发展：知识图谱

语义网发展为知识图谱，知识图谱没有一个普遍接受的定义。大多数定义是通过语义网视角来看待的，主要包含以下特点 $^{[1]}$ ：

- 知识图（i）定义实体的抽象类和关系，（ii）主要描述现实世界的实体及其相互关系，以图形式组织，（iii）允许任意实体之间潜在的相互关联，以及（iv）涵盖多个领域的知识 $^{[2]}$ 。
- 一般结构：实体及其语义类型、属性和关系的网络 $^{[3,4]}$ 。经常使用分类标签或数值表示属性。
- 支持基于本体的推理：知识图谱获取信息并将其集成到本体中，并应用推理算法来获得新知识 $^{[5]}$ 。

然而，有许多知识图谱与其中一些特征不相关。对于那些知识图，这个更简单的定义可能更有用：

- 知识图谱将知识表示为概念及其之间关系的结构。知识图谱可以包含一个允许人类和机器理解和推理其内容的本体知识库 $^{[6]}$ 。

### 6.2.2 符合主义和联结主义的结合：概念学习

传统的深度学习，将数据表示为高维度向量，有利于计算机处理，但是是人类不可读的。例如在 ChatGPT 中，词向量空间是一个 768 维的空间，每个词语都可以在这个空间中表示为一个 768 维的向量，人类很难读懂一个向量是如何和词建立联系的。

描述逻辑提供了一种解决的可能，将计算机形成的语言表征和概念系统联系起来，形成概念学习，如下图所示。DLs 提供了人类和计算机均可读的本体知识库，利用 DLs 被认为是实现可解释人工智能（AI）的方法之一。

![Concept Learning](assert/concept%20learning.png)

定义好的初始 DLs 提供了类和实例，可以供神经网络学习，然后在接受新的实例时，根据习得的模型进行分类（类抽象），或者在接受到外部反馈时进行纠正。
<!-- 在何种差异下形成新的类，并如何在外部反馈下进行命名。 -->

### 6.2.3 智能机器人上的应用：自动规划和调度 $^{[7]}$ 

自动规划和调度（Automated planning and scheduling）是人工智能的一个分支，涉及策略或行动序列的实现。机器人需要对环境具有复杂的知识，以处理任务或执行行动。知识表示和推理（KR＆R）技术提供了这种程度的知识，以感知任务环境。这些技术包括描述逻辑（DL）和基于本体的方法 。


<!-- ### 我的临时起意：标准 $\mathcal{ALC}$ 和认知逻辑的结合

1. $K_a(\text{Aristotle} : Person)$
2. $K_a(\text{LogicFrontiers} : Course)$
3. $K_a((\text{Aristotle} , \text{LogicFrontiers}) : attends)$
4. $K_a(Student \equiv Person \sqcap \exists attends.Course)$

$\therefore$ $K_a(\text{Aristotle} : Student)$

动机：一个 DL 系统为了保持一致性，就必须使概念之间不能冲突，而从哲学史可以看到，基本概念之间的冲突是不可避免的，并且也普遍存在不同主体对同一个概念存在不同解释的繁琐情况。于是相比于在系统中允许不一致而带来混乱，更合理的做法是在系统中引入多主体。 -->



## 参考文献

- [1] Hogan, Aidan; Blomqvist, Eva; Cochez, Michael; d'Amato, Claudia; de Melo, Gerard; Gutierrez, Claudio; Labra Gayo, José Emilio; Kirrane, Sabrina; Neumaier, Sebastian; Polleres, Axel; Navigli, Roberto; Ngonga Ngomo, Axel-Cyrille; Rashid, Sabbir M.; Rula, Anisa; Schmelzeisen, Lukas; Sequeda, Juan; Staab, Steffen; Zimmermann, Antoine (2021-01-24). "Knowledge Graphs". ACM Computing Surveys. 54 (4): 1–37.
- [2] Paulheim, Heiko (2017). "Knowledge Graph Refinement: A Survey of Approaches and Evaluation Methods" (PDF). Semantic Web: 489–508. Retrieved 21 March 2017.
- [3] Krötsch, Markus; Weikum, Gerhard (March 2016). "Editorial of the Special Issue on Knowledge Graphs". Journal of Web Semantics. 37–38: 53–54. doi:10.1016/j.websem.2016.04.002. Retrieved 10 February 2021.
- [4] "What is a Knowledge Graph?|Ontotext". Ontotext. Retrieved 2020-07-01.
- [5] Ehrlinger, Lisa; Wöß, Wolfram (2016). Towards a Definition of Knowledge Graphs (PDF). SEMANTiCS2016. Leipzig: Joint Proceedings of the Posters and Demos Track of 12th International Conference on Semantic Systems – SEMANTiCS2016 and 1st International Workshop on Semantic Change & Evolving Semantics (SuCCESS16). pp. 13–16.
- [6] "The Knowledge Graph about Knowledge Graphs". 2020.
- [7] A. N. Krishna et al. (eds.), Integrated Intelligent Computing, Communication and Security, Studies in Computational Intelligence 771
- [8] Cheng, H., Ma, Z. & Li, P. A fuzzy spatial description logic for the semantic web. J Ambient Intell Human Comput 13, 4991–5009 (2022). https://doi.org/10.1007/s12652-020-01864-9
- [9] Steven Schockaert, Yazmín Ibáñez-García, Víctor Gutiérrez-Basulto, A Description Logic for Analogical Reasoning. https://doi.org/10.48550/arXiv.2105.04620
- [10] R. Ramanayake and J. Urban (Eds.): TABLEAUX 2023, LNAI 14278, pp. 49–69, 2023. https://doi.org/10.1007/978-3-031-43513-3_4
- [11] Franz Baader and Filippo De Bortoli: On the Abstract Expressive Power of Description Logics with Concrete Domains. In Oliver Kutz and Ana Ozaki, editors, Proceedings of the 36th International Workshop on Description Logics (DL'23), volume of CEUR Workshop Proceedings. Rhodes, Greece, CEUR-WS, 2023. To appear
- [12] Baader, F., De Bortoli, F. (2019). On the Expressive Power of Description Logics with Cardinality Constraints on Finite and Infinite Sets. In: Herzig, A., Popescu, A. (eds) Frontiers of Combining Systems. FroCoS 2019. Lecture Notes in Computer Science(), vol 11715. Springer, Cham. https://doi.org/10.1007/978-3-030-29007-8_12