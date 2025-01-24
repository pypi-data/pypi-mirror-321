class TechVAIChat:
    def __init__(self, client):
        self.client = client

    def chat(self, messages, model="llama-3.2-3b-preview", temperature=0.1, max_tokens=1024, top_p=0.9, stream=True):
        response_stream = self.client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stream=stream,
        )
        return response_stream
