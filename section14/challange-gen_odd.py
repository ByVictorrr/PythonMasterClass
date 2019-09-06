# generate odd list of infinite seq of odd starting at one

def infinite_odd():
	odd = 1
	while True:
		yield odd
		odd +=2


def pi_series():
	odds = infinite_odd()
	approx = 0
	while True:
		approx += 4/next(odds)
		yield approx
		approx -= 4/next(odds)
		yield approx

approx_pi = pi_series()
for i in range(1,100):
	print(next(approx_pi))
