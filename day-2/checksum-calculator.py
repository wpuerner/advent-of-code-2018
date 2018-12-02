
def check_duplicates(box_id):
	is_double = 0
	is_triple = 0
	for i in range(len(box_id)):
		num_count = sum(1 for x in box_id if x == box_id[i])
		if num_count == 2:
			is_double = 1
		elif num_count == 3:
			is_triple = 1

	print "Duplicates for " + box_id + ": is_double = " + str(is_double) + " is_triple: " + str(is_triple)

	return (is_double, is_triple)


num_doubles = 0
num_triples = 0

with open("box-ids.txt") as f:
	box_ids = f.readlines()
	box_ids = [x.strip() for x in box_ids]

	for i in range(len(box_ids)):
		dup_tuple = check_duplicates(box_ids[i])
		num_doubles = num_doubles + dup_tuple[0]
		num_triples = num_triples + dup_tuple[1]

	print "Calculated Checksum: " + str(num_doubles * num_triples)

