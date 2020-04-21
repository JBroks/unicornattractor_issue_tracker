// TOOLTIPS
/**
 * Function to initialize all tooltips on a page
 **/
$(function() {
  $('[data-toggle="tooltip"]').tooltip()
});


// RESET TICKETS FILTERS
/** 
 * Onclick functions for the ticket type and status filters.
 * Function that clears the filters after reset button is clicked by a user
 **/
$('#reset').click(function() {
  $("#ticket-type").val($("#ticket-type option:first").val());
  $("#ticket-status").val($("#ticket-status option:first").val());
});


$('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
  e.target // newly activated tab
  e.relatedTarget // previous active tab
});