from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Computer(models.Model):
	DESIGNATION_CHOICES=(
	('Dir', 'Director'),		
	('D', 'Developer'),
	('HR', 'Manager'),
	('P', 'Peon'),
	('SG', 'Security Guard'),
	('SW', 'Sweeper'),	
	)
	
	WORK_PROFILES = (
	('C++', 'C++'),
	('PHP', 'PHP'),
	('JAVA','Core Java'),
	('C#', 'C#'),
	('PY', 'Python'),
	('Non', 'None'),
	)
	name = models.CharField(max_length = 20)
	designation = models.CharField(max_length = 50, choices = DESIGNATION_CHOICES)
	work_profile = models.CharField(max_length =50, choices = WORK_PROFILES)
	salary = models.IntegerField(default = 10)
	address = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name


class Attendence(models.Model):

	name = models.CharField(max_length = 20)
	day1 = models.CharField(max_length = 5)
	day2 = models.CharField(max_length = 5)
	day3 = models.CharField(max_length = 5)
	day4 = models.CharField(max_length = 5)
	day5 = models.CharField(max_length = 5)
	day6 = models.CharField(max_length = 5)
	day7 = models.CharField(max_length = 5)
	day8 = models.CharField(max_length = 5)
	day9 = models.CharField(max_length = 5)
	day10 = models.CharField(max_length = 5)
	day11 = models.CharField(max_length = 5)
	day12 = models.CharField(max_length = 5)
	day13 = models.CharField(max_length = 5)
	day14 = models.CharField(max_length = 5)
	day15 = models.CharField(max_length = 5)
	day16 = models.CharField(max_length = 5)
	day17 = models.CharField(max_length = 5)
	day18 = models.CharField(max_length = 5)
	day19 = models.CharField(max_length = 5)
	day20 = models.CharField(max_length = 5)
	day21 = models.CharField(max_length = 5)
	day22 = models.CharField(max_length = 5)
	day23 = models.CharField(max_length = 5)
	day24 = models.CharField(max_length = 5)
	day25 = models.CharField(max_length = 5)
	day26 = models.CharField(max_length = 5)
	day27 = models.CharField(max_length = 5)
	day28 = models.CharField(max_length = 5)
	day29 = models.CharField(max_length = 5)
	day30 = models.CharField(max_length = 5)
	day31 = models.CharField(max_length = 5)

	def __unicode__(self):
		return self.name
