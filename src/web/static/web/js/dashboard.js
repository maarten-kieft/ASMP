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
        Dashboard.State.CurrentUsageChart = Highcharts.chart('donut-container',dashboardDonutChartDefaults);
    },

    Update(){
         $.ajax({
            url: "/last-current-usage",
            success: function (lastMeasurement) {
                Dashboard.UpdateCurrentUsageChart(lastMeasurement);
                Dashboard.UpdateLastUpdateLabel(lastMeasurement);
            },
            error: function () {
               
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
          var relativeTimeStamp = moment(lastMeasurement.timestamp).fromNow(); 
          $("#js-last-update-label").html(relativeTimeStamp);

    }
};

$(document).ready(Dashboard.Init);