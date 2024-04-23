class subject:
    
    def __init__(self,name,sgrade,fgrade):
        self.name=name
        self.sgrade=sgrade
        self.fgrade=fgrade

        print(f"{self.name} ,{self.fgrade} , {self.sgrade} ")

class student(subject):
    def __init__(self,sub,name,sgrade,fgrade,gpa=None):
        super().__init__(name,sgrade,fgrade)
        self.sub=sub
        self.gpa=self.fgrade/self.sgrade
        if self.gpa>=0.5:
         print(f"his subject {self.sub} and his name {self.name} and his gpa {self.gpa}")
         print("you pass")
        else:
         print(f"his subject  {self.sub} and his name {self.name} and his gpa {self.gpa}")
         print('you failed')


# subject1=subject('math',100,50)      
subject2=student('math','khaled',100,50)  
subject3=student('science','ahmed',100,20) 