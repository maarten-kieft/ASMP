var CurrentChart = {
    chart : null,
    max : 0,

    init : function(){
        var chart = Highcharts.chart('js-current-chart',dashboardDonutChartDefaults);
        
        chart.series[0].data[0].y = 0
        chart.series[0].data[0].description = 0;
        chart.yAxis[0].isDirty = true;
        chart.redraw();
        CurrentChart.chart = chart;
    },

    update : function(lastMeasurements){
        var lastMeasurement = lastMeasurements[0];
        var currentUsage = parseFloat(lastMeasurement.currentUsage);
        var chart = CurrentChart.chart;

        if(lastMeasurement.currentUsage > CurrentChart.max){
            CurrentChart.max = currentUsage;
        }

        chart.series[0].data[0].y = currentUsage / (CurrentChart.max / 100)
        chart.series[0].data[0].description = currentUsage * 1000;
        chart.yAxis[0].isDirty = true;
        chart.redraw();
    },

}


