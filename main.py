target = 5

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
        
        string = " " * spaces
        
        # left side
        string += "/"
        string += "*" * stars
        # door
        if l <= height - 2:
            string += "*"
        else:
            string += "|"
        # right side
        string += "*" * stars
        string += "\\"

        print(string)
        
        
# lines(1) = 2 + t                                  = 3
# lines(2) = lines(1) +                             = 4
# lines(3) = lines(2) + 1 = lines(1) + 2            = 5
# lines(x) = S lines(i) pour i de 0 à x