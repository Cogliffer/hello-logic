document.addEventListener("DOMContentLoaded", function() {
    var toc = document.querySelector('.md-sidebar--secondary');
    if(window.MathJax && toc){
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, toc]);
    }
});
