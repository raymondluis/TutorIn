class User:
    username = None
    _password = None
    name = None
    _email = None
    _userRole = None
    message = None

    def __init__(self,username,password,name,email,userRole):
        self.username = username
        self._password = password
        self.name = name
        self._email = email
        self._userRole = userRole
        self.message = None
        
    def login(self, username,password):
        if (self.username == username) and (self._password == password):
            return True
        else:
            return False

    def verifyAccount(self):
        if (self.username != None) and (self._password != None):
            return True
        else:
            return False

    def forgetPassword(self):
        return self._password

    def changePassword(self, new_pw):
        self._password = new_pw
        return True

class Admin(User):
    def verifyUser(self):
        if (self.username != None) and (self._password != None):
            return True
        else:
            return False

    def solveThreadProblem(self):
        print("Thread solved!")
        return True
    
    def verifyPayment(self):
        print("Payment verified!")
        return True

class Siswa(User):
    _siswaId = None
    angkatan = None
    _nomorHp = None
    _identificationCard = None

    def createAccount(self,siswaId,angkatan,nomorHp,identificationCard):
        self._siswaId = siswaId
        self.angkatan = angkatan
        self._nomorHp = nomorHp
        self._identificationCard = identificationCard

    def bookTutor(self):
        return True

    def sendMessage(self):
        message = chatMessage('test','test','test')
        self.message.sendMessage('test')    

class Tutor(User):
    _tutorId = None
    lastEducation = None
    _nomorHp = None
    _identificationCard = None
    rating = None

    def createAccount(self,tutorId,lastEducation,nomorHp,identificationCard,rating):
        self._tutorId = tutorId
        self.lastEducation = lastEducation
        self._nomorHp = nomorHp
        self._identificationCard = identificationCard
        self.rating = rating
    
    def manageRequest(self):
        return True
    
    def sendMessage(self):
        message = chatMessage('test','test','test')
        self.message.sendMessage('test')


class chatMessage(User):
    _senderName = None
    _receiveName = None
    _datetime = None
    _chatHistory = []

    def __init__(self,senderName,receiveName,datetime):
        self._senderName = senderName
        self._receiveName = receiveName
        self._datetime = datetime
        self._chatHistory = []
        
    def seeMessage(self):
        return self._chatHistory
    
    def sendMessage(self, message):
        self._chatHistory.append(message)
        return self._chatHistory

class tutoringSession:
    _sessionId = None
    _mentorName = None
    _siswaName = None
    _tutoringPeriod = None
    _paymentStatus = None

    def __init__(self,sessionId,mentorName,siswaName):
        self._sessionId = sessionId
        self._mentorName = mentorName
        self._siswaName = siswaName
        self._tutoringPeriod = None
        self._paymentStatus = False

    def bookSchedule(self, date):
        self._tutoringPeriod = date
        return True

class Payment(tutoringSession):
    _mentorFee = None
    _paymentId = None

    def checkOut(self, paymentID, fee):
        self._mentorFee = fee
        self._paymentId = paymentID
        return True

    def verifiedBilling(self):
        if (self._paymentId != None):
            self._paymentStatus = True
        return self._paymentStatus

# nunggu relasi dari tutor ama siswa
class Thread:
    _threadId = None
    threadTag = None
    threadHeader = None
    senderName = None
    replies = []
    
    def createThread(self,threadId,threadTag,threadHeader,senderName):
        self._threadId = threadId
        self.threadTag = threadTag
        self.threadHeader = threadHeader
        self.senderName = senderName
    
    def replyThread(self, reply):
        self.replies.append(reply)
        return True

    def removeThread(self):
        self._threadId = None
        return True

class Post:
    _threadId = None
    text = None

    def writePost(self, text):
        self.text = text
        return True

    def seePost(self):
        return self.text
    
    def deletePost(self):
        self.text = None
        return True
    
    
    
class __main___:
    print("main")
