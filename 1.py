def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True
		
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
			
			


			
	
		
		
		
		
	
			
		