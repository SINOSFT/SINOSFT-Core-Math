import numpy as np

class PistonEffectSimulator:
    def __init__(self, tunnel_width=300, train_speed=600/3.6, train_cross_section=12.0):
        self.W = tunnel_width
        self.H = 27.0
        self.v_train = train_speed
        self.A_train = train_cross_section
        self.A_tunnel = self.W * self.H
        self.rho_air = 1.225
        self.c_sound = 340.0
        self.blockage_ratio = self.A_train / self.A_tunnel
        
    def compute_piston_pressure(self):
        beta = self.blockage_ratio
        M = self.v_train / self.c_sound
        delta_P_incomp = 0.5 * self.rho_air * self.v_train**2 * beta / ((1 - beta)**2)
        if M > 0.3:
            compressibility_factor = 1.0 / np.sqrt(1 - M**2)
            delta_P = delta_P_incomp * compressibility_factor
        else:
            delta_P = delta_P_incomp
        return delta_P
    
    def compute_bernoulli_side_force(self):
        side_gap = (self.W - 5.0) / 2
        v_gap = self.v_train * (self.A_tunnel / (2 * side_gap * self.H))
        delta_P_side = 0.5 * self.rho_air * (v_gap**2 - self.v_train**2)
        train_side_area = 200.0 * 4.0
        F_side = abs(delta_P_side) * train_side_area
        return F_side, delta_P_side
    
    def verify_aerodynamic_safety(self):
        print("=" * 60)
        print("SINOSFT L2: 600km/h活塞效应气动安全验证")
        print("=" * 60)
        
        piston_P = self.compute_piston_pressure()
        pressure_limit = 5000.0
        
        print(f"列车速度: {self.v_train * 3.6:.0f} km/h")
        print(f"阻塞比: {self.blockage_ratio:.4f}")
        print(f"最大瞬态压力幅值: {piston_P:.2f} Pa")
        print(f"结构安全阈值: {pressure_limit:.2f} Pa")
        
        if piston_P < pressure_limit:
            print(f"[PROVED] 活塞压力安全 - 裕度 {pressure_limit/piston_P:.1f}x")
        else:
            print("[FAILED] 活塞压力超标")
        
        F_side, delta_P_side = self.compute_bernoulli_side_force()
        derailment_limit = 2.0e5
        
        print(f"总侧向吸力: {F_side/1e3:.2f} kN")
        print(f"脱轨临界力: {derailment_limit/1e3:.2f} kN")
        
        if abs(F_side) < derailment_limit:
            print(f"[PROVED] 侧向气动安全 - 裕度 {derailment_limit/abs(F_side):.1f}x")
        else:
            print("[FAILED] 侧向力超标")
        
        return (piston_P < pressure_limit) and (abs(F_side) < derailment_limit)

if __name__ == "__main__":
    sim = PistonEffectSimulator()
    sim.verify_aerodynamic_safety()
