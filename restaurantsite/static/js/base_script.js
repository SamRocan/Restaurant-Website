var testbutton = document.getElementsByClassName("filldiv")
var spinner1 = document.getElementById("m1")
var spinner2 = document.getElementById("m2")
var spinner3 = document.getElementById("m3")
var navMain = document.getElementById("main")
var navitems = document.getElementById("navlist")
$(testbutton).click(function() {
    console.log($(navMain).css("visibility"))
    if ($(spinner1).css("top") == "0px" ){
        $(navMain).height("calc(100vh + 60px)")
        $(spinner1).animate({
            top: '11px'
        });
        $(spinner2).animate({
            top: '0px'
        });
        $(spinner3).animate({
            top: '-11px'
        });
        $(navitems).removeClass('notVisibleList').addClass('visibleList');
        $(navMain).animate({
            opacity: 1
        });
        /* Prevents scroll on
        window.onscroll = function () { window.scrollTo(0, 0); };*/
    } else {
        $(navMain).height("0px")
        $(spinner1).animate({
            top: '0px'
        });
        $(spinner2).animate({
            top: '0px'
        });
        $(spinner3).animate({
            top: '0px'
        });
        $(navMain).animate({
            opacity: 0
        });
        setTimeout(() => {
            $(navitems).removeClass('visibleList').addClass('notVisibleList');
        }, 700);
        window.onscroll = function () {}
        }
});
var doc = $(document)
const menu = document.getElementById('menu')
const divs =  menu.querySelectorAll('div')
const wrapper = document.getElementById('wrapper')
$(doc).scroll(function() {
    if ($(doc).scrollTop() >= $(wrapper).height()) {
        divs.forEach(function (todo){
            $(divs).css('background-color', 'black');
        })
        // user scrolled 50 pixels or more;
        // do stuff
    } else {
        divs.forEach(function (todo){
            $(divs).css('background-color', 'white');
        })
    }
});
