import random

def start():
	a = int(input("Enter number: "))
	b = int(input("Enter number: "))
	
	n = generate_keypair(a,b)
	
	return n

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
		
def multiplicative_inverse(a,b):
	if b == 0:
		return a
	else:
		d = multiplicative_inverse(b,a % b)
	return a // b
	
		
def generate_keypair(p, q):

	if not (isprime(p) and isprime(q)):
		print("'Both numbers must be prime.")
		start()
	elif p == q:
		print('p and q cannot be equal')
		start()
	else:
		print("These numbers are prime")
		
			
	n = p * q
		
	phi = (p - 1)*(q - 1)
		
	e = random.randrange(1, phi)
		
	g = gcd(e,phi)
		
	while g != 1:
		e = random.randrange(1, phi)
		g = gcd(e, phi)
		
		
			
			
	d = multiplicative_inverse(e, phi)
		
	return ((e, n), (d, n))


print(start())				