Q1 = input("what do u want to do? add, subtract, multiply, divide, square, cube, perimeter, area, percentage or volume ? ")

#addition
while Q1 == "add" :
    Q2 = input("what is the first number ")
    Q3 = input("what is the seconed number ")
    print (f'Your Answer is: {float (Q2) + float (Q3)}')

#subtraction

while Q1 == "subtract":
    Q4 = input("what is the first number? ")
    Q5 = input("What is the seconed number? ")
    print (f'Your Answer is : {float (Q4) - float (Q5)}')

#division

while Q1 == "divide":
    Q6 = input("what is the first number? ")
    Q7 = input("What is the seconed number? ")
    print (f'Your Answer is : {float (Q6) / float (Q7)}')

#multiplication

while Q1 == "multiply":
    Q8 = input("what is the first number? ")
    Q9 = input("What is the seconed number? ")
    print (f'Your Answer is : {float (Q8) * float (Q9)}')

#cube of a number

while Q1 == "cube":
    Q10 = input("what is the number? ")
    print(float (Q10)*float(Q10)*float(Q10))

#square of a number

while Q1 == "square":
    Q11 = input("what is the number? ")
    print(float(Q11)*float(Q11))

#perimeter

while Q1 == "perimeter":
    Q12 = input("what is the shape? square, rectangle, triangle or circle? ")
    
#perimeter square
    
    if Q12 == "square":
        Q13 = input("what is the side? ")
        print(float(Q13)*4)
    
#perimeter of a rectangle
    
    if Q12 == "rectangle":
        Q14=input ("what is the length ")
        Q15=input ("what is the breadth ")
        print ((float (Q14)+ float (Q15))*2)
    
#perimeter of a triangle
    
    if Q12 == "triangle":
        Q16=input ("is it a equilateral triangle? ")
        if Q16 == "yes":
            Q17= input("what is the side? ")
            print(float(Q17)*3)
        if Q16 == "no":
            Q18= input ("what is the first side? ")
            Q19= input ("what is the seconed side? ")
            Q20= input ("what is the third side? ")
            print (float (Q18)+float (Q19)+float (Q20))
    
#perimeter of a circle
    
    if Q12 == "circle":
        Q28= input ("what is the radius? ")
        pi=input ("is the pi value 22/7? ")
        if pi == "yes":
            print (2*22/7* float (Q28))
        if pi== "no":
            print (2*3.14* float (Q28))

#area

while Q1 == "area":
    Q21 = input ("what is the shape? square, rectangle, triangle or circle? ")
    
#area of a square
    
    if Q21 == "square":
        Q22= input ("what is the side? ")
        print (float (Q22)* float (Q22))
    
#area of rectangle
    
    if Q21 == "rectangle":
        Q23= input ("what is the length? ")
        Q24= input ("what is the breadth? ")
        print (float (Q23)* float (Q24))
    
#area of triangle
    
    if Q21 == "triangle":
        Q25= input ("what is the hieght? ")
        Q26= input ("what is the base? ")
        print ((float (Q25)* float (Q26)) * 1/2)
    
#area of circle
    
    if Q21 ==  "circle":
        Q27= input ("what is the radius? ")
        pi1 = input ("is pi value 22/7? ")
        if pi1=="yes":
            print (22/7 * float (Q27) * float (Q27))
        if pi1=="no":
            print (3.14 * float (Q27) * float (Q27))

#area of parallelogram
    if Q21 == "parallelogram":
        Q38= input ("what is the base? ")
        Q39= input ("what is the hieght? ")
        print (float (Q38)* float (Q39))

#percentage

while Q1 == "percentage":
    Q29=input ("what do you want to convert from? decimal or fraction? ")
    if Q29 == "decimal":
        Q30= input ("what is the decimal number? ")
        print (float(Q30) * 100)
    
    if Q29 == "fraction":
        Q31= input ("what is the numerator? ")
        Q32= input ("what is the denominator? ")
        print (float (Q31) / float (Q32)*100)

#volume

while Q1 == "volume":
    Q33= input ("what is the shape? cube or cuboid? ")

#area of cube

    if Q33 == "cube":
        Q34= input ("what is the side? ")
        print (float (Q34)* float (Q34) * float (Q34))

#area of cuboid

    if Q33 == "cuboid":
        Q35= input ("what is the length? ")
        Q36= input ("what is the breadth? ")
        Q37= input ("what is the hieght? ")
        print (float (Q35)* float (Q36)* float (Q37))
