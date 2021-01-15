from engines import std_dev_engine

def init():
    print("Initialize configuration")

def main():
    print ("Tseng Tunel Program Started")
    init()
    std_dev_engine.calc_std_dev()

#Core Step
# 1. Trigger Standard Deviation Engine
main()