import { User, Product, Sale, Purchase, Account } from '../types';

// API base URL - will be proxied to Django backend in development
const API_BASE_URL = '/api';

// Helper function for API requests
const apiRequest = async <T>(endpoint: string, options: RequestInit = {}): Promise<T> => {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        headers: {
            'Content-Type': 'application/json',
            ...options.headers,
        },
        credentials: 'include',
        ...options,
    });
    
    if (!response.ok) {
        throw new Error(`API request failed: ${response.status} ${response.statusText}`);
    }
    
    return response.json();
};

// --- API FUNCTIONS ---

export const loginUser = async (email: string, password: string): Promise<User> => {
    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);
    
    const response = await fetch('/accounts/login/', {
        method: 'POST',
        body: formData,
        credentials: 'include',
    });
    
    if (!response.ok) {
        throw new Error('Invalid email or password');
    }
    
    // Get user profile after login
    return apiRequest<User>('/accounts/api/profile/');
};

export const logoutUser = async (): Promise<void> => {
    await apiRequest('/accounts/api/logout/', { method: 'POST' });
};

export const getUserProfile = async (): Promise<User> => {
    return apiRequest<User>('/accounts/api/profile/');
};

// Dashboard API
export const getDashboardData = async (): Promise<any> => {
    return apiRequest('/dashboard/api/data/');
};

// Inventory APIs
export const getProducts = async (): Promise<Product[]> => {
    return apiRequest<Product[]>('/inventory/api/products/');
};

export const getProduct = async (id: string): Promise<Product> => {
    return apiRequest<Product>(`/inventory/api/products/${id}/`);
};

export const createProduct = async (productData: Omit<Product, 'id'>): Promise<Product> => {
    return apiRequest<Product>('/inventory/api/products/', {
        method: 'POST',
        body: JSON.stringify(productData),
    });
};

export const updateProduct = async (productData: Product): Promise<Product> => {
    return apiRequest<Product>(`/inventory/api/products/${productData.id}/`, {
        method: 'PUT',
        body: JSON.stringify(productData),
    });
};

export const deleteProduct = async (id: string): Promise<void> => {
    await apiRequest(`/inventory/api/products/${id}/`, {
        method: 'DELETE',
    });
};

// Sales APIs
export const getSales = async (): Promise<Sale[]> => {
    return apiRequest<Sale[]>('/sales/api/invoices/');
};

export const getSale = async (id: string): Promise<Sale> => {
    return apiRequest<Sale>(`/sales/api/invoices/${id}/`);
};

export const createSale = async (saleData: any): Promise<Sale> => {
    return apiRequest<Sale>('/sales/api/invoices/', {
        method: 'POST',
        body: JSON.stringify(saleData),
    });
};

export const updateSale = async (saleData: Sale): Promise<Sale> => {
    return apiRequest<Sale>(`/sales/api/invoices/${saleData.id}/`, {
        method: 'PUT',
        body: JSON.stringify(saleData),
    });
};

export const deleteSale = async (id: string): Promise<void> => {
    await apiRequest(`/sales/api/invoices/${id}/`, {
        method: 'DELETE',
    });
};

// Purchases APIs
export const getPurchases = async (): Promise<Purchase[]> => {
    return apiRequest<Purchase[]>('/purchases/api/bills/');
};

export const getPurchase = async (id: string): Promise<Purchase> => {
    return apiRequest<Purchase>(`/purchases/api/bills/${id}/`);
};

export const createPurchase = async (purchaseData: any): Promise<Purchase> => {
    return apiRequest<Purchase>('/purchases/api/bills/', {
        method: 'POST',
        body: JSON.stringify(purchaseData),
    });
};

export const updatePurchase = async (purchaseData: Purchase): Promise<Purchase> => {
    return apiRequest<Purchase>(`/purchases/api/bills/${purchaseData.id}/`, {
        method: 'PUT',
        body: JSON.stringify(purchaseData),
    });
};

export const deletePurchase = async (id: string): Promise<void> => {
    await apiRequest(`/purchases/api/bills/${id}/`, {
        method: 'DELETE',
    });
};

// Accounting APIs
export const getChartOfAccounts = async (): Promise<Account[]> => {
    return apiRequest<Account[]>('/accounting/api/accounts/');
};

export const getAccount = async (id: string): Promise<Account> => {
    return apiRequest<Account>(`/accounting/api/accounts/${id}/`);
};

export const createAccount = async (accountData: any): Promise<Account> => {
    return apiRequest<Account>('/accounting/api/accounts/', {
        method: 'POST',
        body: JSON.stringify(accountData),
    });
};

export const updateAccount = async (accountData: Account): Promise<Account> => {
    return apiRequest<Account>(`/accounting/api/accounts/${accountData.id}/`, {
        method: 'PUT',
        body: JSON.stringify(accountData),
    });
};

export const deleteAccount = async (id: string): Promise<void> => {
    await apiRequest(`/accounting/api/accounts/${id}/`, {
        method: 'DELETE',
    });
};

// Reports APIs
export const getSalesReport = async (params?: any): Promise<any> => {
    const queryParams = new URLSearchParams(params).toString();
    const url = `/reports/api/sales/${queryParams ? `?${queryParams}` : ''}`;
    return apiRequest(url);
};

export const getPurchasesReport = async (params?: any): Promise<any> => {
    const queryParams = new URLSearchParams(params).toString();
    const url = `/reports/api/purchases/${queryParams ? `?${queryParams}` : ''}`;
    return apiRequest(url);
};

export const getInventoryReport = async (params?: any): Promise<any> => {
    const queryParams = new URLSearchParams(params).toString();
    const url = `/reports/api/inventory/${queryParams ? `?${queryParams}` : ''}`;
    return apiRequest(url);
};