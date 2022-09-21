

def encryption(secret):
    infile = open('info_security.txt', 'r')
    infile_read = infile.read()
    file_encrypt = open('encrypted.txt', 'w')

    for x in infile_read:
        if x in secret:
            file_encrypt.write(secret[x])
        else:
            file_encrypt.write(x)
    file_encrypt.close()

def main():
    secret = {'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', 'C' : '_', 'c' : '1', 'D' : ';', 'd' : 'x', 'E' : 'O', 'e' : 'T',
            'F' : 'G', 'f' : '5', 'G' : '0', 'g' : 'E', 'H' : '~', 'h' : '`', 'I' : 'b', 'i' : 'k', 'J' : '[', 'j' : '*',
            'K' : '.', 'k' : ':', 'L' : 'q', 'l' : 'w', 'M' : '8', 'm' : '=', 'N' : 'y', 'n' : '}', 'O' : ']', 'o' : 'A',
            'P' : '!', 'p' : '|', 'Q' : '(', 'q' : '"', 'R' : 'J', 'r' : '?', 'S' : 'u', 's' : '{', 'T' : '-', 't' : '3',
            'U' : '^', 'u' : 's', 'V' : 'r', 'v' : 'L', 'W' : 't', 'w' : 'p', 'X' : 'a', 'x' : 'v', 'Y' : 'i', 'y' : '&',
            'Z' : '>', 'z' : ','}

    encryption(secret)

main()
