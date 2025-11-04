
import React, { useState, useEffect } from 'react';
import { Account } from '../types';
import { getChartOfAccounts } from '../services/api';
import { useToast } from '../context/AppContext';
import { Card } from '../components/common/Card';

const AccountList: React.FC<{ title: string, accounts: Account[] }> = ({ title, accounts }) => (
    <Card title={title}>
        <ul className="divide-y divide-gray-200 dark:divide-gray-700">
            {accounts.map(account => (
                <li key={account.id} className="py-3 flex justify-between items-center">
                    <span className="text-gray-900 dark:text-white">{account.name}</span>
                    <span className={`font-mono ${account.balance >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                        ${Math.abs(account.balance).toFixed(2)}
                    </span>
                </li>
            ))}
        </ul>
    </Card>
);

const AccountingPage: React.FC = () => {
    const [accounts, setAccounts] = useState<Account[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const addToast = useToast();

    useEffect(() => {
        const fetchAccounts = async () => {
            setIsLoading(true);
            try {
                const data = await getChartOfAccounts();
                setAccounts(data);
            } catch (error) {
                addToast('Failed to fetch chart of accounts', 'error');
            } finally {
                setIsLoading(false);
            }
        };
        fetchAccounts();
    }, []);

    const groupedAccounts = accounts.reduce((acc, account) => {
        if (!acc[account.type]) {
            acc[account.type] = [];
        }
        acc[account.type].push(account);
        return acc;
    }, {} as Record<Account['type'], Account[]>);

    return (
        <div>
            <h1 className="text-3xl font-bold mb-6">Chart of Accounts</h1>
            {isLoading ? (
                 <div className="text-center p-6">Loading chart of accounts...</div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <AccountList title="Assets" accounts={groupedAccounts.Asset || []} />
                    <AccountList title="Liabilities" accounts={groupedAccounts.Liability || []} />
                    <AccountList title="Equity" accounts={groupedAccounts.Equity || []} />
                    <AccountList title="Revenue" accounts={groupedAccounts.Revenue || []} />
                    <AccountList title="Expenses" accounts={groupedAccounts.Expense || []} />
                </div>
            )}
        </div>
    );
};

export default AccountingPage;
