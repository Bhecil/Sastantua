target = int(input(""))

totalLines = 0
for i in range(target):
    totalLines += 3 + i

currentLine = 0

for floor in range(target):
    height = 3 + floor
    
    for l in range(0, height):
        currentLine += 1
        
        spaces = totalLines - currentLine + 2 * (target - floor - 1)
        stars = currentLine + 2 * floor - 1
        
        hasDoor = floor == target - 1 and l >= 2
        if hasDoor:
            halfDoor = (target - 1) // 2 
            stars -= halfDoor
        
        string = " " * spaces
        
        # left side
        string += "/"
        string += "*" * stars
        # middle
        if hasDoor:
            string += "|" * (halfDoor * 2 + 1)
        else:
            string += "*"
        # right side
        string += "*" * stars
        string += "\\"

        print(string)