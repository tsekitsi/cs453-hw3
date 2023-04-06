from phe import paillier
import numpy as np
import random

def enc_mat_mul(en_A, B):
    """
    The matrix multiplication is performed by Bob.
    According to Paillier implementation, we have:
    E(a*b) = E(a)*b
    E(a+b) = E(a)+E(b)
    """  
    C = []
    for i in range(len(en_A)):
        row =[]
        for j in range(len(B[0])):           
            for k in range(len(B)):
                if k==0:
                    num = en_A[i][k]*B[k][j]
                else: 
                    num += en_A[i][k]*B[k][j]
            row.append(num)
        C.append(row)
    return C


def main():
    #genenrating keys with length 512
    public_key, private_key = paillier.generate_paillier_keypair(n_length=512)

    #Alice encrypt the matrix A
    A_np = np.random.randint(500, size=(5, 8))
    A = [[int(x) for x in row] for row in A_np]
    encrypted_A = [[public_key.encrypt(x) for x in row] for row in A]
    print('Alice\'s matrix:\n', A)

    #Bob performs the matrix multiplication on B and encrypted A from Alice, then 
    #send back to Alice.
    B_np = np.random.randint(500, size=(8, 4))
    B = [[int(x) for x in row] for row in B_np]
    print('Bob\'s matrix:\n', B)
    enc_mat = enc_mat_mul(encrypted_A, B)
    print('cyphertext:\n', enc_mat)
    
    #Alice perform decryption
    mat_prod = [[private_key.decrypt(x) for x in row] for row in enc_mat]
    print('decrypted matrix multiplication:\n', mat_prod)
    print('To verify:\n',np.matmul(A_np, B_np))

if __name__ == "__main__":
    main()


