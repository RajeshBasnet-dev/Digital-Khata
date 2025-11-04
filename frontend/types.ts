
export enum Page {
    Landing = 'landing',
    Login = 'login',
    Signup = 'signup',
    Dashboard = 'dashboard',
    Inventory = 'inventory',
    Sales = 'sales',
    Purchases = 'purchases',
    Accounting = 'accounting',
    Reports = 'reports',
    Settings = 'settings',
}

export interface User {
    id: string;
    name: string;
    email: string;
    businessName: string;
}

export interface Product {
    id: string;
    name: string;
    sku: string;
    category: string;
    stock: number;
    price: number;
    supplier: string;
    lowStockThreshold: number;
}

export interface Sale {
    id: string;
    invoiceNumber: string;
    customerName: string;
    date: string;
    amount: number;
    status: 'Paid' | 'Unpaid' | 'Overdue';
}

export interface Purchase {
    id: string;
    billNumber: string;
    supplierName: string;
    date: string;
    amount: number;
    status: 'Paid' | 'Unpaid';
}

export interface Account {
    id: string;
    name: string;
    type: 'Asset' | 'Liability' | 'Equity' | 'Revenue' | 'Expense';
    balance: number;
}

export interface Notification {
    id: number;
    message: string;
    type: 'success' | 'error' | 'info';
}
