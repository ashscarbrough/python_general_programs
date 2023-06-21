'''
Python program to find minimum possible time for a full production item to complete
- Production assembly line has multiple stations (n) to assemble a part
- There may be multiple assembly lines
- Items can be transfered between assembly lines to accelerate production
'''

def assembly(assembly_line, time_switch, entry_time, exit_time):
    '''
    Function to represent an assembly line and determine minimum time for production
    '''

    # Number of stations in assembly line
    NUM_STATION = len(assembly_line[0])  # length of number of stations
    TIMES_1 = [0 for i in range(NUM_STATION)]  # initialize times for line 1 stations
    TIMES_2 = [0 for i in range(NUM_STATION)]  # initialize times for line 2 stations

    TIMES_1[0] = entry_time[0] + assembly_line[0][0] # time taken to leave first station in line 1
    TIMES_2[0] = entry_time[1] + assembly_line[1][0] # time taken to leave first station in line 2

    # Fill tables T1[] and T2[] using above given recursive relations
    for i in range(1, NUM_STATION):
        TIMES_1[i] = min(TIMES_1[i-1] + assembly_line[0][i],
                    TIMES_2[i-1] + time_switch[1][i] + assembly_line[0][i])
        TIMES_2[i] = min(TIMES_2[i-1] + assembly_line[1][i],
                    TIMES_1[i-1] + time_switch[0][i] + assembly_line[1][i] )

    # consider exit times and return minimum
    return min(TIMES_1[NUM_STATION - 1] + exit_time[0],
               TIMES_2[NUM_STATION - 1] + exit_time[1])

assembly_line_times = [[4, 5, 3, 2], [2, 10, 1, 4]]  # time taken at each station per assembly line
time_switch_lines = [[0, 7, 4, 5], [0, 9, 2, 8]]  # time taken to switch assembly lines
entrance_times = [10, 12]  # time taken to enter asembly lines
exit_times = [18, 7]  # time taken to exit assembly lines

print(assembly(assembly_line_times, time_switch_lines, entrance_times, exit_times))
