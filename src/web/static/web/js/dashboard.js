var Dashboard = {
    State : {
        MaxCurrentUsage : null,
        CurrentUsageChart : null,
    },
    
    Init : function(){
        Dashboard.InitTotalUsageChart();
        Dashboard.InitCurrentUsageChart();
        Dashboard.Update();
        setInterval(Dashboard.Update, 10000);  
    },

    InitTotalUsageChart : function(){
        Highcharts.chart('container-area',dashboardAreaChartDefaults);
    },

    InitCurrentUsageChart : function(){
        var chart = Highcharts.chart('donut-container',dashboardDonutChartDefaults);
        
        chart.series[0].data[0].y = 0
        chart.series[0].data[0].description = 0;
        chart.yAxis[0].isDirty = true;
        chart.redraw();
        Dashboard.State.CurrentUsageChart = chart;
    },

    Update(){
        Dashboard.ToggleLoader(true);
        
        $.ajax({
            url: "/last-current-usage",
            success: function (lastMeasurement) {
                Dashboard.UpdateCurrentUsageChart(lastMeasurement);
                Dashboard.UpdateLastUpdateLabel(lastMeasurement);
            },
            error: function () {
               
            },
            complete: function(){
                Dashboard.ToggleLoader(false);
            }
        });
    },

    UpdateCurrentUsageChart : function(lastMeasurement){
        var currentUsage = parseFloat(lastMeasurement.currentUsage);
      
        if(lastMeasurement.currentUsage > Dashboard.State.MaxCurrentUsage){
            Dashboard.State.MaxCurrentUsage = currentUsage;
        }

        Dashboard.State.CurrentUsageChart.series[0].data[0].y = currentUsage / (Dashboard.State.MaxCurrentUsage / 100)
        Dashboard.State.CurrentUsageChart.series[0].data[0].description = currentUsage * 1000;
        Dashboard.State.CurrentUsageChart.yAxis[0].isDirty = true;
        Dashboard.State.CurrentUsageChart.redraw();
    },

    UpdateLastUpdateLabel : function(lastMeasurement){
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