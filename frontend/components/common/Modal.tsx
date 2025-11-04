
import React from 'react';
import { Icons } from '../../constants';

interface ModalProps {
    isOpen: boolean;
    onClose: () => void;
    title: string;
    children: React.ReactNode;
    footer?: React.ReactNode;
}

export const Modal: React.FC<ModalProps> = ({ isOpen, onClose, title, children, footer }) => {
    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50" aria-modal="true" role="dialog">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-xl w-full max-w-lg m-4 transform transition-all">
                <div className="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700">
                    <h3 className="text-xl font-semibold text-gray-900 dark:text-white">{title}</h3>
                    <button
                        onClick={onClose}
                        className="text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600 hover:text-gray-900 dark:hover:text-white rounded-lg text-sm p-1.5 ml-auto inline-flex items-center"
                    >
                        {Icons.close}
                        <span className="sr-only">Close modal</span>
                    </button>
                </div>
                <div className="p-6 space-y-6">
                    {children}
                </div>
                {footer && (
                    <div className="flex items-center p-6 space-x-2 border-t border-gray-200 dark:border-gray-700 rounded-b">
                        {footer}
                    </div>
                )}
            </div>
        </div>
    );
};
