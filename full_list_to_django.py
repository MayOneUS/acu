from VideoQuiz.models import Voter, Code, Quiz
f = open('list_for_second_mailing_with_codes.csv')
rows = [row.split(',') for row in f.read().split('\r')]

headers = rows.pop(0)
quiz = Quiz.objects.all()[0]
voters = [(Voter.objects.create(firstName=row[3], lastName=row[5], address=[7]), row) for row in rows]
for voter in voters:
    print "code: " + voter[1][26]
    Code.objects.create(giftcard_amount=float(voter[1][25]), quiz=quiz, code=voter[1][26], voter=voter[0], charity=True if voter[1][24]=='donation' else False)

