class SimpleAgent:
    def __init__(self, goal: str):
        self.goal = goal
        self.state = {}

    def observe(self, observation: str):
        self.state["last_observation"] = observation

    def decide(self) -> str:
        # Placeholder for LLM call later
        return "RESPOND"

    def act(self, action: str):
        if action == "RESPOND":
            return "Agent response placeholder"
        else:
            return "NO-OP"

    def run(self, observation: str):
        self.observe(observation)
        action = self.decide()
        return self.act(action)


if __name__ == "__main__":
    agent = SimpleAgent(goal="Answer user questions accurately")
    output = agent.run("What is an AI agent?")
    print(output)
