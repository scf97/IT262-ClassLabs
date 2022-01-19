    google.charts.load('current', {
      'packages': ['gantt']
    });
    google.charts.setOnLoadCallback(drawChart);

    function daysToMilliseconds(days) {
      return days * 24 * 60 * 60 * 1000;
    }

    function drawChart() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Task ID');
      data.addColumn('string', 'Task Name');
      data.addColumn('date', 'Start Date');
      data.addColumn('date', 'End Date');
      data.addColumn('number', 'Duration');
      data.addColumn('number', 'Percent Complete');
      data.addColumn('string', 'Dependencies');

      data.addRows([
        ['P1', 'Initiate', new Date(2021, 0, 1), new Date(2021, 0, 7), null, 100, null],
        ['P2', 'Plan', new Date(2021, 0, 9), new Date(2021, 0, 13), null, 100, 'P1'],
        ['P3', 'Execute', new Date(2021, 0, 15), new Date(2021, 0, 20), null, 100, 'P2'],
        ['P4', 'Evaluate', new Date(2021, 0, 23), new Date(2021, 0, 25), null, 57, 'P3'],
        ['P5', 'Close', new Date(2021, 0, 26), new Date(2021, 0, 30), null, 0, 'P4']
      ]);

      var options = {
        height: 275
      };

      var chart = new google.visualization.Gantt(document.getElementById('chart_div'));

      chart.draw(data, options);
    }
