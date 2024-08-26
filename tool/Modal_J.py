from Modal_K import *

class TBox(UnaryOperator):

    def __init__(self, formula, term):
        super().__init__(formula)
        self.term = term
        self.str = "□_{"+str(self.term)+"} "
        self.latex = r"\Box"+"_"+str(self.term)+" "

    def forget(self):
        return Box(self.subformulas[0].forget())

# 定义符号
class Var:
    """表示一个变元"""
    def __init__(self, num):
        self.num = num
    
    def __str__(self):
        return "x_{" + str(self.num) + "}"

    def __mul__(self, other):
        """定义两个 Var 实例的点积"""
        if isinstance(other, Var):
            # 返回一个格式化的字符串，表示这两个变量的点乘
            return Dot(self, other)

# 定义表达式
class Dot:
    """表示一个变元的点积"""
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    
    def __str__(self):
        return "(" + str(self.t1) + " · " + str(self.t2) + ")"

#定义项
class Term:
    """表示一个项"""
    def __init__(self, term):
        self.term = term

    def __str__(self):
        return str(self.term)

class Equation:
    """表示一个等式"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " = " + str(self.right)


class VariableSequence:
    """定义一个变元序列，并管理已使用的变元"""
    def __init__(self, max_length):
        self.max_length = max_length
        self.unused_variable = [Var(i+1) for i in range(max_length)]
        self.used_variables = set()

    def get_unused_variable(self):
        """获取一个尚未使用的变元"""
        return self.unused_variable.pop(0)

def replace_box_with_unused_var(self, vars):
    return self  # 命题变量不需要替换
Prop.replace_box_with_unused_var = replace_box_with_unused_var
def forget(self):
    return self  # 命题变量不需要忘记
Prop.forget = forget

def replace_box_with_unused_var(self, vars):
    return Not(self.subformulas[0].replace_box_with_unused_var(vars))
Not.replace_box_with_unused_var = replace_box_with_unused_var
def forget(self):
    return Not(self.subformulas[0].forget())
Not.forget = forget

def replace_box_with_unused_var(self, vars):
    left_replaced = self.subformulas[0].replace_box_with_unused_var(vars)
    right_replaced = self.subformulas[1].replace_box_with_unused_var(vars)
    return type(self)([left_replaced, right_replaced])
def forget(self):
    return type(self)([self.subformulas[0].forget(), self.subformulas[1].forget()])
BinaryOperator.replace_box_with_unused_var = replace_box_with_unused_var
BinaryOperator.forget = forget

def replace_box_with_unused_var(self, vars):
    unused_var = vars.get_unused_variable()
    return TBox(self.subformulas[0].replace_box_with_unused_var(vars), term=Term(unused_var))
Box.replace_box_with_unused_var = replace_box_with_unused_var

def check_T_Necessitation(formulas):
    A,B = formulas
    return Box(A) == B

T_NEC = Justification("T_Necessitation", "Rule", TBox, check_T_Necessitation)

MJ = Logic({
    "Formulas": {Prop, Not, Implication, TBox, And, Or},
    "Axioms": PL_Axioms,
    "Rules": {MP},
})

def equal_equations(formulas1:list, formulas2:list):
    """两个公式序列相同的变元条件"""
    if len(formulas1) != len(formulas2):
        return
    for formula1, formula2 in zip(formulas1, formulas2):
        if formula1.forget() != formula2.forget():
            return
    equations = set()
    for formula1, formula2 in zip(formulas1, formulas2):
        if isinstance(formula1, TBox) and isinstance(formula2, TBox):
            equations.add(Equation(formula1.term, formula2.term))
        if not isinstance(formula1, Prop) and not isinstance(formula2, Prop):
            f = equal_equations(formula1.subformulas, formula2.subformulas)
            equations |= equal_equations(formula1.subformulas, formula2.subformulas)
    return equations


def MJ_modus_ponens(formula1, formula2):
    """应用 Modus Ponens 规则，返回推导出的公式"""
    print(formula1,"\n", formula2)
    # 检查 formula1 是否为蕴含公式 (A → B)
    if isinstance(formula1, Implication):
        if formula2 == formula1.subformulas[0]:
            return formula1.subformulas[1], equal_equations([formula2] , [formula1.subformulas[0]])
    
    # 检查 formula2 是否为蕴含公式 (A → B)
    if isinstance(formula2, Implication):
        if formula1 == formula2.subformulas[0]:
            return formula2.subformulas[1], equal_equations([formula1] , [formula2.subformulas[0]])
    
    return None

class MJSubstitution(Substitution):

    def __init__(self, substitutions, name, vars):
        super().__init__(substitutions, name)
        self.logic = MJ
        for k,v in substitutions.items():
            substitutions[k] = v.replace_box_with_unused_var(vars)
        self.substitutions = substitutions

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
                elif isinstance(formula, TBox):
                    return operator([self.apply(subformula) for subformula in formula.subformulas],formula.term)
                else:
                    return operator([self.apply(subformula) for subformula in formula.subformulas])
    

class MJProofSequence(ProofSequence):
    def __init__(self): 
        super().__init__()
        self.equations = set()

    def convert_from_ML(self, proof):
        var = VariableSequence(100)
        def instance_of_K_Axiom():
            j1 = var.unused_variable.pop(0)
            j2 = var.unused_variable.pop(0)
            var.unused_variable = [j1,j2,j1 * j2] + var.unused_variable
            K, = K_Axiom
            return K.replace_box_with_unused_var(var)
        for step in proof.steps:
            # print(str(step.formula))
            if step.justification.type == "Axiom":
                if step.formula in PL_Axioms:
                    self.steps.append(step)
                elif step.formula in MK.Axioms:
                    self.add_step(instance_of_K_Axiom(), step.justification, step.content)
                elif step.justification.name == "TAUT":
                    self.steps.append(step)
            elif step.justification.type == "Substitution":
                s = step.content[0]
                js = MJSubstitution(s.substitutions, s.name, var)
                i = step.content[1]
                if self.steps[i].formula.forget() in K_Axiom:
                    f = js.apply(instance_of_K_Axiom())
                else:
                    f = js.apply(self.steps[i].formula)
                self.add_step(f,S, step.content) 
            elif step.justification.type == "Rule" and step.justification.name == "Necessitation":
                i = step.content[0]
                v = var.get_unused_variable()
                f = TBox(self.steps[i].formula,v)
                self.add_step(f, T_NEC, step.content)
            elif step.justification.type == "Rule" and step.justification.name == "Modus Ponens":
                i1 = step.content[0]
                i2 = step.content[1]
                f, eq = MJ_modus_ponens(self.steps[i1].formula, self.steps[i2].formula)
                self.add_step(f, MP, step.content)
                self.equations.update(eq)
            # print(str(self.steps[-1].formula))


class EquationSolver:

    def __init__(self, equations, proof :MJProofSequence):
        self.equations = equations
        self.proof = proof

    def solve(self):
        pass

# # 示例公式
# var_seq = VariableSequence(max_length=100)
# formula = Implication([Box(Prop("P")), Box(Not(Prop("Q")))])


# # 替换 Box 操作符
# new_formula = formula.replace_box_with_unused_var(var_seq)

# print(new_formula)  # 应该输出: (□_{x_1}P → □_{x_2}¬Q)

# jproof = MJProofSequence()
# jproof.convert_from_ML(proof)
# print(proof,"\n")
# print(jproof)