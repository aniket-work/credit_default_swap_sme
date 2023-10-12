
var question = document.getElementById('question');
var answerDiv = document.getElementById('answer-div');
var answer = document.getElementById('answer');
var loader = document.getElementById('loader');

$(document).ready(function () {
    $("#submit-btn").click(async function (event) {
        event.preventDefault();
        const formData = new FormData();
        const question = document.getElementById('question').value;
        if (question == null || question == "") {
            Swal.fire({
                icon: 'error',
                title: 'Query Required',
                text: "Please enter your query!",
                allowOutsideClick: false,
                allowEscapeKey: false,
                confirmButtonColor: "#000"
            });
        }else{                                    
            formData.append('question', question);
            $("#loader").modal("show"); 
            let response = await fetch('/get_answer', {
                method: "POST",
                body: formData                
            });                
            processAnswerResponse(response);   
        }
                     
    });
});

async function processAnswerResponse(response){
    $("#loader").modal("hide");
    switch (response.status) {
        case 400:  
            Swal.fire({
                icon: 'error',
                title: 'ERROR',
                text: "Encountered an internal error",
                confirmButtonColor: "#040b14"
            })
        break;
        case 200:                      
            var json = await response.json(); 
            var answerResult = json.answer;                  
            answerDiv.style.display = "block";
            answer.value = answerResult;                  
            break;
        default:
            Swal.fire({
                icon: 'error',
                title: 'ERROR',
                text: "There is a "+response.status+" error.",
                confirmButtonColor: "#040b14"
            })
    }
}

question.onchange = function () {
    answerDiv.style.display = "none";
}
