import React, { useState, useEffect, useRef } from 'react'; // useRef import 추가
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import 'chartjs-adapter-date-fns';
import { Chart, TimeScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend } from 'chart.js';

// 필요한 컴포넌트 등록
Chart.register(TimeScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend);



const ServerStatus = () => {
    const [cpuData, setCpuData] = useState([]);
    const [memoryData, setMemoryData] = useState([]);
    const [labels, setLabels] = useState([]);


    const chartRef = useRef(null);

    useEffect(() => {
        const interval = setInterval(() => {
            axios.get('http://220.69.203.87:30080/api/server-status/metrics/')
                .then((response) => {
                    const { cpu_usage, memory_percentage } = response.data;

                    setCpuData((prevData) => [...prevData, cpu_usage].slice(-10));
                    setMemoryData((prevData) => [...prevData, memory_percentage].slice(-10));
                    setLabels((prevLabels) => [...prevLabels, new Date()].slice(-10)); // Date 객체 사용
                })
                .catch((error) => {
                    console.error('서버 상태를 가져오는 중 오류 발생:', error);
                });
        }, 1000);

        return () => clearInterval(interval);
    }, []);

    const data = {
        labels: labels,
        datasets: [
            {
                label: 'CPU 사용량 (%)',
                data: cpuData,
                borderColor: 'rgba(75, 192, 192, 1)',
                fill: false,
            },
            {
                label: '메모리 사용량 (%)',
                data: memoryData,
                borderColor: 'rgba(153, 102, 255, 1)',
                fill: false,
            },
        ],
    };

    const options = {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'second'
                }
            },
            y: {
                beginAtZero: true,
                max: 100
            }
        }
    };

    return (
        <div>
            <h2>서버 상태</h2>
            <Line data={data} options={options} />
        </div>
    );
};

export default ServerStatus;
