def aaa():
    # global a
    # a = a + 1
    a = 10
    print(a)
    print("locals", locals())
    print("globals", globals())

    # print(a)


def bbb():
    # b[0] = 10
    # b = b.append(10)
    b = [4, 5, 6]
    # print(b)
    # print("locals", locals())
    # print("globals", globals())
    # print(b)


a = 1
aaa()

b = [1, 2, 3]
bbb()
print(b)
