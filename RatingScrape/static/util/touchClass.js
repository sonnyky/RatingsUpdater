/// <reference path="../thirdparty/jquery.d.ts" />
var util;
(function (util) {
    var touchClass = (function () {
        function touchClass(param) {
            this.target = param.target ? param.target : " ";
            this.callback_end = param.callback_end ? param.callback_end : function () { };
            this.doBindings();
        }
        touchClass.prototype.doBindings = function () {
            var _this = this;
            var $ = jQuery;
            $(this.target).on("touchstart mousedown", function (e) {
                e.preventDefault();
            });
            $(this.target).on("touchend mouseup", function (e) {
                e.preventDefault();
                _this.callback_end();
            });
        };
        return touchClass;
    }());
    util.touchClass = touchClass;
})(util || (util = {}));
//# sourceMappingURL=touchClass.js.map