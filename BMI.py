'''
Created on Dec 29, 2013

@author: Tuna
'''

class User():
        
    def __init__(self):
        self.bmi_dict = {
            'very severely underweight': [0,150],
            'severly underweight':[150,160],
            'underweight':[160,180],
            'normal (healthy weight)':[180,250],
            'overweight':[250,300],
            'moderately obese':[300,350],
            'severely obese':[350,400],
            'very severely obese':[400,1000]
            }
                
    def bmi_calc(self):
        if self.height=='0':
            return 0
        else:
            return (float(self.weight)/(float(self.height)**2))*703 
    
    def category(self):
        for cat in self.bmi_dict:
            updbmi = int(round(self.bmi*10))
            if updbmi in range(self.bmi_dict[cat][0],self.bmi_dict[cat][1]):
                return cat
        return None


#===============================================================================
# test1=User()
# test1.weight=270
# test1.height=73
# test1.bmi=test1.bmi_calc()
# test1.bmi=int(round(test1.bmi,0))
# assert(test1.bmi==36)
# test1.bmi_category=test1.category()
# assert(test1.bmi_category=='severely obese')
#  
# test2=User()
# test2.weight=130
# test2.height=65
# test2.bmi=test2.bmi_calc()
# test2.bmi=int(round(test2.bmi,0))
# assert(test2.bmi==22)
# test2.bmi_category=test2.category()
# assert(test2.bmi_category=='normal (healthy weight)')
#===============================================================================
