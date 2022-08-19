#https://replit.com/@dbwaller/boilerplate-arithmetic-formatter#arithmetic_arranger.py

def arithmetic_arranger(problems, showres=False):   
    """
    problems : list
    """
    results=[]
    sup_line=[]
    inf_line=[]
    dash_line=[]
    res_line=[]

    #1) test len of the problem:
    n_probl = len(problems)
    if len(problems)>5:
        return('Error: Too many problems.')
  
  
    for p in problems:
  
        index = problems.index(p)
       # removing any white spaces in begginign or end
                # strip(): returns a new string after removing any leading and trailing whitespaces including tabs (\t).
        p=p.strip()   # 32 + 698    
        #splitting terms of problem
        sp = p.split() #or p.split(" ")    # ['32', '+', '698']

        #Check operator + or -
        if sp[1] not in ["+",'-']:
            return("Error: Operator must be '+' or '-'.") 

        #Each number (operand) should only contain digits.
        n_sup=sp[0]
        n_inf=sp[2]
        try:
            isup = int(n_sup)
            iinf = int(n_inf)
        except:
            return("Error: Numbers must only contain digits.")

        #check nbr of digits of each operand
        if len(n_sup)>4 or len(n_inf)>4:
            return("Error: Numbers cannot be more than four digits.") 

        #results
        oper = sp[1]
        if oper=="+":
            res=isup+iinf
        elif oper=="-": 
            res=isup+iinf
        results.append(res)

        # max
        len_max= max(len(n_sup),len(n_inf))

        # Superior line string 
        delta_spaces_sup = len_max-len(n_sup)
        string_sup = '  ' + ' '* delta_spaces_sup + n_sup

        # Inferior line string 
        delta_spaces_inf =  len_max-len(n_inf)
        string_inf = oper+' ' + ' '* delta_spaces_inf + n_inf

        #dash line
        string_dash='-'*(2+len_max)

        #----------------------
        if res>=0:
            string_res= '  '+str(res)
        else:
            string_res= ' '+ str(res)
        #-----------------------

        #adding extra 2 spaces after nbr
        if index <len(problems)-1:  #0<0 ==> false ..ok
            string_sup = string_sup +'    ' 
            string_inf = string_inf +'    ' 
            string_dash = string_dash +'    ' 
            string_res = string_res +'    '

        sup_line.append(string_sup)
        inf_line.append(string_inf)
        dash_line.append(string_dash)
        res_line.append(string_res)


        print(sup_line)
        print(inf_line)
        print(dash_line)
        print(res_line)

    sup_line2 = "".join(sup_line)
    inf_line2 = "".join(inf_line)
    dash_line2 = "".join(dash_line)
    res_line2 = "".join(res_line)

    if showres==False:
        #arranged_problems =   sup_line2 + '\n' + inf_line2 + '\n' + dash_line2 
        return sup_line2,
                inf_line2,
                 dash_line2 
              
    if showres==True:
        #arranged_problems =   sup_line2 + '\n' + inf_line2 + '\n' + dash_line2  + '\n'+ res_line2 
        return (sup_line2,
                inf_line2,
                 dash_line2,
                 res_line2 
               )
   



# basic test
#problems2 = ["  32 + 698  ", "3801 - 2", "45 + 43", "123 + 49"]
#arithmetic_arranger(problems2)  
