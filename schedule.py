def free_days(booked, holidays):
	occupied = booked + holidays
	free = []

	for x in range(1,30):
		if x not in occupied:
			free.append(x)

	return free

if __name__ == "__main__":
	booked = [1,3,9,12,13,18,26,27,28,29]
	holidays = [4,5,15,16,21,22]
	free = free_days(booked, holidays)
	print("Free dates:", free)
