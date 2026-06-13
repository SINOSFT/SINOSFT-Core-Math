from z3 import *

def theorem_transmission_coefficient_safe():
    solver = Solver()
    
    H_offshore = 18.0
    Kt = Real('Kt')
    solver.add(Kt >= 0.01, Kt <= 0.055)
    
    H_inshore = H_offshore * Kt
    solver.add(H_inshore >= 1.0)
    
    if solver.check() == unsat:
        print("[PROVED] theorem_transmission: 防波堤透射系数安全 - 港内波高恒 < 1.0m")
        return True
    else:
        print("[FAILED] 发现消波失效的透射系数组合")
        return False

if __name__ == "__main__":
    theorem_transmission_coefficient_safe()
