var CurrentChart = {
    chart : null,
    max : 0,
    min: 0,
    color: null,

    init : function(initializedCallback){
        CurrentChart.initChart();
        initializedCallback("currentChart");
    },

    initChart : function(color){
        var options = dashboardDonutChartDefaults;

        if(color){
            options.pane.background[0].backgroundColor = Highcharts.Color(color).setOpacity(0.3).get();
            options.series[0].data[0].color = color;
        }

        if(CurrentChart.chart){
            CurrentChart.chart.destroy();
        }

        CurrentChart.chart = Highcharts.chart('js-current-chart',options);
    },

    update : function(lastMeasurements){
        var lastMeasurement = lastMeasurements[0];
        var currentUsage = parseFloat(lastMeasurement.currentUsage);
        var currentReturn = parseFloat(lastMeasurement.currentReturn);
        var amount = currentUsage - currentReturn ;
        var color = amount < 0 ? "#4da74d" : "#2677B5";

        if(amount > CurrentChart.max){
            CurrentChart.max = amount;
        }

        if(amount < CurrentChart.min){
            CurrentChart.min = amount;
        }

        if(color !== CurrentChart.color){
            CurrentChart.initChart(color);
            CurrentChart.color = color;
        }

        var chart = CurrentChart.chart;
        chart.series[0].data[0].y = Math.abs(amount) / (CurrentChart.max / 100)
        chart.series[0].data[0].description = amount * 1000;
        chart.yAxis[0].isDirty = true;
        chart.redraw();
    },

}


