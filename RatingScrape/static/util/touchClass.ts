/// <reference path="../thirdparty/jquery.d.ts" />
interface touchInterface{
	target:string;
	callback_end:Function;
}

module util{
	export class touchClass implements touchInterface{

		target:string;
		callback_end:Function;

		constructor(param:any){
			this.target = param.target?param.target:" ";
			this.callback_end = param.callback_end?param.callback_end : function(){};

			this.doBindings();
		}

		doBindings(){
			var $ = jQuery;
			$(this.target).on("touchstart",(e)=>{
				e.preventDefault();
				});
			$(this.target).on("touchend",(e)=>{
				e.preventDefault();
				this.callback_end();
				})
		}

	}
}