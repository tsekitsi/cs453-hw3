### SCM protocol design:

1. Alice generates a key pair (pk, sk) and shares pk with Bob, Chris and David.
2. Alice encrypts $\vec{V_a}$ and sends $\vec{\Sigma} = \text{E}_{\text{pk}}(\vec{V_a})$ to Bob.
3. Each of Bob, Chris and David generates a random integer $r_i$, where $i \in \lbrace b, c, d\rbrace$. Let $\mathbf{1}$ denote the vector of ten 1's.
Each party, upon receiving $\vec{\Sigma}$, adds $\mathbf{1} \times r_i$ to  $\vec{V_i}$, sets
$\vec{\Sigma} \leftarrow \vec{\Sigma} * \text{E}_{\text{pk}}(\vec{V_i} + \mathbf{1} \times r_i)$, thus maintaining summation in the plaintext domain,
and sends the updated $\vec{\Sigma}$ to the next party.
4. David sends the final $\vec{\Sigma}$ back to Alice. Upon receiving $\vec{\Sigma}$, Alice decrypts it using sk and obtains $\vec{V_n}$.
5. Alice computes $m_n = \max(\vec{V_n})$ and sends $\sigma = \text{E}_{\text{pk}}(m_n)$ to Bob.
6. Each of Bob, Chris and David sets $\sigma \leftarrow \sigma \div \text{E}_{\text{pk}}(r_i)$, thus subtracting $r_i$ in the plaintext domain, where
$i \in \lbrace b, c, d\rbrace$, and sends the updated $\sigma$ to the next party.
7. David sends the final $\sigma$ back to Alice. Alice decrypts it using sk and obtains $m$, the maximum value in $\vec{V}=\vec{V_a}+\vec{V_b}+\vec{V_c}+\vec{V_d}$.
