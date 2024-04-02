"""Write a function so that the columns of the output matrix are powers of the input vector.
The order of the powers is determined by the increasing boolean argument. Specifically, when increasing is False, the i-th output column is the input vector raised element-wise to the power ofN-i-1.
HINT: Such a matrix with a geometric progression in each row is named for Alexandre- Theophile Vandermonde."""
import numpy as np

def vandermonde_matrix(input_vector, N, increasing=True):
    input_vector = np.array(input_vector)
    input_vector = input_vector.reshape(-1, 1)

    if increasing:
        exponents = np.arange(N)
    else:
        exponents = np.arange(N-1,-1,-1)  

    powers_of_matrix = input_vector ** exponents
    return powers_of_matrix


#print(vandermonde_matrix([1,2,3,4,5], 4))

"""Problem Statement 2:
Given a sequence of n values x1, x2, ..., xn and a window size k>0, the k-th moving average of the given sequence is defined as follows:
The moving average sequence has n-k+1 elements as shown below.
The moving averages with k=4 of a ten-value sequence (n=10) is shown below
i 12345678910
===== ====================
Input102030405060708090100
y1 25 = (10+20+30+40)/4
y2 35 = (20+30+40+50)/4
y3 45 = (30+40+50+60)/4
y4 55 = (40+50+60+70)/4
y5 65 = (50+60+70+80)/4
y6 75 = (60+70+80+90)/4
y7 85 = (70+80+90+100)/4
Thus, the moving average sequence has n-k+1=10-4+1=7 values.
Question: Write a function to find moving average in an array over a window:
Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3."""


def moving_average(seq, k):  # k is the window size
    seq = np.array(seq)
    moving_averages = np.zeros(len(seq)- k +1)
    for i in range(len(seq)- k +1):
        moving_averages[i] = np.sum(seq[i:i+k]) / k
    return moving_averages

print(moving_average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150],3))        