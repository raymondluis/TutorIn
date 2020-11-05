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
        # check if credentials is 
        return True

    def verifyAccount(self):
        return True

    def forgetPassword(self):
        return True

    def changePassword(self):
        return True

class Admin(User):
    def verifyUser(self):
        return True

    def solveThreadProblem(self):
        return True
    
    def verifyPayment(self):
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
    
    def checkOut(self):
        return True

    def sendMessage(self):
        message = chatMessage('test','test','test','test')
        self.message.sendMessage(message)    

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
        message = chatMessage('test','test','test','test')
        self.message.sendMessage(message)


class chatMessage(User):
    _senderName = None
    _receiveName = None
    _datetime = None
    _chatHistory = None

    def __init__(self,senderName,receiveName,datetime,chatHistory):
        self._senderName = senderName
        self._receiveName = receiveName
        self._datetime = datetime
        self._chatHistory = chatHistory

    def seeMessage(self):
        return True
    
    def sendMessage(self):
        return self.message

class tutoringSession:
    _sessionId = None
    _mentorName = None
    _siswaName = None
    _tutoringPeriod = None
    _paymentStatus = None

    def __init__(self,sessionId,mentorName,siswaName,tutoringPeriod,paymentStatus):
        self._sessionId = sessionId
        self._mentorName = mentorName
        self._siswaName = siswaName
        self._tutoringPeriod = tutoringPeriod
        self._paymentStatus = paymentStatus

    def bookSchedule(self, date):
        return True
    
    def tutoringSession(self):
        return True

class Payment(tutoringSession):
    _mentorFee = None
    _payerName = None
    _paymentId = None

    def checkOut(self):
        return True

    def verifiedBilling(self):
        return True

# nunggu relasi dari tutor ama siswa
class Thread:
    _threadId = None
    threadTag = None
    threadHeader = None
    senderName = None
    
    def createThread(self,threadId,threadTag,threadHeader,senderName):
        self._threadId = threadId
        self.threadTag = threadTag
        self.threadHeader = threadHeader
        self.senderName = senderName
    
    def replyThread(self):
        return True

    def removeThread(self):
        return True

class Post:
    _threadId = None
    text = None

    def writePost(self):
        return True

    def seePost(self):
        return True
    
    def deletePost(self):
        return True
        