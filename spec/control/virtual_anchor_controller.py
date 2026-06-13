import numpy as np

class VirtualAnchorTLD:
    def __init__(self, tank_width=300, water_depth=10):
        self.W = tank_width
        self.d = water_depth
        self.omega_tld = np.sqrt(np.pi * 9.81 / self.W * np.tanh(np.pi * self.d / self.W))
        
    def compute_control_moment(self, roll_angle, roll_rate, wave_elevation):
        Kp, Kd, Kff = 5e8, 2e8, 1e7
        control_moment = -(Kp * roll_angle + Kd * roll_rate) + Kff * wave_elevation
        return np.clip(control_moment, -1e10, 1e10)

    def verify_angular_stability(self, trials=1000):
        max_angle = 0.0
        for _ in range(trials):
            t = np.linspace(0, 60, 6000)
            wave = 0.5 * np.random.randn(len(t))
            angle = 0.0
            for i in range(1, len(t)):
                M_ctrl = self.compute_control_moment(angle, 0, wave[i])
                angle += (-0.2 * angle + 1e-10 * M_ctrl + 0.01 * wave[i]) * 0.01
                max_angle = max(max_angle, abs(angle))
        print(f"虚拟水锚验证：{trials}次随机海况下，最大横摇角 = {max_angle*1e3:.4f} mrad")
        return max_angle

if __name__ == "__main__":
    np.random.seed(42)
    anchor = VirtualAnchorTLD()
    anchor.verify_angular_stability()
