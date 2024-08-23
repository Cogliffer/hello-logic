from Modal_K import *


PL_replacements = {
    '→': r'\rightarrow ',
    '¬': r'\neg '
}

ML_replacements = {
    '→': r'\rightarrow ',
    '□': r'\Box ',
    '¬': r'\neg '
}

def replace_operators_with_latex(formula_str, replacements = PL_replacements):
    """将公式字符串中的逻辑算子替换为 LaTeX 符号"""
    
    for symbol, latex in replacements.items():
        formula_str = formula_str.replace(symbol, latex)
    
    return formula_str

def parse_latex_ML(latex_str):
    """将 LaTeX 字符串解析为 Formula 对象"""
    
    # 去除外部的空格
    latex_str = latex_str.strip()

    # 移除外部括号
    if latex_str.startswith('(') and latex_str.endswith(')'):
        latex_str = latex_str[1:-1]
    
    # 处理否定符号
    if latex_str.startswith(r'\neg'):
        subformula = parse_latex_ML(latex_str[4:].strip())
        return Not(subformula)

    # 处理 Box 算子
    if latex_str.startswith(r'\Box'):
        subformula = parse_latex_ML(latex_str[4:].strip())
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
        return Implication(parse_latex_ML(left), parse_latex_ML(right))

    # 如果不是 \neg、\Box 或 \rightarrow，处理为命题变量
    return Prop(latex_str)