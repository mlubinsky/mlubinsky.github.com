$(document).ready(function() {
  var oldSize = parseFloat($("#zoom").css('font-size'));
  var newSize = oldSize  * 2;
  $("#zoom").hover(
    function() {
     $("#zoom").animate({ fontSize: newSize}, 200);
    },
    function() {
    $("#zoom").animate({ fontSize: oldSize}, 200);
   }
 );
});