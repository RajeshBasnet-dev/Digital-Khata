
import React, { createContext, useContext, useReducer, useEffect, ReactNode } from 'react';
import { User, Notification } from '../types';

type Theme = 'light' | 'dark';

interface AppState {
    isAuthenticated: boolean;
    user: User | null;
    theme: Theme;
    notifications: Notification[];
}

type Action =
    | { type: 'LOGIN'; payload: User }
    | { type: 'LOGOUT' }
    | { type: 'SET_THEME'; payload: Theme }
    | { type: 'ADD_NOTIFICATION'; payload: Omit<Notification, 'id'> }
    | { type: 'REMOVE_NOTIFICATION'; payload: number };

const AppContext = createContext<{
    state: AppState;
    dispatch: React.Dispatch<Action>;
}>({
    state: {
        isAuthenticated: false,
        user: null,
        theme: 'light',
        notifications: [],
    },
    dispatch: () => null,
});

const appReducer = (state: AppState, action: Action): AppState => {
    switch (action.type) {
        case 'LOGIN':
            localStorage.setItem('isAuthenticated', 'true');
            localStorage.setItem('user', JSON.stringify(action.payload));
            return {
                ...state,
                isAuthenticated: true,
                user: action.payload,
            };
        case 'LOGOUT':
            localStorage.removeItem('isAuthenticated');
            localStorage.removeItem('user');
            return {
                ...state,
                isAuthenticated: false,
                user: null,
            };
        case 'SET_THEME':
            localStorage.setItem('theme', action.payload);
            if (action.payload === 'dark') {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
            return {
                ...state,
                theme: action.payload,
            };
        case 'ADD_NOTIFICATION':
            return {
                ...state,
                notifications: [...state.notifications, { ...action.payload, id: Date.now() }],
            };
        case 'REMOVE_NOTIFICATION':
            return {
                ...state,
                notifications: state.notifications.filter(n => n.id !== action.payload),
            };
        default:
            return state;
    }
};

export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [state, dispatch] = useReducer(appReducer, {
        isAuthenticated: !!localStorage.getItem('isAuthenticated'),
        user: JSON.parse(localStorage.getItem('user') || 'null'),
        theme: (localStorage.getItem('theme') as Theme) || 'light',
        notifications: [],
    });

    useEffect(() => {
        const storedTheme = localStorage.getItem('theme') as Theme;
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (storedTheme) {
            dispatch({ type: 'SET_THEME', payload: storedTheme });
        } else {
            dispatch({ type: 'SET_THEME', payload: prefersDark ? 'dark' : 'light' });
        }
    }, []);

    return (
        <AppContext.Provider value={{ state, dispatch }}>
            {children}
        </AppContext.Provider>
    );
};

export const useAuth = () => {
    const { state, dispatch } = useContext(AppContext);
    return {
        ...state,
        login: (user: User) => dispatch({ type: 'LOGIN', payload: user }),
        logout: () => dispatch({ type: 'LOGOUT' }),
    };
};

export const useTheme = () => {
    const { state, dispatch } = useContext(AppContext);
    return {
        theme: state.theme,
        toggleTheme: () => {
            const newTheme = state.theme === 'light' ? 'dark' : 'light';
            dispatch({ type: 'SET_THEME', payload: newTheme });
        },
    };
};

export const useToast = () => {
    const { dispatch } = useContext(AppContext);
    const addToast = (message: string, type: 'success' | 'error' | 'info' = 'info') => {
        dispatch({ type: 'ADD_NOTIFICATION', payload: { message, type } });
    };
    return addToast;
};

export const useNotifications = () => {
    const { state, dispatch } = useContext(AppContext);
    return {
        notifications: state.notifications,
        removeNotification: (id: number) => dispatch({ type: 'REMOVE_NOTIFICATION', payload: id }),
    };
};
