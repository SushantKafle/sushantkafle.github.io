var PageTransitions = (function() {

	var $main = $( '#pt-main' ),
		$pages = $main.children( 'div.pt-page' ),
		$aboutBtn = $('#AcPro'),
		animcursor = 1,
		pagesCount = $pages.length,
		
		animEndEventNames = {
			'WebkitAnimation' : 'webkitAnimationEnd',
			'OAnimation' : 'oAnimationEnd',
			'msAnimation' : 'MSAnimationEnd',
			'animation' : 'animationend'
		};
        

	function init() {
	
        
        $("#AcPro").click(function(){
                
        });

	}

	function nextPage(page ) {
		//var $currPage = $pages.eq( current );
		var $nextPage = $pages.eq( page ).addClass( 'pt-page-current' ),
        outClass = '', inClass = '';

        outClass = 'pt-page-moveToLeft';
        inClass = 'pt-page-moveFromRight';
				
		/*$currPage.addClass( outClass ).on( animEndEventName, function() {
			$currPage.off( animEndEventName );
			endCurrPage = true;
			if( endNextPage ) {
				onEndAnimation( $currPage, $nextPage );
			}
		} );*/

		$nextPage.addClass( inClass ).on( animEndEventName, function() {
			$nextPage.off( animEndEventName );
			endNextPage = true;
			if( endCurrPage ) {
				onEndAnimation( $currPage, $nextPage );
			}
		} );

	}

	init();

	return {
		init : init,
		nextPage : nextPage
	};

})();
