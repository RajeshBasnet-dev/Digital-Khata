
import React from 'react';
import { Page } from '../types';
import { Button } from '../components/common/Button';
import { Icons } from '../constants';

interface LandingPageProps {
    setCurrentPage: (page: Page) => void;
}

const FeatureCard: React.FC<{ icon: React.ReactNode, title: string, description: string }> = ({ icon, title, description }) => (
    <div className="flex flex-col items-center text-center p-6 bg-white dark:bg-gray-800 rounded-lg shadow-lg transform hover:-translate-y-2 transition-transform duration-300">
        <div className="p-4 bg-primary-100 dark:bg-primary-900 rounded-full text-primary-600 dark:text-primary-300 mb-4">
            {icon}
        </div>
        <h3 className="text-xl font-bold mb-2">{title}</h3>
        <p className="text-gray-600 dark:text-gray-400">{description}</p>
    </div>
);

const LandingPage: React.FC<LandingPageProps> = ({ setCurrentPage }) => {
    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-800 dark:text-gray-200">
            {/* Header */}
            <header className="py-4 px-6 md:px-12 flex justify-between items-center bg-white dark:bg-gray-800 shadow-md">
                <div className="flex items-center space-x-2">
                    {React.cloneElement(Icons.logo, { className: "h-8 w-8 text-primary-600"})}
                    <h1 className="text-2xl font-bold text-primary-600 dark:text-primary-400">Digital Khata</h1>
                </div>
                <div>
                    <Button variant="secondary" onClick={() => setCurrentPage(Page.Login)} className="mr-2">Login</Button>
                    <Button onClick={() => setCurrentPage(Page.Signup)}>Sign Up</Button>
                </div>
            </header>

            {/* Hero Section */}
            <main className="text-center py-20 px-6">
                <h2 className="text-4xl md:text-6xl font-extrabold text-gray-900 dark:text-white mb-4">
                    The Smart Way to Manage Your Business
                </h2>
                <p className="text-lg md:text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto mb-8">
                    Digital Khata is the all-in-one solution for small businesses to track sales, manage inventory, handle accounting, and grow effortlessly.
                </p>
                <Button size="lg" onClick={() => setCurrentPage(Page.Signup)}>Get Started for Free</Button>
            </main>

            {/* Features Section */}
            <section id="features" className="py-20 bg-gray-100 dark:bg-gray-950 px-6 md:px-12">
                <div className="max-w-7xl mx-auto">
                    <h3 className="text-3xl font-bold text-center mb-12">Everything You Need, All in One Place</h3>
                    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                        <FeatureCard icon={Icons.inventory} title="Inventory Management" description="Keep track of your stock levels in real-time. Get alerts for low stock and never miss a sale." />
                        <FeatureCard icon={Icons.sales} title="Sales & Invoicing" description="Create and send professional invoices in seconds. Track payments and manage customer balances." />
                        <FeatureCard icon={Icons.purchases} title="Purchase Tracking" description="Manage supplier bills, track expenses, and stay on top of your payables with ease." />
                        <FeatureCard icon={Icons.accounting} title="Automated Accounting" description="Simplified double-entry bookkeeping. Sales and purchases are automatically recorded." />
                        <FeatureCard icon={Icons.reports} title="Insightful Reports" description="Generate Profit & Loss, Balance Sheets, and other crucial reports to understand your business health." />
                        <FeatureCard icon={Icons.dashboard} title="Real-time Dashboard" description="Get a bird's-eye view of your business performance with our intuitive and powerful dashboard." />
                    </div>
                </div>
            </section>

            {/* CTA Section */}
            <section className="py-20 px-6 text-center">
                <h3 className="text-3xl font-bold mb-4">Ready to take control of your business?</h3>
                <p className="text-lg text-gray-600 dark:text-gray-400 mb-8">Join thousands of businesses thriving with Digital Khata.</p>
                <Button size="lg" onClick={() => setCurrentPage(Page.Signup)}>Sign Up Now</Button>
            </section>

            {/* Footer */}
            <footer className="py-6 px-6 md:px-12 bg-gray-800 text-gray-400 text-center">
                <p>&copy; {new Date().getFullYear()} Digital Khata. All rights reserved.</p>
            </footer>
        </div>
    );
};

export default LandingPage;
