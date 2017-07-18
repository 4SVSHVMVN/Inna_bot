#!/usr/bin/env python
# -*- coding: utf-8
from datetime import datetime, timedelta
now = datetime.now()
startdate = datetime(1900, 1, 1)


def ChinaGor(days):
	bdate = startdate + timedelta(days=days - 1)
	year = bdate.year
	arrZodiakKitay = ["Крыса", "Бык", "Тигр", "Кролик", "Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья"]
	if year % 12 == 4:
		zodiakKitay = arrZodiakKitay[0]
	elif year % 12 == 5:
		zodiakKitay = arrZodiakKitay[1]
	elif year % 12 == 6:
		zodiakKitay = arrZodiakKitay[2]
	elif year % 12 == 7:
		zodiakKitay = arrZodiakKitay[3]
	elif year % 12 == 8:
		zodiakKitay = arrZodiakKitay[4]
	elif year % 12 == 9:
		zodiakKitay = arrZodiakKitay[5]
	elif year % 12 == 10:
		zodiakKitay = arrZodiakKitay[6]
	elif year % 12 == 11:
		zodiakKitay = arrZodiakKitay[7]
	elif year % 12 == 0:
		zodiakKitay = arrZodiakKitay[8]
	elif year % 12 == 1:
		zodiakKitay = arrZodiakKitay[9]
	elif year % 12 == 2:
		zodiakKitay = arrZodiakKitay[10]
	elif year % 12 == 3:
		zodiakKitay = arrZodiakKitay[11]
	msg = "Восточный календарь: "
	msg += zodiakKitay
	msg += "\n"
	return msg


def gor(days):
	bdate = startdate + timedelta(days=days - 1)
	month = bdate.month
	day = bdate.day
	arrZodiak = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]
	if (month == 3 and day > 20) or (month == 4 and day < 19):
		zodiak = arrZodiak[0]
	if (month == 4 and day > 20) or (month == 5 and day < 19):
		zodiak = arrZodiak[1]
	if (month == 5 and day > 20) or (month == 6 and day < 20):
		zodiak = arrZodiak[2]
	if (month == 6 and day > 21) or (month == 7 and day < 21):
		zodiak = arrZodiak[3]
	if (month == 7 and day > 22) or (month == 8 and day < 22):
		zodiak = arrZodiak[4]
	if (month == 8 and day > 23) or (month == 9 and day < 22):
		zodiak = arrZodiak[5]
	if (month == 9 and day > 23) or (month == 10 and day < 21):
		zodiak = arrZodiak[6]
	if (month == 10 and day > 22) or (month == 11 and day < 21):
		zodiak = arrZodiak[7]
	if (month == 11 and day > 22) or (month == 12 and day < 20):
		zodiak = arrZodiak[8]
	if (month == 12 and day > 21) or (month == 1 and day < 19):
		zodiak = arrZodiak[9]
	if (month == 1 and day > 20) or (month == 2 and day < 18):
		zodiak = arrZodiak[10]
	if (month == 2 and day > 19) or (month == 3 and day < 19):
		zodiak = arrZodiak[11]
	msg = "Знак зодиака: "
	msg += zodiak
	msg += "\n"
	return msg


def vozr(days):
	bdate = startdate + timedelta(days=days - 1)
	age = datetime.today() - bdate
	vozrast = int(age.days // 365.2425)
	year = vozrast
	if year % 10 == 0 or year % 10 > 4 and year % 10 < 20:
		 scl = " лет"
	elif year % 10 == 1:
		 scl = " год"
	else:
		scl = " года"
	msg = "Возраст: "
	msg += str(vozrast)
	msg += scl
	msg += "\n"
	return msg


def hello():
	print ("hello")


def check(inn):
	if len(inn) != 10:
		return False
	inn = [inn[0], inn[1], inn[2], inn[3], inn[4], inn[5], inn[6], inn[7], inn[8], inn[9]]
	for i in range(len(inn)):
		inn[i] = int(inn[i])

	s = inn[0]*(-1)+inn[1]*5+inn[2]*7+inn[3]*9+inn[4]*4+inn[5]*6+inn[6]*10+inn[7]*5+inn[8]*7
	p = s // 11
	p = s - (11 * p)
	if p > 9:
		p = p // 10
	if p == inn[9]:
		return True
	else:
		return False


def info(inn):
	inn = [inn[0], inn[1], inn[2], inn[3], inn[4], inn[5], inn[6], inn[7], inn[8], inn[9]]
	days = inn[0] + inn[1] + inn[2] + inn[3] + inn[4]
	nn0 = inn[5] + inn[6] + inn[7] + inn[8]
	for i in range(len(inn)):
		inn[i] = int(inn[i])
	if inn[0] != 8:
		days = int(days)
		msg = ""
		bdate = startdate + timedelta(days=days - 1)
		week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
		nmonth = ["", "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
		birth_date = bdate.day, nmonth[bdate.month], bdate.year, week[bdate.weekday()]
		msg += ("Дата рождения: ")
		msg += (" ".join(map(str, birth_date)))
		msg += ("\n")
		if inn[8] % 2 == 0:
			deadline = 0
			msg += ("Пол: Женский \n")
		else:
			deadline = 1
			msg += ("Пол: Мужской \n")
		msg += vozr(days)
		msg += gor(days)
		msg += ChinaGor(days)
		age = datetime.today() - bdate
		if deadline == 0:
			death = now.year + 75 - int(age.days // 365.2425)
			msg += "Примерная дата смерти:	"
			msg += str(death)
			msg += " год \n"
		else:
			death = now.year + 65 - int(age.days // 365.2425)
			msg += "Примерная дата смерти:	"
			msg += str(death)
			msg += " год \n"
		msg += "Порядковый номер: "
		msg += str(nn0)
		msg += "\n"
	else:
		msg = "Дата рождения: Информация скрыта \n"
		if inn[8] % 2 == 0:
		   msg += "Пол: Женский \n"
		else:
			msg += "Пол: Мужской \n"
			msg += "Порядковый номер: "
			msg += nn0
	return msg
