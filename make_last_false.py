def make_last_false(n):
    """
    Takes a range n of values as an input. The function makes n-1 True bools and the n bool a False statement. The intention of this function is to see if you can pass a function as a while loop condition. It seems that the while loop only conciders the first iteration ending therefore in a endless loop.
    """
    for i in range(n, -1, -1):
        yield  bool(i)
        

if __name__ == "__main__":
    n = 10
    
    print(list(make_last_false(n)))
    
#     this while loop ends in an endless loop
#     while make_last_false(n):
#         pass
