#Gaussian Elimination, Gauss-Jordan Elimination, and LU Decomposition Method. This code solves simultaneous linear equations of 3 and 4 unknown variables.

#Declaraton Of The Gaussian-Elimination Function.
def gaussian(var):
    if len(var) == 3:
        multiplier1 = var[1][0] / var[0][0]   
        for i in range(0, len(var) + 1):
            new = multiplier1 * var[0][i]
            var[1][i] = var[1][i] - new
        if var[1][1] == 0 or var[1][2] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        multiplier2 = var[2][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier2 * var[0][i]
            var[2][i] = var[2][i] - new
        if var[2][1] == 0 or var[2][2] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        multiplier3 = var[2][1] / var[1][1] 
        for i in range(0, len(var) + 1):
            new = multiplier3 * var[1][i]
            var[2][i] = var[2][i] - new
        if var[2][2] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        if var[2][2] == 0 or var[1][1] == 0 or var[0][0] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        else:
            x3 = var[2][3] / var[2][2]                                              #Computation of results: Back Substitution. 
            x2 = (var[1][3] - (var[1][2] * x3)) / var[1][1]                         #Computation of results: Back Substitution.
            x1 = (var[0][3] - (var[0][2] * x3) - (var[0][1] * x2)) / var[0][0]      #Computation of results: Back Substitution.
            x1 = round(x1, 3)                                                       #Rounding up results.
            x2 = round(x2, 3)                                                       #Rounding up results.
            x3 = round(x3, 3)                                                       #Rounding up results.
            print("Gaussian Elimination Method: x1 =", x1," ", "x2 =", x2," ", "x3 =", x3)
            return
    elif len(var) == 4:
        multiplier1 = var[1][0] / var[0][0]   
        for i in range(0, len(var) + 1):
            new = multiplier1 * var[0][i]
            var[1][i] = var[1][i] - new
        if var[1][1] == 0 or var[1][2] == 0 or var[1][3] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        multiplier2 = var[2][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier2 * var[0][i]
            var[2][i] = var[2][i] - new
        if var[2][1] == 0 or var[2][2] == 0 or var[2][3] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        multiplier3 = var[3][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier3 * var[0][i]
            var[3][i] = var[3][i] - new
        if var[3][1] == 0 or var[3][2] == 0 or var[3][3] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        multiplier4 = var[3][1] / var[2][1] 
        for i in range(0, len(var) + 1):
            new = multiplier4 * var[2][i]
            var[3][i] = var[3][i] - new
        if var[3][2] == 0 or var[3][3] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        multiplier5 = var[2][1] / var[1][1] 
        for i in range(0, len(var) + 1):
            new = multiplier5 * var[1][i]
            var[2][i] = var[2][i] - new
        if var[2][2] == 0 or var[2][3] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        multiplier6 = var[3][2] / var[2][2]
        for i in range(0, len(var) + 1):
            new = multiplier6 * var[2][i]
            var[3][i] = var[3][i] - new
        if var[3][3] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        if var[3][3] == 0 or var[2][2] == 0 or var[1][1] == 0 or var[0][0] == 0:
            print("Gaussian Elimination Method: MATH ERROR")
            return
        else:
            x4 = var[3][4] / var[3][3]                                                               #Computation of results: Back Substitution.  
            x3 = (var[2][4] - (var[2][3] * x4)) / var[2][2]                                          #Computation of results: Back Substitution. 
            x2 = (var[1][4] - (var[1][2] * x3) - (var[1][3] * x4)) / var[1][1]                       #Computation of results: Back Substitution.
            x1 = (var[0][4] - (var[0][1] * x2) - (var[0][2] * x3) - (var[0][3] * x4)) / var[0][0]    #Computation of results: Back Substitution.
            x1 = round(x1, 3)                                                                        #Rounding Up results.
            x2 = round(x2, 3)                                                                        #Rounding Up results.
            x3 = round(x3, 3)                                                                        #Rounding Up results.
            x4 = round(x4, 3)                                                                        #Rounding Up results.
            print("Gaussian Elimination Method: x1 =", x1," ", "x2 =", x2," ", "x3 =", x3," ", "x4 =", x4)
        return
#Declaraton Of The Gaussian-Jordan Elimination Function.
def gauss_jordan(var):
    if len(var) == 3:
        multiplier1 = var[1][0] / var[0][0]   
        for i in range(0, len(var) + 1):
            new = multiplier1 * var[0][i]
            var[1][i] = var[1][i] - new
        if var[1][1] == 0 or var[1][2] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        multiplier2 = var[2][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier2 * var[0][i]
            var[2][i] = var[2][i] - new
        if var[2][1] == 0 or var[2][2] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        multiplier3 = var[2][1] / var[1][1] 
        for i in range(0, len(var) + 1):
            new = multiplier3 * var[1][i]
            var[2][i] = var[2][i] - new
        if var[2][2] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        multiplier4 = var[1][1] / var[0][1] 
        for i in range(0, len(var) + 1):
            new = multiplier4 * var[0][i]
            var[0][i] = new - var[1][i]
        multiplier5 = var[0][2] / var[2][2] 
        for i in range(0, len(var) + 1):
            new = multiplier5 * var[2][i]
            var[0][i] = var[0][i] - new
        multiplier6 = var[1][2] / var[2][2] 
        for i in range(0, len(var) + 1):
            new = multiplier6 * var[2][i]
            var[1][i] = var[1][i] - new
        for i in range(0, len(var) + 1):
            if i == 0:
                continue
            var[0][i] = var[0][i] / var[0][0]
        for i in range(0, len(var) + 1):                                #Computation of result.
            if i == 1:                                                  #Computation of result.
                continue                                                #Computation of result.
            var[1][i] = var[1][i] / var[1][1]                           #Computation of result.
        for i in range(0, len(var) + 1):                                #Computation of result.
            if i == 2:                                                  #Computation of result.
                continue                                                #Computation of result.
            var[2][i] = var[2][i] / var[2][2]                           #Computation of result.
        if var[2][2] == 0 or var[1][1] == 0 or var[0][0] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        else:
            x1 = round(var[0][3], 3)                                    #Rounding up results.
            x2 = round(var[1][3], 3)                                    #Rounding up results.
            x3 = round(var[2][3], 3)                                    #Rounding up results.
            print("Gauss-Jordan Elimination Method: x1 =", x1," ", "x2 =", x2," ", "x3 =", x3)
        return
    elif len(var) == 4:
        multiplier1 = var[1][0] / var[0][0]   
        for i in range(0, len(var) + 1):
            new = multiplier1 * var[0][i]
            var[1][i] = var[1][i] - new
        if var[1][1] == 0 or var[1][2] == 0 or var[1][3] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        multiplier2 = var[2][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier2 * var[0][i]
            var[2][i] = var[2][i] - new
        if var[2][1] == 0 or var[2][2] == 0 or var[2][3] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        multiplier3 = var[3][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier3 * var[0][i]
            var[3][i] = var[3][i] - new
        if var[3][1] == 0 or var[3][2] == 0 or var[3][3] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        multiplier4 = var[3][1] / var[2][1] 
        for i in range(0, len(var) + 1):
            new = multiplier4 * var[2][i]
            var[3][i] = var[3][i] - new
        if var[3][2] == 0 or var[3][3] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        multiplier5 = var[2][1] / var[1][1] 
        for i in range(0, len(var) + 1):
            new = multiplier5 * var[1][i]
            var[2][i] = var[2][i] - new
        if var[2][2] == 0 or var[2][3] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        multiplier6 = var[3][2] / var[2][2]
        for i in range(0, len(var) + 1):
            new = multiplier6 * var[2][i]
            var[3][i] = var[3][i] - new
        if var[3][3] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        multiplier7 = var[2][3] / var[3][3]
        for i in range(0, len(var) + 1):
            new = multiplier7 * var[3][i]
            var[2][i] = var[2][i] - new
        multiplier8 = var[1][3] / var[3][3]
        for i in range(0, len(var) + 1):
            new = multiplier8 * var[3][i]
            var[1][i] = var[1][i] - new
        multiplier9 = var[0][3] / var[3][3]
        for i in range(0, len(var) + 1):
            new = multiplier9 * var[3][i]
            var[0][i] = var[0][i] - new
        multiplier10 = var[1][2] / var[2][2]
        for i in range(0, len(var) + 1):
            new = multiplier10 * var[2][i]
            var[1][i] = var[1][i] - new
        multiplier11 = var[0][2] / var[2][2]
        for i in range(0, len(var) + 1):
            new = multiplier11 * var[2][i]
            var[0][i] = var[0][i] - new
        multiplier12 = var[0][1] / var[1][1]
        for i in range(0, len(var) + 1):
            new = multiplier12 * var[1][i]
            var[0][i] = var[0][i] - new
        for i in range(0, len(var) + 1):                                #Computation of result.
            if i == 0:                                                  #Computation of result.
                continue                                                #Computation of result.
            var[0][i] = var[0][i] / var[0][0]                           #Computation of result.
        for i in range(0, len(var) + 1):                                #Computation of result.
            if i == 1:                                                  #Computation of result.
                continue                                                #Computation of result.
            var[1][i] = var[1][i] / var[1][1]                           #Computation of result.
        for i in range(0, len(var) + 1):                                #Computation of result.
            if i == 2:                                                  #Computation of result.
                continue                                                #Computation of result.
            var[2][i] = var[2][i] / var[2][2]                           #Computation of result.
        for i in range(0, len(var) + 1):                                #Computation of result.
            if i == 3:                                                  #Computation of result.
                continue                                                #Computation of result.
            var[3][i] = var[3][i] / var[3][3]                           #Computation of result.
        if var[3][3] == 0 or var[2][2] == 0 or var[1][1] == 0 or var[0][0] == 0:
            print("Gauss-Jordan Elimination: MATH ERROR")
            return
        else:
            x1 = round(var[0][4], 3)                                    #Rounding up results.
            x2 = round(var[1][4], 3)                                    #Rounding up results.
            x3 = round(var[2][4], 3)                                    #Rounding up results.
            x4 = round(var[3][4], 3)                                    #Rounding up results.
            print("Gauss-Jordan Elimination Method: x1 =", x1," ", "x2 =", x2," ", "x3 =", x3," ", "x4 =", x4)
        return
#Declaraton Of The LU Decomposition Function.
def lu_decomposition(var):
    if len(var) == 3:
        lower = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]           #Variable declaration of matrix to be used for LU Decomposition.
        upper = []                                          #Variable declaration of matrix to be used for LU Decomposition.
        b = [var[i][3] for i in range(len(var))]            #Variable declaration of matrix to be used for LU Decomposition.
        y = [0 for i in range(len(var))]                  #Variable declaration of matrix to be used for LU Decomposition.
        x = [0 for i in range(len(var))]                    #Variable declaration of matrix to be used for LU Decomposition.
        multiplier1 = var[1][0] / var[0][0]   
        for i in range(0, len(var) + 1):
            new = multiplier1 * var[0][i]
            var[1][i] = var[1][i] - new
        if var[1][1] == 0 or var[1][2] == 0:
            print("LU Decomposition Method: MATH ERROR")
            return
        lower[1][0] = multiplier1
        multiplier2 = var[2][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier2 * var[0][i]
            var[2][i] = var[2][i] - new
        if var[2][1] == 0 or var[2][2] == 0:
            print("LU Decomposition Method: MATH ERROR")
            return
        lower[2][0] = multiplier2
        multiplier3 = var[2][1] / var[1][1] 
        for i in range(0, len(var) + 1):
            new = multiplier3 * var[1][i]
            var[2][i] = var[2][i] - new
        if var[2][2] == 0:
            print("LU Decomposition Method: MATH ERROR")
            return
        lower[2][1] = multiplier3
        for i in range(len(var)):
            del var[i][3]
        upper = var
        y[0] += b[0]                                                                          #Computation of results.                                    
        y[1] += b[1] - (lower[1][0] * y[0])                                                   #Computation of results.  
        y[2] += b[2] - (lower[2][0] * y[0]) - (lower[2][1] * y[1])                            #Computation of results.  
        x[2] += y[2] / upper[2][2]                                                            #Computation of results.                
        x[1] += (y[1] - (upper[1][2] * x[2])) / upper[1][1]                                   #Computation of results.  
        x[0] += (y[0] - (upper[0][1] * x[1]) - (upper[0][2] * x[2])) / upper[0][0]            #Computation of results. 
        x[0] = round(x[0], 3)                                                                 #Rounding up results.  
        x[1] = round(x[1], 3)                                                                 #Rounding up results.  
        x[2] = round(x[2], 3)                                                                 #Rounding up results.  
        print("LU Decomposition Method: x1 =", x[0]," ", "x2 =", x[1]," ", "x3 =", x[2])
        return
    elif len(var) == 4:
        lower = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]                       #Variable declaration of matrix to be used for LU Decomposition.
        upper = []                                                                             #Variable declaration of matrix to be used for LU Decomposition.
        b = [var[i][4] for i in range(len(var))]                                               #Variable declaration of matrix to be used for LU Decomposition. 
        y = [0 for i in range(len(var))]                                                       #Variable declaration of matrix to be used for LU Decomposition.
        x = [0 for i in range(len(var))]                                                       #Variable declaration of matrix to be used for LU Decomposition.
        multiplier1 = var[1][0] / var[0][0]   
        for i in range(0, len(var) + 1):
            new = multiplier1 * var[0][i]
            var[1][i] = var[1][i] - new
        if var[1][1] == 0 or var[1][2] == 0 or var[1][3] == 0:
            print("LU Decomposition Method: MATH ERROR")
            return
        lower[1][0] = multiplier1
        multiplier2 = var[2][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier2 * var[0][i]
            var[2][i] = var[2][i] - new
        if var[2][1] == 0 or var[2][2] == 0 or var[2][3] == 0:
            print("LU Decomposition Method: MATH ERROR")
            return
        lower[2][0] = multiplier2
        multiplier3 = var[3][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier3 * var[0][i]
            var[3][i] = var[3][i] - new
        if var[3][1] == 0 or var[3][2] == 0 or var[3][3] == 0:
            print("LU Decomposition Method: MATH ERROR")
            return
        lower[3][0] = multiplier3
        multiplier4 = var[3][1] / var[2][1] 
        for i in range(0, len(var) + 1):
            new = multiplier4 * var[2][i]
            var[3][i] = var[3][i] - new
        if var[3][2] == 0 or var[3][3] == 0:
            print("LU Decomposition Method: MATH ERROR")
            return
        lower[3][1] = multiplier4
        multiplier5 = var[2][1] / var[1][1] 
        for i in range(0, len(var) + 1):
            new = multiplier5 * var[1][i]
            var[2][i] = var[2][i] - new
        if var[2][2] == 0 or var[2][3] == 0:
            print("LU Decomposition Method: MATH ERROR")
            return
        lower[2][1] = multiplier5
        multiplier6 = var[3][2] / var[2][2]
        for i in range(0, len(var) + 1):
            new = multiplier6 * var[2][i]
            var[3][i] = var[3][i] - new
        if var[3][3] == 0:
            print("LU Decomposition Method: MATH ERROR")
            return
        lower[3][2] = multiplier6
        y = [var[i][4] for i in range(len(var))]                                      #Variable declaration of matrix to be used for LU Decomposition.
        for i in range(len(var)):
            del var[i][4]
        upper = var       
        # y[0] += b[0]
        # y[1] += b[1] - (lower[1][0] * y[0])
        # y[2] += b[2] - (lower[2][0] * y[0]) - (lower[2][1] * y[1])
        # y[3] += b[3] - (lower[3][0] * y[0]) - (lower[3][1] * y[1]) - (lower[3][2] * y[2])
        x[3] += y[3] / upper[3][3]                                                                              #Computation of results.
        x[2] += (y[2] - (upper[2][3] * x[3])) / upper[2][2]                                                     #Computation of results.                   
        x[1] += (y[1] - (upper[1][3] * x[3]) - (upper[1][2] * x[2])) / upper[1][1]                              #Computation of results.
        x[0] += (y[0] - (upper[0][3] * x[3]) - (upper[0][2] * x[2]) - (upper[0][1] * x[1])) / upper[0][0]       #Computation of results. 
        x[0] = round(x[0], 3)                                                                                   #Rounding up results.
        x[1] = round(x[1], 3)                                                                                   #Rounding up results.
        x[2] = round(x[2], 3)                                                                                   #Rounding up results.
        x[3] = round(x[3], 3)                                                                                   #Rounding up results.
        print("LU Decomposition Method: x1 =", x[0]," ", "x2 =", x[1]," ", "x3 =", x[2]," ", "x4 =", x[3])
        return
