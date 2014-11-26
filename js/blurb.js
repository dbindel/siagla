---
---

$(document).ready(function() {

    // Show blurbs on demand
    $(".blurb").hide();
    $(".toggler").click(function(e) {
        e.preventDefault();
        var target = $(this).attr("id");
        $("." + target).toggle()
        $(this).children(":first").toggleClass("fa-plus-square");
        $(this).children(":first").toggleClass("fa-minus-square");
    });
    
});
