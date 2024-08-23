import random

class PropositionalLogicFormulaGenerator:
    def __init__(self, num_symbols, logic_symbols=None):
        self.num_symbols = num_symbols
        self.logic_symbols = logic_symbols if logic_symbols else [r'\neg', r'\lor', r'\land', r'\rightarrow']
        self.used_symbols = set()
        self.symbol_list = ["A_{"+str(i+1)+"}" for i in range(num_symbols)]
        self.formula = ""

    def get_random_symbol(self):
        if len(self.used_symbols) == 0:
            # First symbol, always use A_1
            symbol = self.symbol_list[0]
            self.used_symbols.add(symbol)
        else:
            # Randomly select a symbol
            symbol = random.choice(self.symbol_list)
            if symbol not in self.used_symbols:
                symbol = self.symbol_list[len(self.used_symbols)]
                self.used_symbols.add(symbol)
        return symbol

    def generate_formula(self, length):
        if length == 1:
            return self.get_random_symbol()
        
        logic_symbol = random.choice(self.logic_symbols)
        
        if logic_symbol == r'\neg':
            return f'({logic_symbol} {self.generate_formula(random.randint(1, length - 1))})'
        else:
            left_formula = self.generate_formula(length - random.randint(1, length - 1))
            right_formula = self.generate_formula(length - random.randint(1, length - 1))
            return f'({left_formula} {logic_symbol} {right_formula})'

    def generate_random_formula(self, length):
        self.used_symbols.clear()  # Clear the used symbols for a fresh formula
        return self.generate_formula(length)


# 示例使用
num_symbols = 5  # 可以使用的命题符号数量
generator = PropositionalLogicFormulaGenerator(num_symbols, [r'\neg', r'\rightarrow'])

# 生成一个随机的命题逻辑公式
random_formula = generator.generate_random_formula(10)  # 设置公式的长度

with open(r'hello-logic\tool\test.md', 'w') as f:
    f.write("$"+random_formula+"$")
print(random_formula)
