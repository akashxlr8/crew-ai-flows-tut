from crewai.flow.flow import Flow, listen, start


class UnstructuredFlow(Flow):
    
    @start()
    def first_method(self):
        print("First method")
        print("State before first method: \n", self.state)
        self.state["message"] = " Hello from first method"
        self.state["counter"] = 0
    
    @listen(first_method)
    def second_method(self):
        print("Second method")
        print("State before second method: \n", self.state)
        self.state["counter"] += 1
        self.state["message"] += " Hello from second method"
        
    @listen(second_method)
    def third_method(self):
        print("Third method")
        print("State before third method: \n", self.state)
        self.state["counter"] += 1
        self.state["message"] += " Hello from third method"

        print("State after third method: \n", self.state)
flow = UnstructuredFlow()
result = flow.kickoff()
print(result)

