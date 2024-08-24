import re

# 示例 LaTeX 证明字符串
latex_code = r"""
\begin{align*}
    &(1)\ P \rightarrow (Q \rightarrow P) \quad \text{(Axiom)} \\
    &(2)\ \Box(P \rightarrow (Q \rightarrow P)) \quad \text{(NEC, 1)} \\
    &(3)\ \Box(P \rightarrow (Q \rightarrow P)) \rightarrow (\Box P \rightarrow \Box(Q \rightarrow P)) \quad \text{(Axiom)} \\
    &(4)\ \Box P \rightarrow \Box(Q \rightarrow P) \quad \text{(MP, 2, 3)} \\
    &(5)\ P \rightarrow \Box P \quad \text{(Axiom)} \\
    &(6)\ P \rightarrow \Box(Q \rightarrow P) \quad \text{(MP, 4, 5)} \\
    &(7)\ P \rightarrow \Box(\neg Q \rightarrow \neg P) \quad \text{(S, 6)}
\end{align*}
"""

# 正则表达式用于提取每一行的公式、推理规则及其依赖步骤
step_pattern = re.compile(r'&\((\d+)\)\s*')
step_pattern = re.compile(r'([^\s\(\)]+(?:\([^\)]+\))*)')
step_pattern = re.compile(r'&\((\d+)\)\s*(.*?)\s*\\text\{(.*?)\}')

# 测试正则表达式
for match in step_pattern.finditer(latex_code):
    step_number = match.group(1)
    formula_str = match.group(2)
    justification_str = match.group(3)
    
    print(f"Step Number: {step_number}")
    print(f"Formula: {formula_str}")
    print(f"Justification: {justification_str}")
    print()

# 如果需要，可以在这里添加调试信息，检查正则表达式的行为
