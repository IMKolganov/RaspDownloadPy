import React, { useEffect, useState } from 'react';

const Dashboard = () => {
    const [temperature, setTemperature] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('/api/temperature')
            .then(response => response.json())
            .then(data => {
                setTemperature(data.temperature);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching temperature:', error);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Dashboard</h1>
            <p>Current Temperature: {temperature}°C</p>
        </div>
    );
};

export default Dashboard;
