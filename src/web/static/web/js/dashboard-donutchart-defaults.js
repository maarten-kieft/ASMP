var dashboardDonutChartDefaults =  {
    navigation : {
        buttonOptions : {
            enabled: false
        }
    },
    chart: {
        type: 'solidgauge',
        marginTop: 50
    },
    title: {
        text: ''
    },
    pane: {
        startAngle: 0,
        endAngle: 360,
        background: [
            { // Track for Move
                outerRadius: '112%',
                innerRadius: '88%',
                backgroundColor: Highcharts.Color("#2677B5").setOpacity(0.3).get(),
                borderWidth: 0
            }
        ]
    },
    yAxis: {
        min: 0,
        max: 100,
        lineWidth: 0,
        tickPositions: []
    },
    plotOptions: {
        solidgauge: {
            dataLabels: {
                enabled: true,
                format: '<p><span style="font-size:72px; color: {point.color}; font-weight: bold; text-align:center;">{point.description}</span><br/>watt</p>',
                borderWidth:0
            },
            linecap: 'round',
            stickyTracking: false,
            rounded: true
        }
    },

    series: [{
        name: 'Move',
        borderColor: Highcharts.getOptions().colors[0],
        data: [{
            color: "#2677B5",
            radius: '112%',
            innerRadius: '88%',
            y: 0
        }]
    }
    ]
};