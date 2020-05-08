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

/** 
 * Function that displays only the comment form which user chose to update.
 * Function is initiated on edit button click.
 * When users clicks 'edit' button card view is hidden and editable comment is
 * being displayed
 **/

$(document).ready(function() {
  // Hide all (update) form as a default
  $('.edit-comment').hide();
  $('.edit-comment-btn').click(function() {
    $(this).parents('div.card-header').nextAll('.posted-comment').hide();
    $(this).parents('div.card-header').nextAll('.edit-comment').show();
  });
});