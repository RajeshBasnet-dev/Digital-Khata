
import React, { useState } from 'react';
import { Page } from '../types';
import { Button } from '../components/common/Button';
import { Input } from '../components/common/Input';
import { useToast } from '../context/AppContext';
import { Icons } from '../constants';

interface SignupPageProps {
    setCurrentPage: (page: Page) => void;
}

const SignupPage: React.FC<SignupPageProps> = ({ setCurrentPage }) => {
    const addToast = useToast();
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [businessName, setBusinessName] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setIsLoading(true);
        // Mock signup
        setTimeout(() => {
            addToast('Account created successfully! Please log in.', 'success');
            setIsLoading(false);
            setCurrentPage(Page.Login);
        }, 1000);
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
            <div className="max-w-md w-full bg-white dark:bg-gray-800 shadow-md rounded-lg p-8 space-y-6">
                <div className="text-center">
                    <div className="flex justify-center items-center space-x-2 mb-4">
                        {React.cloneElement(Icons.logo, { className: "h-10 w-10 text-primary-600"})}
                        <h2 className="text-3xl font-bold text-gray-900 dark:text-white">Create an Account</h2>
                    </div>
                    <p className="text-gray-600 dark:text-gray-400">Join Digital Khata today!</p>
                </div>
                <form className="space-y-4" onSubmit={handleSubmit}>
                    <Input id="name" label="Full Name" type="text" value={name} onChange={(e) => setName(e.target.value)} required />
                    <Input id="businessName" label="Business Name" type="text" value={businessName} onChange={(e) => setBusinessName(e.target.value)} required />
                    <Input id="email" label="Email Address" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
                    <Input id="password" label="Password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                    
                    <Button type="submit" className="w-full" disabled={isLoading}>
                        {isLoading ? 'Creating Account...' : 'Sign Up'}
                    </Button>
                </form>
                <p className="text-center text-sm text-gray-600 dark:text-gray-400">
                    Already have an account?{' '}
                    <button onClick={() => setCurrentPage(Page.Login)} className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                        Sign in
                    </button>
                </p>
                 <p className="text-center text-sm text-gray-600 dark:text-gray-400">
                    <button onClick={() => setCurrentPage(Page.Landing)} className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                        Back to Home
                    </button>
                </p>
            </div>
        </div>
    );
};

export default SignupPage;
