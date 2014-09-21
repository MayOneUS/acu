var entryCodeURI = '/entry_code';
var quiz_question ={
	description: 'Query',
	answers:  []
};
var quiz = {
	question_index: 0,
	questions: [
		Object.create(quiz_question, {
			description: {value: 'This is Question 1'},
			answers: {value: ['Answer1', 'Answer2', 'Kittens']}
		}),
		Object.create(quiz_question, {
			description: {value: 'This is Question 2'},
			answers: {value: ['Answer1', 'Answer2', 'Kittens']}
		}),
		Object.create(quiz_question, {
			description: {value: 'This is Kittens!'},
			answers: {value: ['Kittens', 'Kittens!', 'More Kittens!']}
		})
	],
	next_question: function (){
		var next_q = this.questions[this.question_index];
		this.question_index++;
		if(!next_q){
			validateQuiz();
		}
		return next_q;
	}
};
function load_question(question){
	var question_container = document.getElementById('quiz_question_display');
	question_container.innerHTML = "";
	var question_description = document.createElement('span');
	question_description.textContent = question.description;
	console.log(question.description)
	question_container.appendChild(question_description);
	question.answers.forEach(function (answer){
		var answer_button = document.createElement('button');
		answer_button.textContent = answer;
		question_container.appendChild(answer_button);
		answer_button.addEventListener("click", function(){
			answer_question(answer);
		});
	});
};
function answer_question(answer){
	load_question(quiz.next_question());
};

function submitEntryCode(entryCode) {
	/*jQuery.ajax({
		url: entryCodeURI,
		data: entryCode,
		success: function (data, textStatus, jqXHR){},
		error: function (jqXHR, textStatus, errorThrown){},
		complete: function (jqXHR, textStatus){},
	});
	*/
	setTimeout(function (){
		jQuery('#step_code').fadeOut(500, function (){
			jQuery('#step_results').fadeIn(500);
		});
	}, 0);
};
function videoComplete() {
	setTimeout(function (){
		var question = quiz.next_question();
		load_question(question);
		jQuery('#step_video').fadeOut(500, function (){
			jQuery('#step_quiz').fadeIn(500);
		});
	}, 0);
};
function validateQuiz() {
	setTimeout(function (){
		jQuery('#step_quiz').fadeOut(500, function (){
			jQuery('#step_code').fadeIn(500);
		});
	}, 0);
};

jQuery('#redemption_code').submit(submitEntryCode);