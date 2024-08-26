
def digit(number,n) -> str:
        
            res = [number[i:i + n]for i in range(len(number)-n +1 )]
            if n > len(number):
                    print (f"Eror you can not subdtring bigger than {len(number)}" )
            return res
            
        
        


number = "45678"
n= 2
num = digit(number, n)
print(num)


















        
            



