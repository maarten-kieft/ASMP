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
       

        $.ajax({
            url: "/graph-overview-data",
            success: function (graphData) {
                var data = [];
                
                for(var i=0;i<graphData["current"].length;i++){
                    var record = graphData["current"][i];
                    data.push([Date.parse(record.timestamp),parseFloat(record.usage)])
                }


                var settings = {
                    series: [
                        {
                            name: "Today",
                            data: data
                        }
                    ]
                }

                $.extend(settings,dashboardAreaChartDefaults);

                 Dashboard.State.TotalUsageChart = Highcharts.chart('container-area',settings);
            },
            error: function () {
               
            }
        });
/*
        series: [{
        name: 'Today',
        data: [
            [Date.UTC(2017,10,1,9,0),2.34],
            [Date.UTC(2017,10,1,10,0),3.34],
            [Date.UTC(2017,10,1,11,0),2.54],
            [Date.UTC(2017,10,1,12,0),1.34],
            [Date.UTC(2017,10,1,13,0),6.34],
            [Date.UTC(2017,10,1,14,0),1.54]
        ]
    }, {
        name: 'Yesterday',
        data: [
            [Date.UTC(2017,10,1,9,0),2.34],
            [Date.UTC(2017,10,1,10,0),1.34],
            [Date.UTC(2017,10,1,11,0),2.87],
            [Date.UTC(2017,10,1,12,0),4.24],
            [Date.UTC(2017,10,1,13,0),2.34],
            [Date.UTC(2017,10,1,14,0),2.54]
        ]
    }, {
        name: 'Average',
        data: [
            [Date.UTC(2017,10,1,9,0),0.34],
            [Date.UTC(2017,10,1,10,0),3.34],
            [Date.UTC(2017,10,1,11,0),5.87],
            [Date.UTC(2017,10,1,12,0),6.24],
            [Date.UTC(2017,10,1,13,0),1.34],
            [Date.UTC(2017,10,1,14,0),3.54]
        ]
    }]
*/
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