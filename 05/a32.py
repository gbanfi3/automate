import logging
logging.basicConfig(filename='./logFile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def fact(n):
    i = 1
    for j in range(1,n+1):
        i *= j
        logging.info("j=%s" % (i))
        if j==1:
            logging.debug("nagy öröm     j=%s" % (j))
    return i

for i in range(1,5):
    print(str(i) + ": " + str(fact(i)))