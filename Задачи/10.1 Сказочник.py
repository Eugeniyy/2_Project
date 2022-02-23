# Сказочник. Задача

from tkinter import *
import random

class Application(Frame):
    """ Основной класс при работе с окном. """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ Основные элементы окна. """
        Label(self,
            text = "Программа создает случайный рассказ."
            ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        Label(self,
            text = "Введите имя персонажа:"
            ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)
        Label(self,
            text = "Введите лучшее качество:"
            ).grid(row = 2, column = 0, sticky = W)
        self.quality_ent = Entry(self)
        self.quality_ent.grid(row = 2, column = 1, sticky = W)
        Label(self,
            text = "Введите глагол:"
            ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
        Label(self,
            text = "Введите существительно в мн.ч.:"
            ).grid(row = 4, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 4, column = 1, sticky = W)
        Label(self,
            text = "Выберите один из вариантов:"
            ).grid(row = 6, column = 0, sticky = W)
        Label(self,
            text = "Прилагательные:"
            ).grid(row = 7, column = 0, sticky = W)
        self.adjective = StringVar()
        self.adjective.set(None)
        column = 1
        ADJECTIVES = ["яростный", "тихий", "благородный"]
        for word in ADJECTIVES:
            Radiobutton(self,
                text = word,
                variable = self.adjective,
                value = word
                ).grid(row = 7, column = column, sticky = W)
            column += 1
        Label(self,
            text = "Активный навык:"
            ).grid(row = 8, column = 0, sticky = W)
        self.skill = StringVar()
        self.skill.set(None)
        column = 1
        A_SKILLS = ["сокрушающий удар", "выстрел", "кувырок"]
        for word in A_SKILLS:
            Radiobutton(self,
                text = word,
                variable = self.skill,
                value = word
                ).grid(row = 8, column = column, sticky = W)
            column += 1
        Label(self,
            text = "Пассивный навык:"
            ).grid(row = 9, column = 0, sticky = W)
        self.is_blessing = BooleanVar()
        self.is_ench_weapons = BooleanVar()
        self.is_quick_reflexes = BooleanVar()
        column = 1
        P_SKILLS = ["благословление", "зачарованное оружие", "быстрая реакция"]
        for word in P_SKILLS:
            if word == "благословление":
                Checkbutton(self,
                    text = word,
                    variable = self.is_blessing
                    ).grid(row = 9, column = column, sticky = W)
                column += 1
            elif word == "зачарованное оружие":
                Checkbutton(self,
                    text = word,
                    variable = self.is_ench_weapons
                    ).grid(row = 9, column = column, sticky = W)
                column += 1
            else:
                Checkbutton(self,
                    text = word,
                    variable = self.is_quick_reflexes
                    ).grid(row = 9, column = column, sticky = W)
        Button(self,
            text = "Получить рассказ",
            command = self.tell_story
            ).grid(row = 10, column = 0, sticky = W)
        self.text_story = Text(self, width = 100, height = 18, wrap = WORD)
        self.text_story.grid(row = 11, column = 0, columnspan = 5)
    def tell_story(self):
        """ Создаем рассказ. """
        person = self.person_ent.get()
        quality = self.quality_ent.get()
        verb = self.verb_ent.get()
        noun = self.noun_ent.get()
        ajec = self.adjective.get()
        ability = self.skill.get()
        story = ""
        value_random_one = random.randint(0, 2)
        value_random_two = random.randint(0, 2)
        if value_random_one == 0:
            story += "  Это рассказ про великого война. "
        elif value_random_one == 1:
            story += "  Мало кто знал про его скрытый клинок. Те, кто его видел, уже не могли рассказать о его способностях. "
        else:
            story += "  Во всей округе не сыскать такого же благородного человека, как тот, о котором пойдет сей рассказ. "
        story += "Известен он был под именем " + person + ". "
        if value_random_two == 0:
            story += "Ничто не предвещало беды, но на деревню, где рос герой напали враги. "
        elif value_random_two == 1:
            story += "Как то раз наш герой решил разобраться с разбойниками, что поселились неподалёку и угражали городу. "
        else:
            story += "Уже 7 лет шла война между страной, где располагалсь его деревня и неприятелем. Часто стычки случались совсем неподалеку. Эта история об одной такой битве. "
        story += "И " + person + " решил действовать решительно. "
        story += "Не раз " + quality + " мог(-ла) его выручить. Он тренировался каждый день, чтобы достичь совершенства. "
        if value_random_one == 0:
            story += "Так как наш герой был великим войном, ему не составило труда ворваться в строй врага. "
        if value_random_one == 1:
            story += "Невероятные скрытные способности нашего героя позволили ему проникнуть в тыл врага. "
        else:
            story += "Наш благородный герой собрал лучших войнов деревни. Вместе они смогли пробиться в ряды врагов. "
        story += "В этот раз " + ajec + " нрав не смог спасти. "
        story += "Шансов на победу не было изначально, врагов было больше тысячи. "
        story += "Но неожиданно для всех в бой вступила третья сторона. Это были " + noun + ". "
        story += "Все, что оставалось герою, это " + verb + ". Неожиданно для всех " + noun + " превосходили силу всех, кто был на поле боя. "
        if value_random_two == 0:
            story += "Ополчение деревни решило отступить. Но наш герой был не такой. Он остался биться до конца с обеими сторонами. "
        if value_random_two == 1:
            story += "Разбойники трезво оценили ситуацию и решили отступить. Героя окружили " + noun + ". "
        else:
            story += "Никто не собирался уступать. Ведь на кону была жизнь родных. "
        story += "Герой совершает последний " + ability + ". И получает сильное ранение от неприятеля. "
        if self.is_ench_weapons.get():
            story += "Зачарованное оружие героя помогло проредить войска врагов. "
        else:
            story += "Обычным оружием наш герой не смог убить достаточно врагов. "
        if self.is_quick_reflexes.get():
            story += "Благодаря быстрой реакции он смог ещё долго избегать атаки противников. "
        else:
            story += "Не имея быстрой реакции ему пришлось туго. Он получал и блокировал удар за ударом. "
        if self.is_blessing.get():
            story += "Один из врагов применил нечестный приём и " + person + " был отравлен. Только благословление помогло ему выжить. "
        else:
            story += "Отравленная стрела попала в героя. Не имея благословления, он чудом смог избежать мгновенной смерти. "
        if self.is_blessing.get() or self.is_quick_reflexes.get():
            story += "Из последних сил он покидает поле боя. Битва была неравной, но он сделал всё, что мог. "
        else:
            story += "Израненный и отравленный герой падает на землю. Выпускает из рук свое оружие. И делает последний вдох духа непрекращающейся битвы."
        story += "\n  Бой был проигран. Но деревня будет в безопасности ещё долгое время. Враг ещё не скоро восстановит силы, чтобы напасть снова."
        self.text_story.delete(0.0, END)
        self.text_story.insert(0.0, story)

# основная часть
root = Tk()
root.title("Сказочник")
app = Application(root)
root.mainloop()