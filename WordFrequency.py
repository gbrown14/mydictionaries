

def main():
    infile = open('sometext.txt','r')
    wc = wordcount(infile)
    print(wc)

def wordcount(infile):
    wc = {}
    reader = infile.readlines()
    
    for line in reader:
        words = line.split()

        for w in words:
            w = w.replace("."," ")
            
            if w[-1] == ",":
                w = w.replace("."," ")

                if w in wc:
                    wc[w] += 1
                else:
                    wc[w] = 1

            if w in wc:
                wc[w] += 1
            else:
                wc[w] = 1

        return wc

    def print(wc):
        print("Word | Frequency")

        for key in wc:
            print(key, "--", wc[key])

main()
