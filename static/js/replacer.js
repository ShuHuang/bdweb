// Navbar

$(window).scroll(function() {

    var scroll = $(window).scrollTop();

    if (scroll > 0) {

        $(".navbar-dark").addClass("navbar-light");
        $(".navbar-dark").addClass("navbar-dark-scrolled");
        $(".navbar-dark-scrolled").removeClass("navbar-dark");

        $(".navbar").addClass("bg-white");

    } else {

        $(".navbar-dark-scrolled").removeClass("navbar-light");
        $(".navbar-dark-scrolled").addClass("navbar-dark");
        $(".navbar-dark").removeClass("navbar-dark-scrolled");

        $(".navbar").removeClass("bg-white");
    }

});

