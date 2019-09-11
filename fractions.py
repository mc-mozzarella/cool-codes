def simplify_fraction(a, b):
    """
    Simplifies the fraction a/b
    """
    gcd = greatest_common_divisor(a,b)
    
    return int(a/gcd), int(b/gcd)

def greatest_common_divisor(a, b):
    """
    Finds the GCD of a/b
    """
    divisor = min(a,b)
    
    not_divisible = a % divisor != 0 or b % divisor != 0
    not_one = divisor != 1
    while not_divisible and divisor != 1:
        divisor -= 1
        
        not_divisible = a % divisor != 0 or b % divisor != 0
        not_one = divisor != 1

    else:
        if not not_one:
            return 1
        
        elif not not_divisible:
            return divisor
        
        else:
            raise

