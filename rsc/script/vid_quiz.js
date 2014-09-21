var entryCodeURI = '/entry_code';
var quizQuestion ={
	description: 'Query',
	answers:  []
};
var quiz = {
	questionIndex: 0,
	questions: [
		Object.create(quizQuestion, {
			id: {value: 0},
			description: {value: 'This is Question 1'},
			answers: {value: ['Answer1', 'Answer2', 'Kittens']}
		}),
		Object.create(quizQuestion, {
			id: {value: 1},
			description: {value: 'This is Question 2'},
			answers: {value: ['Answer1', 'Answer2', 'Kittens']}
		}),
		Object.create(quizQuestion, {
			id: {value: 2},
			description: {value: 'This is Kittens!'},
			answers: {value: ['Kittens', 'Kittens!', 'More Kittens!']}
		})
	],
	nextQuestion: function (){
		var nextQ = this.questions[this.questionIndex];
		this.questionIndex++;
		return nextQ;
	}
};
function loadQuestion(question){
	var questionContainer = document.getElementById('quiz_question_display');
	jContainer = jQuery('#quiz_question_display');
	jContainer.fadeOut(300, function (){
		questionContainer.innerHTML = "";
		var questionDescription = document.createElement('span');
		questionDescription.textContent = question.description;
		questionContainer.appendChild(questionDescription);
		question.answers.forEach(function (answer){
			var answerButton = document.createElement('button');
			answerButton.textContent = answer;
			questionContainer.appendChild(answerButton);
			answerButton.addEventListener("click", function(){
				answerQuestion(question.id, answer);
			});
		});
		jContainer.fadeIn(300);
	});
};
function answerQuestion(questionId, answer){
	var quizForm = document.getElementById('quiz_submitter');
	var answerInput = document.createElement('input');
	answerInput.name = questionId;
	answerInput.value = answer;
	var nextQuestion = quiz.nextQuestion();
	quizForm.appendChild(answerInput);
	if(!nextQuestion){
		finishQuiz();
	} else{
		loadQuestion(nextQuestion);
	}
};

function submitQuiz() {
	/*jQuery.ajax({
		url: entryCodeURI,
		data: entryCode,
		success: function (data, textStatus, jqXHR){},
		error: function (jqXHR, textStatus, errorThrown){},
		complete: function (jqXHR, textStatus){},
	});
	*/
	// TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	var redemptionCodeInput = document.getElementById('redemption_code_input');
	var redemptionCode = redemptionCodeInput.value;
	var quizForm = document.getElementById('quiz_submitter');
	var codeInput = document.createElement('input');
	codeInput.name = 'redemption_code';
	codeInput.value = redemptionCode;
	quizForm.appendChild(codeInput);
	quizForm.submit()
	return false
};
function videoComplete() {
	setTimeout(function (){
		var question = quiz.nextQuestion();
		loadQuestion(question);
		jQuery('#step_video').fadeOut(500, function (){
			jQuery('#step_quiz').fadeIn(500);
		});
	}, 0);
};
function finishQuiz() {
	setTimeout(function (){
		jQuery('#step_quiz').fadeOut(500, function (){
			jQuery('#step_code').fadeIn(500);
		});
	}, 0);
};
jQuery('#redemption_code').submit(submitQuiz);