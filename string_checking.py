''' to document this algorithm is really easy, you just need infinite inteligence-jk.
instead of compearing string_1[n] == string_2[n], which needs immensive time to compute, this algorithm will
implement hash table, using hash table a certain string will have its own value, for example "abc" = 1*29^2 + 2*29^1 + 3*29^0, 
However, long string will need high memory, so we shall take value of string mod in 1000000007=10^9 +7 and double check in modulo 999119999, which is highest prime number
i know, with this a string not being same ,but value - same will be improbable, so we should be okay. '''


# constant Prime 
P_1, P_2,= (10**9 + 7, 999119999) 



# rolling hash table 
rht = {chr(i+96):i for i in range(1,27)}

# converting string to int
def convert(s: str, p: int) -> int :
	value = 0
	for power,char in enumerate(s):
		value += (rht[char.lower()]%p*(29**( len(s) - (power + 1) ))%p)%p
	return value

# compare a with b 
def compare(a: str, b: str) -> bool :
	return convert(a, P_1) == convert(b, P_1) and convert(a, P_2) == convert(b, P_2)