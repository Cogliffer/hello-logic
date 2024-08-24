

class Formula:
    """基类，表示逻辑公式的节点"""
    def __init__(self):
        pass

    def __str__(self):
        raise NotImplementedError("Subclasses should implement this!")

    def __eq__(self, other):
        if not isinstance(other, Formula):
            return False
        return self.equals(other)

    def __hash__(self):
        """Hash method should be implemented in subclasses."""
        raise NotImplementedError("Subclasses should implement this!")

class Prop(Formula):
    """表示命题变量"""
    dim = 0

    def __init__(self, name):
        super().__init__()
        self.subformula = None
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Prop):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

class Not(Formula):
    """表示逻辑非运算符"""
    dim = 1

    def __init__(self, formula):
        super().__init__()
        if isinstance(formula, Formula):
            self.subformulas = [formula]
        elif isinstance(formula, list) and len(formula) == 1:
            if isinstance(formula[0], Formula):
                self.subformulas = formula
            else:
                raise ValueError("Not expects a Formula type")
        else:
            raise ValueError("Not expects exactly one formula")

    def __str__(self):
        return f"¬{self.subformulas[0]}"

    def __eq__(self, other):
        if isinstance(other, Not):
            return self.subformulas == other.subformulas
        return False

    def __hash__(self):
        return hash((self.__class__, self.subformulas[0]))

class Implication(Formula):
    """表示逻辑蕴含运算符"""
    dim = 2

    def __init__(self, formulas):
        super().__init__()
        if isinstance(formulas, list) and len(formulas) == 2:
            if isinstance(formulas[0], Formula) and isinstance(formulas[0], Formula):
                self.subformulas = formulas
            else:
                raise ValueError("Implication expects Formulas")
        else:
            raise ValueError("Implication expects a list of two formulas")

    def __str__(self):
        return f"({self.subformulas[0]} → {self.subformulas[1]})"

    def __eq__(self, other):
        if isinstance(other, Implication):
            return self.subformulas[0] == other.subformulas[0] and self.subformulas[1] == other.subformulas[1]
        return False

    def __hash__(self):
        return hash((self.__class__, self.subformulas[0], self.subformulas[1]))


PL_Axioms = {
    Implication([Prop("p"), Implication([Prop("q"), Prop("p")])]),  # 公理 1
    Implication([
        Implication([Prop("p"), Implication([Prop("q"), Prop("r")])]),
        Implication([Implication([Prop("p"), Prop("q")]), Implication([Prop("p"), Prop("r")])])
    ]),  # 公理 2
    Implication([Not(Prop("p")), Implication([Prop("p"), Prop("q")])])  # 公理 3
}

def modus_ponens(formula1, formula2):
    """应用 Modus Ponens 规则，返回推导出的公式"""
    
    # 检查 formula1 是否为蕴含公式 (A → B)
    if isinstance(formula1, Implication):
        if formula2 == formula1.subformulas[0]:
            return formula1.subformulas[1]
    
    # 检查 formula2 是否为蕴含公式 (A → B)
    if isinstance(formula2, Implication):
        if formula1 == formula2.subformulas[0]:
            return formula2.subformulas[1]
    
    return None

def check_modus_ponens(formulas):
    A,B,C = formulas
    return modus_ponens(A,B) == C

class Justification():
    def __init__(self, name, type, method=None, checker=None):
        self.name = name
        self.type = type # "Rule" or "Axiom" or "Substitution"
        self.method = method
        self.checker = checker
    
    def __str__(self):
        return self.name

A = Justification("Axiom", "Axiom")
S = Justification("Substitution", "Substitution")
MP = Justification("Modus Ponens", "Rule", modus_ponens, check_modus_ponens)

class Logic():

    def __init__(self, logic):
        self.Formulas = logic["Formulas"]
        self.Axioms = logic["Axioms"]
        self.Rules = logic["Rules"]
    
    def add_formulas(self, formulas_set):
        self.Formulas = self.Formulas.union(formulas_set)

    def add_axioms(self, axioms_set):
        self.Axiom = self.Axiom.union(axioms_set)
    
    def add_rules(self, rules_set):
        self.Rules = self.Rules.union(rules_set)

PL = Logic({
    "Formulas": {Prop, Not, Implication},
    "Axioms": PL_Axioms,
    "Rules": {MP},
})

class Substitution:
    """表示一个替换"""
    def __init__(self, substitutions, name):
        self.logic = PL
        self.name = name  # 替换的名称
        self.substitutions = substitutions  # 字典，键为变量名，值为替换的公式

    def apply(self, formula):
        """应用替换到给定的公式"""
        # 这里简化处理，假设公式对象的 replace 方法可以处理替换
        for operator in self.logic.Formulas:
            if isinstance(formula, operator):
                if operator.dim == 0:
                    if formula.name in self.substitutions:
                        return self.substitutions[formula.name]
                    else:
                        return formula
                else:
                    return operator([self.apply(subformula) for subformula in formula.subformulas])
    
    def __str__(self):
        return str(self.name)


class ProofStep:
    """表示证明中的一个步骤"""
    def __init__(self, formula, justification, content=None):
        self.formula = formula  # 公式对象
        self.justification = justification
        self.content = content if content is not None else None  # 默认是空列表，表示没有依赖

    def __str__(self):
        if self.justification.type == "Axiom":
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
        self.logic = PL
        self.proof_sequence = proof_sequence

    def check_axiom(self, step_index):
        step = self.proof_sequence.steps[step_index]
        if step.content is not None:
            return False
        return step.formula in self.logic.Axioms

    def check_substitution(self, step_index):
        step = self.proof_sequence.steps[step_index]
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
            if step.justification.type == "Axiom":
                if not self.check_axiom(i):
                    print(f"Invalid step at index {i}: {step.formula}")
                    return False
            elif step.justification.type == "Substitution":
                if not self.check_substitution(i):
                    print(f"Invalid step at index {i}: {step.formula}")
                    return False
            elif step.justification.type == "Rule" and step.justification in self.logic.Rules:
                checker = step.justification.checker
                if not isinstance(step.content, list):
                    return False
                for index in step.content:
                    if index >= i:
                        return False
                content = [self.proof_sequence.steps[index].formula for index in step.content]+[step.formula]
                if not checker(content):
                    print(f"Invalid step at index {i}: {step.formula}")
                    return False
        return True


