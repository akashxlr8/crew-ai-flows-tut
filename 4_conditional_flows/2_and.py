from crewai.flow.flow import Flow, listen, and_, start

class AndFlow(Flow):
    
    @start()
    def start_method(self):
        print("---Start method---")
        return ("Hello from start method")
    
    @listen(start_method)
    def second_method(self):
        print("---Second method---")
        return ("Hello from second method")
    
    @listen(start_method)
    def third_method(self): 
        print("---Third method---")
        return ("Hello from third method")
    
    @listen(and_(second_method, third_method))
    def logger(self):
        print("logger Result: \n")  
        
flow = AndFlow()
flow.kickoff()

