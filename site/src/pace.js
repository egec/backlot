/* Scrolling is left to the browser: no wheel or touch handling here.
   Step and bar clicks in the features scroll smoothly to their step. */
(function(){
var RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
window.__pace=function(y){scrollTo({top:Math.max(0,Math.round(y)),behavior:RM?'auto':'smooth'})};
})();
