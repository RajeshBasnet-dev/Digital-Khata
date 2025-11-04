
import React, { useState, useEffect } from 'react';
import { Product } from '../types';
import { getProducts, addProduct, updateProduct, deleteProduct } from '../services/api';
import { Button } from '../components/common/Button';
import { Modal } from '../components/common/Modal';
import { Input } from '../components/common/Input';
import { useToast } from '../context/AppContext';

const ProductForm: React.FC<{ product?: Product | null, onSave: (product: Omit<Product, 'id'> | Product) => void, onCancel: () => void }> = ({ product, onSave, onCancel }) => {
    const [formData, setFormData] = useState({
        name: product?.name || '',
        sku: product?.sku || '',
        category: product?.category || '',
        stock: product?.stock || 0,
        price: product?.price || 0,
        supplier: product?.supplier || '',
        lowStockThreshold: product?.lowStockThreshold || 10,
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value, type } = e.target;
        setFormData(prev => ({ ...prev, [name]: type === 'number' ? parseFloat(value) : value }));
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSave({ ...product, ...formData });
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <Input label="Product Name" name="name" value={formData.name} onChange={handleChange} required />
                <Input label="SKU" name="sku" value={formData.sku} onChange={handleChange} required />
            </div>
            <Input label="Category" name="category" value={formData.category} onChange={handleChange} required />
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <Input label="Stock" name="stock" type="number" value={formData.stock} onChange={handleChange} required />
                <Input label="Price" name="price" type="number" step="0.01" value={formData.price} onChange={handleChange} required />
            </div>
            <Input label="Supplier" name="supplier" value={formData.supplier} onChange={handleChange} />
            <Input label="Low Stock Threshold" name="lowStockThreshold" type="number" value={formData.lowStockThreshold} onChange={handleChange} required />
            <div className="flex justify-end gap-2 pt-4">
                <Button type="button" variant="secondary" onClick={onCancel}>Cancel</Button>
                <Button type="submit">Save Product</Button>
            </div>
        </form>
    );
};

const InventoryPage: React.FC = () => {
    const [products, setProducts] = useState<Product[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [editingProduct, setEditingProduct] = useState<Product | null>(null);
    const addToast = useToast();

    useEffect(() => {
        fetchProducts();
    }, []);

    const fetchProducts = async () => {
        setIsLoading(true);
        try {
            const data = await getProducts();
            setProducts(data);
        } catch (error) {
            addToast('Failed to fetch products', 'error');
        } finally {
            setIsLoading(false);
        }
    };

    const handleSave = async (productData: Omit<Product, 'id'> | Product) => {
        try {
            if ('id' in productData && productData.id) {
                await updateProduct(productData as Product);
                addToast('Product updated successfully', 'success');
            } else {
                await addProduct(productData);
                addToast('Product added successfully', 'success');
            }
            fetchProducts();
            closeModal();
        } catch (error) {
            addToast('Failed to save product', 'error');
        }
    };

    const handleDelete = async (id: string) => {
        if (window.confirm('Are you sure you want to delete this product?')) {
            try {
                await deleteProduct(id);
                addToast('Product deleted successfully', 'success');
                fetchProducts();
            } catch (error) {
                addToast('Failed to delete product', 'error');
            }
        }
    };

    const openModal = (product: Product | null = null) => {
        setEditingProduct(product);
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
        setEditingProduct(null);
    };

    return (
        <div>
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold">Inventory</h1>
                <Button onClick={() => openModal()}>Add Product</Button>
            </div>
            <div className="bg-white dark:bg-gray-800 shadow-md rounded-lg overflow-x-auto">
                <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                    <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" className="px-6 py-3">Name</th>
                            <th scope="col" className="px-6 py-3">SKU</th>
                            <th scope="col" className="px-6 py-3">Stock</th>
                            <th scope="col" className="px-6 py-3">Price</th>
                            <th scope="col" className="px-6 py-3">Category</th>
                            <th scope="col" className="px-6 py-3">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {isLoading ? (
                            <tr><td colSpan={6} className="text-center p-6">Loading...</td></tr>
                        ) : (
                            products.map(product => (
                                <tr key={product.id} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                                    <td className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">{product.name}</td>
                                    <td className="px-6 py-4">{product.sku}</td>
                                    <td className={`px-6 py-4 ${product.stock <= product.lowStockThreshold ? 'text-red-500 font-bold' : ''}`}>{product.stock}</td>
                                    <td className="px-6 py-4">${product.price.toFixed(2)}</td>
                                    <td className="px-6 py-4">{product.category}</td>
                                    <td className="px-6 py-4 space-x-2">
                                        <Button size="sm" onClick={() => openModal(product)}>Edit</Button>
                                        <Button size="sm" variant="danger" onClick={() => handleDelete(product.id)}>Delete</Button>
                                    </td>
                                </tr>
                            ))
                        )}
                    </tbody>
                </table>
            </div>

            <Modal isOpen={isModalOpen} onClose={closeModal} title={editingProduct ? 'Edit Product' : 'Add New Product'}>
                <ProductForm product={editingProduct} onSave={handleSave} onCancel={closeModal} />
            </Modal>
        </div>
    );
};

export default InventoryPage;
