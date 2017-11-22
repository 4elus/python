import random

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True
		
def gcd(a,b):
	while a!=0 and b!=0:
		if a > b:
			a %= b
		else:
			b %= a
	return a + b		
		
	
		
def generate_keypair(p, q):
	cycle_var = False
	
	while cycle_var != True:
		if not (isprime(p) and isprime(q)):
			raise ValueError("'Both numbers must be prime.")
		elif p == q:
			raise ValueError('p and q cannot be equal')
		else:
			print("These numbers are prime")
			cycle_var = True
			
	n = p * q
		
	phi = (p - 1)  (q - 1)
		
	e = random.randrange(1, phi)
		
	g = gcd(e,phi)
		
	while g != 1:
		e = random.randrange(1, phi)
        g = gcd(e, phi)
			
			
	d = multiplicative_inverse(e, phi)
		
	return ((e, n), (d, n))



	
	
	
n = generate_keypair(5,7)			
			


			
	
		
		
		
		
	
			
		