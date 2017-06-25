var RecentChart = { 
    chart: null,
    lastPoint: null,
    settings : { 
        /*labels: {
            formatter: function() {
                return Highcharts.dateFormat(OverviewChart.currentPeriod.format, this.value);
            }
        },*/
        series: [ 
            { 
                name: "Usage"
            /*
                point: { events: { click: function() {OverviewChart.handleClick(this);}  }} 
                */
            }
        ]
    },
        
    init : function() {
        $.extend(RecentChart.settings,dashboardAreaChartDefaults);

        RecentChart.chart = Highcharts.chart('js-recent-chart',RecentChart.settings);
        RecentChart.load();
    },

    load : function(period, startDate){
        var url = "/last-current-usage/30";
        
        $.ajax({
            url: url,
            success: function(lastMeasurements){
                 var data = [];
                var chart = RecentChart.chart;
        
                for(var i=0;i<lastMeasurements.length;i++){
                    var record = lastMeasurements[i];
                    data.push([Date.parse(record.timestamp),parseFloat(record.currentUsage)])
                }

                chart.yAxis[0].isDirty = true;
                chart.series[0].setData(data, false);
                chart.redraw();
            }
        });
    },

    update : function(lastMeasurements){
        var chart = RecentChart.chart;

        for(var i =0; i< lastMeasurements.length;i++){
            var lastMeasurement = lastMeasurements[i];
            var currentUsage = parseFloat(lastMeasurement.currentUsage);
            var timestamp = Date.parse(lastMeasurement.timestamp);

            if(timestamp <= RecentChart.lastPoint){
                continue;
            }

            var shift = RecentChart.chart.series[0].points.length >= 30;
            RecentChart.lastPoint = timestamp;
            chart.series[0].addPoint([timestamp, currentUsage], false, shift);
        }
            
        chart.yAxis[0].isDirty = true;
        chart.redraw();
    },
}

