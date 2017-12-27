    var Dashboard = {
    State : {
        MaxCurrentUsage : null,
        CurrentUsageChart : null,
        TotalUsageChart : null,
        TotalUsageChartPeriod : "year",
        LoadedComponents : [],
    },
    
    Init: function () {
        powerOverviewChart = new OverviewChart("#js-power-overview-chart", Dashboard.ComponentIntiialized,"power");
        gasOverviewChart = new OverviewChart("#js-gas-overview-chart", Dashboard.ComponentIntiialized,"gas");

        CurrentChart.init(Dashboard.ComponentIntiialized);
        RecentChart.init(Dashboard.ComponentIntiialized);
        Dashboard.Update();
        setInterval(Dashboard.Update, 10000);  
    },

    ComponentIntiialized : function(name){
        Dashboard.State.LoadedComponents.push(name);
        App.ResizeLoadingOverlay()

        if(Dashboard.State.LoadedComponents.length === 3){
            App.PageLoaded();
        }
    },

    Update : function(){
        Dashboard.ToggleLoader(true);
        
        $.ajax({
            url: "/last-measurements",
            success: function (lastMeasurement) {
                CurrentChart.update(lastMeasurement);
                RecentChart.update(lastMeasurement);
                Dashboard.UpdateLastUpdateLabel(lastMeasurement);
                Dashboard.ToggleLoader(false);
            },
            error: function () {
               
            }
        });
    },

    UpdateLastUpdateLabel : function(lastMeasurements){
        var lastMeasurement = lastMeasurements[lastMeasurements.length-1];
          var relativeTimeStamp = lastMeasurement.timestamp ? moment(lastMeasurement.timestamp).fromNow() : "-"; 
          $("#js-last-update-label").html(relativeTimeStamp);

    },

    ToggleLoader : function(showLoader){
        if(showLoader){
            $("#js-loader").removeClass("hide");
            $("#js-last-update-label").addClass("hide");
        }else{
            $("#js-loader").addClass("hide");
            $("#js-last-update-label").removeClass("hide");
        }
    }
};

App.InitPage(Dashboard.Init);
