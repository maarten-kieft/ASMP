var OverviewChart = {
    currentPeriod : null, 
    chart: null,
    periods : [
        {period : "year", format : "%b %Y"},
        {period : "month", format : "%b %Y"},
        {period : "day", format : "%b %Y"}
    ],
    settings : { 
        labels: {
            formatter: function() {
                return Highcharts.dateFormat(OverviewChart.currentPeriod.format, this.value);
            }
        },
        series: [ 
            { 
                name: "Usage",
                cursor: "pointer",
                point: { events: { click: function() {OverviewChart.handleClick(this);}  }} 
            }
        ]
    },
        
    init : function() {
        $.extend(OverviewChart.settings,dashboardAreaChartDefaults);

        OverviewChart.currentPeriod = OverviewChart.periods[0];
        OverviewChart.chart = Highcharts.chart('js-overview-chart',OverviewChart.settings);
        OverviewChart.load();
    },

    load : function(period, startDate){
        var url = "/graph-overview-data";

        if(period && startDate){
            url += "/" + period.period + "/" + startDate;
        }
        
        $.ajax({
            url: url,
            success: OverviewChart.update
        });
    },

    update :  function (graphData) {
        var data = [];
        var chart = OverviewChart.chart;
        
        for(var i=0;i<graphData["data"].length;i++){
            var record = graphData["data"][i];
            data.push([Date.parse(record.timestamp),parseFloat(record.usage)])
        }

        chart.yAxis[0].isDirty = true;
        chart.series[0].setData(data, false);
        chart.redraw();
    },

    handleClick : function(e){ 
        var periods = OverviewChart.periods;
        var currentPeriod = OverviewChart.currentPeriod;
        var newPeriod = currentPeriod;

        for(var i=0;i<periods.length;i++){
            if(periods[i].period === currentPeriod.period){
                if(periods.length <= i+1){
                    return
                }

                newPeriod = periods[i+1];
                break;
            }
        }
        
        OverviewChart.currentPeriod = newPeriod;
        OverviewChart.load(newPeriod,Highcharts.dateFormat('%Y-%m-%d',e.x))
    }
}
