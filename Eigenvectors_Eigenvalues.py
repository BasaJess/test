import numpy as np
v = np.array([3, 1])
v2 = np.array([2,1])
v3 = np.array([-3,-1])
v4 = np.array([-1,1])
A = np.array([[-1, 4], [2, -2]])
E = np.array([[-1, 4], [2, -2]])
Ev = np.dot(E, v)
F = np.array([[-1, 0], [0, 1]])
Fv = np.dot(F, v)
V = np.concatenate((np.matrix(v).T, np.matrix(v2).T, np.matrix(v3).T,np.matrix(v4).T),axis=1)
AV = np.dot(A, V)

# function to convert column of matrix to 1D vector: 
def vectorfy(mtrx, clmn):
    return np.array(mtrx[:,clmn]).reshape(-1)

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


plot_vectors([vectorfy(V, 0), Ev, Fv, vectorfy(V, 1), vectorfy(V, 2), vectorfy(V, 3),
             vectorfy(AV, 0), vectorfy(AV, 1), vectorfy(AV, 2), vectorfy(AV, 3)], ['lightblue', 'blue', 'darkblue', 'green', 'gray', 'red', 'lightgreen', 'lightgray', 'orange', 'blue'])
plt.xlim(-4, 5)
_ = plt.ylim(-4, 5)

plt.show()

