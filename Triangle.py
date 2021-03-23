class Triangle(object):# pylint: disable=missing-docstring
    def __init__(self):# pylint: disable=missing-docstring
        super().__init__()
    def triangle(self, A, B, c) :# pylint: disable=missing-docstring
        if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
            if (a == b) and (a == c):# pylint: disable=missing-docstring
                print('equilateral triangle')
                return 3
            elif ((a == b) or (a == c) or (b == c)):# pylint: disable=missing-docstring
                print('isosceles triangle')
                return 2
            elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
                print('right triangle')
                if ((a == b) or (a == c) or (b == c)):# pylint: disable=missing-docstring
                    print('isosceles right triangle')
                    return 2
                else:# pylint: disable=missing-docstring
                    return 1
            else:# pylint: disable=missing-docstring
                print('general triangle')
                return 1
        else:# pylint: disable=missing-docstring
            print('not a triangle')
if __name__ == '__main__':# pylint: disable=missing-docstring
    while True:# pylint: disable=missing-docstring
        a = int(input('please enter the value of a:')) 
        b = int(input('please enter the value of b:'))
        c = int(input('please enter the value of c:'))
        if (0 < a <= 200) and (0 < b <= 200) and (0 < c <= 200):# pylint: disable=missing-docstring
            print('the three sides of the input are correct')
            triangle = Triangle()
            print('the number of equal sides is:', triangle.triangle(a, b, c))
            break
        else:# pylint: disable=missing-docstring
            print('wrong input')
