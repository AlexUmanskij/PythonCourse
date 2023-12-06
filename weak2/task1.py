def deleter(line):
    lineFilter = ['Python', 'php', 'go', 'C']
    lineMassive = line.split(' ')
    newLine = ''
    for i in lineMassive:
        if i not in lineFilter:
            newLine += ' '
            newLine += i
    return newLine

line = 'asfa 111 kak php Python sfsf go Co'
print(deleter(line))