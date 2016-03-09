__author__ = 'Dario Hermida'
from sys import argv

def get_player_name(line):

    init_name = line.find('">') + 2
    finish_name = line.find('</a>') - 1
    player_name = line[init_name: finish_name+1]
    return (player_name)

script, filename, create = argv
count = 1
player_count = 1
print("Opening the file:")
target = open(filename, 'r')
output = open(create, 'w')
writing = True
player_found = False
print("I'm going to read from the target file:")
player_result = []
s = ''
allowed_results = ['0', '1', '2', '3']

total_players_found = 0
for line in target:
    # this is able to write al member lines
    if "memberID" in line:
        output.write(str(player_count))
        output.write(' - ')
        output.write(get_player_name(line))
        # player_list.append(get_player_name(line))
        output.write(' ')
        player_count %= 5
        player_count += 1
        print(line[line.find('">') + 2])
        print(line[line.find('</a>') - 1])
        print(line)
        # input()
        player_found = True

    if player_found:
        for read_lines in range(0, 5):
            print(target.readline())  # 6th position is the first result of the player
        player_result.append(target.readline()[0])
        for k in range(0, 4):
            for read_lines in range(0, 3):
                target.readline()
            player_result.append(target.readline()[0])
        player_found = False
        # print(player_result)
        player_result[total_players_found] = '*'
        for i in range(0, 5):
            if player_result[i] not in allowed_results:
                s += '* '
            else:
                s += (player_result[i] + ' ')
        output.write(s)
        total_players_found += 1
        total_players_found %= 5
        output.write('\n')
        print(s)
        s = ''
        player_result = []
        if player_count % 5 == 1:
            output.write('\n')

    count += 1
print("And finally, we close it")
target.close()
output.close()
