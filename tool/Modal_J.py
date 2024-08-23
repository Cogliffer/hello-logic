from Modal_K import *

class VariableSequence:
    """定义一个变元序列，并管理已使用的变元"""
    def __init__(self, max_length):
        self.max_length = max_length
        self.variable_list = [f"x_{i+1}" for i in range(max_length)]
        self.used_variables = set()

    def get_unused_variable(self):
        """获取一个尚未使用的变元"""
        for var in self.variable_list:
            if var not in self.used_variables:
                self.used_variables.add(var)
                return var
        raise ValueError("No unused variables left!")

class Formula:
    """逻辑公式的基类"""
    def replace_box_with_unused_var(self, var_sequence):
        """替换公式中的 Box 为 Box_{x_i} 形式"""
        raise NotImplementedError("Subclasses should implement this!")

class Prop(Formula):
    """命题变量"""
    def replace_box_with_unused_var(self, var_sequence):
        return self  # 命题变量不需要替换

class Not(Formula):
    """逻辑非运算符"""
    def replace_box_with_unused_var(self, var_sequence):
        return Not(self.subformulas[0].replace_box_with_unused_var(var_sequence))

class Implication(Formula):
    """逻辑蕴含运算符"""
    def replace_box_with_unused_var(self, var_sequence):
        left_replaced = self.subformulas[0].replace_box_with_unused_var(var_sequence)
        right_replaced = self.subformulas[1].replace_box_with_unused_var(var_sequence)
        return Implication([left_replaced, right_replaced])

class Box(Formula):
    """模态逻辑中的 Box 算子"""
    def replace_box_with_unused_var(self, var_sequence):
        unused_var = var_sequence.get_unused_variable()
        return TBox(self.subformula.replace_box_with_unused_var(var_sequence), var=unused_var)


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
            return self.subformulas == other.subformulas
        return False

    def __hash__(self):
        return hash((self.__class__, self.subformulas[0]))


# 示例公式
var_seq = VariableSequence(max_length=10)
formula = Implication([Box(Prop("P")), Box(Not(Prop("Q")))])

# 替换 Box 操作符
new_formula = formula.replace_box_with_unused_var(var_seq)

print(new_formula)  # 应该输出: (□_{x_1}P → □_{x_2}¬Q)