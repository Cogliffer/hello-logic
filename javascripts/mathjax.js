window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
  
  document$.subscribe(() => { 
    MathJax.typesetPromise()
})
// document.addEventListener("DOMContentLoaded", function() {
//     // 监听所有的 <details> 标签
//     var allDetails = document.querySelectorAll('details');
//     allDetails.forEach(function(details) {
//         details.addEventListener('toggle', function() {
//             if (details.open) {
//                 alert("JavaScript is working!");
//                 // 当 <details> 打开时，告诉 MathJax 重新处理页面
//                 if (window.MathJax) {
//                     MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
//                 }
//             }
//         });
//     });
// });
