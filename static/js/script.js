// TOOLTIPS
/**
 * Function to initialize all tooltips on a page
 **/
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});


// RESET TICKETS FILTERS
/** 
 * Onclick functions for the ticket type and status filters.
 * Function that clears the filters after reset button is clicked by a user
 **/
$('#reset').click(function(){
    $("#ticket_type").val($("#ticket_type option:first").val());
    $("#ticket_status").val($("#ticket_status option:first").val());
});