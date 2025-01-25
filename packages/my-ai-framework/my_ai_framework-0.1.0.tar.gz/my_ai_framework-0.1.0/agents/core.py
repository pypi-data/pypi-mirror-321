class Agent:
    def __init__(self, name: str, model: object):
        self.name = name
        self.model = model
        self.memory = []

    def add_to_memory(self, message: str):
        """Add a message to the agent's memory."""
        self.memory.append(message)

    def generate_response(self, input_text: str) -> str:
        """Generate a response using the model."""
        # Example with a placeholder model
        self.add_to_memory(input_text)
        response = self.model.generate(input_text)  # Replace with actual model logic
        self.add_to_memory(response)
        return response
