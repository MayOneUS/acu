__author__ = 'daniel'


from VideoQuiz.models import Quiz, Question, Answer, Code, Voter, Store

quiz = Quiz.objects.create(name="First Issue", video_url='https://www.youtube.com/watch?v=KoS-CNYcTlY')
q1 = Question.objects.create(quiz=quiz, question="Today, politicans spend as much as what percentage of their time on fundraising?")
Answer.objects.create(question=q1, answer="10%")
Answer.objects.create(question=q1, answer="30%")
Answer.objects.create(question=q1, answer="50%")
Answer.objects.create(question=q1, answer="70%", correct=True)
Answer.objects.create(question=q1, answer="80%")
q2 = Question.objects.create(quiz=quiz, question="Instead of spending their time fundraising, what should politicians do in a democracy that functions as our founders designed?")
Answer.objects.create(question=q2, answer="Maintain an immaculate head of hair")
Answer.objects.create(question=q2, answer="Visit various locations around the country")
Answer.objects.create(question=q2, answer="Represent we, the people", correct=True)
Answer.objects.create(question=q2, answer="Wait for an emergency, and then step in to act")
Answer.objects.create(question=q2, answer="Practice making speeches in front of the mirror")

q3 = Question.objects.create(quiz=quiz, question="Three of the US's top 10 grossing companies paid taxes at a low rate. That rate was:")
Answer.objects.create(question=q3, answer="0%", correct=True)
Answer.objects.create(question=q3, answer="1%")
Answer.objects.create(question=q3, answer="3%")
Answer.objects.create(question=q3, answer="3.5%")
Answer.objects.create(question=q3, answer="5%")


Store.objects.create(name="Target", image_url="/static/images/GiftCardImages/Target.jpg")
Store.objects.create(name="Walmart", image_url="/static/images/GiftCardImages/walmart.jpg")
Store.objects.create(name="Netflix", image_url="/static/images/GiftCardImages/Netflix.jpeg")
Store.objects.create(name="Ebay", image_url="/static/images/GiftCardImages/ebay.jpeg")
Store.objects.create(name="Best Buy", image_url="/static/images/GiftCardImages/bestbuy.jpeg")
Store.objects.create(name="Amazon", image_url="/static/images/GiftCardImages/amazon.png")
Store.objects.create(name="Kohl's", image_url="/static/images/GiftCardImages/Kohls-Gift-Card.png")

Store.objects.create(name="Red Cross", image_url="none", charity=True)
Store.objects.create(name="National Park Service", image_url="none", charity=True)
Store.objects.create(name="National Coalition Against Domestic Violence", image_url="none", charity=True)
Store.objects.create(name="National Council on Aging", image_url="none", charity=True)
Store.objects.create(name="Doctors Without Borders", image_url="none", charity=True)
Store.objects.create(name="Journalists Without Border", image_url="none", charity=True)


james = Voter.objects.create(firstName='james', lastName='madison', address='america')
code = Code.objects.create(code='TESTCODE', voter=james, quiz=quiz)
