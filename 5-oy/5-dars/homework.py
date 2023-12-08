# Bank yoki Davlat xizmatlari markazi kabi tashkilotlarning navbat turish dasturining algoritmini shakillantirish. 
# classdan foydalanib ushbu class quyidagicha ishlarni amalga oshirsin 
# -smen ochish - navbat olish - xizmat ko`rsatish - navbat qaysi mijozga tegishlik ekanligini ko`rish - xodimni baholash, baho, izoh - smen yopish. 
# har bir smenga teishlik ma`lumotlarni classda saqlash 
# 1) necha nafar mijozga xizmat ko`rsatilingani 2) smen id raqami 3) o`rtacha baho 4) izohlar (har bir yozgan class va methodlarningizga comment yozing)

import json

class BankQueue:

    """
    Navbaat turish dasturi uchun yozilgan klass.
    Methods: open_smen,service,employee,feedback,get_queue,close_queue
    properties: customers,smen_id,avg_grade,grades,comments,opened 
    """

    __id = 0
    customers = 0 # enjoyed the service overall(xizmatdan umumiy foydalanilganlar)
    smen_id = 0 # identifier for shift identification(smenani aniqlash uchun id)
    opened = False # shift status(status holati)

    grades = [] # grades(baholar)
    comments = [] # comments(izohlar)
    queues = [] # Queues(Navbatlarni saqlab turish uchun list)
    data = [] # info after closing the shift(xizmat yopilgandan keyin chiqariladigan info)
    
    avg_grade = 0 # avarage grade(o`rtacha baho)
    

    def __init__(self):

        """Mijozlarni yozib olish uchun constructor"""
        
        BankQueue.__id += 1
        BankQueue.customers += 1
        self.id = BankQueue.__id
        self.service_being = False


    @classmethod
    def open_smen(cls):

        """Smen ochish uchun method."""

        if not cls.opened:
            cls.grades.clear()
            cls.customers = 0
            cls.smen_id += 1
            cls.avg_grade = 0
            cls.comments = []
            print('-'*100)
            print(f'#{cls.smen_id} xizmat ochildi.')
            print('-'*100)
            cls.opened = True
        else:
            print('-'*100)
            print('Xizmat oldin ochilgan')
            print('-'*100)


    def get_queue(self):

        """Navbat olish uchun method"""
        if BankQueue.opened:
            if self.id not in BankQueue.queues:
                BankQueue.queues.append(self.id)
                print('-'*100)
                print(f'Navbatlar: {BankQueue.queues}')
                print('-'*100)
            else:
                print('-'*100)
                print(f'Siz navbatga yozilgansiz. Sizning navbatingiz: {BankQueue.queues.index(self.id)+1}')
                print('-'*100)
        else:
            print('-'*100)
            print('Xali xizmat ochilmadi. BankQueue.open_smen() methodni ishlating.')
            print('-'*100)


    def service(self):

        """Xizmat ko`rsatish uchun method"""

        if self.id in BankQueue.queues:
            if BankQueue.queues[0] == self.id:
                self.service_being = True
                print('-'*100)
                print(f'Biz id = {self.id} raqamli mijozga xizmat ko`rsatayapmiz.')
                print('Xizmat ko`rsatib bo`ldik.')
                BankQueue.queues.pop(BankQueue.queues.index(self.id))
                print(f'feedback() methodi bilan baho hamda comment qoldirishingiz mumkin.')
                print('-'*100)
            else:
                print('-'*100)
                print(f'Sizning navbatingiz hali kelmadi. Sizning navbatingiz {BankQueue.queues.index(self.id)+1}')
                print('-'*100)
        else:
            print('-'*100)
            print('Siz hali navbat olmadingiz. get_queue() methodi orqali navbat olishingiz mumkin.')
            print('-'*100)


    def feedback(self,grade,comment):

        """Baholash uchun method"""

        if isinstance(grade,(float,int)) and 1 <= grade <= 5:
            if self.service_being:
                BankQueue.comments.append(comment)
                BankQueue.grades.append(grade)
                print('-'*100)
                print(f'Sizning {grade} baho va "{comment}" commentingiz qo`shildi.')
                print('-'*100)
            else:
                print('-'*100)
                print('Siz servicedan foydalanmadingiz. service() methodi orqali xizmatimizdan foydalanishingiz mumkin.')
                print('-'*100)
        else:
            print('-'*100)
            print('Qo`yayotgan bahoyingiz haqiqiy son bo`lishi kerak.')
            print('-'*100)


   
    @classmethod
    def close_queue(cls):

        """Smenni yopish uchun method"""

        if cls.opened:
            print('-'*100)
            print(f'#{cls.smen_id} xizmat yopildi.')
            print('-'*100)
            cls.calc()
            cls.opened = False
        else:
            print('-'*100)
            print('Xizmat hali ochilmadi')
            print('-'*100)


    @staticmethod
    def calc():

        """Hisob kitoblar uchun method"""
        
        if BankQueue.grades:
            BankQueue.avg_grade = sum(BankQueue.grades)/len(BankQueue.grades)
        BankQueue.data.append({
            'smena':BankQueue.smen_id,
            'Mijozlar':BankQueue.customers,
            'o`rtacha baho':BankQueue.avg_grade,
            'izohlar':BankQueue.comments
            })
    

    @classmethod
    def info(cls):

        """Smena tugatilgandan keyingi info"""

        if not cls.opened:
            for d in cls.data:
                print(f"{d['smena']} smena haqida ma`lumot")
                pretty_json = json.dumps(d, indent=4)
                print('-'*100)
                print(pretty_json)
                print('-'*100)
        else:
            print('-'*100)
            print('Xizmatimiz haqidagi ma`lumotlar to`liq bo`lishi uchun shu smena yopilishini kuting.\nKeyin xizmat haqidagi infoni olishingiz mumkin.')
            print('-'*100)
    

    @staticmethod
    def queue():
        print('-'*100)
        print(f'Ayni vaqtdagi navbatlar ko`rsatgichi: {BankQueue.queues}')
        print('-'*100)
