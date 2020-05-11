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

// DISPLAY EDIT COMMENT FORM

/** 
 * Function that displays only the comment form which user chose to update.
 * Function is initiated on edit button click.
 * When users clicks 'edit' button card view is hidden and editable comment is
 * being displayed
 * When edit form cancel button is clicked the form is hidden again
 **/

$(document).ready(function() {
  // Hide all (update) form as a default
  $('.edit-comment').hide();
  $('.edit-comment-btn').click(function() {
    $('.edit-comment').hide();
    $('.posted-comment').show();
    $(this).parents('div.card-header').nextAll('.posted-comment').hide();
    $(this).parents('div.card-header').nextAll('.edit-comment').show();
  });
});

 
$(document).ready(function() {
  $(function() {
    $('.cancel-edit').click(function() {
      $('.edit-comment').hide();
      $('.posted-comment').show();
    });
  });
});

// CHECK TRUNCATE

/**
 * Function that checks which comments were truncated in order to display
 * 'read more' link only for those comments
 **/

$(function() {
     $('.comment-text').each(function(index, elem) {
         if(elem.offsetWidth === elem.scrollWidth){
          	$(this).siblings('.read-more').hide();
          	$(this).siblings('hr').hide();
         }
     });
 });
 
 // SHOW MORE / LESS COMMENT

/**
 * Function that toggles bootstrap class truncate-text for the comment text
 * in order to manage very long comments.
 * When comments are truncated link 'more' can be clicked to see full text.
 * On other other hand when user wants to hide the comment again he / she can 
 * click 'read less' which will truncate the comment 
 * At the same time when the user is done reading and does not click read less
 * and clicks on other comment read mor button, the previous comment will
 * automatically truncate text
 **/
  
// Read more
$(document).ready(function() {
  $(function() {
    $('.read-less').hide();
    $('.read-more').click(function() {
      $(".comment-text:not([class*='text-truncate'])").addClass("text-truncate");
      $('.read-less').hide();
      $('.read-more').show();
      $(this).siblings('.comment-text').toggleClass('text-truncate');
      $(this).hide();
      $(this).siblings('.read-less').show();
    });
  });
});

// Read less
$(document).ready(function() {
  $(function() {
    $('.read-less').click(function() {
      $(this).siblings('.comment-text').toggleClass('text-truncate');
      $(this).hide();
      $(this).siblings('.read-more').show();
    });
  });
});