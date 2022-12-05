
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import random
import os


#########################
#       단어장
#########################
Test_English1 = {"applicant":"지원자""/""신청자", "associate":"관련시키다", "candidate":"후보자""/""지원자", "certification":"증명서","confidence": "확신""/""자신감",
                 "degree":"학위","eligible":"자격이 있는","employment":"고용", "entitle":"~에게 자격을 주다", "meet":"만족시키다", "occupaton":"직업",
                 "paycheck":"급료""/""지불", "payroll":"급료명부", "professional":"직업의", "proficiency":"능숙""/""숙달","prospective":"미래의", "reference":"추천서""/""참고",
                 "recruit":"모집하다", "qualified":"자격 있는", "resume":"이력서", "requirement":"필요""/""조건", "abolish":"폐지하다", "access":"접근", "according to":"~에 따라",
                 "accuse":"비난하다", "approval":"승인""/""인가", "at all times":"항상""/""언제나", "attorney":"변호사", "authorize":"~을 인가하다", "comply with":"~따르다", 
                 "custody":"감금""/""구류", "effect":"효과" "영향", "enforce":"시행하다", "exception":"예외", "fraud":"사기", "legislation":"법률", "legitimate":"합법적인",
                 "litigation":"소송""/""기소", "observance":"준수", "petition":"진정서"
                 }

Test_English2 = {"policy":"규정""/""보험증권", "procedure":"절차", "prohibit":"금지하다", "prosecute":"기소하다", "regulation":"규정", "rstrict":"제한하다", "thoroughly":"철저하게",
                 "violate":"위반하다", "accustomed":"~에 익숙한", "acquaint":"잘 알게 하다", "attendance":"출석", "check":"조사하다", "colleague":"동료", "concentrate":"집중하다",
                 "convey":"전달하다", "corporation":"법인", "delegate":"위임하다", "division":"부서", "efficiently":"효율적으로", "impending":"임박한", "instruct":"가르치다",
                 "involved":"관계된", "notify":"~에게 통지하다", "oversee":"감독하다", "release":"발표하다", "reminder":"상기시켜주는 것", "request":"요청", "revision":"수정",
                 "submit":"제출하다", "subordinate":"부하 직원", "supervision":"감독", "translation":"번역", "accomplish":"성취하다", "adjust":"적응하다", "assign":"배정하다",
                 "assist":"돕다", "assume":"가정하다", "conduct":"수행하다", "confidential":"기밀의", "coordinate":"조정하다"
                 }

Test_English3 = {




                }

Test_English4 = {




                }              


words = []
for word in Test_English2:
    words.append(word)

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        global current_index, k
        current_index = 0
        k= 0

        ######################################################
        # 2. 윈도우 폼 구성하기
        ######################################################
        self.setWindowTitle("단어 Test")

        self.lb_info1 = QtWidgets.QLabel(" 영어는 한글로, 한글은 영어로 입력하세요.", self)
        self.lb_info1.setAlignment(QtCore.Qt.AlignLeft)
        self.lb_info1.setStyleSheet("font-family:맑은 고딕;color:balck; font-size:16px;")

        self.lb_quiz = QtWidgets.QLabel("현재 퀴즈 부분 입니다.", self)
        self.lb_quiz.setAlignment(QtCore.Qt.AlignLeft)
        self.lb_quiz.setStyleSheet("font-family:맑은 고딕;color:blue; font-size:20px;")

        self.lb_info2 = QtWidgets.QLabel("총 문제수: 0개<br>맞춘개수: 0개<br>최종점수: 00점", self)
        self.lb_info2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info2.setStyleSheet("font-family:맑은 고딕;color:red; font-size:20px;")

        self.input = QtWidgets.QLineEdit(self)
        self.input.setFixedHeight(30)
        self.input.setStyleSheet("font-family:맑은 고딕;color:black; font-size:20px;")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lb_info1)
        layout.addWidget(self.lb_quiz)
        layout.addWidget(self.lb_info2)
        layout.addWidget(self.input)
        self.resize(650, 200)
        self.setLayout(layout)

        ######################################################
        # 3. enter_key 함수 호출 및 정의
        ######################################################
        self.input.returnPressed.connect(self.enter_key)

        ######################################################
        # 7. 최초 게임 시작 시 동일한 문제가 출제되지 않고 시작시 마다
        # 다르게 출제하게 하기 위해서 초기화(섞어주고)하고, 
        ######################################################
        self.init_quiz()
        self.next_word()

        self.show()

    ######################################################
    # 3. enter_key 함수 호출 및 정의
    ######################################################
    def enter_key(self):
        global current_index, k
        
        if current_index < len(words):
            q = words[current_index]
        else:
            current_index = 0
            q = words[current_index]
        
        user_input = self.input.text()

        if self.rNum == 0 and user_input == self.shuffleKorWords[current_index] \
            or self.rNum == 1 and user_input == words[current_index] :
            
            k = k + 1
            self.lb_info2.setText("정답")
            self.input.setText("")
            current_index = current_index + 1
        else:
            if self.rNum == 0:
                self.lb_info2.setText("오답 <br> 정답은 "+ self.shuffleKorWords[current_index]+"입니다.")
            else:
                self.lb_info2.setText("오답 <br> 정답은 "+ words[current_index]+"입니다.")
            current_index = current_index + 1
            self.input.setText("")

        
        ######################################################
        # 4. 다음 문제 출제 함수 호출 및 실행
        ######################################################
        self.next_word()


    ######################################################
    # 5. 게임 초기화 함수 호출 및 실행
    ######################################################
    def init_quiz(self):
        global k
        random.shuffle(words)
        print(words)
        self.current_index = 0
        k = 0

        self.shuffleEngWords = []
        self.shuffleKorWords = []
        for idx, key in enumerate(words):
            # print("[{}] {} : {}".format(idx, key, Test_English.get(key)))
            self.shuffleEngWords.append(key)
            self.shuffleKorWords.append(Test_English2.get(key))

    ######################################################
    # 4. 다음 문제 출제 함수 호출 및 실행
    ######################################################
    def next_word(self):
        global next_question

        # if self.current_index == 20:
        #     r = "총 문제수: "+str(self.current_index)+"개<br>맞춘 개수: "+str(k)+"개<br>점수: "+str(k/self.current_index * 100)+"점"
        #     self.lb_info2.setText("총 문제수: "+str(self.current_index)+"개<br>맞춘 개수: "+str(k)+"개<br>점수: "+str(k/self.current_index * 100)+"점")
        #     reply = QtWidgets.QMessageBox.question(self, '단어 Test','모든 문제를 출제했습니다.\n다시 하시겠습니까?\n'+r,
        #             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        
        if self.current_index < len(words):
            self.rNum = random.randint(0, 1)
            question = None
            if self.rNum == 0:
                question = self.shuffleEngWords[self.current_index]
            elif self.rNum == 1:
                question = self.shuffleKorWords[self.current_index]
            question = str(self.current_index+1)+". "+question
            if self.current_index + 1 < len(words):
                next_question = words[self.current_index + 1]
            else:
                pass

            self.lb_quiz.setText(question)
            self.current_index = self.current_index + 1
        else:
            r = "총 문제수: "+str(self.current_index)+"개<br>맞춘 개수: "+str(k)+"개<br>점수: "+str(k/self.current_index * 100)+"점"
            self.lb_info2.setText("총 문제수: "+str(self.current_index)+"개<br>맞춘 개수: "+str(k)+"개<br>점수: "+str(k/self.current_index * 100)+"점")
            reply = QtWidgets.QMessageBox.question(self, '단어 Test','모든 문제를 출제했습니다.\n다시 하시겠습니까?\n'+r,
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            # reply.place(x=300,y=300)
            if reply == QtWidgets.QMessageBox.Yes:

                ######################################################
                # 5. 게임 초기화 함수 호출 및 실행
                ######################################################
                self.init_quiz()
                self.next_word()
                self.lb_info2.setText("")
            else:
                exit(0)

######################################################
# 1. 윈도우 창 띄우기
######################################################
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = MyWindow()
    app.exec_()