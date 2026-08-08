import pandas as pd

class flight_transformer:


    def __init__(self,data):
        self.data = data



    def transform(self):

        states = self.data['states']

        #convert aircraft into DataFrame

        df = pd.DataFrame(states)
        print(f"Before cleaning{df.info()}, Shape {df.shape},Null vaues{df.isnull().sum()}")

        # basic cleaning here

        df =  df.drop_duplicates()
        df =  df.dropna(how='all')
        print("After minor cleaning{df.info()}")

        return df.head()
    

        
        

