from django.db import models


class OrderQuerySet(models.QuerySet):
    def paid(self):
        return self.filter(status="Paid")

    def deposit(self):
        return self.filter(status="Deposit")

    def expect(self):
        return self.filter(status="Expect")

    def archived(self):
        return self.filter(status="Archived")

