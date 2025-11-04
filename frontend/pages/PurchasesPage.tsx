
import React, { useState, useEffect } from 'react';
import { Purchase } from '../types';
import { getPurchases } from '../services/api';
import { Button } from '../components/common/Button';
import { Modal } from '../components/common/Modal';
import { Input } from '../components/common/Input';
import { useToast } from '../context/AppContext';

const PurchasesPage: React.FC = () => {
    const [purchases, setPurchases] = useState<Purchase[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const addToast = useToast();

    useEffect(() => {
        fetchPurchases();
    }, []);

    const fetchPurchases = async () => {
        setIsLoading(true);
        try {
            const data = await getPurchases();
            setPurchases(data);
        } catch (error) {
            addToast('Failed to fetch purchases data', 'error');
        } finally {
            setIsLoading(false);
        }
    };
    
    const getStatusBadge = (status: Purchase['status']) => {
        switch (status) {
            case 'Paid': return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300';
            case 'Unpaid': return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-300';
        }
    };

    return (
        <div>
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold">Purchases</h1>
                <Button onClick={() => setIsModalOpen(true)}>Add Purchase Bill</Button>
            </div>
            <div className="bg-white dark:bg-gray-800 shadow-md rounded-lg overflow-x-auto">
                <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                    <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" className="px-6 py-3">Bill #</th>
                            <th scope="col" className="px-6 py-3">Supplier</th>
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
                            purchases.map(purchase => (
                                <tr key={purchase.id} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                                    <td className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">{purchase.billNumber}</td>
                                    <td className="px-6 py-4">{purchase.supplierName}</td>
                                    <td className="px-6 py-4">{purchase.date}</td>
                                    <td className="px-6 py-4">${purchase.amount.toFixed(2)}</td>
                                    <td className="px-6 py-4">
                                        <span className={`px-2 py-1 text-xs font-medium rounded-full ${getStatusBadge(purchase.status)}`}>
                                            {purchase.status}
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
            <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title="Add New Purchase Bill">
                <form className="space-y-4">
                     <Input label="Supplier Name" name="supplierName" required />
                     <Input label="Bill Date" name="date" type="date" required />
                     <Input label="Amount" name="amount" type="number" required />
                     <div className="flex justify-end gap-2 pt-4">
                        <Button type="button" variant="secondary" onClick={() => setIsModalOpen(false)}>Cancel</Button>
                        <Button type="submit">Save Bill</Button>
                    </div>
                </form>
            </Modal>
        </div>
    );
};

export default PurchasesPage;
