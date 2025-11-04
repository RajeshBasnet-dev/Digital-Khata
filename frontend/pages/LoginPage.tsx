
import React, { useState } from 'react';
import { Page } from '../types';
import { Button } from '../components/common/Button';
import { Input } from '../components/common/Input';
import { useAuth, useToast } from '../context/AppContext';
import { loginUser } from '../services/api';
import { Icons } from '../constants';

interface LoginPageProps {
    setCurrentPage: (page: Page) => void;
}

const LoginPage: React.FC<LoginPageProps> = ({ setCurrentPage }) => {
    const { login } = useAuth();
    const addToast = useToast();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [errors, setErrors] = useState<{ email?: string; password?: string }>({});

    const validate = () => {
        const newErrors: { email?: string; password?: string } = {};
        if (!email) newErrors.email = 'Email is required';
        if (!/\S+@\S+\.\S+/.test(email)) newErrors.email = 'Email address is invalid';
        if (!password) newErrors.password = 'Password is required';
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!validate()) return;
        setIsLoading(true);
        try {
            const user = await loginUser(email, password);
            login(user);
            addToast('Login successful!', 'success');
            // No need to set page, App.tsx will handle re-render
        } catch (error) {
            addToast((error as Error).message, 'error');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
            <div className="max-w-md w-full bg-white dark:bg-gray-800 shadow-md rounded-lg p-8 space-y-6">
                <div className="text-center">
                    <div className="flex justify-center items-center space-x-2 mb-4">
                        {React.cloneElement(Icons.logo, { className: "h-10 w-10 text-primary-600"})}
                        <h2 className="text-3xl font-bold text-gray-900 dark:text-white">Welcome Back</h2>
                    </div>
                    <p className="text-gray-600 dark:text-gray-400">Sign in to continue to Digital Khata</p>
                </div>
                <form className="space-y-6" onSubmit={handleSubmit}>
                    <Input
                        id="email"
                        label="Email Address"
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        error={errors.email}
                        placeholder="test@example.com"
                        required
                    />
                    <Input
                        id="password"
                        label="Password"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        error={errors.password}
                        placeholder="password"
                        required
                    />
                    <div className="flex items-center justify-between">
                        <a href="#" className="text-sm text-primary-600 hover:underline dark:text-primary-500">
                            Forgot password?
                        </a>
                    </div>
                    <Button type="submit" className="w-full" disabled={isLoading}>
                        {isLoading ? 'Signing In...' : 'Sign In'}
                    </Button>
                </form>
                <p className="text-center text-sm text-gray-600 dark:text-gray-400">
                    Don't have an account?{' '}
                    <button onClick={() => setCurrentPage(Page.Signup)} className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                        Sign up
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

export default LoginPage;