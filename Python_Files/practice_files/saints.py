class Saint:

    def __init__(self, name, attribute, patron_of, home, feast_day, manner_of_death ):
        self.name = name
        self.attribute = attribute
        self.patron_of = patron_of
        self.home = home
        self.feast_day = feast_day
        self.manner_of_death = manner_of_death

    def story(self):
        print(self.name + "whose feast day is " + self.feast_day +
              ", is the patron saint of " + self.patron_of +
              " and is often seen carrying a " + self.attribute + ".")


    def origin(self):
        print(self.name + "'s church is in " + self.home + ".")

    def celebrate(self):
        print(self.name + "'feast day is on " + self.feast_day + ".")

    def carrying(self):
        print(self.name + " is often seen carrying a " + self.attribute + ".")

saint1 = Saint("Joan of Arc",
               "sword",
               "soldiers",
               "Orleans",
               "May 30",
               "burned at the stake")

saint2 = Saint("Thomas Aquinas",
               "pen",
               "students",
               "Toulouse ",
               "January 28",
               "keeled over while delivering a sermon")


saint3 = Saint("Sebastian",
               "arrow",
               "athletes",
               "Rome ",
               "January 20",
               "beaten to death with clubs")



saint1.celebrate()
saint2.celebrate()
saint3.celebrate()
saint1.origin()
saint2.origin()
saint3.origin()
saint1.carrying()
saint1.story()
