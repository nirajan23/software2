
const image = document.getElementById('target');
const trigger = document.getElementById('trigger');


trigger.addEventListener('mouseenter', function() {
    // Change the image source to picB.jpg when hovering over the paragraph
    image.src = 'img/picB.jpg';
});


trigger.addEventListener('mouseleave', function() {
    image.src = 'img/picA.jpg';
});
