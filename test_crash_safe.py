from core.runtime.crash_safe_state import enable_crash_safe_state
import time

class DummyAgent:
    def __init__(self):
        self.counter = 0

    def dump_state(self):
        return {"counter": self.counter}

    def load_state(self, state):
        print("🔁 Restored state:", state)
        self.counter = state["counter"]

agent = DummyAgent()

persist = enable_crash_safe_state(agent)

print("🚀 Agent started. Press Ctrl+C to simulate crash.")

while True:
    agent.counter += 1
    print("Tick:", agent.counter)
    persist()
    time.sleep(2)
