import time

class RetryBudget:
    def __init__(self, max_tokens: int = 20, refill_per_second: float = 0.5):
        self.max_tokens = max_tokens
        self.refill_per_second = refill_per_second
        self.tokens = max_tokens
        self.last_update = time.time()

    def can_retry((self) -> bool:
        now = time.time()
        elapsed = now - self.last_update
        self.tokens = min(self.max_tokens, self.tokens + elapsed * self.refill_per_second)
        self.last_update = now

        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False

retry_budget = RetryBudget()