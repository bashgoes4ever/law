$(document).ready(function() {

	//prices
	$('.button-price').click(function(){
		var fText = $(this).closest('.price-main__head').siblings('.price-main__body');

		$('.ftab-active').slideToggle();
		$('.price-main__body').removeClass('ftab-active');

		if (fText.is(':hidden')) {
			fText.addClass('ftab-active');
			fText.slideToggle();
		}
	});

	//faq slider
	$('.faq-slider').owlCarousel({
		items : 2,
		mouseDrag: true,
		nav: true,
		navText : ["<div class='faq-button-prev'><img src='/static/img/arr-l.png'/></div>", "<div class='faq-button-next'><img src='/static/img/arr-r.png'/></div>"],
	});

	//replies slider
	$('.replies-slider').owlCarousel({
		items : 1,
		mouseDrag: true,
		nav: true,
		navText : ["<div class='replies-button-prev'><img src='/static/img/arr-l1.png'/></div>", "<div class='replies-button-next'><img src='/static/img/arr-r1.png'/></div>"],
	});

	//callback
	$('.call, .inner-conv').click(function() {
		$('.layer').fadeIn(300)
		$('.callback').fadeIn(500)
	})

	$('.layer').click(function(e) {
		if ($(this).has(e.target).length === 0) {
			$(this).fadeOut(300)
			$('.popup').fadeOut(300)
			$('.thank').fadeOut(300)
		}
	})

	$('.popup .close').click(function() {
		$('.layer').fadeOut(300)
		$('.popup').fadeOut(300)
	})

	//stuff
	$('.stuff-tab').each(function(e) {
		$(this).attr('data-tab', e)
	})
	var stuff_slider = $('.stuff-items')
	stuff_slider.owlCarousel({
		items : 1,
		mouseDrag: true,
		nav: true,
		navText : ["<div class='stuff-button-prev'><img src='/static/img/arr-l1.png'/></div>", "<div class='stuff-button-next'><img src='/static/img/arr-r1.png'/></div>"],
	});
	$('.stuff-tab').click(function() {
		var t = $(this).data('tab')
		stuff_slider.trigger('to.owl.carousel', t)
	})


	//apply
	$('.inner-conv, .call').click(function() {
		var t = $(this).data('type')
		$('.callback.popup input[name=type]').val(t)
	})

	$('form').submit(function(e) {
		e.preventDefault()
		var url = $(this).attr('action')
		var r = $(this).serialize()
		$.ajax({
			url: url,
			data: r,
			type: 'POST',
			success: function(data) {
				$('.layer').fadeIn(300)
				$('.popup').hide()
				$('.thank').fadeIn(300)
			},
			error: function() {
				console.log('an error has been occured...')
			}
		})
	})


});