var RecentChart = { 
    chart: null,
    lastPoint: null,
    settings : { 
        series: [ 
            { name: "Usage"},
            { name: "Return"}
        ]
    },
        
    init : function(initializedCallback) {
        $.extend(RecentChart.settings,dashboardAreaChartDefaults);

        RecentChart.chart = Highcharts.chart('js-recent-chart',RecentChart.settings);
        RecentChart.load();
        initializedCallback("overviewChart");
    },

    load : function(period, startDate){
        var url = "/last-measurements/30";
        
        $.ajax({
            url: url,
            success: function(lastMeasurements){
                var usageData = [];
                var returnData = [];
                var chart = RecentChart.chart;
        
                for(var i=0;i<lastMeasurements.length;i++){
                    var record = lastMeasurements[i];
                    usageData.push([Date.parse(record.timestamp),parseFloat(record.currentUsage)]);
                    returnData.push([Date.parse(record.timestamp),-parseFloat(record.currentReturn)])
                }

                chart.yAxis[0].isDirty = true;
                chart.series[0].setData(usageData, false);
                chart.series[1].setData(returnData, false);
                chart.redraw();
            }
        });
    },

    update : function(lastMeasurements){
        var chart = RecentChart.chart;

        for(var i =0; i< lastMeasurements.length;i++){
            var lastMeasurement = lastMeasurements[i];
            var currentUsage = parseFloat(lastMeasurement.currentUsage);
            var currentReturn = parseFloat(lastMeasurement.currentReturn);
            var timestamp = new Date(lastMeasurement.timestamp);

            if(timestamp <= RecentChart.lastPoint){
                continue;
            }

            var shift = RecentChart.chart.series[0].points.length >= 30;
            RecentChart.lastPoint = timestamp;
            chart.series[0].addPoint({x:timestamp, y:currentUsage}, false, shift);
            chart.series[1].addPoint({x:timestamp, y:-currentReturn}, false, shift);

        }
            
        chart.yAxis[0].isDirty = true;
        chart.redraw();
    },
}

