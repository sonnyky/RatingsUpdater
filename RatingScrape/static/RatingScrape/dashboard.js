/// <reference path="../thirdparty/jquery.d.ts" />
/// <reference path="../util/touchClass.ts" />
var dashboard;
(function (dashboard) {
    var dashboardClass = (function () {
        function dashboardClass() {
            var _this = this;
            this.cookieValue = null;
            this.csrftoken = null;
            var $ = jQuery;
            var sel;
            this.csrftoken = this.getCookie('csrftoken');
            this.filter_keyword = "NONE";
            var review_tab_touch_param = {
                target: "#reviews_tab",
                callback_end: function () {
                    _this.reviewView();
                }
            };
            var get_review_btn_param = {
                target: "#get_reviews_button",
                callback_end: function () {
                    _this.getReviews();
                }
            };
            var filter_review_btn_param = {
                target: "#filter_by_keyword",
                callback_end: function () {
                    _this.getFilterKeyword();
                    _this.filterByKeyword();
                }
            };
            var rating_view_btn_param = {
                target: "#ratings_tab",
                callback_end: function () {
                    _this.ratingsView();
                }
            };
            new util.touchClass(review_tab_touch_param);
            new util.touchClass(get_review_btn_param);
            new util.touchClass(rating_view_btn_param);
            new util.touchClass(filter_review_btn_param);
        }
        dashboardClass.prototype.reviewView = function () {
            $("#ios_app_rating").hide();
            $("#ios_app_get_rating_btn").hide();
            $("#ios_app_review").show();
            $("#ios_app_get_review_btn").show();
            $("#reviews_tab").addClass("active");
            $("#ratings_tab").removeClass();
            this.refreshReviews();
        };
        dashboardClass.prototype.refreshReviews = function () {
            $.ajax({
                type: "GET",
                url: "/ios_app_review_fragment/",
                success: function (response) {
                    $("#ios_app_review").html(response);
                    console.log("Review list refreshed");
                }
            });
        };
        dashboardClass.prototype.getReviews = function () {
            var _this = this;
            console.log("Getting reviews");
            $.ajax({
                type: "GET",
                url: "/get_reviews/",
                success: function () {
                    _this.refreshReviews();
                }
            });
        };
        dashboardClass.prototype.filterByKeyword = function () {
            var encoded_string = encodeURIComponent(this.filter_keyword);
            $.ajax({
                type: "POST",
                url: "/filter_by_keyword/",
                headers: { "X-CSRFToken": this.csrftoken },
                data: { filter_to_use: encoded_string },
                success: function (response) {
                    $("#ios_app_review").html(response);
                }
            });
        };
        dashboardClass.prototype.ratingsView = function () {
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
        };
        dashboardClass.prototype.getCookie = function (name) {
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
        dashboardClass.prototype.getFilterKeyword = function () {
            this.filter_keyword = $("#filter_keyword_input").val();
        };
        return dashboardClass;
    }());
    dashboard.dashboardClass = dashboardClass;
})(dashboard || (dashboard = {}));
//# sourceMappingURL=dashboard.js.map