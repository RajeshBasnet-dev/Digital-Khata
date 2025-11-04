
import React, { useState, useEffect } from 'react';
import { AppProvider, useAuth } from './context/AppContext';
import LandingPage from './pages/LandingPage';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import MainAppLayout from './pages/MainAppLayout';
import DashboardPage from './pages/DashboardPage';
import InventoryPage from './pages/InventoryPage';
import SalesPage from './pages/SalesPage';
import PurchasesPage from './pages/PurchasesPage';
import AccountingPage from './pages/AccountingPage';
import ReportsPage from './pages/ReportsPage';
import SettingsPage from './pages/SettingsPage';
import { Page } from './types';

const AppContent: React.FC = () => {
    const { isAuthenticated } = useAuth();
    const [currentPage, setCurrentPage] = useState<Page>(() => isAuthenticated ? Page.Dashboard : Page.Landing);

    useEffect(() => {
        if (isAuthenticated) {
            if ([Page.Landing, Page.Login, Page.Signup].includes(currentPage)) {
                setCurrentPage(Page.Dashboard);
            }
        } else {
            if (![Page.Landing, Page.Login, Page.Signup].includes(currentPage)) {
                setCurrentPage(Page.Landing);
            }
        }
    }, [isAuthenticated, currentPage]);


    const renderPage = () => {
        if (!isAuthenticated) {
            switch (currentPage) {
                case Page.Login:
                    return <LoginPage setCurrentPage={setCurrentPage} />;
                case Page.Signup:
                    return <SignupPage setCurrentPage={setCurrentPage} />;
                case Page.Landing:
                default:
                    return <LandingPage setCurrentPage={setCurrentPage} />;
            }
        }

        const pageComponents: { [key in Page]?: React.ReactNode } = {
            [Page.Dashboard]: <DashboardPage />,
            [Page.Inventory]: <InventoryPage />,
            [Page.Sales]: <SalesPage />,
            [Page.Purchases]: <PurchasesPage />,
            [Page.Accounting]: <AccountingPage />,
            [Page.Reports]: <ReportsPage />,
            [Page.Settings]: <SettingsPage />,
        };

        const activeComponent = pageComponents[currentPage] || <DashboardPage />;

        return <MainAppLayout currentPage={currentPage} setCurrentPage={setCurrentPage}>{activeComponent}</MainAppLayout>;
    };

    return <div className="min-h-screen text-gray-800 dark:text-gray-200">{renderPage()}</div>;
};

const App: React.FC = () => {
    return (
        <AppProvider>
            <AppContent />
        </AppProvider>
    );
};

export default App;