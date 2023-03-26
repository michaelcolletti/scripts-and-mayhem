import { Grafana } from 'cdk8s-grafana';

// inside your chart:
const grafana = new Grafana(this, 'my-grafana', {
  defaultDataSource: {
    name: 'Prometheus',
    type: 'prometheus',
    access: 'proxy',
    url: 'http://prometheus-service:9090',
  }
});
const github = grafana.addDatasource('github', ...);
const dashboard = grafana.addDashboard('my-dashboard', {
  title: 'My Dashboard',
  refreshRate: Duration.seconds(10),
  timeRange: Duration.hours(6), // show metrics from now-6h to now
  plugins: [
    {
      name: 'grafana-piechart-panel',
      version: '1.3.6',
    }
  ],
});
