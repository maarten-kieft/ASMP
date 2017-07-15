var OverviewChart = {
    currentPeriod : null, 
    startDate: null,
    chart: null,
    periods : [
        {period : "year", format : "%b %Y", momentInterval : "years"},
        {period : "month", format : "%b %Y", momentInterval : "months"},
        {period : "day", format : "%b %Y", momentInterval : "days"}
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
                point: { events: { click: function() {OverviewChart.handleBarClick(this);}  }} 
            }
        ]
    },
        
    init : function(initializedCallback) {
        $.extend(OverviewChart.settings,dashboardBarChartDefaults);

        OverviewChart.currentPeriod = OverviewChart.periods[0];
        OverviewChart.startDate = moment().startOf('year');
        OverviewChart.chart = Highcharts.chart('js-overview-chart',OverviewChart.settings);
        OverviewChart.load();
        OverviewChart.initBindings();
        initializedCallback("overviewChart");
    },

    initBindings : function(){
        $("#js-overview-chart-prev").click(function(){OverviewChart.handleNavClick("prev")});
        $("#js-overview-chart-next").click(function(){OverviewChart.handleNavClick("next")});
        $("#js-overview-chart-zoomout").click(OverviewChart.handleZoomOutClick);
    },

    load : function(period, startDate){
        $("#js-overview-chart-loader-overlay").removeClass("hidden");
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
        $("#js-overview-chart-loader-overlay").addClass("hidden");
    },

    handleBarClick : function(e){ 
        var newPeriod = OverviewChart.getNewPeriod("next");
        var startDate = Highcharts.dateFormat('%Y-%m-%d',e.x);
        
        OverviewChart.currentPeriod = newPeriod;
        OverviewChart.startDate = moment(startDate, "YYYY-MM-DD")
        OverviewChart.load(newPeriod,startDate)
    },

    handleZoomOutClick : function(){
        var newPeriod = OverviewChart.getNewPeriod("prev");
          
        OverviewChart.currentPeriod = newPeriod;
        OverviewChart.startDate.startOf(newPeriod.period);
        OverviewChart.load(newPeriod,OverviewChart.startDate.format("YYYY-MM-DD"))
    },

    handleNavClick : function(direction){
        var period = OverviewChart.currentPeriod;
        var amount = direction == "prev" ? -1 : 1;
        OverviewChart.startDate =OverviewChart.startDate.add(amount, period.momentInterval);
        OverviewChart.load(period,OverviewChart.startDate.format("YYYY-MM-DD"));
    },

    getNewPeriod : function(direction){
        var periods = OverviewChart.periods;
        var currentPeriod = OverviewChart.currentPeriod;
        var index = periods.findIndex(p => p.period === currentPeriod.period);

        if(direction == "next"){
            return periods.length <= index+1
                ?  currentPeriod
                : periods[index+1];
        }
        
        return index == 0
            ? currentPeriod
            : periods[index-1];
    }


}

