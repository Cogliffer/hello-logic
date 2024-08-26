from Modal_J import *


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

    # 处理二元算子
    bracket_level = 0
    main_operator_index = -1
    imply_index = -1
    and_index = -1
    or_index = -1
    
    # 查找最外层的二元算子
    for i in range(len(latex_str)):
        char = latex_str[i]
        imply_ = latex_str[i:i+11]
        and_ = latex_str[i:i+5]
        or_ = latex_str[i:i+3]
        if char == '(':
            bracket_level += 1
        elif char == ')':
            bracket_level -= 1
        elif bracket_level == 0 and imply_ == r'\rightarrow':
            imply_index = i
            break
        elif bracket_level == 0 and and_ == r'\land':
            and_index = i
            break
        elif bracket_level == 0 and or_ == r'\lor':
            or_index = i
            break
        

    # 如果找到了二元算子，分割公式并递归解析
    if imply_index != -1:
        left = latex_str[:imply_index].strip()
        right = latex_str[imply_index + 11:].strip()
        return Implication([parse_latex_ML(left), parse_latex_ML(right)])
    elif and_index != -1:
        left = latex_str[:and_index].strip()
        right = latex_str[and_index + 5:].strip()
        return And([parse_latex_ML(left), parse_latex_ML(right)])
    elif or_index != -1:
        left = latex_str[:or_index].strip()
        right = latex_str[or_index + 4:].strip()
        return Or([parse_latex_ML(left), parse_latex_ML(right)])
    
    # 处理否定符号
    if latex_str.startswith(r'\neg'):
        subformula = parse_latex_ML(latex_str[4:].strip())
        return Not(subformula)

    # 处理 Box 算子
    if latex_str.startswith(r'\Box'):
        subformula = parse_latex_ML(latex_str[4:].strip())
        return Box(subformula)
    
    # 移除外部括号
    if latex_str.startswith('(') and latex_str.endswith(')'):
        latex_str = latex_str[1:-1]
        return parse_latex_ML(latex_str)
    
    # 如果不是 \neg、\Box 或 \rightarrow，处理为命题变量
    return Prop(latex_str)


import re

def parse_latex_proof(latex):
    """解析LaTeX代码并将其转换为ProofSequence"""
    proof_sequence = ProofSequence()
    
    # 正则表达式用于提取每一行的公式、推理规则及其依赖步骤
    step_pattern = re.compile(r'&\((\d+)\)\\\s*(.*?)\s*\\quad\s*\\text\{\((.*?)\)\}')
    
    for match in step_pattern.finditer(latex):
        step_number = int(match.group(1))
        formula_str = match.group(2)
        justification_str, *content_strs = match.group(3).split(",")
        
        # 使用parse_latex_ML解析公式
        formula = parse_latex_ML(formula_str.strip())
        
        # 创建 Justification 对象
        if justification_str == "Axiom":
            justification_obj = A
            content = None
        elif justification_str == "TAUT":
            justification_obj = Justification("TAUT", "Axiom")
            content = None
        elif justification_str == "S":
            s = content_strs[0].strip()
            s = globals()[s]
            i = int(content_strs[1])
            justification_obj = S
            content = [s, i]
        else:
            # 处理其他规则或公理
            content = [int(c) for c in content_strs] if content_strs else None
            justification_obj = globals()[justification_str]
        
        proof_sequence.add_step(formula, justification_obj, content)
    
    return proof_sequence

# LaTeX代码示例
latex_code = r"""
$$\begin{align*}
    &(0)\ (p\land q)\rightarrow p \quad \text{(TAUT)} \\
    &(1)\ \Box((p\land q)\rightarrow p) \quad \text{(NEC, 0)} \\
    &(2)\ \Box(p \rightarrow q) \rightarrow (\Box p \rightarrow \Box q) \quad \text{(Axiom, K)} \\
    &(3)\ \Box((p\land q) \rightarrow p) \rightarrow (\Box (p\land q) \rightarrow \Box p) \quad \text{(S, s1, 2)} \\
    &(4)\ \Box (p\land q) \rightarrow \Box p \quad \text{(MP, 1, 3)}\\
    &(5)\ (p\land q)\rightarrow q \quad \text{(TAUT)} \\
    &(6)\ \Box((p\land q)\rightarrow q) \quad \text{(NEC, 5)} \\
    &(7)\ \Box((p\land q) \rightarrow q) \rightarrow (\Box (p\land q) \rightarrow \Box q) \quad \text{(S, s2, 2)} \\
    &(8)\ \Box (p\land q) \rightarrow \Box q \quad \text{(MP, 6, 7)}\\
    &(9)\ (p \rightarrow q)\rightarrow ((p\rightarrow r)\rightarrow(p\rightarrow(q\land r))) \quad \text{(TAUT)} \\
    &(10)\ (\Box (p\land q) \rightarrow \Box p)\rightarrow ((\Box (p\land q)\rightarrow \Box q)\rightarrow(\Box (p\land q)\rightarrow  (\Box p\land \Box q))) \quad \text{(S, s3, 9)} \\
    &(11)\ (\Box (p\land q)\rightarrow \Box q)\rightarrow(\Box (p\land q)\rightarrow(\Box p\land \Box q)) \quad \text{(MP, 4, 10)} \\
    &(12)\ \Box (p\land q)\rightarrow(\Box p\land \Box q) \quad \text{(MP, 8, 11)} \\
\end{align*}$$
"""
s1 = MKSubstitution({
    "p": And([Prop("p"), Prop("q")]),
    "q": Prop("p")
},"s1")
s2 = MKSubstitution({
    "p": And([Prop("p"), Prop("q")]),
},"s2")
s3 = MKSubstitution({
    "p": Box(And([Prop("p"), Prop("q")])),
    "q": Box(Prop("p")),
    "r": Box(Prop("q"))
},"s3")

def standard(content):
    return r"$$\begin{align*}"+"\n"+content+"\n"+r"\end{align*}$$"

# 解析LaTeX代码
proof = parse_latex_proof(latex_code)

# 打印证明序列
print(proof,"\n")

jproof = MJProofSequence()
jproof.convert_from_ML(proof)
print(standard(str(jproof)))

eq = "&"+"\\\\\n&".join([str(eq) for eq in jproof.equations])
print(standard(eq))