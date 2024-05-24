import datetime


class SuperDate(datetime.datetime):
    def get_season(self):
        m = self.month
        # print('номер месяца:', m)
        season = m % 12 // 3 + 1
        if season == 1:
            print("Winter")
        if season == 2:
            print("Spring")
        if season == 3:
            print("Summer")
        if season == 4:
            print("Autumn")
        return

    def get_time_of_day(self):
        c = self.hour
        if 6 <= c < 12:
            print("Morning")
        if 12 <= c < 18:
            print("Day")
        if 18 <= c < 24:
            print("Evening")
        if 0 <= c < 6:
            print("Night")
        return


a = (SuperDate(2024, 2, 22, 12))
a.get_season()
a.get_time_of_day()
