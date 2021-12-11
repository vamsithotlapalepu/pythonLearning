def main():
    a = [1,2,3,4,5,6,7,8,9,10]

    a_t = (1,2,3,4,5,6,7,8,9,10)

    

    # Indexing always starts from 0
    b = [1,2.5,"abc"]
    b_t = (1,2.5,"abc")
    """print(type(b[0]))
    print(type(b[1]))
    print(type(b[2]))"""

    #List of list
    #tuple of tuple
    c = [a,b]
    c_t = (a_t,b_t)
    #print(c_t)

    #print(c[0][4])

    # Adding/deleting elements to a existing
    a_t[0] = 100

    #a[0]=100
    #print(a)

    #Adding two lists together
    d = a + b
    #print(d)

    # Operations on the list
    #print(a[-2])
    #print(a[2:6])

main()