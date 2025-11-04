
import React from 'react';
import { Card } from '../components/common/Card';
import { Button } from '../components/common/Button';
import { useToast } from '../context/AppContext';

const ReportCard: React.FC<{ title: string, description: string }> = ({ title, description }) => {
    const addToast = useToast();
    const handleExport = (format: string) => {
        addToast(`Exporting ${title} as ${format}...`, 'info');
        // In a real app, this would trigger a download.
    };

    return (
        <Card>
            <h3 className="text-xl font-semibold mb-2">{title}</h3>
            <p className="text-gray-600 dark:text-gray-400 mb-4">{description}</p>
            <div className="flex space-x-2">
                <Button onClick={() => handleExport('CSV')}>Export CSV</Button>
                <Button variant="secondary" onClick={() => handleExport('PDF')}>Export PDF</Button>
            </div>
        </Card>
    );
};

const ReportsPage: React.FC = () => {
    return (
        <div>
            <h1 className="text-3xl font-bold mb-6">Reports</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <ReportCard
                    title="Profit & Loss Statement"
                    description="View your business's financial performance over a specific period of time."
                />
                <ReportCard
                    title="Balance Sheet"
                    description="Get a snapshot of your company's financial health at a single point in time."
                />
                <ReportCard
                    title="Sales Tax Report"
                    description="Summarizes the sales tax you've collected from customers for easy filing."
                />
                <ReportCard
                    title="Inventory Summary"
                    description="Detailed report of stock levels, values, and turnover rates for all your products."
                />
            </div>
        </div>
    );
};

export default ReportsPage;
