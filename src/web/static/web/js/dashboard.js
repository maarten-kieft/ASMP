var Dashboard = {
    State : {
        MaxCurrentUsage : null,
        CurrentUsageChart : null,
        TotalUsageChart : null,
        TotalUsageChartPeriod : "year",
        LoadedComponents : []
    },
    
    Init : function(){
        Highcharts.setOptions({global: {timezone: 'Europe/Amsterdam'}});

        OverviewChart.init(Dashboard.ComponentIntiialized);
        CurrentChart.init(Dashboard.ComponentIntiialized);
        RecentChart.init(Dashboard.ComponentIntiialized);
        Dashboard.Update();
        setInterval(Dashboard.Update, 10000);  
    },

    ComponentIntiialized : function(name){
        Dashboard.State.LoadedComponents.push(name);
        $("#loading-overlay").height($("#page-wrapper").height())

        if(Dashboard.State.LoadedComponents.length === 3){
            $("#loading-overlay").addClass("hidden")
            $("#page-wrapper").removeClass("hidden")
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

$(document).ready(Dashboard.Init);