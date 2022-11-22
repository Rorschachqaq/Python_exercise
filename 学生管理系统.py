class stu:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.score1 = 0  # 语文
        self.score2 = 0  # 数学
        self.score3 = 0  # 英语
        self.sum = 0  # 总分

    def sumscore(self):
        self.sum = self.score1 + self.score2 + self.score3
        return self.sum



class Student:
    def __init__(self, stulist: list):
        self.stulist = stulist

        print("欢迎来到学生成绩管理系统")
        print("*" * 30)
        print("-" * 7, "菜单", "-" * 7)
        print("1.增加学生信息")
        print("2.删除学生信息")
        print("3.修改学生信息")
        print("4.查找学生信息.")
        print("5.察看所有学生信息")
        print("6.学生成绩排序")
        print("7.退出系统")

        while True:
            a = input("请选择：")
            if (a == "1"):
                self.addstu()
            elif a == "2":
                self.delstu()
            elif a == "3":
                self.changestu()
            elif (a == "4"):
                self.findstu()
            elif (a == "5"):
                self.checkstu()
            elif a == "6":
                self.sortstu()
            elif a == "7":
                print("已退出!")
            print("文件信息已更新!")
            break

    # 查重 已存在：返回列表中坐标，不存在：返回-1
    def cfindstu(self, idin):
        for i in range(0, len(self.stulist)):
            if (idin == self.stulist[i].id):
                return i
        return -1

    # 添加学生信息
    def addstu(self):
        student = stu()
        student.name = input("请输入学生姓名：")
        student.id = input("请输入学生id：")

        # 查重
        if self.cfindstu(student.id) != -1:
            print("该学生已存在")
            return False

        student.score1 = int(input("请输入语文成绩:"))
        student.score2 = int(input("请输入语文成绩:"))
        student.score3 = int(input("请输入语文成绩:"))

        self.stulist.append(student)
        print("添加成功!")
        return True

    # 查找学生信息
    def findstu(self):
        idin = input("请输入学生学号：")
        for i in range(0, len(self.stulist)):
            if (idin == self.stulist[i].id):
                print("该学生信息如下：")
                print("学号：", self.stulist[i].id, end="\t|")
                print("姓名：", self.stulist[i].name, end="\t|")
                print("语文成绩：", self.stulist[i].score1, end="\t|")
                print("数学成绩：", self.stulist[i].score2, end="\t|")
                print("英语成绩：", self.stulist[i].score3, end="\t|")
                print("总成绩：", self.stulist[i].sumscore())
                return True
        print("没有该学生信息")
        return False

    # 查看所有学生信息
    def checkstu(self):
        print("学生信息如下：")
        print("*" * 100)  # 换行
        if len(self.stulist) == 0:
            print("当前无学生信息")
        for i in range(0, len(self.stulist)):
            print("学号：", self.stulist[i].id, end="\t|")
            print("姓名：", self.stulist[i].name, end="\t|")
            print("语文成绩：", self.stulist[i].score1, end="\t|")
            print("数学成绩：", self.stulist[i].score2, end="\t|")
            print("英语成绩：", self.stulist[i].score3, end="\t|")
            print("总成绩：", self.stulist[i].sumscore())
            print("-" * 100)  # 换行

    # 删除学生信息
    def delstu(self):
        idin = input("请输入你要删除学生的学号：")
        # 利用查重函数返回删除学生在列表中坐标
        result = self.cfindstu(idin)
        if result == -1:
            print("该学生不存在")
        else:
            for i in range(result, len(self.stulist) - 1):
                self.stulist[i] = self.stulist[i + 1]
            del self.stulist[len(self.stulist) - 1]
            print("删除成功")

    # 修改学生信息
    def changestu(self):
        idin = input("请输入你要修改学生的学号：")
        result = self.cfindstu(idin)
        if result == -1:
            print("该学生不存在")
        else:
            id = input("请重新输入学生id：")
            if (self.cfindstu(id) != -1):
                print("该id已存在&#xff0c;修改失败")
                return False
            self.stulist[result].id = id
            self.stulist[result].name = input("请重新输入学生姓名：")
            self.stulist[result].score1 = int(input("请重新输入学生语文成绩："))
            self.stulist[result].score2 = int(input("请重新输入学生数学成绩："))
            self.stulist[result].score3 = int(input("请重新输入学生英语成绩："))
            print("修改成功!按“5”查看")

    # 按学生成绩排序,采用插入法
    def sortstu(self):
        for i in range(0, len(self.stulist) - 1):
            for j in range(i + 1, 0, -1):
                if self.stulist[j].sum > self.stulist[j - 1].sum:
                    tmp = stu()
                    tmp = self.stulist[j - 1]
                    self.stulist[j - 1] = self.stulist[j]
                    self.stulist[j] = tmp
        print("排序成功!")


my_student = Student([])