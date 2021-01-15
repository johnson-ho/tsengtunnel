def calc_std_dev():
    print("Calculate Standard Deviation started")
    f = open("/Users/Johnson/tsengtunnel/data/HSI_closing.csv","r")
    for x in f:
        print(x)    
    f.close()
    print("Calculate Standard Deviation finish")