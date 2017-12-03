var RecentChart = { 
    chart: null,
    lastPoint: null,
        
    init : function(initializedCallback) {
        RecentChart.chart = Highcharts.chart('js-recent-chart',dashboardAreaChartDefaults);
        RecentChart.load();
        initializedCallback("overviewChart");
    },

    load : function(period, startDate){
        var url = "/last-measurements/30";
        
        $.ajax({
            url: url,
            success: function(lastMeasurements){
                var usageData = [];
                var chart = RecentChart.chart;
        
                for(var i=0;i<lastMeasurements.length;i++){
                    var record = lastMeasurements[i];
                    var amount = parseFloat(record.currentUsage)-parseFloat(record.currentReturn);
                    usageData.push([Date.parse(record.timestamp),amount]);
                }

                chart.yAxis[0].isDirty = true;
                chart.series[0].setData(usageData, false);
                chart.redraw();
            }
        });
    },

    update : function(lastMeasurements){
        var chart = RecentChart.chart;

        for(var i =0; i< lastMeasurements.length;i++){
            var lastMeasurement = lastMeasurements[i];
            var amount = parseFloat(lastMeasurement.currentUsage) - parseFloat(lastMeasurement.currentReturn);
            var timestamp = new Date(lastMeasurement.timestamp);

            if(timestamp <= RecentChart.lastPoint){
                continue;
            }

            var shift = RecentChart.chart.series[0].points.length >= 30;
            RecentChart.lastPoint = timestamp;
            chart.series[0].addPoint({x:timestamp, y:amount}, false, shift);
        }
            
        chart.yAxis[0].isDirty = true;
        chart.redraw();
    },
}

