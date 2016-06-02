/// <reference path="../thirdparty/jquery.d.ts" />
/// <reference path="../util/touchClass.ts" />
var android_dashboard;
(function (android_dashboard) {
    var androidDashboardClass = (function () {
        function androidDashboardClass() {
            var _this = this;
            this.cookieValue = null;
            this.csrftoken = null;
            var $ = jQuery;
            var sel;
            this.csrftoken = this.getCookie('csrftoken');
            this.filter_keyword = "NONE";
            var get_android_review_btn_param = {
                target: "#get_android_reviews_button",
                callback_end: function () {
                    _this.getAndroidReviews();
                }
            };
            var review_tab_touch_param = {
                target: "#android_reviews_tab",
                callback_end: function () {
                    _this.androidReviewView();
                }
            };
            var rating_view_btn_param = {
                target: "#android_ratings_tab",
                callback_end: function () {
                    _this.androidRatingsView();
                }
            };
            var filter_review_btn_param = {
                target: "#android_filter_by_keyword",
                callback_end: function () {
                    _this.getFilterKeyword();
                    _this.filterAndroidReviewsByKeyword();
                }
            };
            new util.touchClass(get_android_review_btn_param);
            new util.touchClass(review_tab_touch_param);
            new util.touchClass(rating_view_btn_param);
            new util.touchClass(filter_review_btn_param);
        }
        androidDashboardClass.prototype.getAndroidReviews = function () {
            var _this = this;
            console.log("Getting reviews");
            $.ajax({
                type: "GET",
                url: "/get_android_reviews/",
                success: function () {
                    _this.refreshAndroidReviews();
                }
            });
        };
        androidDashboardClass.prototype.androidReviewView = function () {
            $("#android_app_rating").hide();
            $("#android_app_get_rating_btn").hide();
            $("#android_app_review").show();
            $("#android_app_get_review_btn").show();
            $("#android_reviews_tab").addClass("active");
            $("#android_ratings_tab").removeClass();
            this.refreshAndroidReviews();
        };
        androidDashboardClass.prototype.refreshAndroidReviews = function () {
            $.ajax({
                type: "GET",
                url: "/android_app_review_fragment/",
                success: function (response) {
                    console.log(response);
                    $("#android_app_review").html(response);
                }
            });
        };
        androidDashboardClass.prototype.androidRatingsView = function () {
            $.ajax({
                type: "GET",
                url: "/android_app_rating_fragment/",
                success: function (response) {
                    $("#android_app_review").hide();
                    $("#android_app_get_review_btn").hide();
                    $("#android_app_rating").show();
                    $("#android_app_get_rating_btn").show();
                    $("#android_app_rating").html(response);
                    $("#android_reviews_tab").removeClass();
                    $("#android_ratings_tab").addClass("active");
                }
            });
        };
        androidDashboardClass.prototype.getCookie = function (name) {
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
        };
        androidDashboardClass.prototype.getFilterKeyword = function () {
            this.filter_keyword = $("#android_filter_keyword_input").val();
        };
        androidDashboardClass.prototype.filterAndroidReviewsByKeyword = function () {
            var encoded_string = encodeURIComponent(this.filter_keyword);
            $.ajax({
                type: "POST",
                url: "/filter_android_review_by_keyword/",
                headers: { "X-CSRFToken": this.csrftoken },
                data: { filter_to_use: encoded_string },
                success: function (response) {
                    $("#android_app_review").html(response);
                }
            });
        };
        return androidDashboardClass;
    }());
    android_dashboard.androidDashboardClass = androidDashboardClass;
})(android_dashboard || (android_dashboard = {}));
//# sourceMappingURL=android_dashboard.js.map