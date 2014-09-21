var entryCodeURI = '/entry_code';
var quizQuestion ={
	description: 'Query',
	answers:  []
};
var quiz = {
	questionIndex: 0, // In order to skip the Django token which is the first child
	questions: undefined,
	quizTimerHack: false,
	setup: function (){
		this.questions = document.getElementById('quiz_form').children;
		for(var questionIndex = 0; questionIndex < this.questions.length; questionIndex++){
			var indexedQuestion = this.questions[questionIndex];
			if(indexedQuestion.id){
				var jQQ = jQuery('#'+indexedQuestion.id);
				jQQ.fadeOut(1);
				var labelChildren = jQQ.find('label');
				for(var labelIndex = 0; labelIndex < labelChildren.length; labelIndex++){
					var indexedLabel = labelChildren[labelIndex];
					indexedLabel.addEventListener('click', function (){
						answerQuestion();
					})
				}
			}
		}
	},
	currentQuestion: function (){
		if(this.questionIndex > 0 && this.questions){ // Again, because index 0 is the Django token
			return this.questions[this.questionIndex];
		} else{
			return null;
		}
	},
	nextQuestion: function (){
		this.questionIndex++;
		if(this.questionIndex < this.questions.length){
			var nextQ = this.questions[this.questionIndex];
			return nextQ;
		} else{
			return null;
		}
	}
};
function loadQuestion(old_question, question){
	var fader = function (){
		var jQ2 = jQuery('#'+question.id);
		jQ2.fadeIn(300);
	}
	if(old_question){
		console.log('Fading Out '+Math.random())
		var jQ1 = jQuery('#'+old_question.id);
		jQ1.fadeOut(300, fader)
	} else{
		fader();
	}
};
function answerQuestion(){
	if(quiz.quizTimerHack){ return}
	quiz.quizTimerHack = true;
	setTimeout(function (){
		quiz.quizTimerHack = false
	}, 750);
	var currentQuestion = quiz.currentQuestion();
	var nextQuestion = quiz.nextQuestion();
	if(!nextQuestion){
		console.log('Done!')
		finishQuiz();
	} else{
		loadQuestion(currentQuestion, nextQuestion);
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
		var currentQuestion = quiz.currentQuestion();
		var question = quiz.nextQuestion();
		loadQuestion(currentQuestion, question);
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
quiz.setup();
videoComplete();