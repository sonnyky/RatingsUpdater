
/// <reference path="../thirdparty/jquery.d.ts" />
/// <reference path="../util/touchClass.ts" />

module dashboard{

	export class dashboardClass{
		constructor(){
			var $=jQuery;
			var sel:string;

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
			var rating_view_btn_param = {
			    target:"#ratings_tab",
				callback_end:()=>{
					this.ratingsView();
				}
			}
			new util.touchClass(review_tab_touch_param);
			new util.touchClass(get_review_btn_param);
			new util.touchClass(rating_view_btn_param);
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
		
		
    }
}