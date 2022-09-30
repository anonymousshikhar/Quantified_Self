<template>
  <Line :chart-data="chartData" :key="this.cdata" />
</template>

<script>
// DataPage.vue
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "line-chart",
  components: { Line },
  props: ["cdata"],
  data() {
    console.log(this.cdata)
    return {

      chartOptions: {
        responsive: true
      },
    }
  },
  computed:{
    chartData() {
      return{
        labels: this.cdata.labels,
        datasets: [
          { 
            data: this.cdata.cdata ,
            borderColor: 'rgba(0,0,0,0.4)',
            fill:true,
            tension:0.3,
            
          }
        ],
      }
  }
  },
};
</script>
