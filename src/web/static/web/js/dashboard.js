var Dashboard = {
    State : {
        MaxCurrentUsage : null,
        CurrentUsageChart : null
    },
    
    Init : function(){
        Dashboard.InitCurrentUsageChart();
    },

    InitCurrentUsageChart : function(){
        Dashboard.State.CurrentUsageChart = Highcharts.chart('donut-container',dashboardDonutChartDefaults);


        Dashboard.UpdateCurrentUsageChart();
        setInterval(Dashboard.UpdateCurrentUsageChart, 10000);  
    },

    UpdateCurrentUsageChart : function(){
        $.ajax({
            url: "/last-current-usage",
            success: function (lastMeasurement) {
                var currentUsage = parseFloat(lastMeasurement.currentUsage);
                
                if(lastMeasurement.currentUsage > Dashboard.State.MaxCurrentUsage){
                    Dashboard.State.MaxCurrentUsage = currentUsage;
                }

                Dashboard.State.CurrentUsageChart.series[0].data[0].y = currentUsage / (Dashboard.State.MaxCurrentUsage / 100)
                Dashboard.State.CurrentUsageChart.series[0].data[0].description = currentUsage * 1000;
                Dashboard.State.CurrentUsageChart.yAxis[0].isDirty = true;
                Dashboard.State.CurrentUsageChart.redraw();
            },
            error: function () {
               
            }
        });
        
        //ajax call doen
        //updaten donut
    }
};

$(document).ready(Dashboard.Init);