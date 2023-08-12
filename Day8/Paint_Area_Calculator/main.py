import math

def paint_calc(height, width, cover):
    num_of_cans_required = math.ceil((height*width)/cover)
    print(f"You'll need {num_of_cans_required} of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
