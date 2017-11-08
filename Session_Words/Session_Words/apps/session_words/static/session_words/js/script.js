$(document).ready(function () {
    $(".submit").on("click", function () {
        if ($(".word").val() == "") {
            alert("Please Enter Word")
            return false
        } else {
            return true
        }

    })
})
