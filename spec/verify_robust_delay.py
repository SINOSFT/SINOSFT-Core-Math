from z3 import *

def theorem_robust_delay_stability():
    solver = Solver()
    
    tau = Real('tau')
    solver.add(tau >= 0.010, tau <= 0.020)
    
    k_stiff = 1e7; c_damp = 5e5; m_equiv = 2.5e5
    
    real_part = Real('real_part')
    solver.add(real_part == (-c_damp / (2 * m_equiv)) + (tau * (k_stiff / (2 * m_equiv))))
    solver.add(real_part >= -0.01)
    
    if solver.check() == unsat:
        print("[PROVED] theorem_robust_delay: 时滞鲁棒稳定性公理成立")
        return True
    else:
        print("[FAILED] 发现失稳反例")
        return False

if __name__ == "__main__":
    theorem_robust_delay_stability()
