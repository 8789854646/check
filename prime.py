def is_prime(num):
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				print("Not Prime no")
				break
		else:
			print("PRIME NO")

is_prime(2)