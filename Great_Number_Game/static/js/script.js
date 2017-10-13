$(document).ready(function () {
    $(".submit").on("click", function () {
        if ($(".guess").val() === $(".pick").val()) {
            $(".greenBox").show();
            $(".redBox").hide();
            $(".guessNumber").hide();
        } else if ($(".guess").val() !== $(".pick").val()) {
            if ($(".guess").val() === "" || $(".guess").val() > 100) {
                $(".redBox").show();
                $(".tooLow").hide();
                $(".tooHigh").hide();
                $(".notNumber").show();
            } else if ($(".guess").val() < $(".pick").val()) {
                $(".redBox").show();
                $(".tooHigh").hide();
                $(".notNumber").hide();
                $(".tooLow").show();
            } else {
                $(".redBox").show();
                $(".tooLow").hide();
                $(".tooHigh").show();
                $(".notNumber").hide();
            }
        }
        $('form').trigger("reset");
        return false
    })
})
