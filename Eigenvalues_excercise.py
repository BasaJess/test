import numpy as np
NotEigenV=np.array([-1,-1])
Eigenv1=np.array([0.86011126,0.51010647])
Eigenv2=np.array([-0.76454754,0.64456735])
A=np.array([[-1,4],[2,-2]])
Lam1 = 2
Lam2 = 2
NotEigenVTr=np.dot(NotEigenV,A)
Eigenv1Tr=np.dot(A,Eigenv1)
Eigenv2Tr=np.dot(A,Eigenv2)

print ("A*Eigenv1: ",Eigenv1Tr)
print("Lambda*Eigenv1:","1.37228132")

lambdas, V = np.linalg.eig(A)
print("lambdas: ",lambdas)
print("V:",V)

import matplotlib.pyplot as plt
def plot_vectors(vectors, colors):
    """
    Plot one or more vectors in a 2D plane, specifying a color for each. 

    Arguments
    ---------
    vectors: list of lists or of arrays
        Coordinates of the vectors to plot. For example, [[1, 3], [2, 2]] 
        contains two vectors to plot, [1, 3] and [2, 2].
    colors: list
        Colors of the vectors. For instance: ['red', 'blue'] will display the
        first vector in red and the second in blue.
        
    Example
    -------
    plot_vectors([[1, 3], [2, 2]], ['red', 'blue'])
    plt.xlim(-1, 4)
    plt.ylim(-1, 4)
    """

    plt.figure()
    plt.axvline(x=0, color='lightgray')
    plt.axhline(y=0, color='lightgray')  

    for i in range(len(vectors)):
        x = np.concatenate([[0,0],vectors[i]])
        plt.quiver([x[0]], [x[1]], [x[2]], [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=colors[i],)


plot_vectors([NotEigenV,NotEigenVTr,Eigenv1,Eigenv1Tr,Eigenv2,Eigenv2Tr], ['grey','black','lightblue', 'blue','orange','red'])
plt.xlim(-4, 5)
_ = plt.ylim(-4, 5)

plt.show()


print("V[:,0] ",V[:,0])


