const SELECTOR = 'fade-on-scroll';
const ANIMATE_CLASS_NAME = 'animate';

const animate = element =>  (
    element.classList.add(ANIMATE_CLASS_NAME)
)

const isAnimated = element => (
    element.classList.contains(ANIMATE_CLASS_NAME)
)

const intersectionObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {


        if(entry.intersectionRatio > 0) {
            animate(entry.target);
        }

    });
});

const elements = [].filter.call(
    document.getElementsByClassName(SELECTOR),
    element => !isAnimated(element, ANIMATE_CLASS_NAME)
)

elements.forEach((element) => intersectionObserver.observe(element));

var downBut = document.getElementById('downBut')
var mainInfo = document.getElementById('main-info')
$(downBut).click(function() {
    var infoHeight = mainInfo.getBoundingClientRect()
    console.log(infoHeight.top)
    window.scrollTo(0, infoHeight.top);
});

