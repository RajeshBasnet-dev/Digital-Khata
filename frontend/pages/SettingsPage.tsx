
import React, { useState } from 'react';
import { useAuth, useToast } from '../context/AppContext';
import { Card } from '../components/common/Card';
import { Input } from '../components/common/Input';
import { Button } from '../components/common/Button';

const SettingsPage: React.FC = () => {
    const { user } = useAuth();
    const addToast = useToast();
    const [profile, setProfile] = useState({
        name: user?.name || '',
        email: user?.email || '',
        businessName: user?.businessName || '',
    });
    const [password, setPassword] = useState({
        current: '',
        new: '',
        confirm: '',
    });
    
    const handleProfileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setProfile({ ...profile, [e.target.name]: e.target.value });
    };

    const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setPassword({ ...password, [e.target.name]: e.target.value });
    };

    const handleProfileSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        addToast('Profile updated successfully!', 'success');
        // In a real app, this would call an API.
    };
    
    const handlePasswordSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (password.new !== password.confirm) {
            addToast('New passwords do not match.', 'error');
            return;
        }
        addToast('Password changed successfully!', 'success');
        // In a real app, this would call an API.
        setPassword({ current: '', new: '', confirm: '' });
    };

    return (
        <div>
            <h1 className="text-3xl font-bold mb-6">Settings</h1>
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <Card title="Business Profile">
                    <form className="space-y-4" onSubmit={handleProfileSubmit}>
                        <Input label="Business Name" name="businessName" value={profile.businessName} onChange={handleProfileChange} />
                        <Input label="Your Name" name="name" value={profile.name} onChange={handleProfileChange} />
                        <Input label="Email Address" name="email" type="email" value={profile.email} onChange={handleProfileChange} />
                        <div className="pt-2">
                           <Button type="submit">Save Profile</Button>
                        </div>
                    </form>
                </Card>
                <Card title="Change Password">
                    <form className="space-y-4" onSubmit={handlePasswordSubmit}>
                        <Input label="Current Password" name="current" type="password" value={password.current} onChange={handlePasswordChange} />
                        <Input label="New Password" name="new" type="password" value={password.new} onChange={handlePasswordChange} />
                        <Input label="Confirm New Password" name="confirm" type="password" value={password.confirm} onChange={handlePasswordChange} />
                        <div className="pt-2">
                            <Button type="submit">Change Password</Button>
                        </div>
                    </form>
                </Card>
            </div>
        </div>
    );
};

export default SettingsPage;
