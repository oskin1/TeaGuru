function in_array(value, array) {
		for(var i = 0; i < array.length; i++) {
				if(array[i] == value) return true;
		}
		return false;
}
function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}
Array.prototype.remove = function(value) {
		var idx = this.indexOf(value);
		if (idx != -1) {
				return this.splice(idx, 1);
		}
		return false;
}

$(document).ready(function(){
	initSelects();
	var tags = []
	var facets = 0;
	var params = {
		page : '',
		tags : '',
		limit : '',
		order : '',
		sort : '',
		q : '',
	}
	params.q = $('#product-list').attr('data-query');
	$('header').waypoint(function(direction) {
		var menu = $('#m-menu');
		if (menu.hasClass('fixed')) {
			menu.removeClass('fixed');
		}else{
			menu.addClass('fixed');
		}
	}, {
		offset: '-42px'
	});
	$('.filters').waypoint(function(direction) {
		btn = $('#to-top');
		if (btn.hasClass('active')) {
			btn.removeClass('active');
			btn.fadeOut(100);
		}else{
			btn.addClass('active');
			btn.fadeIn(100);
		}
	}, {
		offset: '-900px'
	});
	$('footer').waypoint(function(direction) {
		btn = $('.to-top');
		if (btn.hasClass('sticked')) {
			btn.removeClass('sticked');
			btn.css('position', 'fixed').css('bottom', '45px');
		}else{
			btn.addClass('sticked');
			btn.css('position', 'absolute').css('bottom', '15px');
		}
	}, {
		offset: ($(window).height() - 30)
	});
	function showSearch(){
	    $('#search').addClass('show');
	    $('#search-overlay').fadeIn(200);
	    $('#search input[type="search"]').focus();
	}
	function hideSearch(){
	    $('#search').removeClass('show');
	    $('#search-overlay').fadeOut(200);
	    $('#search input[type="search"]').blur();
	}	
	function PosTooltip(){
		var contentW = $('.menu').width();
		var windowW = $(window).width();
		$('#minicart').css('right', function(){
			return (windowW - contentW)/2
		});
	}
	PosTooltip();
	function tagManager(v){
		if (in_array(v, tags) == false){
			tags.push(v);
			facets += 1;
		}else{
			tags.remove(v);
			facets -= 1;
		}
		params.tags = tags.join();
		requestList();
	}
	function requestList(){
	    path = window.location.pathname;
		$.ajax({
			type : 'GET',
			url : path,
			data : params,
			cache : true,
			beforeSend: function(){
			    $('#product-list').addClass('unav');
			},
			success: function(data){ /*make preloader*/
				$('#product-list').empty().append(data).removeClass('unav');
				initSelects();
			}		
		});		
	}
	function scrollToTop(){
        $('body,html').animate({
            scrollTop: 0
        }, 400);
        return false;
	}
	$(document).click(function(){
	    $('div.sel').removeClass('on').fadeOut(0);
	    $('.select__gap').removeClass('on');
	    $('.select__list').slideUp(200);
	});
// Select
	function initSelects(){
		$('select').each(function(){
			// Variables
			var $this = $(this),
				selectOption = $this.find('option'),
				selectOptionLength = selectOption.length,
				selectedOption = selectOption.filter(':selected'),
				dur = 200;

			$this.hide();
			// Wrap all in select box
			$this.wrap('<div class="select"></div>');
			// Style box
			$('<div>',{
				class: 'select__gap',
				text: ''
			}).insertAfter($this);
			
			var selectGap = $this.next('.select__gap'),
				caret = selectGap.find('.caret');
			// Add ul list
			$('<ul>',{
				class: 'select__list'
			}).insertAfter(selectGap);		

			var selectList = selectGap.next('.select__list');
			// Add li - option items
			for(var i = 0; i < selectOptionLength; i++){
				$('<li>',{
					class: 'select__item',
					html: $('<span>',{
						text: selectOption.eq(i).text()
					})				
				})
				.attr('data-value', selectOption.eq(i).val())
				.appendTo(selectList);
			}
			// Find all items
			var selectItem = selectList.find('li');
			$(this).val(function(){ /* CHECK THIS LATER */
				return $(selectItem[0]).data('value');
			}).attr('selected', 'selected');
			selectGap.text($(this).find('span').text());
			selectGap.text($(selectItem[0]).find('span').text());
			if ($(this).parent().parent().parent().hasClass('initial')){
				selectGap.text(selectedOption.text());
			}
			selectList.slideUp(0);
			selectGap.on('click', function(e){
			    e.stopPropagation();
				if(!$(this).hasClass('on')){
					$(this).addClass('on');
					selectList.slideDown(dur);

					selectItem.on('click', function(){
						var chooseItem = $(this).data('value');

						$('select').val(chooseItem).attr('selected', 'selected');
						selectGap.text($(this).find('span').text());

						selectList.slideUp(dur);
						selectGap.removeClass('on');

						if ($('form.add').hasClass('change-q')){
							data = selectGap.parent().parent().parent().serialize();
							action = selectGap.parent().parent().parent().attr('action');
							$.ajax({
								type : 'POST',
								url : action,
								data : data,
								cache : false,
								success: function(){ /*make preloader*/
									window.location.reload();
								}			
							});	
						}
					});
					
				} else {
					$(this).removeClass('on');
					selectList.slideUp(dur);
				}
			});		

		});	
	}
    function alignImg(){
        img = $('#viewport img.active').height();
        vp = $('#viewport').height();     
        pos = (vp - img)/2;
        $('#viewport img.active').css('top', pos);
    }
	$('#viewport img:first-child').fadeIn(0).addClass('active');
	$('.img.sm:first-child').addClass('active');
	alignImg();
	$('#to-top').click(function(e){
	    e.preventDefault();
	    scrollToTop();
	})
	$('#show-all-props').click(function(){
	    $('#attr-box').addClass('opened');
	})
	$('#hide-all-props').click(function(){
	    $('#attr-box').removeClass('opened');
	})
	$('#search-button').click(showSearch);
	$('#search-overlay').click(hideSearch);
	$('.fake-overlay').click(function(){
		$('#minicart').fadeOut(150);
		$(this).fadeOut();
	});   
	$('.cart-box').click(function(e){
		$('#minicart').fadeIn(120);
		$('.fake-overlay').fadeIn();
		PosTooltip();
	});
	$(document).on('click', '.subm', function(e){
		e.preventDefault();
		var data = $(this).parent().serialize();
		var action = $(this).parent().attr('action');
		var cartAddData = JSON.stringify({
		    id: $(this).parent().parent().attr('data-id'),
		    name: $(this).parent().parent().attr('data-name'),
		    price: $(this).parent().parent().attr('data-price'),
		    category: $(this).parent().parent().attr('data-category'),
		    quantity: data.quantity,
		});
		$.ajax({
			type: "POST",
			url: action,
			data: data,
			cache: false,
			success: function(data){
				$('.cart-box').empty();
				$('.cart-box').append(data);
				$('.subm.xl').text('Добавлено в')
				.addClass('added').append('<span> корзину</span>');
				yaCounter40980344.reachGoal('CartAdd');
				window.dataLayer.push(cartAddData);
				return true;
			}
		});
		PosTooltip();
	});
	$(document).on('click', '#minicart .delete', function(){
		var p_id = $(this).parent().attr('data-prod-id');
		var data = $(this).find('form').serialize();
		var cartRemoveData = JSON.stringify({
		    id: p_id,
		});
		$.ajax({
			type: "POST",
			url: '/cart/remove/' + p_id + '/',
			data: data,
			cache: false,
			success: function(data){
				$('.cart-box').empty();
				$('.cart-box').append(data);
				$('#minicart').fadeIn('30');
				PosTooltip();
				yaCounter40980344.reachGoal('CartRemove');
				window.dataLayer.push(cartRemoveData);
				return true;
			}
		});    
	});
	$(document).on('click', '#sbe-me', function(e){
	   e.preventDefault();
	   data = $(this).parent().serialize();
	   action = $(this).parent().attr('action')
	   $.ajax({
			type: "POST",
			url: action,
			data: data,
			cache: false,
			success: function(r){
				if (r == 200){
				    $('#resp').empty().append('Вы подписаны, поздравляем!');
				    yaCounter40980344.reachGoal('SUBSCRIBE');
				}else{
				    $('#resp').empty().append('Вы либо уже подписаны, либо данные в форме неверны.');
				}
			}  
	   });
	});
	$('a.ctrl').click(function(e){
		e.preventDefault();
		params.sort = $(this).attr('data-sort');
		params.order = $(this).attr('data-order');
		$('a.ctrl').removeClass('active');
		$(this).addClass('active');
		$(this).parent().prev('.current').empty().append($(this).text());
		$(this).parent().removeClass('on').fadeOut(0);
		requestList();
	});
	$('a.lim').click(function(e){
		e.preventDefault();
		params.limit = $(this).attr('data-limit');
		clim = '.lim[data-limit="' + $(this).attr('data-limit') + '"]';
		$('a.lim').removeClass('active');
		$(clim).addClass('active');
		$(this).parent().prev('.current').empty().append(params.limit + ' товаров');
		$(this).parent().removeClass('on').fadeOut(0);
		requestList();
	});	
	$(document).on('click', 'a.pn', function(e){
		e.preventDefault();
	    url = '?page=' + $(this).attr('data-page');
	    window.history.pushState('', '', url);
		params.page = $(this).attr('data-page');
		$('a.pn').removeClass('active');
		$(this).addClass('active');
		requestList();
		scrollToTop();
	});	
	$('.current').click(function(e){
	    e.stopPropagation();
	    $(this).next('.sel').fadeIn(100).addClass('on');
	});
	$('.option').click(function(){ 
		v = $(this).find('input').attr('value');		
		c = $(this).attr('data-checked');
		if (c == 0){
			$(this).find('input').attr('checked', 1);
			$(this).attr('data-checked', "1");
		}else{
			$(this).find('input').attr('checked', !1);
			$(this).attr('data-checked', "0");
		}
		tagManager(v);
		if (facets > 0){
		    $('#reset').fadeIn(100);
		}else{
		    $('#reset').fadeOut(100);
		}
	});
    $('#reset').click(function(){
        params.tags = [];
        $('.option').find('input').attr('checked', !1);
		$('.option').attr('data-checked', "0");
		$('#reset').fadeOut(100);
		requestList();
		facets = 0;
    });
    
    //popup
    if (getCookie('popup') == undefined){
        setTimeout(function(){
            $('#popup1').fadeIn();
            var date = new Date(new Date().getTime() + 60);
            document.cookie = "popup=shown; path=/; expires=" + date.toUTCString();
        }, 10000);
    }else if (getCookie('popup') == 'shown'){
        $('#popup1').fadeIn();
    }
    $('#popup1 .close').click(function(){
        var date = new Date(new Date().getTime() + 60);
        document.cookie = "popup=closed; path=/; expires=" + date.toUTCString();
    });
});
