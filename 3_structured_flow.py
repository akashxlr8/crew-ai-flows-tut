from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    message: str = ""
    counter: int = 0

class StructuredFlow(Flow[ExampleState]):
    
    @start()
    def first_method(self):
        print("---First method---")
        print("State before first method: \n", self.state)
        self.state.counter += 1
        self.state.message += "Hello from first method"
        
    
    @listen(first_method)
    def second_method(self, state: ExampleState):
        print("---Second method---")
        print("State before second method: \n", self.state)
        self.state.counter += 1
        self.state.message += " Hello from second method"
        
    @listen(second_method)
    def third_method(self, state: ExampleState):
        print("---Third method---")
        print("State before third method: \n", self.state)
        self.state.counter += 1
        self.state.message += " Hello from third method"
        
        print("State after third method: \n", self.state)   
        
flow = StructuredFlow()
result = flow.kickoff()
print("Result: \n", result)

