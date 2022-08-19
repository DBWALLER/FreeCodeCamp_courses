class Category:
    """
    Complete the Category class in budget.py. 
    It should be able to instantiate objects based 
    on different budget categories like food,    clothing, and entertainment. 
    When objects are created, they are passed in the name of the category. 
    The class should have an instance variable called ledger that is a list. 
    The class should also contain the following methods..
    """
    
    #To instantiate object
    def __init__(self, name_given):
        self.name = name_given
        self.balance = 0.0
        self.ledger = []    #ledger = livro-caixa
    
    def get_balance (self):
        """
        A get_balance method that returns the current balance of the budget category 
        based on the deposits and withdrawals that have occurred.
        """
        return self.balance
     
    
    def check_funds(self,amount):
        """
        A check_funds method that accepts an amount as an argument. 
        It returns False if the amount is greater than the balance of the budget category 
        and returns True otherwise. 
        This method should be used by both the withdraw method and transfer method.
        """
        if float(amount)>self.balance:
            return False 
        else:
            return True
          
          
    def deposit(self, amount, description=""):
        """
        A deposit method that accepts an amount and description. 
        If no description is given, it should default to an empty string. 
        The method should append an object to the ledger list
        in the form of {"amount": amount, "description": description}.
        """
        
        self.ledger.append({"amount" : float(amount), "description" : description})
        self.balance = self.balance + float(amount)
        
        
    def withdraw(self, amount,description=""):
        """
        A withdraw method that is similar to the deposit method, 
        but the amount passed in should be stored in the ledger as a negative number.
        If there are not enough funds, nothing should be added to the ledger. 
        This method should return True if the withdrawal took place, and False otherwise.
        """
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({"amount" : (0-amount), "description" : description})
            self.balance = self.balance - float(amount)
            return True
            
    
    def transfer(self,amount,cat_dest):
        """
        A transfer method that accepts an amount and another budget category as arguments. 
        The method should add a withdrawal with the amount 
        and the description "Transfer to [Destination Budget Category]". 
        
        The method should then add a deposit to the other budget category with the amount 
        and the description "Transfer from [Source Budget Category]". 
        If there are not enough funds, nothing should be added to either ledgers. 
        This method should return True if the transfer took place, and False otherwise.
        """
        if self.check_funds(amount) == False:
            return False
        else:
            #withdrawal from this account is a deposit to the destination category account
            self.withdraw(amount,"Transfer to "+ cat_dest.name)
            cat_dest.deposit(amount, "Transfer from " + self.name)
            return True
    

        #Defining return values
    def __str__(self):
        """
        When the budget object is printed it should display:

        A title line of 30 characters where the name of the category is centered in a line of * characters.
        A list of the items in the ledger. 
        Each line should show the description and amount.
        The first 23 characters of the description should be displayed, then the amount. 
        The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.

        A line displaying the category total.

        *************Food*************
        initial deposit        1000.00
        groceries               -10.15
        restaurant and more foo -15.89
        Transfer to Clothing    -50.00
        Total: 923.96
        """
        title_line = self.name
        title_line = title_line.center(30, "*").rstrip()
        display = title_line + "\n"
        """    
        nbr_char_title = len(self.name)
        nbr_ast = 30-nbr_char_title
        if nbr_ast%2=0:
            title= "*" *nbr_ast/2 + self.name + "*" *nbr_ast/2
        """
        for items in self.ledger:
            item = list(items.values())   #exemple: [-50, 'groceries']

            #---descriptiom part
            descr = item[1]   
            descr = descr [0:23].ljust(23)
            #---amount part
            number = item[0]
            number = '%.2f'%number  #the same as str('%.2f'%number)
            number = number.rjust(7)
            #---display update
            display = display + descr + number + "\n"

        #Include total on display
        display = display + "Total: "  + str('%.2f'%self.balance)

        return display

      
      
      
      
def create_spend_chart(categories):
    """
    create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

    The chart should show the percentage spent in each category passed in to the function. 
    The percentage spent should be calculated only with withdrawals and not with deposits. 
    Down the left side of the chart should be labels 0 - 100. 
    The "bars" in the bar chart should be made out of the "o" character.
    The height of each bar should be rounded down to the nearest 10. 
    The horizontal line below the bars should go two spaces past the final bar. 
    Each category name should be written vertically below the bar.
    There should be a title at the top that says "Percentage spent by category".
    
    
    Percentage spent by category
     100|          
      90|          
      80|          
      70|          
      60| o        
      50| o        
      40| o        
      30| o        
      20| o  o     
      10| o  o  o  
       0| o  o  o  
        ----------
          F  C  A  
          o  l  u  
          o  o  t  
          d  t  o  
             h     
             i     
             n     
             g     
    """
    
    
    #---- Name of categories  + lenght ofname string  + check of withdrawals
    
    name_categ=[]
    lenght_name_categ=[]
    withdrawals = []
    
    for categ in categories:
        name_categ.append(categ.name)
        lenght_name_categ.append(len(categ.name))
        
        sum_withdr_cat = 0
        for items in categ.ledger:
            item = list(items.values())
            if item[0]<0:  #mean it's a withdrawal:
                  sum_withdr_cat= sum_withdr_cat-(item[0])
        withdrawals.append(sum_withdr_cat)

    #---- Calculation percentage
    percentage = []
    sum_withdr = sum(withdrawals)
    for i in range (len(withdrawals)):
        perc = withdrawals[i]/sum_withdr
        perc= round(perc,2) *100
        percentage.append(perc)
    #print(percentage)   #------
    #---- Output - bars
    output = "Percentage spent by category\n"
    aux = 100
    while aux>=0:
        #output = output.rstrip(" ")
        if aux==100:
            output = output+str(aux)+"| "
        if aux<=90 and aux>=10:
            output = output+" " + str(aux)+"| "
        if aux==0:
            output= output+"  " + str(aux)+"| "
        
        for x in range(len(percentage)):
            if aux <=percentage[x] :
                output = output + "o" + "  "
            else: 
                output= output + "   "
        output=output + '\n'
        aux = aux-10
    
        
    #---- Output - dashes
    output = output + "    " + "-" + len(name_categ)*"---"
    output=output + '\n'
    
    #---- Output - Names in vertical
    for k in range(max(lenght_name_categ)):
        
        output = output + "     " 
        for name in name_categ:
            try:
                letter = name[k]
                if k==0:
                    letter=letter.upper()
                output = output + letter + "  "
            except:
                output = output + "   "
        if k<max(lenght_name_categ)-1:
            output = output + "\n"                
    return output
