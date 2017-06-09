var Dashboard = {
    State : {
        MaxCurrentUsage : null,
        CurrentUsageChart : null,
        TotalUsageChart : null,
    },
    
    Init : function(){
        Dashboard.InitTotalUsageChart();
        Dashboard.InitCurrentUsageChart();
        Dashboard.LoadStatistics();
        Dashboard.Update();
        setInterval(Dashboard.Update, 10000);  
    },

    InitTotalUsageChart : function(){
        var settings = { series: [ { name: "Usage" } ] }
        $.extend(settings,dashboardAreaChartDefaults);

        Dashboard.State.TotalUsageChart = Highcharts.chart('container-area',settings);
        Dashboard.LoadTotalUsageChartData();
    },

    LoadTotalUsageChartData : function(period, startDate){
        var url = "/graph-overview-data";

        if(period && startDate){
            url += "/" + period + "/" + startDate;
        }
        
        $.ajax({
            url: url,
            success: Dashboard.UpdateTotalUsageChart
        });
    },

    UpdateTotalUsageChart :  function (graphData) {
        var data = [];
        var chart = Dashboard.State.TotalUsageChart;
        for(var i=0;i<graphData["data"].length;i++){
            var record = graphData["data"][i];
            data.push([Date.parse(record.timestamp),parseFloat(record.usage)])
        }

        chart.series[0].setData(data, false);
        chart.redraw();
    },

    InitCurrentUsageChart : function(){
        var chart = Highcharts.chart('donut-container',dashboardDonutChartDefaults);
        
        chart.series[0].data[0].y = 0
        chart.series[0].data[0].description = 0;
        chart.yAxis[0].isDirty = true;
        chart.redraw();
        Dashboard.State.CurrentUsageChart = chart;
    },

    Update : function(){
        Dashboard.ToggleLoader(true);
        
        $.ajax({
            url: "/last-current-usage",
            success: function (lastMeasurement) {
                Dashboard.UpdateCurrentUsageChart(lastMeasurement);
                Dashboard.UpdateLastUpdateLabel(lastMeasurement);
                Dashboard.ToggleLoader(false);
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

    LoadStatistics : function(){
        $("#js-statistics-loader").removeClass("hidden");
        $("#js-statistics-table").addClass("hidden");
         
         $.ajax({
            url: "/statistics",
            success: function (statistics) {
                var current = statistics.current ? statistics.current.usage : 0;               
                var previous = statistics.previous ? statistics.previous.usage : 0;
                var min = statistics.min ? statistics.min.usage : 0;
                var max = statistics.max ? statistics.max.usage : 0;
                var avg = statistics.avg;

                $("#js-stats-current-row td:eq(1)").html(current + " kWh");
                $("#js-stats-previous-row td:eq(1)").html(previous + " kWh");
                $("#js-stats-min-row td:eq(1)").html(min + " kWh");
                $("#js-stats-max-row td:eq(1)").html(max + " kWh");
                $("#js-stats-avg-row td:eq(1)").html(avg + " kWh");

                $("#js-statistics-loader").addClass("hidden");
                $("#js-statistics-table").removeClass("hidden");

            },
            error: function () {
               
            },
            complete: function(){
                Dashboard.ToggleLoader(false);
            }
        });
        
                            
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