
import React from 'react';
import { Card } from '../components/common/Card';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart, Line } from 'recharts';

const salesData = [
    { name: 'Jan', revenue: 4000, expenses: 2400, profit: 1600 },
    { name: 'Feb', revenue: 3000, expenses: 1398, profit: 1602 },
    { name: 'Mar', revenue: 2000, expenses: 9800, profit: -7800 },
    { name: 'Apr', revenue: 2780, expenses: 3908, profit: -1128 },
    { name: 'May', revenue: 1890, expenses: 4800, profit: -2910 },
    { name: 'Jun', revenue: 2390, expenses: 3800, profit: -1410 },
    { name: 'Jul', revenue: 3490, expenses: 4300, profit: -810 },
];

const StatCard: React.FC<{ title: string; value: string; change: string; changeType: 'increase' | 'decrease' }> = ({ title, value, change, changeType }) => (
    <Card>
        <h4 className="text-sm font-medium text-gray-500 dark:text-gray-400">{title}</h4>
        <div className="mt-1 text-3xl font-semibold text-gray-900 dark:text-white">{value}</div>
        <div className={`mt-1 text-sm ${changeType === 'increase' ? 'text-green-600' : 'text-red-600'}`}>
            {change} vs last month
        </div>
    </Card>
);

const DashboardPage: React.FC = () => {
    return (
        <div className="space-y-6">
            <h1 className="text-3xl font-bold">Dashboard</h1>
            
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <StatCard title="Total Sales" value="$12,345" change="+12.5%" changeType="increase" />
                <StatCard title="Total Purchases" value="$5,678" change="+8.2%" changeType="increase" />
                <StatCard title="Net Profit" value="$6,667" change="-2.1%" changeType="decrease" />
                <StatCard title="Low Stock Items" value="5" change="+1 item" changeType="increase" />
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <Card title="Revenue vs Expenses">
                    <ResponsiveContainer width="100%" height={300}>
                        <BarChart data={salesData}>
                            <CartesianGrid strokeDasharray="3 3" className="stroke-gray-200 dark:stroke-gray-700" />
                            <XAxis dataKey="name" />
                            <YAxis />
                            <Tooltip contentStyle={{ backgroundColor: 'rgba(31, 41, 55, 0.8)', border: 'none' }} />
                            <Legend />
                            <Bar dataKey="revenue" fill="#3b82f6" name="Revenue" />
                            <Bar dataKey="expenses" fill="#ef4444" name="Expenses" />
                        </BarChart>
                    </ResponsiveContainer>
                </Card>
                <Card title="Profit/Loss Trend">
                     <ResponsiveContainer width="100%" height={300}>
                        <LineChart data={salesData}>
                            <CartesianGrid strokeDasharray="3 3" className="stroke-gray-200 dark:stroke-gray-700" />
                            <XAxis dataKey="name" />
                            <YAxis />
                            <Tooltip contentStyle={{ backgroundColor: 'rgba(31, 41, 55, 0.8)', border: 'none' }}/>
                            <Legend />
                            <Line type="monotone" dataKey="profit" stroke="#10b981" name="Profit/Loss" strokeWidth={2} />
                        </LineChart>
                    </ResponsiveContainer>
                </Card>
            </div>
        </div>
    );
};

export default DashboardPage;
