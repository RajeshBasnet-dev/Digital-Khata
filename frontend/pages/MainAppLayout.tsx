
import React, { useState } from 'react';
import { Page } from '../types';
import { useAuth, useTheme } from '../context/AppContext';
import { NAV_ITEMS, Icons } from '../constants';
import { ToastContainer } from '../components/common/Toast';

interface MainAppLayoutProps {
    children: React.ReactNode;
    currentPage: Page;
    setCurrentPage: (page: Page) => void;
}

const Sidebar: React.FC<{ currentPage: Page; setCurrentPage: (page: Page) => void; isOpen: boolean; }> = ({ currentPage, setCurrentPage, isOpen }) => {
    const { logout } = useAuth();
    
    return (
        <aside className={`fixed inset-y-0 left-0 bg-gray-800 text-white w-64 transform ${isOpen ? 'translate-x-0' : '-translate-x-full'} md:relative md:translate-x-0 transition-transform duration-200 ease-in-out z-30`}>
            <div className="flex items-center justify-center p-4 h-16 border-b border-gray-700">
                {Icons.logo}
                <span className="ml-3 text-xl font-semibold">Digital Khata</span>
            </div>
            <nav className="flex-1 px-2 py-4 space-y-1">
                {NAV_ITEMS.map(item => (
                    <a
                        key={item.page}
                        href="#"
                        onClick={(e) => { e.preventDefault(); setCurrentPage(item.page); }}
                        className={`flex items-center px-4 py-2 text-sm font-medium rounded-md group ${currentPage === item.page ? 'bg-primary-600 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white'}`}
                    >
                        {item.icon}
                        <span className="ml-3">{item.label}</span>
                    </a>
                ))}
            </nav>
            <div className="absolute bottom-0 w-full border-t border-gray-700">
                <a href="#" onClick={(e) => { e.preventDefault(); setCurrentPage(Page.Settings); }} className="flex items-center px-4 py-3 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
                    {Icons.settings}
                    <span className="ml-3">Settings</span>
                </a>
                <a href="#" onClick={(e) => { e.preventDefault(); logout(); }} className="flex items-center px-4 py-3 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
                    {Icons.logout}
                    <span className="ml-3">Logout</span>
                </a>
            </div>
        </aside>
    );
};

const Header: React.FC<{ onMenuClick: () => void }> = ({ onMenuClick }) => {
    const { user } = useAuth();
    const { theme, toggleTheme } = useTheme();

    return (
        <header className="sticky top-0 bg-white dark:bg-gray-800 shadow-sm z-20">
            <div className="flex items-center justify-between h-16 px-4 sm:px-6 lg:px-8">
                 <button onClick={onMenuClick} className="md:hidden text-gray-500 dark:text-gray-400 focus:outline-none">
                    {Icons.menu}
                </button>
                <div className="flex-1" />
                <div className="flex items-center space-x-4">
                    <button onClick={toggleTheme} className="p-2 rounded-full text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700">
                        {theme === 'light' ? Icons.moon : Icons.sun}
                    </button>
                    <div className="text-right">
                        <div className="font-semibold text-gray-900 dark:text-white">{user?.name}</div>
                        <div className="text-xs text-gray-500 dark:text-gray-400">{user?.businessName}</div>
                    </div>
                </div>
            </div>
        </header>
    );
};


const MainAppLayout: React.FC<MainAppLayoutProps> = ({ children, currentPage, setCurrentPage }) => {
    const [sidebarOpen, setSidebarOpen] = useState(false);

    return (
        <div className="flex h-screen bg-gray-100 dark:bg-gray-900">
            <ToastContainer />
            <Sidebar currentPage={currentPage} setCurrentPage={setCurrentPage} isOpen={sidebarOpen} />
            <div className="flex-1 flex flex-col overflow-hidden">
                <Header onMenuClick={() => setSidebarOpen(!sidebarOpen)} />
                <main className="flex-1 overflow-x-hidden overflow-y-auto p-4 sm:p-6 lg:p-8">
                    {children}
                </main>
            </div>
             {sidebarOpen && <div onClick={() => setSidebarOpen(false)} className="fixed inset-0 bg-black opacity-50 z-20 md:hidden"></div>}
        </div>
    );
};

export default MainAppLayout;
