def split_axiom(axiom, N):
    k, m = divmod(len(axiom), N)
    if k == 0:
        return [axiom[i] for i in range(m)]
    else:
        return [
            axiom[(k+1)*i:(k+1)*(i+1)] if i < m
            else axiom[k*i+m:k*(i+1)+m]
            for i in range(N)
            ]


if __name__ == '__main__':
    axiom_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(split_axiom(axiom_1, 8))
    axiom_2 = 'ABCDE'
    print(split_axiom(axiom_2, 8))
