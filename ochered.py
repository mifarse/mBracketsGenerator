import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


v = 0
n = int(input())

def equal_brackets(s):
        o = c = 0
        for i in s:
                o = o+1 if i == "0" else o
                c = c+1 if i == "1" else c
        if (o==c):
                return True
        else:
                return False
        
def analyze_subarr(s):
        if (s[0] == "0"):
                s = s[1:]
                s = s.replace("1", "", 1)
                #print(s, len(s))
                if (len(s) == 0):
                        return True
                else:
                        return(analyze_subarr(s))
        else:
                return False
                                

logging.debug("Start")
for i in range(2**int(n/2)-1, 2**(n-1), 2):
        brackets = bin(i)[2:]
        for j in range(n-len(str(brackets))):
                brackets = "0"+brackets
        if (not equal_brackets(brackets)):
                continue
        if (analyze_subarr(brackets)):
                v = v+1	
        #print(brackets, i)
print (v)
logging.debug("Finish!")
