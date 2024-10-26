from crewai.flow.flow import Flow, listen, start, or_

class OrExampleState(Flow):
    
    @start()
    def start_method(self):
        print("---Start method---")
        return ("Hello from start method")
    
    @listen(start_method)
    def second_method(self):
        print("---Second method---")
        return ("Hello from second method")
    
    @listen(second_method)
    def third_method(self):
        print("---Third method---")
        return ("Hello from third method")
    
    @listen(or_(start_method, third_method, second_method))
    def logger(self, result):
        print("logger Result: \n", result)
        
    @listen(third_method)
    def fourth_method(self):
        print("---Fourth method---")
        return ("Hello from fourth method")
        
flow = OrExampleState()
result=flow.kickoff()
print("Result: \n", result)