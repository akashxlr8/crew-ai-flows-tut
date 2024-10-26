@listen(or_(start_method, second_method))
    def logger(self, result):
        print("logger Result: \n", result)