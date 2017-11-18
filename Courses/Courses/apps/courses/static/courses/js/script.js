$(document).ready(function () {
    $(".submit").on("click", function () {
        if ($(".name").val() == "") {
            alert("Please Enter Full Name")
            return false
        } else {
            return true
        }

    })
})
