class Agent:
    def __init__(self):
        self.previous = None

    def decide(self, temp, occupied):
        old = self.previous

        if not occupied:
            target = "OFF"
        elif temp < 18:
            target = "HEAT"
        elif temp > 25:
            target = "COOL"
        else:
            target = "OFF"

        send = target != old
        self.previous = target
        return old, target, send


agent = Agent()

tests = [(16, 1), (16, 1), (18, 1),
         (25, 1), (30, 1), (16, 1), (16, 0)]

for temp, occupied in tests:
    old, target, send = agent.decide(temp, occupied)
    print(old, (temp, occupied), target,
          "SEND" if send else "NO COMMAND")