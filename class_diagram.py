class User:
    username = None
    _password = None
    name = None
    _email = None
    _userRole = None

    def __init__(self,username,password,name,email,userRole):
        self.username = username
        self._password = password
        self.name = name
        self._email = email
        self._userRole = userRole
    def login(username,password):
        # check if credentials is 
        return True

    def verifyAccount():
        return True

    def forgetPassword():
        return True

    def changePassword():
        return True

class Admin(User):
    
    
    def verifyUser():
        return True

    def solveThreadProblem():
        return True
    
    def verifyPayment():
        return True

class Siswa(User):
    _siswaId = None
    angkatan = None
    _nomorHp = None
    _identificationCard = None

    def createAccount(self,siswaId,angkata,nomorHp,identificationCard):
        self._siswaId = siswaId
        self.angkatan = angkatan
        self._nomorHp = nomorHp
        self._identificationCard = identificationCard

    def bookTutor():
        return True
    
    def checkOut():
        return True

    def sendMessage():
        message = chatMessage('test','test','test','test')
        message.sendMessage(message)    

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
    
    def manageRequest():
        return True
    
    def sendMessage():
        message = chatMessage('test','test','test','test')
        message.sendMessage(message)


class chatMessage:
    _senderName = None
    _receiveName = None
    _datetime = None
    _chatHistory = None

    def __init__(self,senderName,receiveName,datetime,chatHistory):
        self._senderName = senderName
        self._receiveName = receiveName
        self._datetime = datetime
        self._chatHistory = chatHistory

    def seeMessage():
        return True
    
    def sendMessage(message):
        return message

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

    def bookSchedule(date):
        return True
    
    def tutoringSession():
        return True

class Payment(tutoringSession):
    _mentorFee = None
    _payerName = None
    _paymentId = None

    def checkOut():
        return True

    def verifiedBilling():
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
    
    def replyThread():
        return True
    def replyThread():
        return True
    def removeThread():
        return True

class Post:
    _threadId = None
    text = None

    def writePost():
        return True

    def seePost():
        return True
    
    def deletePost():
        return True
        