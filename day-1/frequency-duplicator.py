import sys

current_freq = 0

with open("frequency-changes.txt") as f:
	freq_changes = f.readlines()

	freq_changes = [x.strip() for x in freq_changes]

	found_freqs = [current_freq]

	while(1):
		for i in range(len(freq_changes)):
			if freq_changes[i][0] == "-":
				current_freq = current_freq - int(freq_changes[i][1:])
				if current_freq in found_freqs:
					print "Found the first duplicate frequency: " + str(current_freq)
					sys.exit()
				else:
					found_freqs.append(current_freq)

			elif freq_changes[i][0] == "+":
				current_freq = current_freq + int(freq_changes[i][1:])
				if current_freq in found_freqs:
					print "Found the first duplicate frequency: " + str(current_freq)
					sys.exit()
				else:
					found_freqs.append(current_freq)
