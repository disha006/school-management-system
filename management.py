import mysql.connector as a
con= a.connect(host="localhost",user="root",password="disha",database="student")

def add_student():
    n=input("ENTER THE NAME OF STUDENT ")
    c=input("ENTER THE CLASS OF STUDENT ")
    r=input("ENTER THE ROLL NUMBER ")
    a=input("ENTER THE ADDRESS ")
    p=input("ENTER THE PHONE NUMBER ")
    data=(n,c,r,a,p)
    sql='insert into student values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data entered successfully")
    print("____________________________________________________________________________________________________________")
    main()

def remove_student():
    c=input("name:")
    r=input("Roll number:")
    data=(c,r)
    sql='delete from student where name =%s and ROLL_no=%s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print("____________________________________________________________________________________________________________")
    main()

def add_teacher():
    b=input("name:")
    p=input("post:")
    s=input("salary:")
    ph=input("phone:")
    ac=input("account:")
    data=(b,p,s,ph,ac)
    sql='insert into teacher values(%s,%s,%s,%s,%s)'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print("____________________________________________________________________________________________________________")
    main()

def remove_teacher():
    n=input("Teacher name :")
    ac=input("Post:")
    data=(n,ac)
    sql='delete from teacher where  name = %s and post =%s'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print("____________________________________________________________________________________________________________")
    main()

def class_attendance():
    d=input("date:")
    cl=input("Class:")
    ab=input("Name:")
    z=input("attendance:")
    data=(d,cl,ab,z)
    sql='insert into class_attendance values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print("____________________________________________________________________________________________________________")
    main()

def teacher_attendance():
    d=input("date:")
    ab=input("Name")
    at=input("attendance:")
    data=(d,ab,at)
    sql='insert into teacher_attendance values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print("____________________________________________________________________________________________________________")
    main()

def display_class():
    cl=input("class:")
    data=(cl,)
    sql="select*from student where class=%s"
    c=con.cursor()
    c.execute(sql,data)
    c=c.fetchall()
    for i in c:
        print("NAME:",i[0])
        print("CLASS:",i[1])
        print("ROLL:",i[2])
        print("ADDRESS:",i[3])
        print("PHONE:",i[4])
        print("________________________________________________________________________________________________________")
    main()

def teacher_list():
    sql="select*from teacher"
    c=con.cursor()
    c.execute(sql)
    c=c.fetchall()
    for  i in c:
        print("NMAE:",i[0])
        print("POST:",i[1])
        print("SALARY:",i[2])
        print("CONTACT:",i[3])
        print("ACNO:",i[4])
        print("________________________________________________________________________________________________________")
    main()

def main():
    print("""     Ｄ．Ｄ．Ｓ．Ｂ．Ｓ ＩＮＴＥＲ ＣＯＬＬＥＧＥ

     1.ADD STUDENT            2.REMOVE STUDENT
     3.ADD TEACHER            4.REMOVE TEACHER
     5.CLASS ATTENDANCE       6.TEACHER ATTENDANCE
     7.DISPLAY CLASS          8.TEACHER LIST

""")
    choice=input("Enter The NO. :")
    print("____________________________________________________________________________________________________________")
    if(choice=='1'):
        add_student()
    elif(choice=='2'):
        remove_student()
    elif(choice=='3'):
        add_teacher()
    elif(choice=='4'):
        remove_teacher()
    elif(choice=='5'):
        class_attendance()
    elif(choice=='6'):
        teacher_attendance()
    elif(choice=='7'):
        display_class()
    elif(choice=='8'):
        teacher_list()
    else:
        print("Wrong choice................")
        main()

def pswd():
    p=input("Password:")
    if p=="12345":
        main()
    else:
        print("Wrong Password:")
        pswd()
pswd()
