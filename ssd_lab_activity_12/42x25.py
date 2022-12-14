fd = open("./input.txt", "r")
input_data = []
left_timestamps = []
right_timestamps = []
left_coords = []
right_coords = []
left_read = False
break_flag = False


def to_seconds(t):
    seconds = 0
    for part in t.split(':'):
        seconds = seconds*60 + float(part)
    return seconds


def get_input():
    for i in range(896):
        line = fd.readline()
        if len(line.split("\t")[1: -1]) == 0:
            continue
        input_data.append(line.split("\t")[: -1])


get_input()


for i in range(len(input_data)):
    for j in range(26):
        if input_data[i][j] != "0" and j < 14:
            left_read = True


for i in range(int(len(input_data)/42)):
    break_flag = False
    # print("time - ", i)
    for r in range(1, 43):
        # print(r, i*42+(r-1))
        if break_flag == True:
            # print("skipping")
            break
        if left_read == True:
            for c in range(1, 14):
                if left_read == True and input_data[i*42+(r-1)][c] != "0":
                    left_coords.append(r-1)
                    left_timestamps.append(input_data[i*42+20][0])
                    # print("got the left heel at - ",
                    #   r, i*42+(r-1), c, input_data[i*42+(r-1)][c])
                    left_read = False
                    break_flag = True
                    break
        if left_read == False:
            for c in range(14, 26):
                if left_read == False and input_data[i*42+(r-1)][c] != "0":
                    right_coords.append(r-1)
                    right_timestamps.append(input_data[i*42+20][0])
                    # print("got the right heel at - ",
                    #   r, i*42+(r-1), c, input_data[i*42+(r-1)][c])
                    left_read = True
                    break_flag = True
                    break


# print(left_coords, right_coords, left_timestamps, right_timestamps)
print()
print("Left-foot Y-coordinate:", left_coords)
print("Right-foot Y-coordinate:", right_coords)
print("Left-foot Timestamps:", left_timestamps)
print("Right-foot Timestamps:", right_timestamps)
print()
print("------------- LEFT FOOT STATISTICS -------------\n")
for (i, j) in zip(range(len(left_coords)-1), range(len(left_timestamps)-1)):
    a = left_coords[i]
    b = left_coords[i+1]
    t1 = left_timestamps[j]
    t2 = left_timestamps[j+1]
    t1_seconds = to_seconds(t1)
    t2_seconds = to_seconds(t2)
    print("For", i, "th and", i+1, "th  left step - ")
    print("     Stride Length - ", abs(a-b))
    print("     Time - ", abs(t2_seconds-t1_seconds))
    print("     Stride Velocity - ", abs(a-b)/abs(t2_seconds-t1_seconds))
    print("     Cadence - ", 180/abs(t2_seconds-t1_seconds))

print("\n------------- RIGHT FOOT STATISTICS -------------\n")
for (i, j) in zip(range(len(right_coords)-1), range(len(right_timestamps)-1)):
    a = right_coords[i]
    b = right_coords[i+1]
    t1 = right_timestamps[j]
    t2 = right_timestamps[j+1]
    t1_seconds = to_seconds(t1)
    t2_seconds = to_seconds(t2)
    print("For", i, "th and", i+1, "th  right step - ")
    print("     Stride Length - ", abs(a-b))
    print("     Time - ", abs(t2_seconds-t1_seconds))
    print("     Stride Velocity - ", abs(a-b)/abs(t2_seconds-t1_seconds))
    print("     Cadence - ", 180/abs(t2_seconds-t1_seconds))
