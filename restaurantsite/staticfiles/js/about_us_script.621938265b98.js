
const SELECTOR = 'right'
const SELECTOR2 = 'left'
const SELECTOR3 = 'aniText'
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
const elements2 = [].filter.call(
    document.getElementsByClassName(SELECTOR2),
    element => !isAnimated(element, ANIMATE_CLASS_NAME)
)
const elements3 = [].filter.call(
    document.getElementsByClassName(SELECTOR3),
    element => !isAnimated(element, ANIMATE_CLASS_NAME)
)

elements.forEach((element) => console.log(element))
elements.forEach((element) => intersectionObserver.observe(element));
elements2.forEach((element) => intersectionObserver.observe(element));
elements3.forEach((element) => intersectionObserver.observe(element));