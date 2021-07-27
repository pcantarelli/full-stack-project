// Search bar open and close
$("#search-icon").on("click", () => {
       $(".search-drawer").toggleClass('search-colapse');
});

$("#search-close").on("click", () => {
       $(".search-drawer").toggleClass('search-colapse');
});

// Toast messages
$(document).ready(function() {
       $(".toast").toast("show");
     });

