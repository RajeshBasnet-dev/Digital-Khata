
import React from 'react';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
    label: string;
    error?: string;
}

export const Input: React.FC<InputProps> = ({ label, id, error, className = '', ...props }) => {
    return (
        <div className="w-full">
            <label htmlFor={id} className="block text-sm font-medium text-gray-700 dark:text-gray-300">
                {label}
            </label>
            <input
                id={id}
                className={`mt-1 block w-full px-3 py-2 bg-white dark:bg-gray-700 border ${error ? 'border-red-500' : 'border-gray-300 dark:border-gray-600'} rounded-md shadow-sm placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm ${className}`}
                {...props}
            />
            {error && <p className="mt-2 text-sm text-red-600">{error}</p>}
        </div>
    );
};
