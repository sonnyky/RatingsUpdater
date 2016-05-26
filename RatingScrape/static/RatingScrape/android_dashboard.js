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
            var get_json_param = {
                target: "#get_android_json_test",
                callback_end: function () {
                    _this.getTestJson();
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
            new util.touchClass(get_json_param);
            new util.touchClass(review_tab_touch_param);
            new util.touchClass(rating_view_btn_param);
        }
        androidDashboardClass.prototype.getTestJson = function () {
            $.ajax({
                type: "GET",
                url: "/get_android_json_test/",
                success: function (response) {
                    console.log(response);
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
            this.filter_keyword = $("#filter_keyword_input").val();
        };
        return androidDashboardClass;
    }());
    android_dashboard.androidDashboardClass = androidDashboardClass;
})(android_dashboard || (android_dashboard = {}));
