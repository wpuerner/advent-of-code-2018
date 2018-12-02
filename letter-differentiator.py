
def check_letters(current_id, check_id):
	num_diffs = 0
	for i in range(len(current_id)):
		if current_id[i] != check_id[i]:
			num_diffs += 1

	return num_diffs


with open("box-ids.txt") as f:
	box_ids = f.readlines()
	box_ids = [x.strip() for x in box_ids]

	for i in range(len(box_ids)):
		for m in range(len(box_ids)):
			num_diffs = check_letters(box_ids[i], box_ids[m])
			if num_diffs == 1:
				print "Found the matching Ids: "
				print box_ids[i]
				print box_ids[m]
