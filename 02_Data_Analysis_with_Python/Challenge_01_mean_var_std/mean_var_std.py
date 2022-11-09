import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    else:
        a=np.array(list)
        m=a.reshape ((3,3))
        dic={}
        
        dic['mean'] =  [ m.mean(axis=0).tolist(), m.mean(axis=1).tolist(), m.mean()]
        dic['variance'] =   [ m.var(axis=0).tolist(), m.var(axis=1).tolist(), m.var()]
        dic['standard deviation']= [ m.std(axis=0).tolist(), m.std(axis=1).tolist(), m.std()]
        dic['max'] =  [ m.max(axis=0).tolist(), m.max(axis=1).tolist(), m.max()]
        dic['min'] =  [ m.min(axis=0).tolist(), m.min(axis=1).tolist(), m.min()]
        dic['sum'] =   [ m.sum(axis=0).tolist(), m.sum(axis=1).tolist(), m.sum()]
        return dic
