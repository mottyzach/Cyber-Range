import time
import random

class AttackEngine:
    def __init__(self, logger_callback):
        self.log = logger_callback
        self.strategy = "bruteforce"  # bruteforce, dos, portscan
        self.success_count = 0
        self.failure_count = 0
        self.consecutive_failures = 0
        self.consecutive_successes = 0

    def choose_strategy(self):
        """Adaptive strategy selection based on past results."""
        if self.consecutive_failures >= 2:
            # Switch to a different attack type if current one keeps failing
            if self.strategy == "bruteforce":
                self.strategy = "dos"
            elif self.strategy == "dos":
                self.strategy = "portscan"
            else:
                self.strategy = "bruteforce"
            self.log(f"[Attack] Switching strategy to {self.strategy} due to failures")
            self.consecutive_failures = 0

    def execute_attack(self, defense_state):
        """
        Simulate an attack. defense_state is a dict with keys:
        - 'blocked_ips': set of blocked IPs
        - 'rate_limited': bool
        Returns: (success: bool, attack_type: str)
        """
        self.choose_strategy()
        attack_type = self.strategy

        if attack_type == "bruteforce":
            success = self._bruteforce(defense_state)
        elif attack_type == "dos":
            success = self._dos(defense_state)
        elif attack_type == "portscan":
            success = self._portscan(defense_state)
        else:
            success = False

        if success:
            self.success_count += 1
            self.consecutive_successes += 1
            self.consecutive_failures = 0
        else:
            self.failure_count += 1
            self.consecutive_failures += 1
            self.consecutive_successes = 0

        return success, attack_type

    def _bruteforce(self, defense_state):
        self.log("[Attack] Starting brute-force login attempt...")
        time.sleep(0.5)  # Simulate time
        # Defense: if IP blocked or rate limited, fail
        if "192.168.1.100" in defense_state.get("blocked_ips", set()):
            self.log("[Attack] Brute-force failed: IP blocked")
            return False
        if defense_state.get("rate_limited", False):
            self.log("[Attack] Brute-force throttled by rate limiting")
            return False

        # Simulate success probability (lower if defense aggressive)
        success_chance = 0.3
        if random.random() < success_chance:
            self.log("[Attack] Brute-force successful! Credentials found.")
            return True
        else:
            self.log("[Attack] Brute-force attempt failed.")
            return False

    def _dos(self, defense_state):
        self.log("[Attack] Launching DoS flood...")
        time.sleep(0.3)
        if "192.168.1.100" in defense_state.get("blocked_ips", set()):
            self.log("[Attack] DoS failed: source IP blocked")
            return False
        # DoS may succeed even with rate limiting, but defense can still block
        success_chance = 0.5
        if random.random() < success_chance:
            self.log("[Attack] DoS caused service degradation!")
            return True
        else:
            self.log("[Attack] DoS mitigated.")
            return False

    def _portscan(self, defense_state):
        self.log("[Attack] Scanning ports...")
        time.sleep(0.4)
        if "192.168.1.100" in defense_state.get("blocked_ips", set()):
            self.log("[Attack] Port scan blocked by firewall")
            return False
        # Port scan success means finding open ports
        if random.random() < 0.4:
            self.log("[Attack] Open ports discovered: 22, 80, 443")
            return True
        else:
            self.log("[Attack] No open ports found.")
            return False