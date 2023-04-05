import random
# from pyfair import fairplay as fp
import pyfair as fp
# Define the length of the vectors
n = 10

# Part a
# Generate Alice's private vector
A = [random.randint(0, 1) for i in range(n)]

# Generate Bob's private vector
B = [random.randint(0, 1) for i in range(n)]

# computes the scalar product
def scalar_product(A, B):
    return sum([A[i]*B[i] for i in range(n)])

# Part b , c , d 
# Define the input and output functions for Alice and Bob
def input_A():
    # Generate a random vector for the input masking
    R = [random.randint(0, 1) for i in range(n)]
    # Compute the shared secrets
    s1 = fp.get_random_bits(n)
    s3 = fp.get_random_bits(1)[0]
    # Compute the masked input
    A_masked = [a ^ r ^ s1[i] for i, a, r in zip(range(n), A, R)]
    return (A_masked, s1, s3)

def input_B():
    # Generate a random vector for the input masking
    R = [random.randint(0, 1) for i in range(n)]
    # Compute the shared secrets
    s2 = fp.get_random_bits(n)
    s3 = fp.get_random_bits(1)[0]
    # Compute the masked input
    B_masked = [b ^ r ^ s2[i] for i, b, r in zip(range(n), B, R)]
    return (B_masked, s2, s3)

def output_A(output):
    # Extract the shared secrets from Bob's output
    s2, s3 = output
    # Compute the unmasked output
    return scalar_product(A, B) ^ s2 ^ s3

def output_B(output):
    # Extract the shared secrets from Alice's output
    s1, s3 = output
    # Compute the unmasked output
    return scalar_product(A, B) ^ s1 ^ s3

# Compile the input and output functions into circuits
input_A_circuit = fp.compile(input_A, "inputA")
input_B_circuit = fp.compile(input_B, "inputB")
output_A_circuit = fp.compile(output_A, "outputA")
output_B_circuit = fp.compile(output_B, "outputB")

# Generate the circuit files for Alice and Bob
input_A_circuit.write("inputA.txt")
input_B_circuit.write("inputB.txt")
output_A_circuit.write("outputA.txt")
output_B_circuit.write("outputB.txt")

# Evaluate the circuits using the Fairplay runtime system
results = fp.run("scalar_product", ["inputA.txt", "inputB.txt"], ["outputA.txt", "outputB.txt"])

# Extract the final output from the results
scalar_product_AB = (A[0] * B[0]) ^ (A[1] * B[1]) ^ (A[2] * B[2]) ^ (A[3] * B[3]) ^ (A[4] * B[4]) ^ (A[5] * B[5]) ^ (A[6] * B[6]) ^ (A[7] * B[7]) ^ (A[8] * B[8]) ^ (A[9] * B[9])

print("Alice's private vector")
print(A)
print("Bob's private vector")
print(B)
print('The scalar product of A and B is' , scalar_product_AB)
