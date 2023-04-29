import random
class CATDATE():
    global catdata
    global i
    i=-1
    catdata={"Name":[], "Health":[],"Location":[]}
    def catname():
        catname=['Стичь', 'Феликс','Вискас','Гламур','Персик','Пышка','Ванилька','Одуванчик','Пухля','Шпрот']
        cat=random.choice(catname)
        print('\n Кличка котенка:', cat)
        return cat
    def kitty(cat):

        while True:
            try:
                health=random.randint(1,11)
                if (health>=1) and(health<=10):break
                else: raise ValueError
            except ValueError:
                print("\n Значения только от 1 до 10")
        print('\n Состояние котенка (1 ужасно, а 10 здоров) ',cat,':',health)
        return health
    def location(cat, health):
        catloc=['Канализация','Парк','Библиотека','Озеро','Мусорка','Ферма Колбас','Набережная']
        place=random.choice(catloc)
        print('\n Местоположение котенка ',cat,' с состоянием ', health,':',place)
        return place
    def catinput():
        global i
        i+=1
        catdata.get("Name").append(CATDATE.catname())
        catdata.get("Health").append(CATDATE.kitty(catdata.get("Name")[i]))
        catdata.get("Location").append(CATDATE.location(catdata.get("Name")[i],catdata.get("Health")[i]))
        return 
    
class VETDATE():
    global j
    j=-1
    global vetdata
    vetdata={"Vet":[], "Busy":[]}
    def volunteer():

        namevet=['А. Ф. Журавлев','К. Т. Ильин','А. Б. Белова','Ц.В. Волков','Г. Д. Бабушкина','А.С. Пушкин','А. Ю. Смирнова']
        who=random.choice(namevet)
        print("\n Ветеринар:",who)
        return who
    def employment(who):
        while True:
            bus=''
            randBits = bool(random.getrandbits(1))
            if randBits:
                bus='занят'
            else:
                bus='свободен'
            print('\n',who,' состояние занятости(свободен или занят):',bus)
            if bus=='занят':
                break
            elif bus=='свободен':
                break
            else:
                print('\n Только свободен или занят')

        return bus
    def nobus():
        global vetdata
        for i in range(len(vetdata.get("Vet"))):
            if vetdata.get("Busy")[i]=='занят':
                vetdata.get("Busy")[i]='свободен'
                print('\n/////////////////')
                print('\n',vetdata.get("Vet")[i],' теперь:',vetdata.get("Busy")[i])
                print('\n/////////////////')
                break
        return
                
        
        
    def vetinput():
        global j
        j+=1
        vetdata.get("Vet").append(VETDATE.volunteer())
        vetdata.get("Busy").append(VETDATE.employment(vetdata.get("Vet")[j]))
        return
class treatment():
    global vetdata, catdata
    global j1,i1
    def svoboda(vetdata):
        global j1
        for c in range(len(vetdata.get("Vet"))):
            if vetdata.get("Busy")[c]=='свободен':
                j1=c
                break
        if vetdata.get("Busy")[j1]=='занят':
            print('\n Нет свободных ветеринаров')
            return VETDATE.vetinput()
        else:
            return j1
    def badcat(catdata):
        global i1
        buble=100
        for d in range(len(catdata.get("Name"))):
            if buble>(catdata.get("Health")[d]):
                buble=catdata.get("Health")[d]
                i1=d
        if catdata.get("Health")[i1]==10:
            print('\n Нет больных котят')
            return CATDATE.catinput()           
        else:
            return i1
    def gear():
        global vetdata, catdata
        global i1,j1
        try:
            j1=treatment.svoboda(vetdata)
            i1=treatment.badcat(catdata)
            return treatment. cure(vetdata.get("Vet")[j1],catdata.get("Name")[i1],catdata.get("Health")[i1],catdata.get("Location")[i1])
        except Exception:
            return
    def cure(who, cat, health, place ):
        print('\n','Ветеринар ', who,' лечит котенка ',cat,' с состоянием здоровья ',health,' в месте ',place, '.')
        vetdata.get("Busy")[j1]='занят'
        catdata.get("Health")[i1]=10

        return treatment.result()
    def result():
        print('\n Котенок здоров!')
        return
class menu():
    def m():
        a=100
        while a!=0:
            print('0. Выход. ')
            print('1. Ввести данные котенка. ')
            print('2. Ввести данные ветеринара. ')
            print('3. Лечение котенка')
            try:
                a=int(input())

            except ValueError:
                print("Такой команды не существует.")
                a=100
            if a==1:
                CATDATE.catinput()
            if a==2:
                VETDATE.vetinput()
            if a==3:
                try:
                    treatment.gear()
                except:
                    print('Сначала необходимо ввести данные')
                
