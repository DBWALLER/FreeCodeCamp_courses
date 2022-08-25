# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:50:25 2022

@author: Dalciana
"""



import copy
import random
    
class Hat:
    """
    The class should take a variable number of arguments that specify 
    the number of balls of each color that are in the hat. 
    
    For example, a class object could be created in any of these ways:
    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    
    # (for the initialization part)
    The arguments passed into the hat object upon creation should be converted 
    to a contents instance variable. 
    contents should be a list of strings containing one item for each ball in the hat.
    
    Each item in the list should be a color name representing a single ball of that color. 
    For example, if your hat is {"red": 2, "blue": 1},
    contents should be ["red", "red", "blue"].
    """

    
    def __init__(self, **kwargs):
        self.contents=[]
        dic = kwargs.items()
        for key, value in dic :
            for i in range(value):
                self.contents.append(key)
    
    
    
    def draw(self, n_removed ):
        """
        The Hat class should have a draw method that accepts an argument 
        indicating the number of balls to draw from the hat. 
        
        This method should remove balls at random from contents
        and return those balls as a list of strings. 
        
        The balls should not go back into the hat during the draw, 
        similar to an urn experiment without replacement. 
        
        If the number of balls to draw exceeds the available quantity, return all the balls.
        """
        removed_balls =[]
        #remaining_balls = copy.deepcopy(self.contents)
        
        if n_removed >= len(self.contents):
            return self.contents
        
        for _ in range(n_removed):  #range(1,n_removed+1):
            #draw_ball = random.choice(remaining_balls)
            #remaining_balls.remove(draw_ball)
            #removed_balls.append(draw_ball)
            draw_ball = random.choice(self.contents)
            self.contents.remove(draw_ball)
            removed_balls.append(draw_ball)
            
        return removed_balls
    

# Function to get the probability

def experiment(hat, expected_balls, num_balls_drawn, num_experiments ):
    """ 
    hat: A hat object containing balls that should be copied inside the function.
    expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
    num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    num_experiments: The number of experiments to perform. 
    (The more experiments performed, the more accurate the approximate probability will be.)
    The experiment function should return a probability.
    
    For example, if you want to determine the probability of getting at least 
   2 red balls and 1 green ball 
   when you draw 5 balls from a hat containing 6 black, 4 red, and 3green. 
   
   To do this, you will perform N experiments, 
   count how many times M you get at least 2 red balls and 1 green ball, ----
   and estimate the probability as M/N. 
   Each experiment consists of starting with a hat containing the specified balls, 
   drawing several balls, and checking if you got the balls you were attempting to draw.
    """ 
    # expected_balls ={"red":2,"green":1}
            
    # Step 1:  Running N experiments and saving results
    results=[]
    for i in range (num_experiments):
        hat_copy = copy.deepcopy(hat)
        removed_balls_experiment = hat_copy.draw(num_balls_drawn)
        results.append(removed_balls_experiment)
    
    
    #Step 2: Transforming results of (N) experiments into dictionaries and 
    # checking if result matches the expected balls condition and if so, counting it (M)
    import numpy as np
    
    M_num_success_exp = 0   
    
    for k in range(len(results)):
       # countsnumber of mentions of each color in the removed balls experiment
        res_experiment = results[k]
        colors, counts = np.unique( res_experiment, return_counts=True)
        #transform into dict
        dic_exp = dict( zip(list(colors),list(counts)))
        
        #compare results of k experiment with the condition of expected balls dictionary 
        check = []
        for k_name, v_count in dic_exp.items():
            if k_name in expected_balls:
                if v_count>= expected_balls[k_name]:
                    check.append("ok")
        if len(check)==len(expected_balls):  #success in all conditions
            M_num_success_exp+=1
    
    #return of probability         
    return M_num_success_exp / num_experiments     
