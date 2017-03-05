var dashboardAreaChartDefaults =  {
    navigation : {
        buttonOptions : {
            enabled: false
        }
    },
    colors: ["#2677B5","#4DA707","#d9534f"],
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Daily usage'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
    },
    xAxis: {
        title : {
            text: 'Time'
        },

        type: 'datetime',
    },
    yAxis: {
        title: {
            text: 'KwH'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' KwH'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
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
};