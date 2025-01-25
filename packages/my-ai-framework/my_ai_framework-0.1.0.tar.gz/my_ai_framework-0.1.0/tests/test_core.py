import unittest
from agents.core import Agent

class TestAgent(unittest.TestCase):
    def test_add_to_memory(self):
        agent = Agent("Test Bot", model=None)
        agent.add_to_memory("Hello!")
        self.assertEqual(agent.memory, ["Hello!"])

if __name__ == "__main__":
    unittest.main()
