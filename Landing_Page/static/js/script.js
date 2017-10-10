$(document).ready(function() {
    $(".submit").on("click", function() {
        if($("input").val() === ""){
            alert("Please enter Full Name and Email Address")
        } else if ($("textarea").val() == "") {
            alert("Please enter a message")
        } else {
            alert("Your message has been submitted");
        }

        $('form').trigger("reset");
        return false;
    })
})
