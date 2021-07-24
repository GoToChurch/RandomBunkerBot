import random

#n = int(input()) Number of players

profs, illness, hobbies, qualities, phobias, dopinfa, packages, katast = [], [], [], [], [], [], [], []
illness_exceptions = [
    'Идеально здоров', 'Слепота', 'Глухонемой',
    'Нет ноги', 'Нет руки', 'Шесть пальцев на руках', 'Нет зубов'
    ]
sex = ['Мужчина','Мужчина','Мужчина','Женщина','Женщина','Женщина','Транс-мужчина','Транс-женщина']
orient = ['Гетеро','Гомо','Би']
information_exceptions = ['Работал 3 года', 'Вырос в семье', 'Проходил курсы']
time, state, food, dops, guests = [], [], [], [], []
chars, land, surr, friend = [], [], [], ['Друг','Враг']
specs = [
    ['Иммунитет на себя (Вас не могут выгнать голосованием на этом ходу)', 'Иммунитет на другого игрока (Выбранного игрока не могут выгнать голосованием на этом ходу)',
     'Снять с себя один голос на голосовании и перекинуть его на другого игрока','Аннулировать один голос против себя на голосовании',
     'Вы решаете кто покинет игру без голосования', 'Аннулировать профессии у всех игроков', 'Уменьшить количетсво мест в бункере на 1', 'Увеличить количетсво мест в бункере на 1'],
    ['Рядом есть - '], ['Бункер находиться на/в - '], ['Смена характеристики у себя - ', 'Смена характеристики у другого игрока - ', 'Поменяться характеристикой с другим игроком - ',
    'Смена характеристики по часовой стрелке - ', 'Смена характеристики против часовой стрелки - ', 'Смена характеристики у всех игроков - ', 'Вскрыть характеристику у другого игрока - '],
    ['Уменьшить процент болезни у себя на ', 'Уменьшить процент болезни у другого игрока на ', 'Увеличить процент болезни у другого игрока - ',],['Слева сидит - ', 'Справа сидит - ']
    ]
dop_specs = []
charachers = [
    'katast', 'time', 'state', 'food', 'dops', 'guests', 'profs','illness', 'hobbies',
    'qualities', 'phobias', 'dopinfa', 'packages', 'chars', 'land', 'surr'
    ]
lists = [
    katast, time, state, food, dops, guests, profs,
    illness, hobbies, qualities, phobias, dopinfa, packages, chars, land, surr
    ]

def filler(n):
    ''' Заполняет списки характеристик из файлов. '''
    for i in range(len(charachers)):
        with open('{}.txt'.format(charachers[i]), 'r', encoding = "utf-8") as file:
            for line in file:
                line = line.strip()
                lists[i].append(line)

def create_catastrophe():
    '''Создает катастофу'''
    return 'Катастрофа: ' + random.choice(katast) + '\n'

def create_bunker():
    '''Создает характеристики бункера'''
    bunker_chels = 'Вместимость бункера - ' + str(int(n/2)) + ' чел.' + '\n'
    bunker_square = 'Площадь бункера - ' + str(random.randrange(50,300, 50)) + ' м2' + '\n'
    bunker_time = 'Время пребывания - ' + random.choice(time) + '\n'
    bunker_state = 'Состояние бункера - ' + random.choice(state) + '\n'
    bunker_food = 'Количество продовольствия - ' + random.choice(food) + '\n'
    bunker_dops = 'Спальные места и всё необходимое для гигиены' + '\n'
    bunker_guests = 'В бункере живут: ' + random.choice(guests) + '\n'
    for i in range(random.randint(0,5)):
        x = random.choice(dops)
        if x not in bunker_dops:
            bunker_dops +=  x + '\n' 
    return [bunker_chels, bunker_square, bunker_time, bunker_state, bunker_food, bunker_dops, bunker_guests]

def create_player_card():
    '''Создает карточки игроков'''
    players_age = random.randint(18,97)
    players_height = random.randint(150,200)
    players_weight = random.randint(50,130)
    illness_stage = random.randrange(10,100,10)
        
    while True:
        players_experience1 = random.randint(0,63)
        players_experience2 = random.randint(0,63)
        uslovie1 = players_age - players_experience1
        uslovie2 = players_age - players_experience2
        if uslovie1 >=18 and uslovie2 >= 14:
            break
        
    players_orient = random.choice(orient)
    player_prof, player_sex = random.choice(profs), random.choice(sex)
    players_prof = f'Profession: {player_prof}; Experience: {players_experience1} year(s)' + '\n'
    players_sex = f'Sex: {player_sex}; Age: {players_age}; Sexual orientation: {players_orient}' +  '\n'
    players_imt = f'Height: {players_height} см; Weight: {players_weight} кг' + '\n'
        
    ill = random.choice(illness)
    if ill in illness_exceptions:
        players_illness = f'Health: {ill}' + '\n'
    elif illness_stage >= 10 and illness_stage <= 30:
        players_illness = f'Health: {ill} в легкой форме - {illness_stage}%' + '\n'
    elif illness_stage > 30 and illness_stage <= 70:
        players_illness = f'Health: {ill} в средней форме - {illness_stage}%' + '\n'
    else:
        players_illness = f'Health: {ill} в тяжелой форме - {illness_stage}%' + '\n'
        
    player_hobby, player_quality, player_phobia = random.choice(hobbies), random.choice(qualities), random.choice(phobias)
    players_hobby = f'Hobby: {player_hobby}; Experience: {players_experience2} year(s)' + '\n'
    players_quality = f'Personal quality: {player_quality}' + '\n'
    players_phobia = f'Phobia: {player_phobia}' + '\n'
        
    inform = random.choice(dopinfa)
    if inform in information_exceptions:
        players_information = f'Additional information: {inform} {player_prof}' + '\n'
    else:
        players_information = f'Additional information: {inform}' + '\n'
       
    player_package = random.choice(packages)
    players_package = f'Baggage: {player_package}' + '\n'
    return [
            players_prof,players_sex, players_imt, players_illness, players_hobby, players_quality,
            players_phobia, players_information, players_package
            ]

def writer(n):
    '''Записывает информацию об игре в файлы'''
    kat = create_catastrophe()
    bunker = create_bunker()
    for i in range(1, n+1):
        player = create_player_card()
        with open(f'player_{i}.txt', 'w') as card:
            card.write(kat)
            card.write('\n')
            
            card.write('Информация о бункере:' + '\n')
            for j in range(len(bunker)):
                card.write(bunker[j])
            card.write('\n')
            
            card.write(f'Player {i}:' + '\n')
            for g in range(len(player)):
                card.write(player[g])
            card.write('\n')
            
            card.write('Специальные условия:' + '\n')
            t, end = 1, 5
            while t != 3:
                nikich = random.randint(0, end)
                player_specs = str(t) + '. ' + random.choice(specs[nikich])
                if nikich == 1:
                    player_specs += random.choice(surr) + '\n'
                elif nikich == 2:
                    player_specs += random.choice(land) + '\n'
                elif nikich == 3:
                    player_specs += random.choice(chars) + '\n'
                elif nikich == 4:
                    player_specs += str(random.randrange(10,100,10)) + '%' + '\n'
                elif nikich == 5:
                    player_specs += random.choice(friend) + '\n'
                    end -= 1
                else:
                    player_specs += '\n'
                if player_specs in dop_specs:
                    t -= 1
                else:
                    dop_specs.append(player_specs)
                    card.write(player_specs)
                t += 1