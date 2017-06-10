var OverviewGraph = {
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
                return Highcharts.dateFormat(OverviewGraph.currentPeriod.format, this.value);
            }
        },
        series: [ 
            { 
                name: "Usage",
                cursor: "pointer",
                point: { events: { click: function() {OverviewGraph.handleClick(this);}  }} 
            }
        ]
    },
        
    init : function() {
        $.extend(OverviewGraph.settings,dashboardAreaChartDefaults);

        OverviewGraph.currentPeriod = OverviewGraph.periods[0];
        OverviewGraph.chart = Highcharts.chart('container-area',OverviewGraph.settings);
        OverviewGraph.load();
    },

    load : function(period, startDate){
        var url = "/graph-overview-data";

        if(period && startDate){
            url += "/" + period.period + "/" + startDate;
        }
        
        $.ajax({
            url: url,
            success: OverviewGraph.update
        });
    },

    update :  function (graphData) {
        var data = [];
        var chart = OverviewGraph.chart;
        
        for(var i=0;i<graphData["data"].length;i++){
            var record = graphData["data"][i];
            data.push([Date.parse(record.timestamp),parseFloat(record.usage)])
        }

        chart.yAxis[0].isDirty = true;
        chart.series[0].setData(data, false);
        chart.redraw();
    },

    handleClick : function(e){ 
        var periods = OverviewGraph.periods;
        var currentPeriod = OverviewGraph.currentPeriod;
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
        
        OverviewGraph.currentPeriod = newPeriod;
        OverviewGraph.load(newPeriod,Highcharts.dateFormat('%Y-%m-%d',e.x))
    }
}

