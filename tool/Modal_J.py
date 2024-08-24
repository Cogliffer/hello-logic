from Modal_K import *


class TBox(Formula):
    """表示模态逻辑中的 Box 算子"""
    dim = 1

    def __init__(self, formula, term):
        super().__init__()
        self.term = term
        if isinstance(formula, Formula):
            self.subformulas = [formula]
        elif isinstance(formula, list) and len(formula) == 1:
            if isinstance(formula[0], Formula):
                self.subformulas = formula
            else:
                raise ValueError("Box expects a Formula type")
        else:
            raise ValueError("Box expects exactly one formula")

    def __str__(self):
        return "□_{"+str(self.term)+"} "+str(self.subformulas[0])

    def __eq__(self, other):
        if isinstance(other, TBox):
            # return self.term == other.term and self.subformulas == other.subformulas
            return self.subformulas == other.subformulas
        return False

    def __hash__(self):
        return hash((self.__class__, self.subformulas[0]))
    
    def forget(self):
        return Box(self.subformulas[0].forget())



class VariableSequence:
    """定义一个变元序列，并管理已使用的变元"""
    def __init__(self, max_length):
        self.max_length = max_length
        self.variable_list = [f"x_{i+1}" for i in range(max_length)]
        self.used_variables = set()

    def get_unused_variable(self):
        """获取一个尚未使用的变元"""
        # for var in self.variable_list:
        #     if var not in self.used_variables:
        #         self.used_variables.add(var)
        #         return var
        # raise ValueError("No unused variables left!")
        return self.variable_list.pop(0)

# class JProp(Prop):
#     """命题变量"""
def replace_box_with_unused_var(self, vars):
    return self  # 命题变量不需要替换
Prop.replace_box_with_unused_var = replace_box_with_unused_var
def forget(self):
    return self  # 命题变量不需要忘记
Prop.forget = forget

# class JNot(Not):
#     """逻辑非运算符"""
def replace_box_with_unused_var(self, vars):
    return Not(self.subformulas[0].replace_box_with_unused_var(vars))
Not.replace_box_with_unused_var = replace_box_with_unused_var
def forget(self):
    return Not(self.subformulas[0].forget())
Not.forget = forget

# class JImplication(Implication):
#     """逻辑蕴含运算符"""
def replace_box_with_unused_var(self, vars):
    left_replaced = self.subformulas[0].replace_box_with_unused_var(vars)
    right_replaced = self.subformulas[1].replace_box_with_unused_var(vars)
    return Implication([left_replaced, right_replaced])
Implication.replace_box_with_unused_var = replace_box_with_unused_var
def forget(self):
    return Implication([self.subformulas[0].forget(), self.subformulas[1].forget()])
Implication.forget = forget

# class JBox(Box):
#     """模态逻辑中的 Box 算子"""
def replace_box_with_unused_var(self, vars):
    unused_var = vars.get_unused_variable()
    return TBox(self.subformulas[0].replace_box_with_unused_var(vars), term=unused_var)
Box.replace_box_with_unused_var = replace_box_with_unused_var

def check_T_Necessitation(formulas):
    A,B = formulas
    return Box(A) == B

T_NEC = Justification("T_Necessitation", "Rule", TBox, check_T_Necessitation)

MJ = Logic({
    "Formulas": {Prop, Not, Implication, TBox},
    "Axioms": PL_Axioms,
    "Rules": {MP},
})


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

    def convert_from_ML(self, proof):
        var = VariableSequence(100)
        for step in proof.steps:
            if step.justification.type == "Axiom":
                if step.formula in PL_Axioms:
                    self.steps.append(step)
                elif step.formula in MK.Axioms:
                    j1 = var.variable_list.pop(0)
                    j2 = var.variable_list.pop(0)
                    var.variable_list = [j1,j2,j1+"·"+j2] + var.variable_list
                    self.add_step(step.formula.replace_box_with_unused_var(var), step.justification, step.content)
            elif step.justification.type == "Substitution":
                i = step.content[0]
                s = step.content[1]
                js = MJSubstitution(s.substitutions, s.name, var)
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
                f = modus_ponens(self.steps[i1].formula, self.steps[i2].formula)
                self.add_step(f, MP, step.content)


# # 示例公式
# var_seq = VariableSequence(max_length=100)
# formula = Implication([Box(Prop("P")), Box(Not(Prop("Q")))])


# # 替换 Box 操作符
# new_formula = formula.replace_box_with_unused_var(var_seq)

# print(new_formula)  # 应该输出: (□_{x_1}P → □_{x_2}¬Q)

jproof = MJProofSequence()
jproof.convert_from_ML(proof)
print(proof,"\n")
print(jproof)