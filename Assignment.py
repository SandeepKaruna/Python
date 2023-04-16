class MulAssignments():
    def oddEven():
        i=int(input("Enter your number:"))
        if(i%2==0):
            print(i,"is even")
            message="the number is even"
        else:
            print(i,"is odd")
            message="the number is odd"
    def Eligiblity():
            age=int(input("Enter you Age:"))
            s=input("Enter your Gender (MALE/FEMALE):")
            if ((s=="MALE")and(age>20)):
                print("You are eligible")
                Status="yes"
            elif ((s=="FEMALE") and (age>17)):
                print("You are eligible")
                Status="yes"
            else:
                print("you are not eligible")
                Status="No"
            return Status
    def Percentage():
            S1=int(input("Subject1="))
            S2=int(input("Subject2="))
            S3=int(input("Subject3="))
            S4=int(input("Subject4="))
            S5=int(input("Subject5="))
            ST=S1+S2+S3+S4+S5
            print("Total=",ST)
            ST1=(ST/float(5))
            print("percentage:",ST1)
    def BMI():
            w=int(input("enter your weight(Kgs):"))
            h=int(input("enter your height(Cms):"))
            y=h/100
            bmi=w/(y*y)
            if(bmi<18.5):
                print("Below Normal")
            elif(bmi<25):
                print("Normal")
            elif(bmi<30):
                print("overweight!")
            else:
                print("You have obesity consult a doctor")
    def Triangle():
            h=int(input("Height:"))
            b=int(input("Breadth:"))
            print("Area formula :(Height*Breadth)/2")
            AreaT=(h*b)/2
            print("Area of Triangle:",AreaT)
            H1=int(input("Height1:"))
            H2=int(input("Height2:"))
            Br=int(input("Breadth:"))
            print("Perimeter formula: Height1+Height2+Breadth")
            PT=H1+H2+Br
            print("Perimeter of Triangle:",PT)
