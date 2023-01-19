import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousHeadBrainPredictor():

    #Load Data
    data = pd.read_csv('MarvellousHeadBrain.csv')

    print("Size if data set",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    
    #Least Square method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

   
    n = len(X)

    numerator = 0
    denomenator = 0
    
    # Equation of line is y = mx+ c

    for i in range(n):
        numerator += (X[i] -mean_x)*(Y[i]- mean_y)

        denomenator += (X[i] - mean_x)**2

    m = numerator / denomenator

    # c = y' - mx'

    c = mean_y - (m * mean_x)

    print("Slope of Regession line is",m) #0.4 
    print("Y intercept of Regession line is",c) # 2.4 
    

    max_x = np.max(X)+100
    min_x = np.min(X)+100

    # Display plotting of above points
    x = np.linspace(max_x,min_x,n)

    y = c + m * x

    plt.plot(x,y,color = '#58b970' , label='Regession Line')

    plt.scatter(X,Y,color ='#ef5423', label ='scatter plot')

    plt.xlabel('Head size in cm3')
    plt.ylabel('Brain Weight(grams)')

    plt.legend()
    plt.show()

    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m *X[i]
        ss_t += (Y[i] - mean_y) **2
        ss_r += (Y[i] - y_pred) **2

    r2 = 1 -(ss_r/ss_t)

    print(r2)

def main():
    print("-----Marvellous Infosystems by Piyush Khairnar--------")

    print("Supervised Machine Learning")

    print("Linear Regression on Head abd Brain size data set")

    MarvellousHeadBrainPredictor()

if __name__=="__main__":
    main()