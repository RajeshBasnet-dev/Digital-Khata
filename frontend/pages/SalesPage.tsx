
import React, { useState, useEffect } from 'react';
import { Sale } from '../types';
import { getSales } from '../services/api';
import { Button } from '../components/common/Button';
import { Modal } from '../components/common/Modal';
import { Input } from '../components/common/Input';
import { useToast } from '../context/AppContext';

const SalesPage: React.FC = () => {
    const [sales, setSales] = useState<Sale[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const addToast = useToast();

    useEffect(() => {
        fetchSales();
    }, []);

    const fetchSales = async () => {
        setIsLoading(true);
        try {
            const data = await getSales();
            setSales(data);
        } catch (error) {
            addToast('Failed to fetch sales data', 'error');
        } finally {
            setIsLoading(false);
        }
    };
    
    const getStatusBadge = (status: Sale['status']) => {
        switch (status) {
            case 'Paid': return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300';
            case 'Unpaid': return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-300';
            case 'Overdue': return 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-300';
        }
    };

    return (
        <div>
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold">Sales</h1>
                <Button onClick={() => setIsModalOpen(true)}>Create Invoice</Button>
            </div>
            <div className="bg-white dark:bg-gray-800 shadow-md rounded-lg overflow-x-auto">
                <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                    <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" className="px-6 py-3">Invoice #</th>
                            <th scope="col" className="px-6 py-3">Customer</th>
                            <th scope="col" className="px-6 py-3">Date</th>
                            <th scope="col" className="px-6 py-3">Amount</th>
                            <th scope="col" className="px-6 py-3">Status</th>
                            <th scope="col" className="px-6 py-3">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {isLoading ? (
                            <tr><td colSpan={6} className="text-center p-6">Loading...</td></tr>
                        ) : (
                            sales.map(sale => (
                                <tr key={sale.id} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                                    <td className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">{sale.invoiceNumber}</td>
                                    <td className="px-6 py-4">{sale.customerName}</td>
                                    <td className="px-6 py-4">{sale.date}</td>
                                    <td className="px-6 py-4">${sale.amount.toFixed(2)}</td>
                                    <td className="px-6 py-4">
                                        <span className={`px-2 py-1 text-xs font-medium rounded-full ${getStatusBadge(sale.status)}`}>
                                            {sale.status}
                                        </span>
                                    </td>
                                    <td className="px-6 py-4 space-x-2">
                                        <Button size="sm">View</Button>
                                    </td>
                                </tr>
                            ))
                        )}
                    </tbody>
                </table>
            </div>

            <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Create New Invoice">
                <form className="space-y-4">
                     <Input label="Customer Name" name="customerName" required />
                     <Input label="Invoice Date" name="date" type="date" required />
                     {/* In a real app, this would be a list of products to add */}
                     <Input label="Amount" name="amount" type="number" required />
                     <div className="flex justify-end gap-2 pt-4">
                        <Button type="button" variant="secondary" onClick={() => setIsModalOpen(false)}>Cancel</Button>
                        <Button type="submit">Create Invoice</Button>
                    </div>
                </form>
            </Modal>
        </div>
    );
};

export default SalesPage;
