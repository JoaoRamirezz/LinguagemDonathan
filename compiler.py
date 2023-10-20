funcs = []
ascii = []

file = "index.don"



def asciiConvert(variable):
    w = [ord(c) for c in variable]
    
    for i in w:
        ascii.append(i)
        
    ascii.append(0)
    
            
            
            
try:
    with open(file, 'r') as f:
        lines = f.readlines()
        for i in lines:
            string = i
            if "profetizou(" in i:
                
                aspas_1 = 0
                aspas_2 = 0
                count_aspas = 0
                
                try:
                    for j in i:
                        if j != "\"" and count_aspas == 0:
                            aspas_1 += 1
                            aspas_2 += 1
                        
                        elif j == "\"":
                            count_aspas += 1
                            
                        elif j != "\"" and count_aspas == 1:
                            aspas_2 += 1
                        
                    
                    if count_aspas == 0:
                        a = 0
                        first = True
                        operation = ""
                        
                        for j in i:
                            if j.isdigit() and first:
                                a += int(j)
                                first = False
                                
                            if j == "+":
                                operation = "sum"
                                
                            if j.isdigit() and operation == "sum":
                                a += int(j)
                            
                        asciiConvert(str(a))
                                
                            
                    elif(count_aspas == 1):
                        print("n fechou as aspas")
                    
                    else:
                        string = string[aspas_1+1:aspas_2+1]
                        asciiConvert(string)
                    
                except:
                    print("Don não sabe até onde profetizar")
        
        print(ascii)
               

                
except:
    print("don esta desaparecido")           
