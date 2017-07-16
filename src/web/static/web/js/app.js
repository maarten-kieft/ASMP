var App = {
    State : {
        Initalized : false,
        Page : null
    },
    
    Init : function(){
        App.InitTimeZone();
        Highcharts.setOptions({global: {timezone: App.GetTimeZone()}});
        App.State.Initalized = true;

        if(App.State.Page != null){
            App.State.Page();
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

    InitPage : function(page) {
        App.State.Page = page;
    },

    PageLoaded : function(){
        $("#loading-overlay").addClass("hidden");
        $("#page-wrapper").removeClass("hidden");
    }
};

$(document).ready(App.Init);