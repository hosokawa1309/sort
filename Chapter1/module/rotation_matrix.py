import numpy as np
def rot_matrix(mat):
    N = len(mat)
    ans = np.zeros([N,N])
    for i in range(N):
        for j in range(N):
            ans[i][j] = mat[N - 1 - j][i]

    return ans

if __name__ == "__main__":
    print(rot_matrix([[1,2,3],[4,5,6],[7,8,9]]))
    print(rot_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
