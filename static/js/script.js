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
    if (elem.offsetWidth === elem.scrollWidth) {
      $(this).siblings('.read-more').hide();
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
    $(".comment-text:not([class*='text-truncate'])").addClass("text-truncate");
    $('.read-less').hide();
    $('.read-more').click(function() {
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

// KEEP THE PILL ACTIVE AFTER REFRESH
/**
 * Function that keeps the selected pill active after page is changed
 **/

$(function() {
    $('a[data-toggle="pill"]').on('click', function(e) {
        window.localStorage.setItem('activePill', $(e.target).attr('href'));
    });
    var activePill = window.localStorage.getItem('activePill');
    if (activePill) {
        $('#pills-tab a[href="' + activePill + '"]').tab('show');
    }
});

// SPINNER OVERLAY

/**
 * Function fading out loading spinner overlay 
 **/

$(window).on('load', function() {
  $("#overlay").fadeOut("slow");
});

// BACK TO TOP BUTTON

/**
 * Function implements smooth scrolling back to top after clicking the button
 **/

let btn = $('#back-to-top-button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(d) {
  d.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});


// TOAST MESSAGES
/**
 * Function that shows toast message and fades it out after 7sec
 **/

$(document).ready(function(){
  $('.toast').toast('show');
  setTimeout(function(){ $('.toast').toast('hide'); }, 7000);
});

// NAVBAR HIDE/SHOW EFFECT
/**
 * Function that hides the navbar when user is scrolling down and shows it back
 * on the scroll to top
 * Based on the following tutorial: 
 * https://www.solodev.com/blog/web-design/bootstrap/
 * /build-a-fixed-top-navigation-that-disappears-as-users-scroll.stml
 **/
 
$(document).ready(function () {
	var previousScroll = 0;
	$(window).scroll(function () {
		var currentScroll = $(this).scrollTop();
		if (currentScroll < 100) {
			showNav();
		} else if (currentScroll > 0 && currentScroll < $(document).height() - $(window).height()) {
			if (currentScroll > previousScroll) {
				hideNav();
			} else {
				showNav();
			}
			previousScroll = currentScroll;
		}
	});

	function hideNav() {
		$(".navbar").removeClass("is-visible").addClass("is-hidden");
	}

	function showNav() {
		$(".navbar").removeClass("is-hidden").addClass("is-visible").addClass("scrolling");
	}
});


// NAVBAR HEIGHT CALCULATOR
/**
 * Function that calulates navbar height and applies margin to the main content
 * by adding nav height plus navbar padding
 **/
 
var heightNav = $('.navbar').height();

$('main').css({ marginTop : heightNav + 48 + 'px' });