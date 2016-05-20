
/// <reference path="../thirdparty/jquery.d.ts" />
/// <reference path="../util/touchClass.ts" />

module dashboard{

	export class dashboardClass{
	 cookieValue:any = null;
     csrftoken:any = null;
		constructor(){
			var $=jQuery;
			var sel:string;
            this.csrftoken = this.getCookie('csrftoken');
			var review_tab_touch_param = {
				target:"#reviews_tab",
				callback_end:()=>{
					this.reviewView();
				}
			}
			var get_review_btn_param = {
				target:"#get_reviews_button",
				callback_end:()=>{
					this.getReviews();
				}
			}
			var filter_review_btn_param = {
				target:"#filter_by_keyword",
				callback_end:()=>{
					this.filterByKeyword("ロード");
				}
			}
			var rating_view_btn_param = {
			    target:"#ratings_tab",
				callback_end:()=>{
					this.ratingsView();
				}
			}
			new util.touchClass(review_tab_touch_param);
			new util.touchClass(get_review_btn_param);
			new util.touchClass(rating_view_btn_param);
			new util.touchClass(filter_review_btn_param);
		}
		
		reviewView(){
			$("#ios_app_rating").hide();
			$("#ios_app_get_rating_btn").hide();
			$("#ios_app_review").show();
			$("#ios_app_get_review_btn").show();
			$("#reviews_tab").addClass("active");
			$("#ratings_tab").removeClass();
			this.refreshReviews();
		}
		refreshReviews(){
			 $.ajax({
				type: "GET",
				url: "/ios_app_review_fragment/",
				success: function (response) {
					$("#ios_app_review").html(response);
					console.log("Review list refreshed");
				}
			});
		}
		getReviews(){
			console.log("Getting reviews")
			$.ajax({
				type: "GET",
				url: "/get_reviews/",
				success: ()=> {
					this.refreshReviews();
				}
			});
		}
		filterByKeyword(filter_word:string){
		var encoded_string = encodeURIComponent(filter_word);
		console.log(this.csrftoken);
			$.ajax({
				type: "POST",
				url: "/filter_by_keyword/",
				headers: { "X-CSRFToken": this.csrftoken },
				data: {filter_to_use : encoded_string},
				success: (response)=> {
				    $("#ios_app_review").html(response);
				}
			});
		}
		
		
		
		ratingsView(){
			$.ajax({
				type: "GET",
				url: "/ios_app_rating_fragment/",
				success: function (response) {
					$("#ios_app_review").hide();
					$("#ios_app_get_review_btn").hide();
					$("#ios_app_rating").show();
					$("#ios_app_get_rating_btn").show();
					$("#ios_app_rating").html(response);
					$("#reviews_tab").removeClass();
					$("#ratings_tab").addClass("active");
				}
			});
    	}

    	getCookie(name) {

            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        this.cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return this.cookieValue;
        }
		
    }
}