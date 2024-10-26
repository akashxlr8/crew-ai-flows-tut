from crewai.flow.flow import Flow, listen, start


class ExampleFlow(Flow):
    
    @start()
    def generate_city(self):
        return "New York"
    
    @listen(generate_city)
    def generate_weather(self, city: str):
        return f"The weather in {city} is sunny"
    
    
flow = ExampleFlow()

result = flow.kickoff()
print(result)
