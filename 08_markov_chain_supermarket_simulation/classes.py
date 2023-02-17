
class Supermarket:
    import pandas as pd
    from datetime import datetime, time, timedelta
    from classes import Customer

    """description"""
    
    locations = ['spices','dairy','drinks','fruit','checkout','entry'] 
    
    def __init__(self, opening_time = datetime(2022, 10, 21, 7, 0, 0), 
                 closing_time = datetime(2022, 10, 21, 22, 0, 0), locations = locations):
        self.opening_time   = opening_time
        self.closing_time   = closing_time
        self.locations      = locations
        #self.numb_customers = numb_customers
        self.time           = opening_time
        self.customer_list  = []
        self.last_id        = 1
        self.df_random_walks= pd.DataFrame()
        self.probs          = get_matrix()

    def get_matrix(self):
        transition_df=pd.read_csv('transition_probability_matrix.csv', delimiter=";",index_col=0)
        transition_df.columns.tolist()

        probs = transition_df.to_dict(orient='index')
        for key in probs.keys():
            probs[key] = list(probs[key].values())
        return probs

    def add_customer(self):
        customer = Customer(self.last_id,transition_df,probs)
        self.customer_list.append(customer)      
        self.last_id += 1
        return self.customer_list
    
    def delete_customer(self):
        for customer in self.customer_list:
            if customer.state=='checkout':
                self.customer_list.remove(customer)
        return self.customer_list
    
    def fill_df(self,active_customer):
        df = pd.DataFrame({"time": [self.time], "customer_id": [active_customer.id_], "location": [active_customer.state]})
        self.df_random_walks = pd.concat([df, self.df_random_walks])
        return self.df_random_walks
    
    def simulation(self):
        while self.time <= self.closing_time: #as long as current time earlier than closing time
            print(self.time)
            self.customer_list = self.delete_customer() #delete customer with state "checkout"
            self.customer_list = self.add_customer()    #add new customer 
            
            for active_customer in self.customer_list[0:1]:
                active_customer.state=active_customer.next_state() #calculate next state of customer
                self.df_random_walks=self.fill_df(active_customer) #fill individual random_walk df of customer
            self.time = self.time + timedelta(minutes=1) #add next minute
        
        #print(self.df_random_walks)

class Customer:
    """description"""
    import random
    from classes import Supermarket 

    def __init__(self, id_,trans_matrix,probs=Supermarket.probs):
        self.id_              = id_
        self.state            = 'entry'
        #self.df_random_walk   = pd.DataFrame()
        self.trans_matrix     = trans_matrix
        self.probs            = probs
        
    def next_state(self):
        #'''calculates the next state based on random choices and probabilites of transition matrix'''
        #print(self.state)
        #print(probs[self.state])
        STATES=self.trans_matrix.columns.tolist()
        next_state=random.choices(STATES,probs[self.state])[0]
        #print(self.id_, next_state)
        return next_state
