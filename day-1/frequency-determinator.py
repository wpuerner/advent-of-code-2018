current_freq = 0

with open("frequency-changes.txt") as f:
	freq_changes = f.readlines()

	freq_changes = [x.strip() for x in freq_changes]

	for i in range(len(freq_changes)):
		if freq_changes[i][0] == "-":
			current_freq = current_freq - int(freq_changes[i][1:])
		elif freq_changes[i][0] == "+":
			current_freq = current_freq + int(freq_changes[i][1:])

print current_freq