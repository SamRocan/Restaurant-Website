var testbutton = document.getElementsByClassName("filldiv")
var spinner1 = document.getElementById("m1")
var spinner2 = document.getElementById("m2")
var spinner3 = document.getElementById("m3")
var navMain = document.getElementById("main")
var navitems = document.getElementById("navlist")

const menu = document.getElementById('menu')
const divs =  menu.querySelectorAll('div')

$(testbutton).click(function() {
    divs.forEach(function (todo){
        $(divs).css('background-color', 'whitesmoke');
    })
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
        setTimeout(function (){
            {
                window.onscroll = function () {
                    window.scrollTo(0, 0);
                };
            }
        }, 700);
    } else {
        divs.forEach(function (todo){
            $(divs).css('background-color', 'black');
        })
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

