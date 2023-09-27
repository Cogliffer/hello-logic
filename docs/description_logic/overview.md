# 引导
描述逻辑（Description Logics，简称DLs）是一族知识表示（knowledge representation）语言，用来以结构化和易读的方式表示知识。

<!-- 整个知识分为几个层面，知识层、构建层、直观层、例子层，构建层在这个文档中声明了，知识层是向抽象、向哲学的思考，直观层更加贴合应用，例子层更容易实在的把握 -->

描述逻辑通常将知识分为两个部分：一个称为TBox（Terminological Box）的术语部分，以及一个称为ABox（Assertional Box）的断言部分。TBox和ABox的组合被称为知识库（Knowledge Base, KB）。TBox表示有关结构的知识，而ABox表示关于具体实例的知识。

## 知识库的例子
比如说在 TBox 中可以有：教师是一个教授课程的人，学生是一个参加课程的人，以及学生不教授课程。在 ABox中可以有：柏拉图和亚里士多德都是人，逻辑学前沿是一门课，柏拉图教授逻辑学前沿，亚里士多德参加逻辑学前沿。这些可以用一阶逻辑的句子来表示：

$$
\begin{align}
    & \forall x (Teacher(x) \Leftrightarrow Person(x) \land \exists y (teaches(x, y) \land Course(y))),\\
    & \forall x (Student(x) \Leftrightarrow Person(x) \land \exists y (attends(x, y) \land Course(y))),\\
    & \forall x ((\exists y \, teaches(x, y)) \Rightarrow \neg Student(x)),\\
    & Person(\text{Plato}),\\
    & Person(\text{Aristotle}),\\
    & Course(\text{LogicFrontiers}),\\
    & attends(\text{Aristotle}, \text{LogicFrontiers}),\\
    & teaches(\text{Plato}, \text{LogicFrontiers})\\
\end{align}
$$

用描述逻辑可以表示为：

$$
\begin{align}
    & Teacher \equiv Person \sqcap \exists teaches.Course,\\
    & Student \equiv Person \sqcap \exists attends.Course,\\
    & \exists attends.\top \sqsubseteq \neg Student,\\
    & \text{Plato} : Person,\\
    & \text{Aristotle} : Person,\\
    & \text{LogicFrontiers} : Course,\\
    & (\text{Aristotle} , \text{LogicFrontiers}) : attends,\\
    & (\text{Plato} , \text{LogicFrontiers}) : teaches\\
\end{align}
$$

前三个构成这个知识库的 Tbox ，后三个构成 ABox。我们能从这个知识库中推出亚里士多德是学生，因为亚里士多德是一个参加逻辑前沿课程的人，这个过程可以形式化的完成。

## 哲学
描述逻辑在这样的知识论前提下进行，将知识区分为抽象类和具体实例，并通过关系谓词表示类之间的关系，由此可以构建出分层的本体论知识体系。

认识论假设：

- 抽象概念 $C$ 的意义由 $C$ 的例子解释，或者说对 $C$ 的认识是通过 $C$ 的实例抽象出来的。

# 总览

![描述逻辑](assert/contents.png)

## 1. 背景
用于知识表示和语义网。

## 2. 定义
描述逻辑（Description Logic）是一种基于谓词逻辑的逻辑语言，用于表示知识库和知识推理。

## 3. 推理问题
一般的推理任务包括检查概念的可满足性，检查知识库 KB 的一致性，判断是否一个概念比另一个概念更具体（subsumption），判断一个对象是否是某个类的实例。
- 唯一性，避免出现两个相同的概念（位态相同/结构相同），结构提取
- 一致性，

## 4. 算法复杂性
DLs 推理问题的求解计算极其复杂，以至于不得不在表达能力和计算复杂度之间做出平衡。因为 DLs 系统众多，并且复杂度问题并不是逻辑主要关注的，因此我将只介绍基本的复杂度结论。
<details>
<summary>Notes</summary>
复杂度问题多在理论计算机领域被研究，因为描述逻辑在计算机科学里涉及具体的应用，是否存在合理的运行时间直接决定是否能够应用，因此算法问题被看作重要的一部分。
</details>

## 5. 非标准系统
能在模态逻辑找到对应的成为标准部分，非标准的就是没有直接对应的

## 6. 当代进展
对 DLs 的扩展仍然随着应用的需求不断丰富，同时 DLs 也作为知识表示和推理的基础，在语义网和知识库中占据重要地位。