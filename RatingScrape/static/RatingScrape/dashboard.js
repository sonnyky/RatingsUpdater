/// <reference path="../thirdparty/jquery.d.ts" />
/// <reference path="../util/touchClass.ts" />
var dashboard;
(function (dashboard) {
    var dashboardClass = (function () {
        function dashboardClass() {
            var _this = this;
            var $ = jQuery;
            var sel;
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
            new util.touchClass(review_tab_touch_param);
            new util.touchClass(get_review_btn_param);
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
                    console.log(response);
                    $("#ios_app_review").html(response);
                }
            });
        };
        dashboardClass.prototype.getReviews = function () {
            console.log("Getting reviews");
            $.ajax({
                type: "GET",
                url: "/get_reviews/",
                success: function (response) {
                    console.log(response);
                }
            });
        };
        dashboardClass.prototype.ratingView = function () {
            $.ajax({
                type: "GET",
                url: "/ios_app_rating_fragment/",
                success: function (response) {
                    console.log(response);
                    $("#ios_app_review").hide();
                    $("#ios_app_rating").show();
                    $("#ios_app_get_rating_btn").show();
                    $("#ios_app_rating").html(response);
                    $("#reviews_tab").removeClass();
                    $("#ratings_tab").addClass("active");
                }
            });
        };
        return dashboardClass;
    }());
    dashboard.dashboardClass = dashboardClass;
})(dashboard || (dashboard = {}));
//# sourceMappingURL=dashboard.js.map