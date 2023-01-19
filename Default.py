def Area(Radius,PI = 3.14):
    Result = PI * Radius * Radius
    return Result



def main():
    RValue = 10.5
    PIValue = 3.14

    Ans = Area(RValue,PIValue)  # positional  # Ans = Area(10.5,3.14)
    print("Area of circle is : ",Ans)

    Ans = Area(PI = PIValue, Radius= RValue)  # Keyword # Ans = Area (3.14,10.5)
    print("Area of circle is : ", Ans)

    Ans = Area(10.5)  # positional , Default   # Ans = Area(10.5)
    print("Area of circle is : ", Ans)

    Ans = Area(Radius = 10.5)  # Keyword , Default
    print("Area of circle is : ", Ans)

    Ans = Area(PI = 7.10, Radius=10.5)
    print("Area of circle is : ", Ans)

if __name__=="__main__":
    main()
