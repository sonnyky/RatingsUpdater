window.addEventListener('load', function(){ // on page load

    $("#reviews_tab").on("touchstart", function(){
        $(this).addClass("active");
        $("#ratings_tab").removeClass();
        $("#others_tab").removeClass();
    });
     $("#ratings_tab").on("touchstart", function(){
        $(this).addClass("active");
        $("#reviews_tab").removeClass();
        $("#others_tab").removeClass();
    });
     $("#others_tab").on("touchstart", function(){
        $(this).addClass("active");
        $("#ratings_tab").removeClass();
        $("#reviews_tab").removeClass();
    });


}, false)