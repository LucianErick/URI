leds = [(1,2),(2,5),(3,5),(4,4),(5,5),(6,6),(7,3),(8,7),(9,6),(0,6)]
def qtsLeds(number):
    amount = 0
    for char in number:
        for led in leds:
            if int(char) == led[0]:
                amount+=led[1]
    return str(amount) + " leds"

qtInputs = int(input())
for i in range(qtInputs):
    number = input()
    print (qtsLeds(number))
    