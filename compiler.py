funcs = []
ascii = []

file = "index.don"

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
                            
                    if (count_aspas < 2):
                        print("n fechou as aspas")
                    
                    else:
                        string = string[aspas_1+1:aspas_2+1]
                        print(string)
                except:
                    print("Don não sabe até onde profetizar")
               
            # w = [ord(c) for c in string]
            # for i in w:
            #     ascii.append(i)
                
            # ascii.append(0)
            # print(ascii)
                
except:
    print("don esta desaparecido")           
