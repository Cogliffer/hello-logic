class Formula:
    """基类，表示逻辑公式的节点"""
    def __init__(self):
        pass

    def __str__(self):
        raise NotImplementedError("Subclasses should implement this!")

    def replace(self, substitution):
        """替换公式中的变量"""
        raise NotImplementedError("Subclasses should implement this!")

    def __eq__(self, other):
        if not isinstance(other, Formula):
            return False
        return self.equals(other)

    def __hash__(self):
        """Hash method should be implemented in subclasses."""
        raise NotImplementedError("Subclasses should implement this!")

    def equals(self, other):
        """ Method to be overridden by subclasses. """
        raise NotImplementedError("Subclasses should implement this!")

class Prop(Formula):
    """表示命题变量"""
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def replace(self, substitution):
        if self.name in substitution.substitutions:
            return substitution.apply(self)
        return self

    def __eq__(self, other):
        if isinstance(other, Prop):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

class Not(Formula):
    """表示逻辑非运算符"""
    def __init__(self, subformula):
        super().__init__()
        self.subformula = subformula

    def __str__(self):
        return f"¬{self.subformula}"

    def replace(self, substitution):
        return Not(self.subformula.replace(substitution))

    def __eq__(self, other):
        if isinstance(other, Not):
            return self.subformula == other.subformula
        return False

    def __hash__(self):
        return hash((self.__class__, self.subformula))

class Implication(Formula):
    """表示逻辑蕴含运算符"""
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} → {self.right})"

    def replace(self, substitution):
        return Implication(self.left.replace(substitution), self.right.replace(substitution))

    def __eq__(self, other):
        if isinstance(other, Implication):
            return self.left == other.left and self.right == other.right
        return False

    def __hash__(self):
        return hash((self.__class__, self.left, self.right))

class Box(Formula):
    """表示模态逻辑中的 Box 算子"""
    def __init__(self, subformula):
        super().__init__()
        self.subformula = subformula

    def __str__(self):
        return f"□{self.subformula}"

    def replace(self, substitution):
        return Box(self.subformula.replace(substitution))

    def __eq__(self, other):
        if isinstance(other, Box):
            return self.subformula == other.subformula
        return False

    def __hash__(self):
        return hash((self.__class__, self.subformula))




class Substitution:
    """表示一个替换"""
    def __init__(self, substitutions, name):
        self.substitutions = substitutions  # 字典，键为变量名，值为替换的公式
        self.name = name  # 替换的名称

    def apply(self, formula):
        """应用替换到给定的公式"""
        # 这里简化处理，假设公式对象的 replace 方法可以处理替换
        if isinstance(formula, Prop):
            # 查找替换规则
            if formula.name in self.substitutions:
                return self.substitutions[formula.name]
            else:
                return formula
        elif isinstance(formula, Not):
            return Not(self.apply(formula.subformula))
        elif isinstance(formula, Implication):
            return Implication(self.apply(formula.left), self.apply(formula.right))
        elif isinstance(formula, Box):
            return Box(self.apply(formula.subformula))
        return formula

    def __str__(self):
        return str(self.name)


import random

class ModalLogicFormulaGenerator:
    def __init__(self, num_symbols):
        self.num_symbols = num_symbols
        self.symbol_list = ["A_" + str(i + 1) for i in range(num_symbols)]
        self.logic_symbols = [r'\neg', r'\rightarrow', r'\Box']
        self.used_symbols = set()
    
    def get_random_symbol(self):
        if len(self.used_symbols) == 0:
            # First symbol, always use A_1
            symbol = self.symbol_list[0]
            self.used_symbols.add(symbol)
        else:
            # Randomly select a symbol
            symbol = random.choice(self.symbol_list)
            if symbol not in self.used_symbols:
                symbol = self.symbol_list[len(self.used_symbols) % self.num_symbols]
                self.used_symbols.add(symbol)
        return symbol
    
    def generate_formula(self, depth):
        """递归生成公式"""
        if depth == 1:
            return self.get_random_symbol()
        
        logic_symbol = random.choice(self.logic_symbols)
        
        if logic_symbol == r'\neg':
            return f"({logic_symbol} {self.generate_formula(depth - 1)})"
        elif logic_symbol == r'\Box':
            return f"({logic_symbol} {self.generate_formula(depth - 1)})"
        else:  # r'\rightarrow'
            left_formula = self.generate_formula(depth - random.randint(1, depth - 1))
            right_formula = self.generate_formula(depth - random.randint(1, depth - 1))
            return f"({left_formula} {logic_symbol} {right_formula})"
    
    def generate_random_formula(self, depth):
        self.used_symbols.clear()  # 清除已使用的符号以生成新公式
        return self.generate_formula(depth)


def replace_operators_with_latex(formula_str):
    """将公式字符串中的逻辑算子替换为 LaTeX 符号"""
    replacements = {
        '→': r'\rightarrow ',
        '□': r'\Box ',
        '¬': r'\neg '
    }
    
    for symbol, latex in replacements.items():
        formula_str = formula_str.replace(symbol, latex)
    
    return formula_str


def parse_latex(latex_str):
    """将 LaTeX 字符串解析为 Formula 对象"""
    
    # 去除外部的空格
    latex_str = latex_str.strip()

    # 移除外部括号
    if latex_str.startswith('(') and latex_str.endswith(')'):
        latex_str = latex_str[1:-1]
    
    # 处理否定符号
    if latex_str.startswith(r'\neg'):
        subformula = parse_latex(latex_str[4:].strip())
        return Not(subformula)

    # 处理 Box 算子
    if latex_str.startswith(r'\Box'):
        subformula = parse_latex(latex_str[4:].strip())
        return Box(subformula)

    # 处理蕴含符号
    bracket_level = 0
    main_operator_index = -1
    
    # 查找最外层的蕴含符号
    for i in range(len(latex_str)):
        char = latex_str[i]
        t = latex_str[i:i+11]
        if char == '(':
            bracket_level += 1
        elif char == ')':
            bracket_level -= 1
        elif bracket_level == 0 and latex_str[i:i+11] == r'\rightarrow':
            main_operator_index = i
            break

    # 如果找到了蕴含符号，分割公式并递归解析
    if main_operator_index != -1:
        left = latex_str[:main_operator_index].strip()
        right = latex_str[main_operator_index + 11:].strip()  # 10 是 "\rightarrow" 的长度
        return Implication(parse_latex(left), parse_latex(right))

    # 如果不是 \neg、\Box 或 \rightarrow，处理为命题变量
    return Prop(latex_str)


class ProofStep:
    """表示证明中的一个步骤"""
    def __init__(self, formula, justification, content=None):
        self.formula = formula  # 公式对象
        self.justification = justification
        self.content = content if content is not None else None  # 默认是空列表，表示没有依赖

    def __str__(self):
        if self.justification == "Axiom":
            return f"{self.formula}     ({self.justification})"
        else:
            content_str = ", ".join(map(str, self.content))
            return f"{self.formula}     ({self.justification}, {content_str})"


# 创建证明序列
class ProofSequence:
    def __init__(self):
        self.steps = []

    def add_step(self, formula, justification, content=None):
        self.steps.append(ProofStep(formula, justification, content))
    
    def __str__(self):
        return "\n".join([str(i)+") "+str(step) for i, step in enumerate(self.steps)])


class ProofValidator:
    def __init__(self, proof_sequence):
        self.proof_sequence = proof_sequence
        # 定义希尔伯特三条公理
        self.axioms = {
            Implication(Prop("p"), Implication(Prop("q"), Prop("p"))),  # 公理 1
            Implication(
                Implication(Prop("p"), Implication(Prop("q"), Prop("r"))),
                Implication(Implication(Prop("p"), Prop("q")), Implication(Prop("p"), Prop("r")))
            ),  # 公理 2
            Implication(Not(Prop("p")), Implication(Prop("p"), Prop("q")))  # 公理 3
        }
        # 定义 K 公理
        self.k_axiom = Implication(
            Box(Implication(Prop("p"), Prop("q"))),
            Implication(Box(Prop("p")), Box(Prop("q")))
        )

    def check_axiom(self, step_index):
        step = self.proof_sequence.steps[step_index]
        if step.justification != "Axiom":
            return False
        if step.content is not None:
            return False
        return step.formula in self.axioms or step.formula == self.k_axiom

    def check_modus_ponens(self, step_index):
        step = self.proof_sequence.steps[step_index]
        if step.justification != "Modus Ponens":
            return False
        if not isinstance(step.content, list) or len(step.content) != 2:
            return False
        index1, index2 = step.content
        if index1 >= step_index or index2 >= step_index:
            return False
        formula1 = self.proof_sequence.steps[index1].formula
        formula2 = self.proof_sequence.steps[index2].formula
        mp = modus_ponens(formula1, formula2)
        if mp is None:
            return False
        return mp == step.formula

    def check_necessitation(self, step_index):
        step = self.proof_sequence.steps[step_index]
        if step.justification != "Necessitation":
            return False
        if not isinstance(step.content, list) or len(step.content) != 1:
            return False
        index = step.content[0]
        if index >= step_index:
            return False
        formula = self.proof_sequence.steps[index].formula
        return Box(formula) == step.formula

    def check_substitution(self, step_index):
        step = self.proof_sequence.steps[step_index]
        if step.justification != "Substitution":
            return False
        if not isinstance(step.content, list) or len(step.content) != 2:
            return False
        index = step.content[0]
        substitution = step.content[1]
        if not isinstance(index, int) or not isinstance(substitution, Substitution):
            return False
        original_formula = self.proof_sequence.steps[index].formula
        substituted_formula = substitution.apply(original_formula)
        return substituted_formula == step.formula

    def validate(self):
        for i in range(len(self.proof_sequence.steps)):
            step = self.proof_sequence.steps[i]
            if step.justification == "Modus Ponens":
                if not self.check_modus_ponens(i):
                    print(f"Invalid step at index {i}: {step.formula}")
                    return False
            elif step.justification == "Necessitation":
                if not self.check_necessitation(i):
                    print(f"Invalid step at index {i}: {step.formula}")
                    return False
            elif step.justification == "Substitution":
                if not self.check_substitution(i):
                    print(f"Invalid step at index {i}: {step.formula}")
                    return False
            elif step.justification == "Axiom":
                if not self.check_axiom(i):
                    print(f"Invalid step at index {i}: {step.formula}")
                    return False
        return True




# generator = ModalLogicFormulaGenerator(num_symbols=5)

# # 生成一个深度为 3 的随机模态逻辑公式
# formula = generator.generate_random_formula(depth=6)
# print(formula)

# # 创建公式实例
# formula_p = Prop("p")
# formula_q = Prop("q")
# formula = Implication(formula_p, Not(formula_q))


# # 应用替换
# new_formula = substitution.apply(formula)

# # 打印结果
# print("Original formula:", formula)
# print("Substituted formula:", new_formula)

# 创建公式实例
formula1 = Implication(Prop("p"), Implication(Prop("q"), Prop("p")))
formula2 = Implication(
    Implication(Prop("p"), Implication(Prop("q"), Prop("r"))),
    Implication(Implication(Prop("p"), Prop("q")), Implication(Prop("p"), Prop("r")))
)
formula3 = Implication(Not(Prop("p")), Implication(Prop("p"), Prop("q")))
formula4 = Implication(
    Box(Implication(Prop("p"), Prop("q"))),
    Implication(Box(Prop("p")), Box(Prop("q")))
)

# 定义替换规则
s1 = Substitution({
    "p": Implication(Prop("p"),Prop("q"))
},"\sigma1")

s2 = Substitution({
    "p": Implication(Prop("p"),Prop("q")),
    "q": Implication(Prop("q"),Implication(Prop("p"),Prop("q")))
},"\sigma2")


def modus_ponens(formula1, formula2):
    """应用 Modus Ponens 规则，返回推导出的公式"""
    
    # 检查 formula1 是否为蕴含公式 (A → B)
    if isinstance(formula1, Implication):
        if formula2 == formula1.left:
            return formula1.right
    
    # 检查 formula2 是否为蕴含公式 (A → B)
    if isinstance(formula2, Implication):
        if formula1 == formula2.left:
            return formula2.right
    
    return None



proof = ProofSequence()
proof.add_step(formula1, "Axiom")
proof.add_step(formula2, "Axiom")
proof.add_step(formula3, "Axiom")
proof.add_step(formula4, "Axiom")
proof.add_step(s1.apply(formula1), "Substitution",[0,s1])
proof.add_step(s2.apply(formula4), "Substitution",[3,s2])
proof.add_step(Box(s1.apply(formula1)), "Necessitation",[4])
proof.add_step(modus_ponens(Box(s1.apply(formula1)), s2.apply(formula4)), "Modus Ponens",[5,6])

# 验证证明
validator = ProofValidator(proof)
if not validator.validate():
    print("Proof is invalid.")
else:
    print("Proof is Valid.")
    print(proof)