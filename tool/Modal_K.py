from PL import *


class Box(Formula):
    """表示模态逻辑中的 Box 算子"""
    dim = 1

    def __init__(self, formula):
        super().__init__()
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
        return f"□{self.subformulas[0]}"

    def __eq__(self, other):
        if isinstance(other, Box):
            return self.subformulas == other.subformulas
        return False

    def __hash__(self):
        return hash((self.__class__, self.subformulas[0]))


K_Axiom = {Implication([
    Box(Implication([Prop("p"), Prop("q")])),
    Implication([Box(Prop("p")), Box(Prop("q"))])
])}

def check_Necessitation(formulas):
    A,B = formulas
    return Box(A) == B

NEC = Justification("Necessitation", "Rule", Box, check_Necessitation)

MK = Logic({
    "Formulas": {Prop, Not, Implication, Box},
    "Axioms": PL_Axioms.union(K_Axiom),
    "Rules": {MP, NEC},
})

class MKSubstitution(Substitution):

    def __init__(self, substitutions, name):
        super().__init__(substitutions, name)
        self.logic = MK

class MKProofValidator(ProofValidator):

    def __init__(self, proof_sequence):
        super().__init__(proof_sequence)
        self.logic = MK




# formula1 = Implication([Prop("p"), Implication([Prop("q"), Prop("p")])])
# formula2 = Implication([
#     Implication([Prop("p"), Implication([Prop("q"), Prop("r")])]),
#     Implication([Implication([Prop("p"), Prop("q")]), Implication([Prop("p"), Prop("r")])])
# ])
# formula3 = Implication([Not(Prop("p")), Implication([Prop("p"), Prop("q")])])
# formula4 = Implication([
#     Box(Implication([Prop("p"), Prop("q")])),
#     Implication([Box(Prop("p")), Box(Prop("q"))])
# ])


# # 定义替换规则
# s1 = MKSubstitution({
#     "p": Implication([Prop("p"),Prop("q")])
# },"\sigma1")
# s2 = MKSubstitution({
#     "p": Implication([Prop("p"),Prop("q")]),
#     "q": Implication([Prop("q"),Implication([Prop("p"),Prop("q")])])
# },"\sigma2")




# proof = ProofSequence()
# proof.add_step(formula1, A)
# proof.add_step(formula2, A)
# proof.add_step(formula3, A)
# proof.add_step(formula4, A)
# proof.add_step(s1.apply(formula1), S,[0,s1])
# proof.add_step(s2.apply(formula4), S,[3,s2])
# proof.add_step(Box(s1.apply(formula1)), NEC,[4])
# proof.add_step(modus_ponens(Box(s1.apply(formula1)), s2.apply(formula4)), MP,[5,6])



# # 验证证明
# validator = MKProofValidator(proof)

# if not validator.validate():
#     print("Proof is invalid.")
# else:
#     print("Proof is Valid.")
#     print(proof)