'''
Created on Dec 30, 2013

@author: Tuna
'''
import wx
import BMI


class RootApp(wx.Frame):
        
    def closewindow(self,event):
        '''Upon click of red X'''
        self.Destroy()
        
    def bmiFind(self,event):
#         self.name=self.tc1.GetValue()
        self.user=BMI.User()
        self.weight=self.tc3.GetValue()
        self.user.weight=self.weight
#         wx.MessageBox('Weight='+self.weight,'Weight',wx.OK|wx.ICON_INFORMATION)
        self.height=self.tc4.GetValue()
        self.user.height=self.height
        self.bmi=self.user.bmi_calc()
        self.user.bmi=self.bmi
        self.st5.SetLabel('Your BMI is '+str(int(self.bmi))+'.')
        self.category=self.user.category()
        self.st6.SetLabel('You are '+self.category+'.')
        
        
        
    
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='BMI Calculator v0.1',size=(250,385))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)        
        
        '''Create BMI.User object'''
        
        title1='''This program will calculate your BMI 
(Body Mass Index) based on 
your height and weight.'''
        st8 = wx.StaticText(panel,label=title1,style=wx.ALIGN_CENTRE_HORIZONTAL)
        title2='''Here is the BMI Range:
Very severely underweight: 0-14.9
Severly underweight: 15-15.9
Underweight: 16-17.9
Normal (healthy weight): 18-24.9
Overweight: 25-29.9
Moderately obese: 30-34.9
Severely obese: 35-39.9
Very severely obese: 40+
        '''
        st9 = wx.StaticText(panel,label=title2)
        
        '''Name'''
        
#         hbox1 = wx.BoxSizer(wx.HORIZONTAL)
#         st1 = wx.StaticText(panel,label='Name:')
#         hbox1.Add(st1,flag=wx.RIGHT,border=0)
#         self.tc1 = wx.TextCtrl(panel)
#         hbox1.Add(self.tc1,proportion=1,flag=wx.LEFT|wx.RIGHT,border=10)
        
        '''Age'''
        
#         hbox2 = wx.BoxSizer(wx.HORIZONTAL)
#         st2a = wx.StaticText(panel,label='Age:')
#         hbox2.Add(st2a,flag=wx.RIGHT,border=95)
#         tc2 = wx.TextCtrl(panel)
#         hbox2.Add(tc2,proportion=1,flag=wx.LEFT|wx.RIGHT,border=10)
#         st2b = wx.StaticText(panel,label='years')
#         hbox2.Add(st2b,flag=wx.RIGHT,border=10)        
        
        '''Weight'''
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st3a = wx.StaticText(panel,label='Weight:')
        hbox3.Add(st3a,flag=wx.RIGHT,border=80)
        self.tc3 = wx.TextCtrl(panel,value='0')
        hbox3.Add(self.tc3,proportion=1,flag=wx.LEFT|wx.RIGHT,border=10)
        st3b = wx.StaticText(panel,label='lbs')
        hbox3.Add(st3b,flag=wx.RIGHT,border=10)
        
        '''Height'''
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st4a = wx.StaticText(panel,label='Height:')
        hbox4.Add(st4a,flag=wx.RIGHT,border=83)
        self.tc4 = wx.TextCtrl(panel,value='0')
        hbox4.Add(self.tc4,proportion=1,flag=wx.LEFT|wx.RIGHT,border=10)
        st4b = wx.StaticText(panel,label='inches')
        hbox4.Add(st4b,flag=wx.RIGHT,border=10)
        
        '''BMI result'''
        
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.st5 = wx.StaticText(panel,label='')
        hbox5.Add(self.st5)
        
        '''BMI Category result'''
        
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        self.st6 = wx.StaticText(panel,label='')
        hbox6.Add(self.st6)
        
        '''Calculate Button'''
        
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        buttonCalc = wx.Button(panel,wx.ID_ANY,label='Calculate BMI',size=(220,25))
        hbox7.Add(buttonCalc,flag=wx.EXPAND)
        
        '''Bind Buttons'''
       
        self.Bind(wx.EVT_CLOSE, self.closewindow)
        self.Bind(wx.EVT_BUTTON,self.bmiFind,source=buttonCalc)
        
        '''Add horizontal boxes to vertical box'''
        
        vbox.Add(st8,flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.BOTTOM,border=10)
        vbox.Add(st9,flag=wx.EXPAND|wx.TOP|wx.LEFT,border=10)
        vbox.Add((-1,10))
#         vbox.Add(hbox1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM,border=10)
#         vbox.Add(hbox2,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM,border=10)
        vbox.Add(hbox3,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM,border=10)
        vbox.Add(hbox4,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM,border=10)
        vbox.Add(hbox5,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM,border=10)
        vbox.Add(hbox6,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM,border=10)
        vbox.Add(hbox7,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM,border=10)
        panel.SetSizer(vbox)
        

if __name__=='__main__':
    app = wx.App()
    frame = RootApp(parent=None,id=-1)
    frame.Move((1450,500))
    frame.Show()
    app.MainLoop()
