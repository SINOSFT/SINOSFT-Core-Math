from z3 import *

def theorem_static_equilibrium():
    solver = Solver()
    
    g = Real('g'); rho = Real('rho')
    solver.add(g == 9.81); solver.add(rho == 1025.0)
    
    tube_weight = Real('tube_weight')
    tube_volume = Real('tube_volume')
    max_tension_limit = Real('max_tension_limit')
    
    solver.add(tube_weight == 5e7)
    solver.add(tube_volume == 6e4)
    solver.add(max_tension_limit == 5e8)
    
    F_buoyancy = Real('F_buoyancy')
    F_weight = Real('F_weight')
    T_cable = Real('T_cable')
    
    solver.add(F_buoyancy == rho * g * tube_volume)
    solver.add(F_weight == tube_weight * g)
    solver.add(F_buoyancy == F_weight + T_cable)
    solver.add(T_cable >= 0)
    
    allowable_tension = max_tension_limit / 2.5
    solver.add(T_cable > allowable_tension)
    
    if solver.check() == unsat:
        print("[PROVED] theorem_static_equilibrium: 静力平衡公理验证通过")
        return True
    else:
        print("[FAILED] 发现物理反例")
        return False

if __name__ == "__main__":
    theorem_static_equilibrium()
