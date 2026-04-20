import time
from collections import defaultdict

class DefenseEngine:
    def __init__(self, logger_callback):
        self.log = logger_callback
        self.blocked_ips = set()
        self.failed_login_attempts = defaultdict(int)
        self.request_counts = defaultdict(int)
        self.last_attack_time = time.time()
        self.aggressiveness = 1.0  # multiplier for thresholds
        self.rate_limit_enabled = False
        self.consecutive_detections = 0

    def analyze(self, attack_type, attack_success):
        """Analyze attack and decide defensive actions."""
        detection = False
        action = None

        if attack_type == "bruteforce":
            self.failed_login_attempts["192.168.1.100"] += 1
            if self.failed_login_attempts["192.168.1.100"] >= 3 * self.aggressiveness:
                detection = True
                action = "block_ip"
                self.log("[Defense] Multiple failed logins detected. Blocking IP.")
        elif attack_type == "dos":
            self.request_counts["192.168.1.100"] += 50
            if self.request_counts["192.168.1.100"] > 100 * self.aggressiveness:
                detection = True
                action = "rate_limit"
                self.log("[Defense] High request rate detected. Enabling rate limiting.")
        elif attack_type == "portscan":
            # Port scan detection: if we see consecutive scans
            self.consecutive_detections += 1
            if self.consecutive_detections >= 2:
                detection = True
                action = "block_ip"
                self.log("[Defense] Port scan pattern detected. Blocking IP.")

        if detection:
            self._apply_defense(action)
            self.consecutive_detections += 1
            # Adaptive: increase aggressiveness on repeated attacks
            if self.consecutive_detections > 2:
                self.aggressiveness = min(2.0, self.aggressiveness + 0.2)
                self.log(f"[Defense] Adapting: aggressiveness increased to {self.aggressiveness:.1f}")
        else:
            self.consecutive_detections = max(0, self.consecutive_detections - 1)

        return detection

    def _apply_defense(self, action):
        if action == "block_ip":
            self.blocked_ips.add("192.168.1.100")
        elif action == "rate_limit":
            self.rate_limit_enabled = True

    def get_state(self):
        return {
            "blocked_ips": self.blocked_ips.copy(),
            "rate_limited": self.rate_limit_enabled,
        }

    def reset_rate_limit(self):
        self.rate_limit_enabled = False