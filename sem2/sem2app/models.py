from django.db import models
from django.utils import timezone


class Onehed (models.Model):
    rest_time = models.DateTimeField(default= timezone.now)
    res = models.BooleanField(default=False)

    @staticmethod
    def statistic(n):
        dict_res = {"OREL":0,"RESHKA":0}
        query = Onehed.objects.all()
        list_res = query[-n:]
        for item in list_res:
            if item.res:
                dict_res["OREL"] += 1
            else:
                dict_res["RESHKA"] += 1

        return dict_res

    def __str__(self):
        return  f'time:{self.rest_time}, res:{self.res}'
