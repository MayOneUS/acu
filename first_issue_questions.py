__author__ = 'daniel'


from VideoQuiz.models import Quiz, Question, Answer, Code, Voter, Store

quiz = Quiz.objects.create(name="First Issue", video_url='http://www.youtube.com/embed/xnRpMQvW_ow')
q1 = Question.objects.create(quiz=quiz, question="When an individual has incentives that work against their professional responsibilities, this is often called a _______.")
Answer.objects.create(question=q1, answer="Free Market")
Answer.objects.create(question=q1, answer="Fundamental Error")
Answer.objects.create(question=q1, answer="Conflict of Interest", correct=True)
Answer.objects.create(question=q1, answer="System Failure")

q2 = Question.objects.create(quiz=quiz, question="True or False: Conflicts of interest can be found frequently in society")
Answer.objects.create(question=q2, answer="True", correct=True)
Answer.objects.create(question=q2, answer="False")

q3 = Question.objects.create(quiz=quiz, question="When a doctor is seeking the right treatment for a patient, which of these factors would most likely become a conflict of interest?")
Answer.objects.create(question=q3, answer="Patient's medical history")
Answer.objects.create(question=q3, answer="A medicine company sending a doctor on a nice buisness trip", correct=True)
Answer.objects.create(question=q3, answer="Doctor's salary increasing with years in the business")
Answer.objects.create(question=q3, answer="Patient grew up in the same state as the doctor")

q4 = Question.objects.create(quiz=quiz, question="Which of these is a clear conflict of interest when someone is buying a home?")
Answer.objects.create(question=q4, answer="The real estate agent represents both the buyer and the seller", correct=True)
Answer.objects.create(question=q4, answer="The buyers know the person selling the house personally")
Answer.objects.create(question=q4, answer="The two different real estate agents represent the buyer and the seller")
Answer.objects.create(question=q4, answer="The real estate agent for the buyer is also on the school committee.")

q5 = Question.objects.create(quiz=quiz, question="Which of these helps to reduce conflicts of interest?")
Answer.objects.create(question=q5, answer="Codes of conduct")
Answer.objects.create(question=q5, answer="Respect customers or clients perspective")
Answer.objects.create(question=q5, answer="Consulting more experienced or trustworthy people")
Answer.objects.create(question=q5, answer="All of the above", correct=True)

q6 = Question.objects.create(quiz=quiz, question="Which professor is likely to design the least challenging class? A professor promoted on. . .")
Answer.objects.create(question=q6, answer="The content of the syllabus.")
Answer.objects.create(question=q6, answer="The opinions of the faculty")
Answer.objects.create(question=q6, answer="The knowledge of their field")
Answer.objects.create(question=q6, answer="The opinions of the students", correct=True)

Store.objects.create(name="Target", image_url="/static/images/giftcardimages/Target.jpg")
Store.objects.create(name="Walmart", image_url="/static/images/giftcardimages/walmart.jpg")
Store.objects.create(name="Netflix", image_url="/static/images/giftcardimages/netflix.jpeg")
Store.objects.create(name="Ebay", image_url="/static/images/giftcardimages/ebay.jpeg")
Store.objects.create(name="Best Buy", image_url="/static/images/giftcardimages/bestbuy.jpeg")
Store.objects.create(name="Amazon", image_url="/static/images/giftcardimages/amazon.jpeg")
Store.objects.create(name="Kohl's", image_url="/static/images/giftcardimages/Kohls-Gift-Card.png")


james = Voter.objects.create(firstName='james', lastName='madison', address='america')
code = Code.objects.create(code='testcode', voter=james, quiz=quiz)
