var App = {
    State : {
        Initalized : false,
        PageInitCallback : null
    },
    
    Init : function(){
        App.ResizeLoadingOverlay();
        App.InitTimeZone();
        Highcharts.setOptions({global: {timezone: App.GetTimeZone()}});
        App.State.Initalized = true;
        
        if(App.State.PageInitCallback != null){
            App.State.PageInitCallback();
        } else{
            App.PageLoaded();
        }
    },

    InitTimeZone : function(){
        if (App.GetTimeZone()) {
            return;
        }

        var timeZone = moment.tz.guess();
        var expireDate = 365 * 24 * 60 * 60; // 1 year
        document.cookie = "asmp-timezone="+timeZone+"; max-age=" + expireDate;
        document.location.reload();
    },

    GetTimeZone : function() {
        if (document.cookie.indexOf("asmp-timezone=") === -1) {
            return;
        }
        
        return document.cookie.replace("asmp-timezone=","");
    },

    InitPage : function(pageInitCallback) {
        App.State.PageInitCallback = pageInitCallback;
    },

    ResizeLoadingOverlay : function(){
        $("#loading-overlay").height($("#page-wrapper").height())
    },

    PageLoaded : function(){
        $("#loading-overlay").addClass("hidden");
    }
};

$(document).ready(App.Init);