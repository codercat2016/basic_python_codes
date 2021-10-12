from os import linesep

class stock:
    
    def __init__(self,name , file_location) -> None:
      
       self.dates = []
       self.volume = []
       self.name = name
       self.location = file_location
       self.lines = None
       self.get_file(file_location)
       self.load_values()
       self.calculate()

  
    
    def get_file(self,loc):
        with open(loc , 'r') as f:
           global lines
           lines = f.readlines()
    def load_values(self):
        for line in lines:
        
           line =line.rstrip('\n')
           values = line.split("\t")
           self.dates.append(values[0])
           self.volume.append(values[1])
    def calculate(self):
        
        i = self.find_months_indexes(self.dates)
        
        #for july 
        date_july= self.dates[0:(i[0])]
        volume_july = self.volume[0:(i[0])]
        july_max_min = self.findmaxmin(date_july,volume_july)
        
        #for August
        
        arrlen = len(self.dates)
        
        date_august = self.dates[i[0]:arrlen]
        volume_august = self.volume[i[0]:arrlen]
        august_max_min = self.findmaxmin(date_august,volume_august)
        print(july_max_min["date1"],"has the maximum trade volume of ",july_max_min["volume1"],"in July")
        print(july_max_min["date2"],"has the minimum trade volume of ",july_max_min["volume2"],"in July")
        print(august_max_min["date1"],"has the maximum trade volume of ",august_max_min["volume1"],"in August")
        print(august_max_min["date2"],"has the minimum trade volume of ",august_max_min["volume2"],"in August")
        amount1 =0
        amount2=0
        for i in range(21):
            amount1 = amount1+int(self.volume[i])
        for i in range(22,43,1):
            amount2 = amount2+int(self.volume[i] )   
        print("The whole trade volume of these two month is",amount1+amount2)
        print("The average trade volume of July is",(amount1/21))
        print("The average trade volume of August is",(amount2/22))
        print("AAPL has higher trading volume in","July" if amount1>amount2 else "August" )
       
        
    def find_months_indexes(self,dates):
        br_points = []
        for index in range(2,len(dates),1) :
            
            sp_date = dates[index-1].split('-')
            sp_date_next = dates[index].split('-')
            if sp_date[1] != sp_date_next[1]:
                br_points.append(index)
        
        return br_points

    def findmaxmin(self, dates , volume):
        
        max = int(volume[0])
        min = int(volume[0])
        max_date = dates[0]
        min_date = dates[0]
        for index , (elem_d,elem_v) in enumerate(zip(dates,volume)):
            if int(elem_v)> max:
                max = int(elem_v)
                max_date = elem_d
            elif(int(elem_v)<min):
                min = int(elem_v)
                min_date = elem_d    
        
        return {"date1":max_date,
                "volume1":max,
                "date2":min_date,
                "volume2":min
        }        
    


stock1 = stock("aapl",'aapl.txt')
