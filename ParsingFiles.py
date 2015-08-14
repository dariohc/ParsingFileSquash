__author__ = 'Dario Hermida'
from sys import argv

def get_player_name(line):
    init_name = line.find('">') + 2
    finish_name = line.find('</a>') - 1
    player_name = line [init_name : finish_name+1]
    return (player_name)

script, filename, create = argv
count = 1
player_count = 1
print ("Opening the file:")
target = open(filename, 'r')
output = open(create, 'w')
writing = True

print ("I'm going to read from the target file:")

for line in target:
    # this is able to write al member lines
    if "memberID" in line:
        output.write(str(player_count))
        output.write(' - ')
        output.write(get_player_name(line))
        output.write('\n')
        player_count += 1
        #print (line[line.find('">') + 2])
        #print (line[line.find('</a>') - 1])
    print(line)
    #input()
    count += 1

print ("And finally, we close it")

target.close()
output.close()
