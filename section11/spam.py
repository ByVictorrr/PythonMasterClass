def spam1():
    
    def spam2():
        
        def spam3():
            z = " even more spam"
            z += y
            #print("In spam3, locals are {}".format(locals()))
            return z
        
        y= " more spam" + x
        y+=spam3()
        #print("In spam2, locals are {}".format(locals()))
        return y

    x = " spam" + spam2()


    #print("In spam1, locals are {}".format(locals()))
    return x
print(spam1())