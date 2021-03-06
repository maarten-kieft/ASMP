var dashboardDonutChartDefaults =  {
    navigation : {
        buttonOptions : {
            enabled: false
        }
    },
    chart: {
        type: 'solidgauge',
        marginTop: 0,
        spacingTop:0
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
    tooltip: {
        enabled: false
    },
    plotOptions: {
        solidgauge: {
            dataLabels: {
                enabled: true,
                format: '<span style="font-size:62px; color: {point.color}; font-weight: bold;">{point.description}</span><span style="font-size:8px;">Watt</span>',
                borderWidth:0
            },
            linecap: 'round',
            stickyTracking: false,
            rounded: true
        }
    },

    series: [{
        name: 'Current usage',
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