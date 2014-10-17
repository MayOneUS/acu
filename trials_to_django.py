from VideoQuiz.models import Voter, Code, Quiz
f = open('trials_final.csv')
rows = [row.split(',') for row in f.read().split('\r')]

headers = rows.pop(0)
quiz = Quiz.objects.all()[0]
voters = [(Voter.objects.create(firstName=row[3], lastName=row[5], address=[7]), row) for row in rows]
codes = [Code.objects.create(giftcard_amount=float(voter[1][27][1:]), quiz=quiz, code=voter[1][25], voter=voter[0], charity=True if voter[1][26]=='donation' else False) for voter in voters]

