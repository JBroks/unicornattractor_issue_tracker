// PIE CHART
chart = new Highcharts.chart('ticket-type-chart', {
  chart: {
    type: 'pie'
  },
  title: {
    style: {
      display: 'none'
    }
  },
  subtitle: {
    text: 'Click the slices to view tickets by status',
  },
  credits: {
    enabled: false
  },
  accessibility: {
    announceNewData: {
      enabled: true
    },
    point: {
      valueSuffix: '%'
    }
  },

  plotOptions: {
    series: {
      dataLabels: {
        enabled: false,
      },
      showInLegend: true,
    }
  },

  tooltip: {
    headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
    pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
  },
  colors: ['#63d37b', '#fcd731', '#ef6354', '#2e3190', '#88fca1', '#fceb9f', '#fcdcd7', '#494de3', '#ee5140'],
  series: [{
    name: "Tickets",
    colorByPoint: true,
    data: [{
        name: "Bugs",
        y: 62.74,
        drilldown: "Bugs"
      },
      {
        name: "Features",
        y: 10.57,
        drilldown: "Features"
      }
    ]
  }],
  drilldown: {
    series: [{
        name: "Bugs",
        id: "Bugs",
        data: [
          [
            "Open",
            1.02
          ],
          [
            "In progress",
            7.36
          ],
          [
            "Completed",
            0.35
          ],
          [
            "Closed",
            0.11
          ]
        ]
      },
      {
        name: "Features",
        id: "Features",
        data: [
          [
            "Open",
            1.02
          ],
          [
            "In progress",
            7.36
          ],
          [
            "Completed",
            0.35
          ],
          [
            "Closed",
            0.11
          ]
        ]
      }
    ],

    drillUpButton: {
      position: {
        verticalAlign: top,
        x: -5,
        y: 10
      },
      theme: undefined
    }
  },
  lang: {
    drillUpText: '< Back'
  },
});
