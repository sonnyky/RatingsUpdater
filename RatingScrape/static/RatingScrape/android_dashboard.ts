
/// <reference path="../thirdparty/jquery.d.ts" />
/// <reference path="../util/touchClass.ts" />

module android_dashboard{

	export class androidDashboardClass{
	 cookieValue:any = null;
     csrftoken:any = null;

     filter_keyword:string;
		constructor(){
			var $=jQuery;
			var sel:string;
            this.csrftoken = this.getCookie('csrftoken');
            this.filter_keyword = "NONE";
			var get_json_param = {
				target:"#get_android_json_test",
				callback_end:()=>{
					this.getTestJson();
				}
			}

			new util.touchClass(get_json_param);
		}




		getTestJson(){
            $.ajax({
                type: "GET",
                url: "/get_android_json_test/",
                success: function (response) {
                 console.log(response);
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

        getFilterKeyword(){
            this.filter_keyword = $("#filter_keyword_input").val();
        }

    }
}