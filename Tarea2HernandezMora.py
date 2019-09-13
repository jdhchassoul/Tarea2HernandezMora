def main(A, B):
    error = -666
    try:
        Aint = int(A)
        Bint = int(B)
        if Aint >= Bint:
            RESTA = Aint-Bint
            SUMA = Aint+Bint
            MULT = Aint*Bint
            return RESTA, SUMA, MULT
        else:
            print(error)
            return error
    except ValueError:
        print(error)
        return error


if __name__ == '__main__':
    main()
