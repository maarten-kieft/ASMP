var OverviewChart = {
    currentPeriod : null, 
    startDate: null,
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
        
    init : function(initializedCallback) {
        $.extend(OverviewChart.settings,dashboardBarChartDefaults);

        OverviewChart.currentPeriod = OverviewChart.periods[0];
        OverviewChart.startDate = moment().startOf('year');
        OverviewChart.chart = Highcharts.chart('js-overview-chart',OverviewChart.settings);
        OverviewChart.load();
        initializedCallback("overviewChart");
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
            if(i > 23 && OverviewChart.currentPeriod.period == "day"){
                break;
            }

            var record = graphData["data"][i];
            data.push([Date.parse(record.timestamp),parseFloat(record.usage)])
        }

        var min = OverviewChart.startDate.toDate();
        var max = OverviewChart.startDate.clone().endOf(OverviewChart.currentPeriod.period).toDate();
        chart.xAxis[0].setExtremes(min,max,true,true);
        chart.xAxis[0].isDirty = true;

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
        OverviewChart.startDate = moment(Highcharts.dateFormat('%Y-%m-%d',e.x), "YYYY-MM-DD")
        OverviewChart.load(newPeriod,Highcharts.dateFormat('%Y-%m-%d',e.x))
    }
}

