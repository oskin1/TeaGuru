function in_array(value, array) {
		for(var i = 0; i < array.length; i++) {
				if(array[i] == value) return true;
		}
		return false;
}
Array.prototype.remove = function(value) {
		var idx = this.indexOf(value);
		if (idx != -1) {
				return this.splice(idx, 1);
		}
		return false;
}

$(document).ready(function(){
    var y = 0;
	var tags = []
    var bdcheck = document.createElement('div');
    if( bdcheck.style['backdrop-filter'] !== undefined || bdcheck.style['-webkit-backdrop-filter'] !== undefined ){
        $('body').addClass('backdrop');
    }
    
	var params = {
		page : '',
		tags : '',
		limit : '',
		order : '',
		sort : '',
		q : '',
	}
	params.q = $('#product-list').attr('data-query');
	
    function tagManager(v){
    	if (in_array(v, tags) == false){
    		tags.push(v);
    	}else{
    		tags.remove(v);
    	}
    	params.tags = tags.join();
    }
    
    function requestList(){
    	$.ajax({
    		type : 'GET',
    		url : window.location.pathname,
    		data : params,
    		cache : true,
    		beforeSend: function(){
    		    $('#product-list').addClass('unav');
    		},
    		success: function(data){ /*make preloader*/
    			$('#product-list').empty().append(data).removeClass('unav');
    		}		
    	});		
    }
    
    function scrollToTop(){
        $('body,html').animate({
            scrollTop: 0
        }, 350);
        return false;
    }
    
    function sidebarOpen(){
            y = $(window).scrollTop();
            scrollTop = $(window).scrollTop;
    	    $('.sidenav').addClass('opened');
    	    $('.shadow-global').fadeIn(100);
    	    $('body').css('top', -$('body').scrollTop() + 'px').addClass('noscroll');
    }
    
    function sidebarClose(){
    	    $('.sidenav').removeClass('opened');
    	    $(this).fadeOut(100);
    	    $('body').removeClass('noscroll');
    	    $('body').removeClass('noscroll').scrollTop(y);
    }
    
    function showSearch(){
        $('#search').addClass('active');
        $('.shadow-undernav').fadeIn(100);
        $('#search input[type="search"]').focus();
    }
    
    function hideSearch(){
        $('#search').removeClass('active');
        $('.shadow-undernav').fadeOut(100);
        $('#search input[type="search"]').blur();
    }
    
    $('#search').click(showSearch);
    $('.shadow-undernav').click(hideSearch);
    
    $(".sidenav").scrollTop(1).on("scroll", function(e) {
        var maxScroll = $(e.target)[0].scrollHeight - $(e.target).outerHeight();
        if ($(this).scrollTop() === 0) {
            $(this).scrollTop(1);
        } else if ($(this).scrollTop() === maxScroll) {
            $(this).scrollTop(maxScroll-1);
        }
    });
	$('.icon-nav').click(sidebarOpen);
	$('.shadow-global').click(sidebarClose);
	$(document).on('click', '.expland', function(){
	   $(this).parent().addClass('opened'); 
	});
	$(document).on('click', '.opened > .expland', function(){
	   $(this).parent().removeClass('opened'); 
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
			success: function(){
				$('.subm.xl').text('Добавлено в')
				.addClass('added').append('<span> корзину</span>');
				yaCounter40980344.reachGoal('CartAdd');
				window.dataLayer.push(cartAddData);
				return true;
			},
		});
	});

    $(window).scroll(function () {
        if ($(this).scrollTop() > 650) {
            $('#scroll-top').addClass('visible');
        } else {
            $('#scroll-top').removeClass('visible');
        }
    });
    $('#scroll-top').click(scrollToTop);
	$('.sort').change(function(){
		params.sort = $('select option:selected').attr('data-sort');
		params.order = $('select option:selected').attr('data-order');
		requestList();
	});
	$(document).on('click', 'a.pn', function(e){
		e.preventDefault();
	    url = '?page=' + $(this).attr('data-page');
		params.page = $(this).attr('data-page');
		if (params.page != undefined){
		    requestList();   
		    window.history.pushState('', '', url);
		    scrollToTop();
		}
	});	
	$('.current').click(function(){
	    $(this).next('.sel').fadeIn(100).addClass('on');
	});
	$('.btn-filter').click(function(){
	   $('#filter').fadeIn(100);
	   $('#close').fadeIn();
	   $('.content').fadeOut();
	});
	$('#close').click(function(){
	   $('.content').fadeIn();
	   $(this).fadeOut();
	   $('#filter').fadeOut(100);	    
	})
	$('#apply-filter').click(function(){
	   requestList();
	   $('.content').fadeIn();
	   $('#filter').fadeOut(100);
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
	});
});
